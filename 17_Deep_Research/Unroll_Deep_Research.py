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

    Use an interactive coding assistant to inspect and run a research workflow: clarify, brief, plan, research, compress, write. The existing tools research a failure from your capability report using the corpus and optional web search, then produce a report and trace.
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

    Open the repository in a coding assistant with file and terminal access. Follow the messages below; the README documents the experiment tools and environment setup.

    Product documentation: [Codex](https://developers.openai.com/codex/), [Claude Code](https://code.claude.com/docs/en/overview), [VS Code Copilot](https://code.visualstudio.com/docs/agents/overview).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to your assistant

    > Read the README beside this guide and research_tools.py. Run inspect. Show the configured model, corpus and capability-report sources, web availability, selected question, and budgets. Do not save anything yet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the input sources and whether web search is enabled. Stop here if the corpus is empty or the capability report does not describe the agent you intend to study.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Read the implementation

    Open `research_tools.py` to inspect the algorithms; the README lists its commands. Keep experiment results for later inspection, and rerun only when a task calls for it.
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to your assistant

    > Explain how failure_modes chooses the research question from the report. Show the selected row or the no-failure fallback. Walk through ResearchConfig and the typed handoffs: clarification, brief, plan, finding, dossier, and final report. Which fields carry evidence and which carry decisions?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the selected failure and six budget settings. Stop here if the parser reports no failures while the report contains failed tasks.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 6 — The tools

    Search finds candidate sources; extract reads one. Keeping them separate makes cost visible in the trace. The corpus tool is a term-overlap ranker over your pages, with the page text as its extract. The web tools are Tavily's search and extract and exist only when the key is set. Both return the same shape, so the researcher does not care which it got.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to your assistant

    > Run tools with the selected question. Show search candidates separately from extracted text and name the actual sources. Explain corpus_search and corpus_extract, then the optional Tavily wrappers. State clearly if web search is off.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see corpus candidates and excerpts, plus web results only if enabled. Stop here if no relevant source is found; a report cannot repair missing evidence.
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to your assistant

    > Run plan for the selected question. Show the clarification decision, brief, and independent search queries. If clarification is needed, show its question and let me resolve it before continuing. Explain that the current graph records this decision but does not automatically pause.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the decision, success criteria, and bounded task list. Stop here if clarification is unresolved or the queries cannot match the corpus.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 6 — Research and compress

    Each task runs in its own function with its own compact context: the miniature version of sub-agent isolation. A researcher searches the corpus and the web, extracts the best sources, reflects on gaps, and hands over a finding that cites only what it observed. Compression turns the findings into one dossier so the writer never sees raw tool output.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to your assistant

    > Run research on the agreed question. Show one task’s queries, search results, extracted source names, reflections, and finding. Then compare the findings with the compressed dossier. Explain how separate researcher contexts and the loop limit constrain the work. Keep gaps visible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see research events, findings, and a dossier. Stop here if a finding has no observed source or compression adds a claim unsupported by its inputs.
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
    <details><summary>Recorded experiment: corpus research and source limits</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Real seed run with <code>gpt-4.1-mini</code>, web search off. Explicit question: how the helpdesk assistant handles VPN routing. One research task. Full state and report: <code>data/recorded_experiments.json</code>.</span>
    <table>
    <thead>
    <tr>
    <th>Measure</th>
    <th>Observed</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>Clarification needed</td>
    <td>No</td>
    </tr>
    <tr>
    <td>Research loops</td>
    <td>1</td>
    </tr>
    <tr>
    <td>Corpus search calls</td>
    <td>1</td>
    </tr>
    <tr>
    <td>Web search calls</td>
    <td>0</td>
    </tr>
    <tr>
    <td>Extraction results</td>
    <td>2</td>
    </tr>
    <tr>
    <td>Distinct observed sources</td>
    <td>3</td>
    </tr>
    <tr>
    <td>Unobserved citations</td>
    <td>0</td>
    </tr>
    <tr>
    <td>Search-only citations</td>
    <td>1</td>
    </tr>
    </tbody>
    </table>
    <span class="paragraph">The report passed the save checks in a temporary workspace. Still check the cited passages: source membership does not verify claims.</span></span>
    </details>
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to your assistant

    > Run the complete graph on the same agreed question with the default budgets. Show the node updates in order and the research trace. This is a fresh measured run, so its plan may differ from the earlier demonstration. Explain exactly what the writer receives.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see six node updates and bounded research events. Stop here if clarification is needed or the writer received claims you cannot trace to the findings.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 6 of 6 — Inspect the trace and report

    Check the report against the sources and trace before saving. The audit flags citations absent from observed results and distinguishes sources that were only found in search from those extracted. A matching source name does not prove a claim. Open the passage and check it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to your assistant

    > Show the report, open gaps, trace summary, and citation audit from the completed run. Check each important claim against the cited passage. Distinguish observed sources from extracted sources and unsupported claims. Keep the report in the result until I choose to save it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the report and audit beside the research counts. Stop here if a citation was never observed or its passage does not support the claim.
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Tell your assistant which deeper budgets you want to test and ask it to run the same question again. Compare the actual traces and reports, then write your own explanation. The extract-URL budget affects web extraction; corpus extraction keeps its two-hit cap.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details><summary>Save results (optional)</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Ask your assistant to run the tool with <code>--save</code> to write measured results through <code>helpers.workspace</code>. This runs a new experiment. Otherwise, readers use existing workspace artifacts or the labeled seed fallback.</span></span>
    </details>
    """)
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
