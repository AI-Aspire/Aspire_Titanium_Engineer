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

    Compare two ways an agent reaches your corpus: ranked sections or tools that list, search, and read pages. Use interactive Claude Code to run the same experiment loop with each interface and inspect the evidence.
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

    Open interactive Claude Code in the repository. Use this guide as a sequence of messages. Claude runs the existing experiment tools; you inspect results and make the decisions. The experiment model comes from `.env`, independently of the model chatting with you.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to Claude

    > Read the README beside this guide and inspect agentic_tools.py. Run inspect. Tell me which model and corpus are active, whether the cases come from workspace or seed, and the page and section counts. Do not save results yet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the model, input sources, page names, and eval cases. Stop here if the corpus or cases are empty.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Read the implementation

    The README beside this guide documents the commands Claude can run. `agentic_tools.py` contains the original experiment algorithms, extracted from the code cells. The other Python file is a generated marimo view of this guide. Reading source is optional; interpreting the results is your work.

    Keep the current experiment results in the session. Ask Claude to run a new experiment only when the instructions call for one.
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to Claude

    > Run wiki and show me the proposed purpose lines beside the page headings. Explain how outline builds the skeleton before the model adds descriptions. Let me check the descriptions against the source pages before we use a reviewed wiki for comparison.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see one wiki row per page. Purpose lines are model proposals. Stop here if a description does not match its page.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 5 — Two corpus interfaces

    Agentic RAG gets one tool. `search_chunks` returns the top sections by BM25 and can be called again with a new query, but it cannot list pages or ask for a whole one. DCI gets three: `list_pages` returns the wiki, `grep_wiki` returns matching lines with the page and line number, `read_page` returns a whole page. In DCI the agent, not a retriever, decides what to read next.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to Claude

    > Run interfaces for the first eval question. Show the ranked sections, matching lines, and a whole-page result. Walk me through search_chunks, list_pages, grep_wiki, and read_page in the source. Which evidence and limits does each expose?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see section IDs, page-and-line matches, and page text. Stop here if you cannot trace a result back to its source. Whole-page reads are capped at 12,000 characters.
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

    Both modes use the same model, question, system prompt, and turn limit. Only the tool interface changes. The trace records calls, returned evidence, and elapsed time. This controls the setup; model variability still affects individual runs.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to Claude

    > Run compare on the first eval question, using the reviewed wiki if available. Show both answers and their full tool traces, evidence characters, elapsed time, and stop reason. Explain the message loop in run_agent. Keep the comparison inside that loop so both modes use the same model and settings.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see both answers and the evidence each received. Stop here if either reaches the turn limit or answers without evidence; inspect that failure before scoring.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details><summary>Recorded experiment: inspect calls beside scores</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Real seed run with <code>gpt-4.1-mini</code>. These are tool outputs, not an interactive UI capture. Full runs and evidence: <code>data/recorded_experiments.json</code>.</span>
    <table>
    <thead>
    <tr>
    <th>Case</th>
    <th>Mode</th>
    <th>Judge /10</th>
    <th>Calls</th>
    <th>Stop</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>v01</td>
    <td>agentic_rag</td>
    <td>7</td>
    <td>1</td>
    <td>answer</td>
    </tr>
    <tr>
    <td>v01</td>
    <td>dci</td>
    <td>9</td>
    <td>1</td>
    <td>answer</td>
    </tr>
    <tr>
    <td>v04</td>
    <td>agentic_rag</td>
    <td>9</td>
    <td>0</td>
    <td>answer</td>
    </tr>
    <tr>
    <td>v04</td>
    <td>dci</td>
    <td>10</td>
    <td>1</td>
    <td>answer</td>
    </tr>
    </tbody>
    </table>
    <span class="paragraph">A high judge score can coexist with zero evidence calls. That violates the experiment's evidence-only instruction even when the answer sounds right. Inspect the trace before choosing a mode. A new run may differ.</span></span>
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
    ## Task 4 of 5 — Score every case

    Run every eval case through both modes. Your judge scores each answer against the reference from the eval case, 0 to 10. If the case names the pages that hold the evidence, the record also says whether the answer named one of them. Calls, evidence characters, and latency go in the same row, so a correct answer cannot hide a wasteful route.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to Claude

    > Run score over the current eval cases with both modes, using the same reviewed wiki. Show scores and rationales per case, whether each answer names an expected page, tool calls, evidence characters, latency, and stop reason. Keep failed or missing judge scores visible. Do not save yet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see two runs per case. Naming an expected page is a string check, not proof that the citation supports the answer. Stop here if a judge score is missing.
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

    Read the biggest score gap and both routes before comparing averages. A retriever may find a useful section cheaply; file navigation may help with exact strings or evidence across pages. These are hypotheses to test on your cases. Neither interface is guaranteed to win.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to Claude

    > Using the results already produced, show mean score, calls, evidence characters, and latency by mode. Open the evidence for the largest score gap. Separate retrieval mistakes from answer mistakes. Do not choose an interface for my product; I will make that decision.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a two-row summary and the underlying runs. Stop here if a conclusion depends only on averages or on page-name matches. Evidence characters and latency are proxies, not token billing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Add two questions from your own product: one that needs an exact string from a page, and one that needs evidence from two pages. Name the pages before you run either mode. Then run both modes and say which interface you would ship for each question and why.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Describe your two cases and expected pages to Claude. Ask it to run those cases only after you have supplied your reasoning. You can inspect or modify the existing tools once you have chosen your approach.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details><summary>Keep measured artifacts for later use</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">The tool can save its real outputs through <code>helpers.workspace</code> when you ask Claude to use <code>--save</code>. This runs an experiment and saves its results; it does not export your Claude conversation. Review inputs first. If you leave the workspace empty, readers use the labeled seed fallback.</span></span>
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
