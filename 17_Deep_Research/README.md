# Unroll Deep Research

Inspect a six-node research workflow, run it on a measured capability failure, and check the findings, compressed dossier, report, and source trace.

Estimated time: 35 minutes. Reads: capability_report, corpus. Writes, when requested: research_report.

## Use the guide

Open `Unroll_Deep_Research.ipynb` as a reading guide and open an interactive coding assistant in the repository. Send the messages one at a time, inspect the evidence, and answer the questions yourself. Students do not need to type shell commands or run notebook cells.

`research_tools.py` contains the experiment algorithms students may inspect. `Unroll_Deep_Research.py` is the generated marimo mirror of the guide, not the tool implementation.

Use the shared repository environment and configured `.env`. Your coding assistant's chat model and authentication are separate from the model/API key used by these experiments. The tool prints model and workspace/seed provenance; never print credentials. Commands return JSON on stdout and progress on stderr. No workspace writes happen without `--save`.

For Codex, Claude Code, Copilot, or another coding assistant, see [agent setup and controls](../docs/CODING_AGENTS.md). Use file and terminal tools in the environment where the repository dependencies are installed.

## Tool reference for your assistant

From this directory, run `uv run --no-sync python research_tools.py COMMAND`.

- `inspect`: input sources, selected failure, question, budgets, and web availability.
- `tools`: actual corpus search and extraction, plus optional web search.
- `plan`: clarification decision, brief, and bounded task list.
- `research`: plan, researcher loops, findings, and compressed dossier.
- `run`: stream the full LangGraph workflow; return all state, report, trace summary, and citation audit.
- `--question TEXT`: use the question the student agreed to study.
- `--tasks N`, `--loops N`, `--extracts N`: research tasks, loops per task, and web extraction URLs per loop. Defaults: three, one, one.
- `--corpus-only`: disable optional Tavily use explicitly.
- `--save`: with `run`, save the measured report and trace through `helpers.workspace`. Unresolved clarification or unobserved citations prevent saving. The tool still returns the state and audit with a blocked save status and exit code 2, so the failed check is inspectable.

Each command is a fresh experiment. Keep a result to inspect later nodes without rerunning. Use the same explicit question and budgets for controlled comparisons; plans may still vary. Do not run the student's deeper-budget exercise or write its interpretation until they choose their approach.

## What the experiment measures

The original typed contracts, term-overlap search, optional Tavily wrappers, isolated researcher functions, thread pool, reflection loop, compression, writer, and LangGraph are preserved. Clarification receives the actual corpus page list and capability report so it can identify available inputs. The graph remains linear: clarification records a decision but does not stop execution. In the interactive guide, pause after the planning command if clarification is needed.

No Tavily key is required for corpus research. When web search is off, the extract-URL setting has no effect. Corpus extraction reads up to two hits per loop, capped at 3,000 characters each. Search and extraction budgets limit evidence, not total tokens or billing. Trace counts are not latency or dollar-cost measurements.

Traces include search-source identities as well as extracted sources. The citation audit checks source membership and identifies search-only citations. It does not verify entailment, freshness, or authority. A source being observed is not proof of a claim. The finding filter drops unobserved source names instead of silently substituting other citations. Open gaps remain part of the report.

## Recorded example

`data/recorded_experiments.json` contains real tool results on the labeled seed fallback. These are experiment outputs, not captures of a coding assistant UI. Use them to illustrate what to inspect, not as expected scores for a new run.

Saving is optional. `--save` runs the experiment and stores the newly measured outputs; it does not save an earlier preview by copying its text. Downstream readers use labeled seed artifacts until you choose to produce workspace results.
