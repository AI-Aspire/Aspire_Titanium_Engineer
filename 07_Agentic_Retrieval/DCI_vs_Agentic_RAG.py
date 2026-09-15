import marimo

__generated_with = "0.24.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # DCI vs agentic RAG

    Your corpus already exists as pages. The question is what interface the agent gets to it: a retriever that returns ranked chunks, or file tools that list, search, and read the pages themselves. This notebook builds both, holds everything else constant, and scores them on your eval cases.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    Two ways for an agent to reach documents: read the pages directly through a model-readable wiki, or call a retriever tool. One loop, two tool sets, and what each one reads.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    A wiki index generated from your corpus, both modes scored over your eval cases, and a table of answer quality, calls, evidence read, and latency per mode.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    Keep the cheaper mode that passes your questions and write down what kind of question would make you switch. Tell your team one question where the modes diverged.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 35 minutes
    **Reads:** corpus, eval_cases
    **Writes:** wiki, agentic_runs
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    Two terms. Direct corpus interaction, DCI, means the agent lists, searches, and reads the pages with file tools. Agentic RAG means the agent calls a retriever that returns ranked chunks and may call it again with a new query. The model, the loop, the questions, and the scoring stay the same; only the tools change.
    """)
    return


@app.cell
def _():
    import json, re, time, textwrap

    import pandas as pd
    from openai import OpenAI
    from rank_bm25 import BM25Okapi

    from helpers.config import KEY, LLM_BASE, LLM_MODEL, require, budget
    from helpers import workspace as ws, ui
    from helpers.llm import client
    from helpers.display import show
    from helpers.judge import make_judge, parse_json

    require("OPENAI_API_KEY")
    client = client()
    CORPUS_DIR = ws.load_path("corpus")
    PAGES = {}
    for p in sorted(CORPUS_DIR.rglob("*.md")):
        rel = p.relative_to(CORPUS_DIR).as_posix()
        if not rel.startswith("wiki/") and rel != "vibe_checks.md":   # the wiki is built below; the vibe checks page is the answer key
            PAGES[rel] = p.read_text(encoding="utf-8")
    CASES = ws.load("eval_cases")
    print(f"✅ model {LLM_MODEL}; {len(PAGES)} pages; {len(CASES)} eval cases")
    return (
        BM25Okapi,
        CASES,
        LLM_MODEL,
        PAGES,
        budget,
        client,
        json,
        make_judge,
        parse_json,
        pd,
        re,
        show,
        textwrap,
        time,
        ui,
        ws,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with the model, a page count above five, and at least four eval cases. Stop here if the page count is zero: the corpus has not been built, so run the RAG notebook first or let the seed carry it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Learn
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 1 of 5 — Build the wiki

    An agent with file tools needs a map, or it reads pages at random. The wiki is one markdown index: every page name, what a reader should use it for, and its section headings. The skeleton is built from the headings by hand. The model writes the one-line purpose for each page, from a digest, and you correct it.
    """)
    return


@app.cell
def _(LLM_MODEL, PAGES, client, parse_json, show, ws):
    def outline(text: str) -> tuple:
        """(title, section headings) of one markdown page."""
        lines = text.splitlines()
        title = next((l[2:].strip() for l in lines if l.startswith('# ')), '')
        return (title, [l[3:].strip() for l in lines if l.startswith('## ')])
    DIGEST = '\n'.join((f"- {name} | {outline(t)[0]} | {' '.join(t.split())[:200]}" for name, t in PAGES.items()))
    reply = client.chat.completions.create(model=LLM_MODEL, temperature=1, messages=[{'role': 'user', 'content': 'For each page below write one line, under fifteen words, saying what a reader should use it for. Return one JSON object: {"notes": [{"page": "<name>", "use_it_for": "<line>"}]}\n\n' + DIGEST}])
    parsed = parse_json(reply.choices[0].message.content) or {}
    USE = {n.get('page'): n.get('use_it_for', '') for n in parsed.get('notes', []) if isinstance(n, dict)}
    rows = ['# Wiki index', '', 'Use this index to decide which page to read. Page names are stable tool inputs.', '', '| Page | Use it for | Sections |', '|---|---|---|']
    for name, _text in PAGES.items():
        title, heads = outline(_text)
        rows.append(f"| `{name}` | {USE.get(name) or title or name} | {', '.join(heads[:5])} |")
    rows += ['', 'Suggested navigation:', '', '- Start from the charter for what the product is and refuses to do, then follow a term to the page that operates on it.', '- For a question about a past request, read the whole transcript rather than one matching line.', "- When a search matches lines on several pages, read each page's section before answering."]
    WIKI = '\n'.join(rows)
    ws.save('wiki', WIKI)
    show(WIKI)
    return (WIKI,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line and a rendered table with one row per page, a purpose line, and its sections. Stop here if the purpose column repeats the page title for every row: the model did not return JSON, so print `reply.choices[0].message.content` and check it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 5 — Two corpus interfaces

    Agentic RAG gets one tool. `search_chunks` returns the top sections by BM25 and can be called again with a new query, but it cannot list pages or ask for a whole one. DCI gets three: `list_pages` returns the wiki, `grep_wiki` returns matching lines with the page and line number, `read_page` returns a whole page. In DCI the agent, not a retriever, decides what to read next.
    """)
    return


@app.cell
def _(BM25Okapi, CASES, PAGES, WIKI, re, textwrap):
    TOKEN = re.compile('[a-z0-9$%]+')

    def tokenize(text: str) -> list:
        return TOKEN.findall(text.lower())
    chunks = []
    for page, _text in PAGES.items():
        sections = re.split('(?=^## )', _text, flags=re.M)
        for i, section in enumerate((s for s in sections if s.strip())):
            chunks.append({'id': f'{page}#s{i}', 'page': page, 'text': section.strip()})
    bm25 = BM25Okapi([tokenize(c['text']) for c in chunks])

    def search_chunks(query: str, k: int=4) -> str:
        scores = bm25.get_scores(tokenize(query))
        order = sorted(range(len(chunks)), key=lambda i: scores[i], reverse=True)[:max(1, min(k, 8))]
        return '\n\n---\n\n'.join((f"[{chunks[i]['id']}]\n{chunks[i]['text'][:1000]}" for i in order))

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
                    hits.append(f'{page}:{number}: {line}')
        return '\n'.join(hits[:40]) or '(no matches)'

    def read_page(page: str) -> str:
        return PAGES[page][:12000] if page in PAGES else f'(unknown page: {page})'

    def schema(name, description, properties, required=()):
        return {'type': 'function', 'function': {'name': name, 'description': description, 'parameters': {'type': 'object', 'properties': properties, 'required': list(required)}}}
    RAG_FUNCS = {'search_chunks': search_chunks}
    RAG_TOOLS = [schema('search_chunks', 'Search ranked corpus sections. Search again with a new query when evidence is incomplete.', {'query': {'type': 'string'}, 'k': {'type': 'integer'}}, ['query'])]
    DCI_FUNCS = {'list_pages': list_pages, 'grep_wiki': grep_wiki, 'read_page': read_page}
    DCI_TOOLS = [schema('list_pages', 'Read the wiki index: every page name, what it is for, and its sections.', {}), schema('grep_wiki', 'Search exact text or a regular expression across all pages; returns page:line: text.', {'pattern': {'type': 'string'}}, ['pattern']), schema('read_page', 'Read one complete page by its name from the index.', {'page': {'type': 'string', 'enum': sorted(PAGES)}}, ['page'])]
    MODES = {'agentic_rag': (RAG_TOOLS, RAG_FUNCS), 'dci': (DCI_TOOLS, DCI_FUNCS)}
    print(f'RAG index: {len(chunks)} sections over {len(PAGES)} pages')
    print(textwrap.shorten(search_chunks(CASES[0]['question'], 2), 300))
    print(grep_wiki('ticket')[:300])
    return (MODES,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the section count, a chunk result with a `page#s` id, and grep lines in `page:line:` form. Stop here if grep returns no matches for a word you know is in the corpus: the pattern is being compiled as a regex, so escape it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which of the four tools could leak one user's transcript into another user's answer, and what would you check on the caller before running it?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 5 — One loop for both

    The loop is the same for both modes: send the question and the tools, run whatever the model calls, append the results, repeat until it answers or hits the turn limit. It records every call and how many characters came back. Keeping the loop identical means any difference in behaviour comes from the interface, not the orchestration.
    """)
    return


@app.cell
def _(CASES, LLM_MODEL, MODES, client, json, textwrap, time):
    SYSTEM = 'Answer questions about the product only from tool evidence. Investigate before answering. Name the page you used. If the evidence is incomplete, say so.'

    def run_agent(question: str, tools: list, funcs: dict, max_turns: int=6) -> dict:
        messages = [{'role': 'system', 'content': SYSTEM}, {'role': 'user', 'content': question}]
        trace, chars, started = ([], 0, time.perf_counter())
        for _ in range(max_turns):
            msg = client.chat.completions.create(model=LLM_MODEL, temperature=1, messages=messages, tools=tools, tool_choice='auto').choices[0].message
            calls = msg.tool_calls or []
            if not calls:
                return {'answer': (msg.content or '').strip(), 'trace': trace, 'evidence_chars': chars, 'latency_s': round(time.perf_counter() - started, 2), 'stopped': 'answer'}
            shaped = [{'id': c.id, 'type': 'function', 'function': {'name': c.function.name, 'arguments': c.function.arguments}} for c in calls]
            messages.append({'role': 'assistant', 'content': msg.content or '', 'tool_calls': shaped})
            for call in shaped:
                name = call['function']['name']
                try:
                    args = json.loads(call['function']['arguments'] or '{}')
                    if name not in funcs:
                        raise KeyError(f'unknown tool {name}')
                    result = str(funcs[name](**args))
                except Exception as exc:
                    args, result = ({}, f'(tool error: {type(exc).__name__}: {exc})')
                chars += len(result)
                trace.append({'tool': name, 'args': args, 'chars': len(result)})
                messages.append({'role': 'tool', 'tool_call_id': call['id'], 'content': result})
        return {'answer': '(max turns reached)', 'trace': trace, 'evidence_chars': chars, 'latency_s': round(time.perf_counter() - started, 2), 'stopped': 'max_turns'}
    question = CASES[0]['question']
    print('Q:', question)
    for _mode, (_tools, _funcs) in MODES.items():
        _r = run_agent(question, _tools, _funcs)
        print(f"\n[{_mode}] {' -> '.join((t['tool'] for t in _r['trace'])) or '(no tools)'} | {_r['evidence_chars']} chars | {_r['latency_s']}s")
        print(textwrap.shorten(_r['answer'], 400))
    return (run_agent,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see one block per mode: the tool sequence, the characters of evidence read, the latency, and a short answer that names a page. Stop here if a mode says max turns reached: the model is looping on the same call, so read its trace before scoring anything.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Create
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 5 — Score every case

    Run every eval case through both modes. Your judge scores each answer against the reference from the eval case, 0 to 10. If the case names the pages that hold the evidence, the record also says whether the answer named one of them. Calls, evidence characters, and latency go in the same row, so a correct answer cannot hide a wasteful route.
    """)
    return


@app.cell
def _(CASES, MODES, budget, make_judge, pd, run_agent, ui, ws):
    coverage = make_judge('coverage', 'Question: {question}\nA good answer includes: {reference}\nAnswer: {response}\n\nScore 0-10 how completely and accurately the answer covers what a good answer includes.', needs_reference=True)
    RUNS = []
    for _case in ui.track(CASES[:budget(len(CASES), 3)], 'both modes'):
        for _mode, (_tools, _funcs) in MODES.items():
            _r = run_agent(_case['question'], _tools, _funcs)
            verdict = coverage({'question': _case['question'], 'response': _r['answer'], 'reference': _case['reference']})
            expected = _case.get('pages') or []
            RUNS.append({'question': _case['question'], 'mode': _mode, 'answer': _r['answer'], 'case_id': _case['id'], 'score': verdict['score'], 'rationale': verdict['rationale'], 'named_expected_page': any((p.lower() in _r['answer'].lower() for p in expected)) if expected else None, 'calls': len(_r['trace']), 'evidence_chars': _r['evidence_chars'], 'latency_s': _r['latency_s'], 'stopped': _r['stopped'], 'trace': _r['trace']})
    ws.save('agentic_runs', RUNS)
    results = pd.DataFrame(RUNS)
    ui.table(results.pivot(index='case_id', columns='mode', values='score'), title='judge score per case', float_fmt='{:.0f}')
    return (results,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with two rows per case and a table of judge scores, one column per mode. Stop here if a column is all None: the judge did not return JSON, so print one rationale and check the model's reply.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Find the case with the biggest score gap between modes. Did the losing mode retrieve the wrong evidence, or retrieve the right evidence and answer badly?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5 of 5 — Inspect the difference

    There is no universal winner. Agentic RAG is usually cheaper when a question maps to one or two sections. DCI earns its extra calls when page structure, exact identifiers, or evidence on two pages matter, and it gives the model broader raw access, which production must gate per caller. Read the traces, not only the averages.
    """)
    return


@app.cell
def _(results, textwrap, ui):
    summary = results.groupby("mode").agg(score=("score", "mean"), calls=("calls", "mean"),
                                          evidence_chars=("evidence_chars", "mean"), latency_s=("latency_s", "mean"))
    ui.table(summary, title="average per mode", float_fmt="{:.2f}")

    for case_id, group in results.groupby("case_id", sort=False):
        print(f"\n=== {case_id}: {group.iloc[0]['question']}")
        for _, row in group.iterrows():
            route = " -> ".join(t["tool"] for t in row["trace"]) or "(no tools)"
            print(f"[{row['mode']}] score {row['score']} | {route} | {row['evidence_chars']} chars")
            print("   ", textwrap.shorten(row["answer"], 260))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a two-row summary and, per case, both traces with their scores and answers. Stop here if DCI never calls `read_page`: it is answering from grep lines alone, so tighten the system prompt to require reading the page before answering.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Add two questions from your own product: one that needs an exact string from a page, and one that needs evidence from two pages. Name the pages before you run either mode. Then run both modes and say which interface you would ship for each question and why.
    """)
    return


@app.cell
def _(MODES, run_agent, textwrap):
    MY_CASES = [{'id': 'exact', 'question': '', 'reference': '', 'pages': []}, {'id': 'two_pages', 'question': '', 'reference': '', 'pages': []}]
    for _case in [c for c in MY_CASES if c['question']]:
        print(f"\n=== {_case['id']}: {_case['question']}")
        for _mode, (_tools, _funcs) in MODES.items():
            _r = run_agent(_case['question'], _tools, _funcs)
            named = [p for p in _case['pages'] if p.lower() in _r['answer'].lower()]
            print(f"[{_mode}] {' -> '.join((t['tool'] for t in _r['trace'])) or '(no tools)'} | named {named or 'no expected page'}")
            print('   ', textwrap.shorten(_r['answer'], 300))
    if not any((c['question'] for c in MY_CASES)):
        print('fill in at least one case above, then rerun')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Grow
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## From prototype to production

    | What we built | Production equivalent |
    |---|---|
    | BM25 over markdown sections | Dense or hybrid retrieval with a reranker and index freshness |
    | Every page visible to every call | Per-user authorisation on list, search, and read |
    | A wiki index written once | Generated navigation with link checks and page ownership |
    | One judge against a reference line | Human-calibrated scoring of answers and citations |
    | In-process tools and a turn limit | Timeouts, rate limits, tracing, and durable run records |
    | Two modes compared on a handful of cases | A routing decision reviewed as the corpus changes |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - File tools scoped to the corpus directory and read-only.
    - Evidence read per answer logged so cost is visible per mode.
    - A rule for which mode handles which question type, reviewed as the corpus grows.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Swap `search_chunks` for the best rung of your retrieval ladder and rerun the comparison; note which cases change sides.
    - Add a caller id to every DCI tool and refuse `read_page` on a transcript that belongs to another user.
    - Write a router: send a question to DCI only when the wiki index names a page for one of its terms, otherwise to agentic RAG, and compare cost per case.
    """)
    return


if __name__ == "__main__":
    app.run()
