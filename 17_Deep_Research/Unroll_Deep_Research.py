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
    # Unroll deep research

    A deep research system is a workflow, not a model with a search tool. This notebook unrolls the open deep research architecture into six LangGraph nodes, points it at the top failure mode in your capability report, and writes a sourced report from your corpus and, when a key is set, the web.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    Deep research unrolled into six nodes: clarify, brief, plan, research, compress, write. Typed contracts between them and a trace you can read.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    A report on the top failure mode in your capability report, researched over your corpus with optional web search, and saved with its trace.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    In production the trace is how you defend the report. Tell your team which boundary did the most work and one gap the report admitted.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 35 minutes
    **Reads:** capability_report, corpus
    **Writes:** research_report
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    The chat model comes from `.env`. Web research runs only when `TAVILY_API_KEY` is set; without it the researchers read your corpus and the cells say so. Budget knobs are plain variables you can change before a run.
    """)
    return


@app.cell
def _():
    import json, os, re, textwrap
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from typing import Literal, TypedDict

    from IPython.display import Markdown, display
    from langchain_openai import ChatOpenAI
    from langgraph.graph import END, START, StateGraph
    from pydantic import BaseModel, Field

    from helpers.config import KEY, LLM_BASE, LLM_MODEL, TAVILY_KEY, require, budget
    from helpers import workspace as ws
    from helpers.llm import chat_model

    require("OPENAI_API_KEY")
    llm = chat_model()
    WEB = bool(TAVILY_KEY)

    REPORT = ws.load("capability_report")
    BASE = ws.load_path("corpus")
    PAGES = []
    for p in sorted(BASE.rglob("*.md")):
        text = p.read_text(encoding="utf-8", errors="ignore")
        title = next((ln.lstrip("# ").strip() for ln in text.splitlines() if ln.strip()), p.stem)
        PAGES.append({"path": str(p.relative_to(BASE)), "title": title[:120], "text": text})
    print(f"model {LLM_MODEL}; web search {'✅ Tavily' if WEB else 'ℹ off, no TAVILY_API_KEY'}")
    print(f"✅ {len(PAGES)} corpus pages and a capability report from the {ws.source('capability_report')}")
    return (
        BaseModel,
        END,
        Field,
        LLM_MODEL,
        Markdown,
        PAGES,
        REPORT,
        START,
        StateGraph,
        ThreadPoolExecutor,
        TypedDict,
        WEB,
        as_completed,
        budget,
        display,
        json,
        llm,
        re,
        textwrap,
        ws,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the model, the web search mode, and a ✅ line with a page count above five. Stop here if the page count is zero: the corpus is rendered by the retrieval notebook, or the seed carries it.
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
    ## Task 1 of 6 — The question and the contracts

    The question is the top failure mode in your capability report: the task with the lowest pass rate. Then the handoff shapes. Each stage passes a typed object to the next, so the workflow is a relay, not a long conversation. The config holds every budget knob in one place.
    """)
    return


@app.cell
def _(BaseModel, Field, REPORT, TypedDict, budget, re):
    def failure_modes(report: str) -> list[dict]:
        """Rows of the pass-rate table that did not pass every run, worst first."""
        rows = re.findall(r"^\|\s*([^|\s]+)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*/\s*(\d+)\s*\|", report, re.M)
        modes = [{"task": t, "category": c, "passed": int(p), "runs": int(n)}
                 for t, c, p, n in rows if n.isdigit() and int(n) > 0 and int(p) < int(n)]
        return sorted(modes, key=lambda m: m["passed"] / m["runs"])


    MODES = failure_modes(REPORT)
    if MODES:
        m = MODES[0]
        QUESTION = (f"The support agent fails the {m['category']} task {m['task']} in {m['runs'] - m['passed']} of {m['runs']} runs. "
                    "What are the likely causes, what does the product's documentation and transcript history say about this case, "
                    "and what change to the agent, its tools, or its corpus would fix it?")
    else:
        QUESTION = ("The support agent passes every task in its capability report. What failure should the next eval case target, "
                    "based on the product's documentation and transcript history?")
    print(QUESTION)


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


    CONFIG = ResearchConfig()
    print(CONFIG)
    return (
        CONFIG,
        ClarificationDecision,
        CompressedDossier,
        DeepResearchState,
        FinalReport,
        QUESTION,
        ResearchBrief,
        ResearchConfig,
        ResearchFinding,
        ResearchLoopNote,
        ResearchPlan,
        ResearchTask,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the research question naming a task id and a category, then the config with its six budgets. Stop here if the question is the no-failure fallback while your report shows failing tasks: the table regex did not match your report's columns.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 6 — The tools

    Search finds candidate sources; extract reads one. Keeping them separate makes cost visible in the trace. The corpus tool is a term-overlap ranker over your pages, with the page text as its extract. The web tools are Tavily's search and extract and exist only when the key is set. Both return the same shape, so the researcher does not care which it got.
    """)
    return


@app.cell
def _(CONFIG, PAGES, QUESTION, WEB, re, textwrap):
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


    if WEB:
        from langchain_tavily import TavilyExtract, TavilySearch
        web_search_tool = TavilySearch(max_results=CONFIG.max_web_results, topic="general", include_answer=False)
        web_extract_tool = TavilyExtract(extract_depth="basic", format="markdown")


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


    for hit in corpus_search(QUESTION):
        print(f"{hit['url']:<44} {hit['title']}")
    print(textwrap.shorten(corpus_extract(corpus_search(QUESTION)[0]["url"])["text"], 200) if corpus_search(QUESTION) else "no corpus hit")
    print("web:", [w["url"] for w in web_search(QUESTION)][:3] if WEB else "off")
    return corpus_extract, corpus_search, web_extract, web_search


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see up to three corpus pages with titles, one page excerpt, and either three URLs or `web: off`. Stop here if the corpus search returns nothing for the question: the task id and category share no words with your pages, so the researchers will rely on the plan's queries.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Search and extract are separate calls. If you could trace only one of them in production, which would you keep and which failure would become harder to diagnose?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 6 — Clarify, brief, plan

    Three nodes, three decisions. Clarify decides whether the question can be scoped at all. Brief turns it into a target with success criteria. Plan splits the brief into independent research tasks, each with a search-ready query. Every node appends one trace event, which is the whole observability story of this notebook.
    """)
    return


@app.cell
def _(
    CONFIG,
    ClarificationDecision,
    DeepResearchState,
    QUESTION,
    ResearchBrief,
    ResearchPlan,
    ResearchTask,
    llm,
):
    def clarify(state: DeepResearchState) -> dict:
        decision = llm.with_structured_output(ClarificationDecision).invoke([
            ("system", "You decide whether a research request has enough context to begin. "
                       "Only ask for clarification if the request is impossible to scope."),
            ("user", state["question"]),
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


    state: DeepResearchState = {"question": QUESTION, "config": CONFIG}
    for node in (clarify, brief, plan):
        state.update(node(state))
    print("clarify:", state["clarification"].needs_clarification, "|", state["clarification"].reason)
    print("brief:", state["brief"].question)
    for t in state["tasks"]:
        print(f"  task {t.name!r}: query={t.query!r}")
    return brief, clarify, plan, state


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the clarification verdict with a reason, the brief's question, and up to three tasks with short queries. Stop here if every query is a full sentence: the corpus tool matches terms, and a sentence dilutes them, so tighten the plan prompt.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 6 — Research and compress

    Each task runs in its own function with its own compact context: the miniature version of sub-agent isolation. A researcher searches the corpus and the web, extracts the best sources, reflects on gaps, and hands over a finding that cites only what it observed. Compression turns the findings into one dossier so the writer never sees raw tool output.
    """)
    return


@app.cell
def _(
    CONFIG,
    CompressedDossier,
    DeepResearchState,
    ResearchConfig,
    ResearchFinding,
    ResearchLoopNote,
    ResearchTask,
    ThreadPoolExecutor,
    as_completed,
    corpus_extract,
    corpus_search,
    json,
    llm,
    state: "DeepResearchState",
    web_extract,
    web_search,
):
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
                          "corpus_hits": len(corpus_hits), "web_hits": len(web_hits), "extracted": [e["url"] for e in extracts]})
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
        kept = [s for s in finding.sources if s in observed] or observed[:3]
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


    finding, events = run_one_task(state["tasks"][0], CONFIG)
    print(events[0])
    print(finding.summary)
    print("sources:", finding.sources)
    print("gaps:", finding.gaps)
    return compress, research


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see one trace event with the query and hit counts, a summary, the sources it kept, and its gaps. Stop here if the sources list is empty: the corpus and web both returned nothing for the query, so the finding is a guess.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Compression decides what evidence survives into the report. Name one detail from the finding above that must survive and one that can go.

    Answer:
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
    ## Task 5 of 6 — Compile and stream

    The writer gets the brief and the dossier, nothing else. The edges are the application lifecycle: clarify, brief, plan, research, compress, write. Compile the graph and stream it, watching which node updates what. Each research event prints its query so you can see where the budget went.
    """)
    return


@app.cell
def _(
    CONFIG,
    DeepResearchState,
    END,
    FinalReport,
    QUESTION,
    ResearchConfig,
    START,
    StateGraph,
    brief,
    clarify,
    compress,
    llm,
    plan,
    research,
):
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


    FINAL = run_with_updates(QUESTION, CONFIG)
    return FINAL, run_with_updates


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see six node updates in order, with one query line per research task under the research node. Stop here if the research node prints no query lines: the plan returned no tasks, and the fallback task ran with the whole brief as its query.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 6 of 6 — Inspect the trace and save the report

    Read the trace summary before the report. The report is the product; the trace is how you debug cost, latency, and source quality. Save the report with its sources, its open gaps, and the trace summary appended, so anyone reading it later can see how much research stands behind it.
    """)
    return


@app.cell
def _(FINAL, Markdown, display):
    trace = FINAL["trace_events"]
    research_events = [e for e in trace if e.get("node") == "research"]
    sources = sorted({s for f in FINAL["findings"] for s in f.sources})
    SUMMARY = {"research tasks": len(FINAL["tasks"]), "search calls": len(research_events),
               "corpus hits": sum(e["corpus_hits"] for e in research_events),
               "web hits": sum(e["web_hits"] for e in research_events),
               "sources extracted": sum(len(e["extracted"]) for e in research_events), "distinct sources": len(sources)}
    for k, v in SUMMARY.items():
        print(f"{k:<18} {v}")

    report = FINAL["final_report"]
    display(Markdown(report.markdown))
    return SUMMARY, report, sources


@app.cell
def _(FINAL, LLM_MODEL, QUESTION, SUMMARY, WEB, report, sources, ws):
    lines = [f"# Research report: {FINAL['brief'].question}", "", f"Question: {QUESTION}", "", report.markdown, "",
             "## Sources", ""] + [f"- {s}" for s in report.sources or sources] + ["", "## Open gaps", ""] + \
            [f"- {g}" for g in report.gaps or ["none recorded"]] + ["", "## Trace", "", "| measure | value |", "|---|---|"] + \
            [f"| {k} | {v} |" for k, v in SUMMARY.items()] + ["", f"Model: `{LLM_MODEL}`. Web search: {'on' if WEB else 'off'}."]
    ws.save("research_report", "\n".join(lines))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the trace summary, the rendered report with inline sources and an open-gaps section, and a ✅ line. Stop here if the report cites a source that is not in the distinct-sources list: the writer invented a citation, and the source filter in the finding step needs to run again on the report.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which node did the most for the answer, and which did the most for the cost? Would a second researcher loop have changed the report or only the bill?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Run the same question with a deeper config: more tasks, more extracts, a second researcher loop. Compare the trace summary and the two reports. Explain to a teammate what the extra budget changed in the answer and what it only added to the cost.
    """)
    return


@app.cell
def _(CONFIG, QUESTION, SUMMARY, run_with_updates, textwrap):
    deeper = CONFIG.model_copy(update={"max_research_tasks": min(CONFIG.max_research_tasks + 1, 6),
                                       "max_extract_urls": 2, "max_researcher_loops": 2})
    DEEPER = run_with_updates(QUESTION, deeper)
    deep_events = [e for e in DEEPER["trace_events"] if e.get("node") == "research"]
    print({"search calls": len(deep_events), "corpus hits": sum(e["corpus_hits"] for e in deep_events),
           "sources": len({s for f in DEEPER["findings"] for s in f.sources})}, "vs", SUMMARY)
    print(textwrap.shorten(DEEPER["final_report"].markdown, 600))
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
    | Six nodes in one linear graph | Conditional edges, a clarification branch that returns to the user, retries |
    | A term-overlap corpus tool and optional Tavily | A retrieval service with permissions, source allow-lists, and freshness rules |
    | Per-task threads as context isolation | Sub-agents with their own budgets, models, and audit trails |
    | A trace list in state | Persistent traces with cost per node and a dashboard per run |
    | One report saved as markdown | A citation verifier, human review before publish, and versioned reports |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - Search and extraction budgets per run.
    - Every claim traceable to a retrieved source in the trace.
    - Web sources allow-listed for anything customer-facing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Add a clarification branch: when `needs_clarification` is true, the graph stops and returns the question to the user instead of continuing.
    - Add a citation verifier node after write: for every bracketed source in the report, confirm it appears in the observed sources, and rewrite the sentence if not.
    - Add a source quality score (authority, freshness, relevance) to each finding and let compress drop the lowest before the writer sees them.
    """)
    return


if __name__ == "__main__":
    app.run()
