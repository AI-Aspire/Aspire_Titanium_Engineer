# Trajectory Evals

Run a simulated user against a corpus agent, inspect full trajectories, compare deterministic checks with a judge, and test whether a planted retrieval regression is detected.

Estimated time: 45 minutes. Reads: corpus, eval_cases. Writes, when requested: tasks, trajectories, capability_report.

## Use the guide

Open `Trajectory_Evals.ipynb` as a reading guide and open an interactive coding assistant in the repository. Follow the messages and inspect the results.

`eval_tools.py` contains the experiment code. `Trajectory_Evals.py` is the generated marimo mirror.

Use the shared repository environment and configured `.env`. Your coding assistant's chat model and authentication are separate from the model/API key used by these experiments. Tools report their input sources. Saving requires `--save`.

Product documentation: [Codex](https://developers.openai.com/codex/), [Claude Code](https://code.claude.com/docs/en/overview), [VS Code Copilot](https://code.visualstudio.com/docs/agents/overview).

## Tool reference for your assistant

From this directory, run `uv run --no-sync python eval_tools.py COMMAND`.

- `inspect`: active corpus, cases, section count, and provenance.
- `compose`: model-proposed tasks from up to six eval cases, plus the original out-of-scope and injection tasks.
- `demo`: one simulation and both scoring views.
- `run`: repeated baseline simulations, one broken-retriever run per task, summaries, and capability report.
- `--tasks FILE`: reuse a reviewed JSON task list from `compose` instead of generating new personas and success conditions.
- `--limit N`: source-case limit when composing; default six.
- `--repeats N`: baseline repeats; default three, minimum two.
- `--save`: with `run`, save actual tasks, trajectories, and report through `helpers.workspace`.

After `compose`, retain the returned `tasks` list in a scratch JSON file outside the workspace and reuse it with `--tasks` for demo and run. This is an experiment input, not a conversation export. Ask the student to supply any changes to success conditions; do not invent their answers or implement their Your turn scorer before they describe an approach.

For the first search demonstration, import the file with `importlib.util`, call `initialize()`, and invoke `search_kb.invoke({'query': ...})`. Importing alone does not run models. The same source exposes `simulate`, `verify`, `judge`, `score`, and `pass_k` for inspection.

## What the experiment measures

The original section ranker, LangChain agent, persona generator, simulator, deterministic checks, judge, combinatorial pass^k, and misrouted retriever remain readable in the tool file. Tool results are matched by call ID; simulator stop signals match exactly. Generated wiki and answer-key pages are excluded from retrieval.

The agent sees the user conversation and corpus tools, not hidden success conditions. The simulator sees its persona, goal, and private details; the scorer sees the task and trajectory. One configured model fills all three roles, so correlated errors remain possible.

Keyword checks can accept a wrong answer or reject a paraphrase. The decline check does not enforce the rubric's one-sentence requirement. The judge sees conversation turns and tool names; deterministic scoring decides lookup passes. With three observations, pass^3 is zero or one. The broken variant has only one observation per task: inspect traces before attributing differences to the change. The injection task includes retrieval, so it may also regress.

The report's first agent turn is only an excerpt. It does not identify the causal failure turn. No repeated-question solution is supplied; that is the student's exercise.

## Recorded example

`data/recorded_experiments.json` contains real tool results on the labeled seed fallback. Repeated tool evidence is stored as character counts and SHA-256 hashes; live runs return full evidence. New runs may differ.

`--save` runs a new experiment and saves its measured outputs. Otherwise, readers use existing workspace artifacts or the labeled seed fallback.
