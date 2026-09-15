"""Corpus interfaces and controlled agent comparison, extracted from the teaching notebook.

Run --help for the experiment interface. Importing this file runs no experiment.
"""
import json, re, time
from rank_bm25 import BM25Okapi
from helpers.config import LLM_MODEL, require
from helpers import workspace as ws
from helpers.llm import client as make_client
from helpers.judge import make_judge, parse_json
INPUTS = ('corpus', 'eval_cases')
import argparse
import contextlib
import hashlib
import sys
from datetime import datetime, timezone

def provenance():
    return {"recorded_at": datetime.now(timezone.utc).isoformat(), "model": LLM_MODEL,
            "inputs": {name: ws.source(name) for name in INPUTS},
            "corpus_sha256": hashlib.sha256(json.dumps(PAGES, sort_keys=True).encode()).hexdigest()}

def emit(value):
    print(json.dumps(value, indent=2, ensure_ascii=False, default=lambda x: x.model_dump() if hasattr(x, "model_dump") else str(x)))

def outline(text: str) -> tuple:
    """(title, section headings) of one markdown page."""
    lines = text.splitlines()
    title = next((l[2:].strip() for l in lines if l.startswith("# ")), "")
    return title, [l[3:].strip() for l in lines if l.startswith("## ")]



def tokenize(text: str) -> list:
    return TOKEN.findall(text.lower())

def search_chunks(query: str, k: int = 4) -> str:
    scores = bm25.get_scores(tokenize(query))
    order = sorted(range(len(chunks)), key=lambda i: scores[i], reverse=True)[:max(1, min(k, 8))]
    return "\n\n---\n\n".join(f"[{chunks[i]['id']}]\n{chunks[i]['text'][:1000]}" for i in order)

def list_pages() -> str:
    return WIKI

def grep_wiki(pattern: str) -> str:
    try:
        rx = re.compile(pattern, re.I)
    except re.error:
        rx = re.compile(re.escape(pattern), re.I)
    hits = []
    for page, text in PAGES.items():
        for number, line in enumerate(text.splitlines(), 1):
            if rx.search(line):
                hits.append(f"{page}:{number}: {line}")
    return "\n".join(hits[:40]) or "(no matches)"

def read_page(page: str) -> str:
    return PAGES[page][:12000] if page in PAGES else f"(unknown page: {page})"

def schema(name, description, properties, required=()):
    return {"type": "function", "function": {"name": name, "description": description,
            "parameters": {"type": "object", "properties": properties, "required": list(required)}}}
SYSTEM = ("Answer questions about the product only from tool evidence. Investigate before answering. "
          "Name the page you used. If the evidence is incomplete, say so.")


def run_agent(question: str, tools: list, funcs: dict, max_turns: int = 6) -> dict:
    messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": question}]
    trace, chars, started = [], 0, time.perf_counter()
    for _ in range(max_turns):
        msg = client.chat.completions.create(model=LLM_MODEL, temperature=0, messages=messages,
                                             tools=tools, tool_choice="auto").choices[0].message
        calls = msg.tool_calls or []
        if not calls:
            return {"answer": (msg.content or "").strip(), "trace": trace, "evidence_chars": chars,
                    "latency_s": round(time.perf_counter() - started, 2), "stopped": "answer"}
        shaped = [{"id": c.id, "type": "function", "function": {"name": c.function.name, "arguments": c.function.arguments}}
                  for c in calls]
        messages.append({"role": "assistant", "content": msg.content or "", "tool_calls": shaped})
        for call in shaped:
            name = call["function"]["name"]
            try:
                args = json.loads(call["function"]["arguments"] or "{}")
                if name not in funcs:
                    raise KeyError(f"unknown tool {name}")
                result = str(funcs[name](**args))
            except Exception as exc:
                args, result = {}, f"(tool error: {type(exc).__name__}: {exc})"
            chars += len(result)
            trace.append({"tool": name, "args": args, "chars": len(result), "result": result})
            messages.append({"role": "tool", "tool_call_id": call["id"], "content": result})
    return {"answer": "(max turns reached)", "trace": trace, "evidence_chars": chars,
            "latency_s": round(time.perf_counter() - started, 2), "stopped": "max_turns"}



def initialize():
    global PAGES, CASES, CORPUS_DIR, client, WIKI, TOKEN, chunks, bm25, RAG_FUNCS, RAG_TOOLS, DCI_FUNCS, DCI_TOOLS, MODES
    require("OPENAI_API_KEY")
    client = make_client()
    CORPUS_DIR = ws.load_path("corpus")
    PAGES = {}
    for p in sorted(CORPUS_DIR.rglob("*.md")):
        rel = p.relative_to(CORPUS_DIR).as_posix()
        if not rel.startswith("wiki/") and rel != "vibe_checks.md":   # the wiki is built below; the vibe checks page is the answer key
            PAGES[rel] = p.read_text(encoding="utf-8")
    CASES = ws.load("eval_cases")
    WIKI = ""
    TOKEN = re.compile(r"[a-z0-9$%]+")
    chunks = []
    for page, text in PAGES.items():
        sections = re.split(r"(?=^## )", text, flags=re.M)
        for i, section in enumerate(s for s in sections if s.strip()):
            chunks.append({"id": f"{page}#s{i}", "page": page, "text": section.strip()})
    bm25 = BM25Okapi([tokenize(c["text"]) for c in chunks])
    RAG_FUNCS = {"search_chunks": search_chunks}
    RAG_TOOLS = [schema("search_chunks", "Search ranked corpus sections. Search again with a new query when evidence is incomplete.",
                        {"query": {"type": "string"}, "k": {"type": "integer"}}, ["query"])]
    DCI_FUNCS = {"list_pages": list_pages, "grep_wiki": grep_wiki, "read_page": read_page}
    DCI_TOOLS = [
        schema("list_pages", "Read the wiki index: every page name, what it is for, and its sections.", {}),
        schema("grep_wiki", "Search exact text or a regular expression across all pages; returns page:line: text.",
               {"pattern": {"type": "string"}}, ["pattern"]),
        schema("read_page", "Read one complete page by its name from the index.",
               {"page": {"type": "string", "enum": sorted(PAGES)}}, ["page"]),
    ]
    MODES = {"agentic_rag": (RAG_TOOLS, RAG_FUNCS), "dci": (DCI_TOOLS, DCI_FUNCS)}

def build_wiki():
    global WIKI
    DIGEST = "\n".join(f"- {name} | {outline(t)[0]} | {' '.join(t.split())[:200]}" for name, t in PAGES.items())
    reply = client.chat.completions.create(model=LLM_MODEL, temperature=0, messages=[{"role": "user", "content":
        "For each page below write one line, under fifteen words, saying what a reader should use it for. "
        'Return one JSON object: {"notes": [{"page": "<name>", "use_it_for": "<line>"}]}\n\n' + DIGEST}])
    parsed = parse_json(reply.choices[0].message.content) or {}
    USE = {n.get("page"): n.get("use_it_for", "") for n in parsed.get("notes", []) if isinstance(n, dict)}

    rows = ["# Wiki index", "", "Use this index to decide which page to read. Page names are stable tool inputs.", "",
            "| Page | Use it for | Sections |", "|---|---|---|"]
    for name, text in PAGES.items():
        title, heads = outline(text)
        rows.append(f"| `{name}` | {USE.get(name) or title or name} | {', '.join(heads[:5])} |")
    rows += ["", "Suggested navigation:", "",
             "- Start from the charter for what the product is and refuses to do, then follow a term to the page that operates on it.",
             "- For a question about a past request, read the whole transcript rather than one matching line.",
             "- When a search matches lines on several pages, read each page's section before answering."]
    WIKI = "\n".join(rows)
    return WIKI

def compare(question):
    return [{"mode": mode, "question": question, **run_agent(question, tools, funcs)}
            for mode, (tools, funcs) in MODES.items()]

def score_cases(cases):
    coverage = make_judge("coverage", "Question: {question}\nA good answer includes: {reference}\nAnswer: {response}\nScore 0-10 how completely and accurately the answer covers what a good answer includes.", needs_reference=True)
    rows = []
    for case in cases:
        for result in compare(case["question"]):
            verdict = coverage({"question": case["question"], "response": result["answer"], "reference": case["reference"]})
            expected = case.get("pages") or []
            rows.append({**result, "case_id": case["id"], "score": verdict["score"], "rationale": verdict["rationale"],
                "named_expected_page": any(p.lower() in result["answer"].lower() for p in expected) if expected else None,
                "calls": len(result["trace"])})
    return rows

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['inspect', 'wiki', 'interfaces', 'compare', 'score'])
    parser.add_argument('--question')
    parser.add_argument('--cases', help='Reviewed JSON case list outside the workspace')
    parser.add_argument('--wiki', help='Reviewed wiki Markdown outside the workspace')
    parser.add_argument('--save', action='store_true', help='Save actual wiki/runs through helpers.workspace')
    args = parser.parse_args()
    if args.save and args.command not in ('wiki', 'score'):
        parser.error('--save is supported only for wiki and score')
    with contextlib.redirect_stdout(sys.stderr):
        initialize()
        global WIKI
        if args.cases:
            from pathlib import Path
            cases = json.loads(Path(args.cases).read_text())
        else:
            cases = CASES
        if not cases:
            raise ValueError('No cases to run')
        unknown = {p for c in cases for p in c.get('pages', []) if p not in PAGES}
        if unknown:
            raise ValueError(f'Case labels refer to unknown pages: {sorted(unknown)}')
        question = args.question or cases[0]['question']
        out = {'provenance': provenance(), 'case_source': args.cases or ws.source('eval_cases')}
        if args.command == 'inspect':
            out.update(pages=list(PAGES), cases=cases, sections=len(chunks))
        elif args.command == 'interfaces':
            out.update(question=question, chunks=search_chunks(question), grep=grep_wiki('ticket'), page=read_page(next(iter(PAGES))))
        else:
            if args.wiki:
                from pathlib import Path
                WIKI = Path(args.wiki).read_text()
            else:
                build_wiki()
            out['wiki'] = WIKI
            out['wiki_status'] = 'provided for review' if args.wiki else 'model proposal; review purpose lines'
            if args.command == 'compare':
                out['runs'] = compare(question)
            elif args.command == 'score':
                out['runs'] = score_cases(cases)
            if args.save:
                ws.save('wiki', WIKI)
                if args.command == 'score':
                    ws.save('agentic_runs', out['runs'])
    emit(out)

if __name__ == '__main__':
    main()
