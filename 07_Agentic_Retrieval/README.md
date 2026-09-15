# DCI vs Agentic RAG

Compare the same agent loop with ranked-section retrieval and direct page tools. Inspect the wiki, evidence, answers, judge scores, and resource use before choosing an interface.

Estimated time: 35 minutes. Reads: corpus, eval_cases. Writes, when requested: wiki, agentic_runs.

## Use the guide

Open `DCI_vs_Agentic_RAG.ipynb` as a reading guide and open interactive Claude Code in the repository. Send the messages one at a time, inspect the evidence, and answer the questions yourself. Students do not need to type shell commands or run notebook cells.

`agentic_tools.py` contains the experiment algorithms students may inspect. `DCI_vs_Agentic_RAG.py` is the generated marimo mirror of the guide, not the tool implementation.

Use the shared repository environment and configured `.env`. Claude Code's chat model and authentication are separate from the model/API key used by these experiments. The tool prints model and workspace/seed provenance; never print credentials. Commands return JSON on stdout and progress on stderr. No workspace writes happen without `--save`.

## Tool reference for Claude

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

`data/recorded_experiments.json` contains real tool results on the labeled seed fallback. These are experiment outputs, not captures of the interactive Claude UI. Use them to illustrate what to inspect, not as expected scores for a new run.

Saving is optional. `--save` runs the experiment and stores the newly measured outputs; it does not save an earlier preview by copying its text. Downstream readers use labeled seed artifacts until you choose to produce workspace results.
