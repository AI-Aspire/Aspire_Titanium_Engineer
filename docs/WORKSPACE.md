# The workspace

What the cohort produces, and how later notebooks read it back.

## Two roots, one API

| Root | Path | Tracked | Purpose |
|---|---|---|---|
| workspace | `workspace/` (or `TE_WORKSPACE`) | no | the cohort's own artifacts |
| seed | `data/seed/` | yes | the instructors' worked example, Deskmate |

Notebooks never open either path directly. They call:

```python
from helpers import workspace as ws
rows = ws.load("transcripts")       # workspace if present and valid, else seed
ws.save("judge_scores", rows)       # validates, writes, records in manifest.json
ws.build_corpus()                   # renders earlier artifacts to corpus/*.md
```

`load()` prints one line when it falls back to the seed, so a student always
knows whose data they are looking at.

## Artifacts

The schema lives in `helpers/workspace.py` (`SCHEMA`). Directories are named
after the artifact, never after a day, so a reorder never moves data.

| Artifact | Path | Format | Producer | Required keys |
|---|---|---|---|---|
| manifest | `manifest.json` | json | 01 | cohort, created, writes |
| charter | `pitch/charter.md` | md | 01 | |
| prompts | `prompts/prompts.jsonl` | jsonl | 02 | pattern, input, output, model |
| transcripts | `transcripts/transcripts.jsonl` | jsonl | 03 | id, turns, tool_calls |
| rubric | `evals/rubric.json` | json | 04 | criteria |
| vibe_checks | `evals/vibe_checks.jsonl` | jsonl | 04 | id, input, expected |
| judge_scores | `evals/judge_scores.jsonl` | jsonl | 04 | id, judge, score, rationale |
| corpus | `corpus/` | dir | 05 | |
| baseline_runs | `retrieval/baseline_runs.jsonl` | jsonl | 05 | question, answer, contexts |
| eval_cases | `retrieval/eval_cases.jsonl` | jsonl | 06 | id, question, reference |
| ladder | `retrieval/ladder.csv` | csv | 06 | retriever, hit_rate, mrr |
| wiki | `corpus/wiki/index.md` | md | 07 | |
| agentic_runs | `retrieval/agentic_runs.jsonl` | jsonl | 07 | question, mode, answer |
| testset | `retrieval/testset.jsonl` | jsonl | 08 | question, reference |
| ragas_scores | `retrieval/ragas_scores.csv` | csv | 08 | variant, faithfulness |
| tasks | `agent/tasks.jsonl` | jsonl | 09 | id, goal, success |
| trajectories | `agent/trajectories.jsonl` | jsonl | 09 | id, task_id, steps, passed |
| capability_report | `agent/capability_report.md` | md | 09 | |
| memory | `memory/MEMORY.md` | md | 10 | |
| episodes | `memory/episodes.jsonl` | jsonl | 10 | id, summary |
| tools_catalog | `agent/tools_catalog.json` | json | 11 | tools |
| multi_agent_report | `research/multi_agent_report.md` | md | 12 | |
| guardrail_cases | `guardrails/cases.jsonl` | jsonl | 13 | id, input, attack, expected |
| ladder_results | `guardrails/ladder_results.jsonl` | jsonl | 13 | case_id, rung, blocked |
| voice_sessions | `research/voice_sessions.jsonl` | jsonl | 14 | id, question, answer |

The voice sessions are the one optional artifact: the notebook needs the speech services running, and nothing later reads the file, so the seed may not carry it.
| dspy_program | `research/dspy_program.json` | json | 15 | optimizer |
| graph | `retrieval/graph.json` | json | 16 | nodes, edges |
| graph_eval | `retrieval/graph_eval.json` | json | 16 | graph, vector |
| research_report | `research/report.md` | md | 17 | |
| ots_results | `guardrails/ots_results.jsonl` | jsonl | 18 | case_id, guardrail, tripped |
| risk_register | `demo/risk_register.md` | md | 19 | |
| owasp_findings | `guardrails/owasp_findings.jsonl` | jsonl | 20 | id, category, succeeded |
| deepeval_results | `demo/deepeval_results.jsonl` | jsonl | 21 | test, version, passed |
| release_decision | `demo/release_decision.md` | md | 21 | |
| scorecard | `demo/scorecard.jsonl` | jsonl | project | group, criterion, score |

## Checking it

```bash
make check-day D=2                          # validate everything produced through day 2
uv run python scripts/check_workspace.py --seed   # validate the committed seed
uv run python scripts/check_workspace.py --status # where each artifact comes from
```

Run `make check-day` at the end of each day before anyone leaves. A missing or
invalid artifact is found in the room, not the next morning.

## The seed

`data/seed/` is produced by `make seed`, which runs the notebooks headlessly
with `TE_WORKSPACE=data/seed` and `TE_SEED_MODE=1` (small budgets, fixed
random seeds), then anonymises emails and phone numbers and validates.

Three inputs are hand-authored and never overwritten:

- `data/seed/pitch/charter.md`: the Deskmate charter
- `data/seed/corpus/kb/*.md`: the helpdesk knowledge base
- `data/seed/transcripts/tickets_raw.jsonl`: raw tickets the first notebooks draw on

Keep the seed under 5 MB. No embedding caches, no vector store directories.
