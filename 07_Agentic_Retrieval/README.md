# DCI vs Agentic RAG

Compare the same agent loop with ranked-section retrieval and direct page tools. Inspect the wiki, evidence, answers, judge scores, and resource use before choosing an interface.

Estimated time: 35 minutes. Reads: corpus, eval_cases. Writes, when requested: wiki, agentic_runs.

## Use the guide

Open `DCI_vs_Agentic_RAG.ipynb` as a reading guide and open an interactive coding assistant in the repository. Follow the messages and inspect the results.

`agentic_tools.py` contains the experiment code. `DCI_vs_Agentic_RAG.py` is the generated marimo mirror.

Use the shared repository environment and configured `.env`. Your coding assistant's chat model and authentication are separate from the model/API key used by these experiments. Tools report their input sources. Saving requires `--save`.

Product documentation: [Codex](https://developers.openai.com/codex/), [Claude Code](https://code.claude.com/docs/en/overview), [VS Code Copilot](https://code.visualstudio.com/docs/agents/overview).

## Tool reference for your assistant

From this directory, run `uv run --no-sync python agentic_tools.py COMMAND`.

- `inspect`: current cases, page names, source provenance, and section count.
- `wiki`: generate purpose-line proposals using the configured model.
- `interfaces`: actual search, grep, and page outputs; accepts `--question`.
- `compare`: run both modes on `--question` (first case by default).
- `score`: run and judge both modes on the same case list.
- `--wiki FILE`: reuse a reviewed wiki Markdown file. Without it, a new wiki is generated for each comparison command.
- `--cases FILE`: use a reviewed JSON list with `id`, `question`, `reference`, and `pages`. Page labels must exist in the active corpus.
- `--save`: with `wiki` or `score`, save the wiki and, for scoring, actual runs through `helpers.workspace`.

Keep the proposed wiki in a scratch file outside the workspace after showing it to the student. Reuse it with `--wiki` so later experiments do not silently change the navigation map. Keep real command results available for follow-up questions; summarize those results without rerunning by default.

## What the experiment measures

The original BM25 section index, three file tools, six-turn message loop, and reference judge are preserved. Tool results are now included in traces so students can distinguish retrieval failures from answer failures. Both modes share model, prompt, question, and loop. DCI reads are capped at 12,000 characters; chunk results at 1,000 characters each. Evidence characters and elapsed seconds do not measure billed tokens. Wiki generation and judging are outside agent latency.

Scores are judge estimates. Naming an expected page is a string check. Neither establishes citation support. Missing scores and turn-limit failures remain visible. The model-written wiki is a proposal, not a human-verified description.

## Recorded example

`data/recorded_experiments.json` contains real tool results on the labeled seed fallback. New runs may differ.

`--save` runs a new experiment and saves its measured outputs. Otherwise, readers use existing workspace artifacts or the labeled seed fallback.
