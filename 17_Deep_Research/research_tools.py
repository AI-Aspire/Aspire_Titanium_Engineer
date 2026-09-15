"""Bounded research workflow extracted from the teaching notebook.

Corpus research works without a Tavily key. Importing runs no experiments.
"""
import json, re, textwrap
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import TypedDict
from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel, Field
from helpers.config import LLM_MODEL, TAVILY_KEY, require, budget
from helpers import workspace as ws
from helpers.llm import chat_model
INPUTS = ('corpus', 'capability_report')
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
def failure_modes(report: str) -> list[dict]:
    """Rows of the pass-rate table that did not pass every run, worst first."""
    rows = re.findall(r"^\|\s*([^|\s]+)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*/\s*(\d+)\s*\|", report, re.M)
    modes = [{"task": t, "category": c, "passed": int(p), "runs": int(n)}
             for t, c, p, n in rows if n.isdigit() and int(n) > 0 and int(p) < int(n)]
    return sorted(modes, key=lambda m: m["passed"] / m["runs"])


class ResearchConfig(BaseModel):
    max_research_tasks: int = Field(default=budget(3, 2), ge=1, le=6)
    max_corpus_hits: int = Field(default=3, ge=1, le=10)
    max_web_results: int = Field(default=3, ge=0, le=10)
    max_extract_urls: int = Field(default=1, ge=0, le=5)
    max_researcher_loops: int = Field(default=1, ge=1, le=3)
    max_workers: int = Field(default=3, ge=1, le=6)


class ClarificationDecision(BaseModel):
    needs_clarification: bool = Field(description="True if the request is too vague to research well.")
    reason: str
    question_to_user: str = Field(description="A concise clarification question, or an empty string.")


class ResearchBrief(BaseModel):
    question: str
    audience: str
    deliverable: str
    success_criteria: list[str]
    constraints: list[str]


class ResearchTask(BaseModel):
    name: str
    query: str
    purpose: str


class ResearchPlan(BaseModel):
    tasks: list[ResearchTask]


class ResearchLoopNote(BaseModel):
    key_points: list[str]
    reflection: str = Field(description="What is known, what is still weak, and whether another query would help.")
    follow_up_queries: list[str]


class ResearchFinding(BaseModel):
    task_name: str
    summary: str
    key_points: list[str]
    sources: list[str] = Field(description="Corpus page paths or URLs actually observed.")
    gaps: list[str]


class CompressedDossier(BaseModel):
    executive_summary: str
    findings: list[ResearchFinding]
    cross_cutting_gaps: list[str]


class FinalReport(BaseModel):
    markdown: str
    sources: list[str]
    gaps: list[str]


class DeepResearchState(TypedDict, total=False):
    question: str
    config: ResearchConfig
    clarification: ClarificationDecision
    brief: ResearchBrief
    tasks: list[ResearchTask]
    findings: list[ResearchFinding]
    dossier: CompressedDossier
    final_report: FinalReport
    trace_events: list[dict]



STOP = {"a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "how", "in", "is", "it", "of", "on", "or",
        "our", "that", "the", "their", "this", "to", "what", "when", "with", "does", "do", "why", "not", "its", "agent"}

def terms(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9][a-z0-9-]{2,}", text.lower()) if t not in STOP}

def corpus_search(query: str, max_results: int = 3) -> list[dict]:
    q = terms(query)
    scored = []
    for page in PAGES:
        hit = q & terms(page["text"])
        if hit:
            scored.append((len(hit) + 2 * len(q & terms(page["title"])), page))
    scored.sort(key=lambda x: -x[0])
    return [{"title": pg["title"], "url": pg["path"], "content": textwrap.shorten(re.sub(r"\s+", " ", pg["text"]), 300)}
            for _s, pg in scored[:max_results]]

def corpus_extract(path: str, max_chars: int = 3000) -> dict:
    page = next((p for p in PAGES if p["path"] == path), None)
    return {"url": path, "text": page["text"][:max_chars] if page else "[no such page]"}

def web_search(query: str) -> list[dict]:
    if not WEB or CONFIG.max_web_results == 0:
        return []
    payload = web_search_tool.invoke({"query": query})
    results = payload.get("results", []) if isinstance(payload, dict) else payload
    return [{"title": r.get("title", ""), "url": r.get("url", ""), "content": (r.get("content") or "")[:600]}
            for r in results if isinstance(r, dict) and r.get("url")]

def web_extract(urls: list[str]) -> list[dict]:
    if not WEB or not urls:
        return []
    payload = web_extract_tool.invoke({"urls": urls})
    results = payload.get("results", []) if isinstance(payload, dict) else payload
    return [{"url": r.get("url", ""), "text": (r.get("raw_content") or r.get("content") or "")[:3000]}
            for r in results if isinstance(r, dict)]
def clarify(state: DeepResearchState) -> dict:
    decision = llm.with_structured_output(ClarificationDecision).invoke([
        ("system", "You decide whether a research request has enough context to begin. "
                   "Researchers already have access to the product corpus and capability report. "
                   "Do not ask the user to provide those available sources. "
                   "Only ask for clarification if the request is impossible to scope."),
        ("user", state["question"] + "\n\nAvailable corpus pages:\n"
                 + "\n".join(p["path"] for p in PAGES)
                 + "\n\nAvailable capability report:\n" + REPORT),
    ])
    return {"clarification": decision,
            "trace_events": [{"node": "clarify", "needs_clarification": decision.needs_clarification}]}


def brief(state: DeepResearchState) -> dict:
    out = llm.with_structured_output(ResearchBrief).invoke([
        ("system", "Turn the request into a research brief about an internal support product and its agent. "
                   "Make the success criteria concrete. The research reads the product's documentation, transcripts, "
                   "and evaluation notes, so prefer framing that those sources can answer."),
        ("user", state["question"]),
    ])
    return {"brief": out, "trace_events": state.get("trace_events", []) + [{"node": "brief", "question": out.question}]}


def plan(state: DeepResearchState) -> dict:
    config = state["config"]
    out = llm.with_structured_output(ResearchPlan).invoke([
        ("system", "Split the research brief into independent research tasks. "
                   f"Return at most {config.max_research_tasks} tasks. Each query is two to six words a search engine "
                   "over product documentation and transcripts would match."),
        ("user", state["brief"].model_dump_json(indent=2)),
    ])
    tasks = out.tasks[:config.max_research_tasks] or [
        ResearchTask(name="Primary research", query=state["brief"].question, purpose="Fallback when the planner returns nothing.")]
    return {"tasks": tasks,
            "trace_events": state.get("trace_events", []) + [{"node": "plan", "tasks": [t.model_dump() for t in tasks]}]}


def compact_json(value, *, limit: int = 8000) -> str:
    text = json.dumps(value, indent=2, ensure_ascii=False, default=str)
    return text if len(text) <= limit else text[:limit] + "\n... [truncated]"


def run_one_task(task: ResearchTask, config: ResearchConfig) -> tuple[ResearchFinding, list[dict]]:
    trace, notes, observed, query = [], [], [], task.query
    for loop in range(config.max_researcher_loops):
        corpus_hits = corpus_search(query, config.max_corpus_hits)
        web_hits = web_search(query)
        extracts = [corpus_extract(h["url"]) for h in corpus_hits[:2]]
        extracts += web_extract([h["url"] for h in web_hits[:config.max_extract_urls]])
        observed += [s for s in [h["url"] for h in corpus_hits + web_hits] if s not in observed]
        trace.append({"node": "research", "task": task.name, "loop": loop + 1, "query": query,
                      "search_sources": [h["url"] for h in corpus_hits + web_hits], "corpus_hits": len(corpus_hits), "web_hits": len(web_hits), "extracted": [e["url"] for e in extracts]})
        note = llm.with_structured_output(ResearchLoopNote).invoke([
            ("system", "You are a bounded researcher. Summarize the useful points from these results, say what is still weak, "
                       "and propose a follow-up query only if it would materially improve the task."),
            ("user", "Task:\n" + task.model_dump_json(indent=2) + "\n\nSearch results:\n" + compact_json(corpus_hits + web_hits)
                     + "\n\nExtracted sources:\n" + compact_json(extracts)),
        ])
        notes.append(note)
        if not note.follow_up_queries:
            break
        query = note.follow_up_queries[0]
    finding = llm.with_structured_output(ResearchFinding).invoke([
        ("system", "Compress this researcher's work into a handoff finding. Cite only the observed sources. "
                   "Be explicit about gaps instead of pretending the research is complete."),
        ("user", "Task:\n" + task.model_dump_json(indent=2) + "\n\nObserved sources:\n" + compact_json(observed)
                 + "\n\nLoop notes:\n" + compact_json([n.model_dump() for n in notes])),
    ])
    kept = [s for s in finding.sources if s in observed]
    return finding.model_copy(update={"sources": kept}), trace


def research(state: DeepResearchState) -> dict:
    config, tasks = state["config"], state["tasks"]
    findings, trace = [], list(state.get("trace_events", []))
    with ThreadPoolExecutor(max_workers=min(config.max_workers, len(tasks))) as pool:
        for future in as_completed([pool.submit(run_one_task, t, config) for t in tasks]):
            finding, events = future.result()
            findings.append(finding)
            trace.extend(events)
    return {"findings": findings, "trace_events": trace}


def compress(state: DeepResearchState) -> dict:
    dossier = llm.with_structured_output(CompressedDossier).invoke([
        ("system", "Compress the researcher findings into a concise dossier for a report writer. Preserve sources and unresolved gaps."),
        ("user", "Research brief:\n" + state["brief"].model_dump_json(indent=2)
                 + "\n\nFindings:\n" + compact_json([f.model_dump() for f in state["findings"]])),
    ])
    return {"dossier": dossier,
            "trace_events": state.get("trace_events", []) + [{"node": "compress", "findings": len(dossier.findings)}]}


def write(state: DeepResearchState) -> dict:
    report = llm.with_structured_output(FinalReport).invoke([
        ("system", "Write a concise research report in Markdown for the engineers who own the support agent. "
                   "Cite sources inline as [source] using only the dossier's sources. "
                   "Include a section called 'Open gaps' when evidence is incomplete."),
        ("user", "Research brief:\n" + state["brief"].model_dump_json(indent=2)
                 + "\n\nCompressed dossier:\n" + state["dossier"].model_dump_json(indent=2)),
    ])
    return {"final_report": report,
            "trace_events": state.get("trace_events", []) + [{"node": "write", "sources": report.sources}]}


builder = StateGraph(DeepResearchState)
for name, fn in [("clarify", clarify), ("brief", brief), ("plan", plan), ("research", research),
                 ("compress", compress), ("write", write)]:
    builder.add_node(name, fn)
builder.add_edge(START, "clarify")
builder.add_edge("clarify", "brief")
builder.add_edge("brief", "plan")
builder.add_edge("plan", "research")
builder.add_edge("research", "compress")
builder.add_edge("compress", "write")
builder.add_edge("write", END)
graph = builder.compile()


def run_with_updates(question: str, config: ResearchConfig) -> DeepResearchState:
    st: DeepResearchState = {"question": question, "config": config}
    for update in graph.stream(st, stream_mode="updates"):
        for node, changes in update.items():
            print(f"[{node}] updated {list(changes) if isinstance(changes, dict) else []}")
            for ev in (changes or {}).get("trace_events", []) if isinstance(changes, dict) else []:
                if ev.get("node") == "research" and node == "research":
                    print(f"  {ev['task']}: query={ev['query']!r} corpus={ev['corpus_hits']} web={ev['web_hits']}")
            if isinstance(changes, dict):
                st.update(changes)
    return st



def initialize(config, web_enabled=True):
    global llm, WEB, REPORT, BASE, PAGES, QUESTION, MODES, CONFIG, web_search_tool, web_extract_tool
    require('OPENAI_API_KEY')
    llm = chat_model()
    CONFIG = config
    WEB = bool(TAVILY_KEY) and web_enabled and config.max_web_results > 0
    REPORT = ws.load("capability_report")
    BASE = ws.load_path("corpus")
    PAGES = []
    for p in sorted(BASE.rglob("*.md")):
        text = p.read_text(encoding="utf-8", errors="ignore")
        title = next((ln.lstrip("# ").strip() for ln in text.splitlines() if ln.strip()), p.stem)
        PAGES.append({"path": str(p.relative_to(BASE)), "title": title[:120], "text": text})

    MODES = failure_modes(REPORT)
    if MODES:
        m = MODES[0]
        QUESTION = (f"The support agent fails the {m['category']} task {m['task']} in {m['runs'] - m['passed']} of {m['runs']} runs. "
                    "What are the likely causes, what does the product's documentation and transcript history say about this case, "
                    "and what change to the agent, its tools, or its corpus would fix it?")
    else:
        QUESTION = ("The support agent passes every task in its capability report. What failure should the next eval case target, "
                    "based on the product's documentation and transcript history?")

    if WEB:
        from langchain_tavily import TavilyExtract, TavilySearch
        web_search_tool = TavilySearch(max_results=CONFIG.max_web_results, topic="general", include_answer=False)
        web_extract_tool = TavilyExtract(extract_depth="basic", format="markdown")

def summarize(state):
    events = [e for e in state['trace_events'] if e.get('node') == 'research']
    observed = sorted({s for e in events for s in e.get('search_sources', [])})
    extracted = sorted({s for e in events for s in e['extracted']})
    return {'research_tasks': len(state['tasks']), 'research_loops': len(events),
            'corpus_search_calls': len(events), 'web_search_calls': len(events) if WEB else 0,
            'corpus_hits': sum(e['corpus_hits'] for e in events),
            'web_hits': sum(e['web_hits'] for e in events),
            'extraction_results': sum(len(e['extracted']) for e in events),
            'observed_sources': observed, 'extracted_sources': extracted}

def citation_audit(state):
    observed = set(summarize(state)['observed_sources'])
    report = state['final_report']
    # The writer is asked for [source] citations, not numbered references.
    inline = []
    for group, target in re.findall(r'\[([^\]\n]+)\](?:\(([^)]+)\))?', report.markdown):
        inline.extend([target] if target else [part.strip() for part in group.split(',')])
    cited = set(report.sources) | set(inline)
    return {'unobserved_citations': sorted(cited - observed),
            'search_only_citations': sorted(cited & observed - set(summarize(state)['extracted_sources'])),
            'note': 'Membership is checked, not whether the source supports the claim. Read the cited passage.'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['inspect', 'tools', 'plan', 'research', 'run'])
    parser.add_argument('--question')
    parser.add_argument('--tasks', type=int, default=3)
    parser.add_argument('--loops', type=int, default=1)
    parser.add_argument('--extracts', type=int, default=1)
    parser.add_argument('--corpus-only', action='store_true')
    parser.add_argument('--save', action='store_true')
    args = parser.parse_args()
    if args.save and args.command != 'run':
        parser.error('--save requires run')
    config = ResearchConfig(max_research_tasks=args.tasks, max_researcher_loops=args.loops, max_extract_urls=args.extracts)
    with contextlib.redirect_stdout(sys.stderr):
        initialize(config, not args.corpus_only)
        question = args.question or QUESTION
        out = {'provenance': provenance(), 'web_enabled': WEB, 'config': config.model_dump(), 'question': question}
        if args.command == 'inspect':
            out.update(pages=[p['path'] for p in PAGES], failure_modes=MODES)
        elif args.command == 'tools':
            hits = corpus_search(question)
            out.update(corpus_hits=hits, extracts=[corpus_extract(h['url']) for h in hits[:2]], web_hits=web_search(question))
        else:
            state = {'question': question, 'config': config}
            if args.command == 'run':
                # The original graph is linear: clarification is diagnostic, not a pause.
                state = run_with_updates(question, config)
            else:
                for node in (clarify, brief, plan):
                    state.update(node(state))
                if args.command == 'research':
                    state.update(research(state))
                    state.update(compress(state))
            out['state'] = state
            if 'findings' in state:
                out['summary'] = summarize(state)
            if 'final_report' in state:
                out['citation_audit'] = citation_audit(state)
                if args.save:
                    if state['clarification'].needs_clarification or out['citation_audit']['unobserved_citations']:
                        out['save_status'] = 'blocked: resolve clarification or unobserved citations; inspect the returned state and audit'
                    else:
                        report = state['final_report']
                        lines = [f"# Research report: {state['brief'].question}", '', report.markdown, '', '## Sources', '']
                        lines += [f'- {s}' for s in report.sources]
                        lines += ['', '## Open gaps', ''] + [f'- {g}' for g in report.gaps or ['none recorded']]
                        lines += ['', '## Trace', '', json.dumps(out['summary'], indent=2), '', f'Model: {LLM_MODEL}. Web search: {WEB}.']
                        ws.save('research_report', '\n'.join(lines))
                        out['save_status'] = 'saved'
    emit(out)
    if out.get('save_status', '').startswith('blocked'):
        raise SystemExit(2)

if __name__ == '__main__':
    main()
