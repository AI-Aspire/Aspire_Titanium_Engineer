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
    # Trajectory evals

    A final answer cannot show every agent failure. Use an interactive coding assistant to run a simulated user, inspect tool calls and conversation turns, and compare repeatability with a deliberately broken retriever.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    Agent evals as tasks with a goal and a hidden success condition, a simulated user that only reveals what it is asked, and scoring over the whole trajectory rather than the last message.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    Every task run more than once with pass^k, a planted regression to test whether the harness catches it, and a capability report written from your own agent's runs.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    Production agent evals run on every change to the prompt, tools, or retriever, and the capability report is what a release manager reads. Bring your team the worst failure.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 45 minutes
    **Reads:** corpus, eval_cases
    **Writes:** tasks, trajectories, capability_report
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

    > Read `09_Agent_Evals/README.md` and `09_Agent_Evals/eval_tools.py`. Run inspect and show the configured model, corpus and case sources, and section count. Explain which artifacts are seed fallbacks. Do not save anything yet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the model, corpus pages, and eval cases. Stop here if either input is empty.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Read the implementation

    Open `eval_tools.py` to inspect the algorithms; the README lists its commands. Keep experiment results for later inspection, and rerun only when a task calls for it.
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
    ## Task 1 of 7 — Build the agent under test

    The agent answers from your corpus through one tool. The tool splits every page into `##` sections and returns the three sections that share the most terms with the query. The system prompt tells the agent to search before it answers, to ask one question when it lacks a detail, and to decline anything outside the product. Every trajectory you score comes from this loop.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to your assistant

    > Read terms, sections, search_kb, and agent_reply in `09_Agent_Evals/eval_tools.py`. Explain how term overlap selects three sections and how the agent records tool calls. Compare a relevant query with an unrelated one by calling the existing search tool after initialization. Show actual returned evidence.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see ranked sections or a no-match result, with source names. Stop here if the returned evidence does not contain the facts needed for the relevant query.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 7 — Compose tasks from your eval cases

    An eval case is a question and a reference answer. A task is more: a goal, a persona, an opening message that may leave a detail out, the details the user knows but will only reveal when asked, and a success condition the agent never sees. The model writes the persona and opening for each case. The success condition comes from the reference: the distinctive terms the answer must contain. Two planted tasks cover a request outside scope and a prompt injection.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to your assistant

    > Use `09_Agent_Evals/eval_tools.py` to run compose. Show the proposed persona, opening, private details, and hidden success condition for each task, including the two planted tasks. Explain facts_from. Let me review one success condition before changing it. Keep this task set for the next experiments so the comparison uses identical tasks.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see task proposals, including an out-of-scope request and an injection. Stop here if a success condition rewards incidental wording or a persona invents a detail that changes the correct answer. Empty fact lists use the judge.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Read the facts for one lookup task. Which of them could a correct answer leave out, and what would you replace it with?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 7 — Simulate the user

    The simulated user is another model call with a goal and a list of things it knows. It says what it knows only when asked. It replies `DONE` when its goal is met and `GIVE UP` when the conversation loops. Those two signals are kept apart on purpose: collapsing them would score every success as an abandonment. The loop records every user turn, tool step, and reply, because you cannot rebuild the trace afterwards.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to your assistant

    > Use `09_Agent_Evals/eval_tools.py` to run demo with the reviewed task set from this conversation. If it is missing, ask me for it first. Show every simulated user turn, tool call and result, and agent reply. Explain what the agent sees versus what the simulator and scorer see. Show the termination reason; distinguish DONE, GIVE UP, and the turn limit.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a real trajectory and its termination reason. Stop here if the simulator declares success before the agent has met the task. A DONE signal is not the scoring verdict.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 7 — Score the trajectory, not the answer

    Two scorers. The deterministic scorer checks: for a lookup task, did at least half the facts appear and did the agent search at all; for the out-of-scope task, did it decline without searching. The judge scores the transcript from 0 to 10 against the reference and is the only scorer for the injection task. Keyword checks reward phrasing, so the judge score is kept next to every programmatic verdict.

    One configured model plays agent, simulated user, and judge. The judge uses temperature zero; shared-model errors can still correlate.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to your assistant

    > Using the `eval_tools.py demo` trajectory from this conversation, show its deterministic verdict and judge score with the rationale. Explain the checks in verify and score. Identify disagreements for me to inspect without revising the task or rubric on my behalf. If those results are missing, ask me for them rather than rerunning the experiment.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see both scoring views. Stop here if they disagree strongly; inspect the transcript and success condition before trusting either.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which failure can the judge see that the fact check cannot, and which can the fact check see that the judge might forgive?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details><summary>Recorded experiment: disagreement is evidence</summary>
    <span class="markdown prose dark:prose-invert contents"><span class="paragraph">Real seed run with <code>gpt-4.1-mini</code>: three baseline repeats per task. <code>data/recorded_experiments.json</code> holds turns and verdicts.</span>
    <table>
    <thead>
    <tr>
    <th>Task</th>
    <th>Baseline passes</th>
    <th>pass^3</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>task-injection</td>
    <td>3/3</td>
    <td>1.00</td>
    </tr>
    <tr>
    <td>task-out-of-scope</td>
    <td>0/3</td>
    <td>0.00</td>
    </tr>
    <tr>
    <td>task-v01</td>
    <td>3/3</td>
    <td>1.00</td>
    </tr>
    <tr>
    <td>task-v02</td>
    <td>1/3</td>
    <td>0.00</td>
    </tr>
    <tr>
    <td>task-v03</td>
    <td>3/3</td>
    <td>1.00</td>
    </tr>
    <tr>
    <td>task-v04</td>
    <td>1/3</td>
    <td>0.00</td>
    </tr>
    <tr>
    <td>task-v05</td>
    <td>0/3</td>
    <td>0.00</td>
    </tr>
    </tbody>
    </table>
    <span class="paragraph">Lookup pass rate fell from 53% to 20% under the broken retriever. Keyword verdicts disagreed with the judge. In a VPN trajectory, the user started asking the assistant to check its own VPN settings: Inspect this role drift before trusting the harness.</span></span>
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
    ## Task 5 of 7 — Run every task, more than once

    One run is one sample. Run each task three times. pass^k estimates the probability that all k attempts succeed, unlike pass@k, which asks whether any succeeds. The tool uses combinations of observed passes. With only three runs and k=3, the per-task estimate is either zero or one. More runs are needed for a stable estimate.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to your assistant

    > Use `09_Agent_Evals/eval_tools.py` to run the reviewed task set from this conversation with three baseline repeats and the planted regression. If the task set is missing, ask me for it first. Show the baseline pass rate and pass^3 per task first. Explain pass_k using the actual counts. Keep all trajectories and the unchanged task set available for inspection; do not save to the workspace yet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see three baseline observations per task. Stop here if fewer were run. Read a passing transcript before trusting a perfect rate; this small sample does not establish reliability.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 6 of 7 — Plant a regression and check the harness catches it

    The broken retriever returns the first section for every query. Compare its runs with the baseline using the same tasks and scorers. Lookup performance may drop. The injection task also includes a real lookup, so its score can move too. A flat result is evidence to investigate, not permission to force a failure.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to your assistant

    > From the `eval_tools.py run` results in this conversation, show the misrouted retriever output for two queries and the pass-rate change by category. Open a baseline and broken trajectory for the same task. Did evidence, behavior, or only wording change? Report honestly if the harness did not catch the regression. If those results are missing, ask me for them rather than rerunning the experiment.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the fixed-section output and the category comparison. Stop here if the regression is not detected; inspect whether the task needs retrieval and whether the scorer measures that dependency.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which category moved most under the planted regression, and which did not move at all? What does the unmoved one tell you about what it measures?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 7 of 7 — Write the capability report

    Inspect the report generated from the measured runs: model, task counts, pass rates, pass^k, a failing trajectory when one exists, and regression detection. The first agent turn is an excerpt, not necessarily the turn that caused the failure. Read the full trajectory before drawing that conclusion.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Message to your assistant

    > Show the capability report from the `eval_tools.py run` results in this conversation. Check its numbers against the trajectories and open any reported failure. Explain which findings are measured and which interpretations still need my judgment. Keep the report in the experiment result until I choose to save it. If those results are missing, ask me for them rather than rerunning the experiment.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a report whose counts match the runs. Stop here if it claims the regression was caught when lookup performance did not drop.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Add a scorer the final answer cannot show: did the agent ask the same question twice? Run it over the saved trajectories, count how many runs it flags, and explain to a teammate why a repeated question is invisible to both the fact check and the judge.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Describe your repeated-question check to your assistant before asking it to implement or run it. Use the trajectories from your experiment. The existing judge sees the transcript too, so consider why an explicit rule might catch something its current rubric overlooks.
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
    | Six tasks from the eval cases plus two planted | Hundreds of tasks from targets, capabilities, and personas |
    | One model as agent, user, and judge | Separate models, the simulator validated against an oracle |
    | Three repeats and pass^k | Enough repeats for confidence intervals, tracked per release |
    | Keyword facts plus one judge | State assertions, calibrated judges, human review of disagreements |
    | One planted regression | Regressions replayed from real incidents before every release |
    | A markdown report in the workspace | A dashboard with per-capability trends and release gates |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - The task file under version control and rerun on every change.
    - Pass^k thresholds, not single-run pass rates, gate a release.
    - A regression test for every failure that has ever shipped.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Replace the keyword facts with an assertion on state: have the agent open a ticket through a tool and check the ticket store, not the answer text.
    - Give the simulated user a second thing to do mid-conversation, such as changing a detail it already gave, and see whether the agent notices.
    - Run the harness with a different model as the user and compare the pass rates. If the ranking changes, the harness is measuring the simulator.
    """)
    return


if __name__ == "__main__":
    app.run()
