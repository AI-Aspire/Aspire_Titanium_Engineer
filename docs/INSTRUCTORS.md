# Instructors

Per cohort, fill in the table and link it from the front page. Names go here
and nowhere else in the repository.

| Role | Name | Reach |
|---|---|---|
| Lead instructor | | |
| Instructor | | |
| Teaching assistant | | |
| Programme operations | | |

## Before the cohort

- Set `cohort.toml` and run `make banner`.
- Run `make check` and `make execute` on a clean clone with the keys the room will use.
- Run `uv run python scripts/check_workspace.py --seed` and read the seed capability report; it is what the first demo shows.
- Print `docs/schedule/day1.md`.

## Each day

- The last block is `make check-day D=N`. Nobody leaves with a red workspace.
- Collect one question per group for the next morning's feedback block.

## Day 4 and day 5

Day 4 is your pick of four modules from 14 to 23; `docs/schedule/day4.md`
says when each one earns its slot. Day 5 is optional and built from what the
cohort asks for. If it holds a demo day, the judges score with
`project/DEMO_SCORECARD.md`, each group's own harness runs in the room, and
the rows are written to the workspace as the `scorecard` artifact.

## Beats per module

Each block is one demo: the moment to land, the question to ask before the
answer is on screen, and the failure to expect in the room.

### 01 Dev environment

- **Reveal:** Task 3, `ws.status()`. Every row reads `seed`. Nothing the group will make exists yet, and every later notebook still runs.
- **Ask the room:** What happens to a notebook that reads an artifact nobody has produced yet?
- **What goes wrong:** `gh auth status` says not logged in, or `origin` is the course repository rather than a fork. Run `gh auth login`, then `gh repo fork --clone`, before the first cell.

### 02 Prompt patterns

- **Reveal:** Task 5, pasted context. With nothing to read, the model fluently names two users the charter never mentions. With the charter pasted in, it names the right ones.
- **Ask the room:** What will the model say when asked who the two named users are?
- **What goes wrong:** A missing-key error at setup: copy `.env.template` to `.env`. A validation error in Task 4 means no structured outputs; fall back to the few-shot JSON.

### 03 Agents 101

- **Reveal:** Task 4, the streamed trace. The in-scope question shows a `model` node calling a tool, a `tools` node returning a charter section, then the answer. The out-of-scope question calls nothing.
- **Ask the room:** Which of the four questions will call a tool?
- **What goes wrong:** A prompt count of zero at setup: run the prompt patterns notebook or let the seed carry it. Every run calling every tool: the docstrings are too vague.

### 04 Vibe checks and judges

- **Reveal:** Task 9, the second table. The gap between two judges spans zero at the real transcript count, then narrows to a difference at 100 rows drawn from the same data.
- **Ask the room:** Judge A agrees with you at 0.82, judge B at 0.74. Which is better?
- **What goes wrong:** Fewer than four hand verdicts at Task 3, so nothing to compare. A RuntimeError in Task 5: the model is not returning JSON.

### 05 RAG

- **Reveal:** Task 2, the four-row table. Same corpus, question, and model. First-token time and cached tokens change with nothing but where the question sits in the prompt.
- **Ask the room:** Which of the four calls will be cheapest, and why?
- **What goes wrong:** A page count of one at setup: prompts and transcripts are missing. A storage-folder-already-accessed error: another kernel holds `.qdrant_local/`, so shut it down.

### 06 Retrieval ladder

- **Reveal:** Task 5, one query twice. Filtering after ranking keeps fewer than four chunks, and the count and rank positions leak what the user may not read. Filtering inside the query returns four.
- **Ask the room:** If forbidden chunks are dropped after ranking, what does the user still learn?
- **What goes wrong:** The cross-encoder download fails on first use: reach the Hugging Face hub once. Every rung at 1.0: the corpus is too small.

### 07 DCI vs agentic RAG

- **Reveal:** Task 5, the per-mode averages next to the per-case traces. The averages agree; the widest-gap case shows one mode holding the right evidence and answering badly.
- **Ask the room:** Which is cheaper, an agent that reads pages or one that calls a retriever?
- **What goes wrong:** A mode ending in max turns reached is looping on one call: read its trace. A purpose column repeating page titles: the model did not return JSON.

### 08 SDG and RAGAS

- **Reveal:** Task 6. Raising `k` from 2 to 6 lifts context recall, and the interval on the faithfulness difference spans zero at six questions. The delta on screen is not a measured difference.
- **Ask the room:** `k` went from 2 to 6 and faithfulness moved a few points. Did it improve?
- **What goes wrong:** `import ragas` fails in the shared environment: `uv sync` in the module folder and pick its kernel. Zero generated questions: the corpus is too small for a graph.

### 09 Trajectory evals

- **Reveal:** Task 6, the spread table. One task, nothing changed, and min and max for steps and tool output differ by a factor of two. Both runs passed.
- **Ask the room:** A run took nine steps when you tried it. What budget do you set?
- **What goes wrong:** With `TE_SEED_MODE=1` the repeat count is 1 and every min equals its max: demo with the full budget. A simulated user that never replies `DONE` fails everything.

### 10 Three kinds of memory

- **Reveal:** Task 6. A fresh harness with an empty conversation, over the same store, names the laptop and the team from the last session. In Task 3 the old team fact is gone, not outranked.
- **Ask the room:** The session ended. Where must a fact live for the next session to know it?
- **What goes wrong:** The second session recalls nothing: the two harnesses point at different store paths. `EMBED_MODEL` must be in `.env`.

### 11 Six ways to give an agent a capability

- **Reveal:** Task 3. The notebook launches `mcp_server.py` as a subprocess, discovers three tools it never declared a schema for, and answers with one. Nobody in the notebook wrote the contract.
- **Ask the room:** Where does the schema come from for a tool you did not write?
- **What goes wrong:** The session never initialises: a stray print in the server breaks stdio. Run `uv run python mcp_server.py` in a terminal and read the error.

### 12 Multi-agent report generator

- **Reveal:** Task 2. The citation audit rejects `[99]` and a URL no tool returned, on a fixture, with no model call. Task 5 runs it under a real report.
- **Ask the room:** Who should catch a citation to a URL no agent saw: an agent or plain code?
- **What goes wrong:** A zero count at setup: the capability report or RAGAS scores are missing, so let the seed carry them. No evals kind: the report lacks `##` headings.

### 13 The guardrail ladder

- **Reveal:** Task 6. Marcus asks politely, with an approval story, for Priya's password. The role table blocks him in microseconds without reading a word. Task 7 puts coverage beside false positives.
- **Ask the room:** Which rung can no phrasing talk round?
- **What goes wrong:** The classifier blocks most benign inputs: its training words overlap the product vocabulary, so add safe examples. The judge returns a sentence, not one word: the check misreads it.

### 14 Voice deep research

- **Reveal:** Task 5, the narrated session. Each role speaks in its own voice, the critic objects aloud, and the judge sends the draft back for a second round before it passes.
- **Ask the room:** Which role in a research panel would you want to hear, and which should stay silent?
- **What goes wrong:** The module has its own environment: `uv sync` in the folder first. An empty transcript: check `STT_MODEL`. Without TTS the panel runs as text.

### 15 DSPy optimizers

- **Reveal:** Task 6. The rewritten instruction next to the original, and held-out agreement that moved by at most a few examples. Sometimes `baseline` wins on a tie: no optimizer earned its calls.
- **Ask the room:** Which optimizer will win, and by how many examples?
- **What goes wrong:** `import dspy` fails: `make setup-optim`, restart the kernel. Zero examples: no judge row carries a `human_score`, so score four transcripts by hand first.

### 16 GraphRAG

- **Reveal:** Task 6, the bar chart. The steelman vector baseline beside three graphs, and on a small corpus the baseline usually holds. The room came expecting the graph to win.
- **Ask the room:** Which condition scores higher on correctness, and by how much must the graph win to earn a rebuild schedule?
- **What goes wrong:** `make setup-graph` not run, so spaCy has no model. Ontology count zero: none of its phrases occur in the corpus, so edit `ONTOLOGY`.

### 17 Unroll deep research

- **Reveal:** Task 6, the trace summary beside the report. Most calls went to research, the writer made one, and the open-gaps section admits what it could not find.
- **Ask the room:** Which node spends most of the budget, and which decides what the report says?
- **What goes wrong:** The question falls back to the no-failure default: the table regex did not match the capability report. Corpus search returns nothing: the plan's queries are full sentences.

### 18 Off-the-shelf guardrails

- **Reveal:** Task 7, the matrix. One attack case trips nothing, and one benign question trips scope. The empty attack row is a finding for the risk register, not a bug.
- **Ask the room:** Which of the five guardrails will fire on a benign question first?
- **What goes wrong:** Every case trips scope: the corpus vocabulary is too small, so raise the `most_common` count. A benign case blocked at input: read the tripwire's `matched_terms` first.

### 19 NIST risk register

- **Reveal:** Task 5. A rubric aspect with no judge behind it becomes a Govern row: the thing nobody measured, found by plain Python with no model call. Task 6 renders the register.
- **Ask the room:** Which of your rubric aspects has no judge?
- **What goes wrong:** Map is empty: the charter has no where-it-will-be-wrong heading. Every attack shows as not blocked: `blocked` is a string, so the join needs `== "true"`.

### 20 Attack your agent

- **Reveal:** Task 4. The direct attack was refused. Then an innocent question pulls a poisoned page and the canary leaks in some of the runs. The user did nothing wrong.
- **Ask the room:** The direct attack was refused. Is the agent safe?
- **What goes wrong:** The agent never called `search_corpus`, so the poisoned page was never served and the attack cannot be scored: read `r['tool_calls']`. Every candidate saying error: the endpoint is failing.

### 21 Release decision

- **Reveal:** Task 6, the pivot. The fluent v1 answer the room believed in Task 2 fails correctness next to v2, and Task 7 names the failing metric rather than a pass rate.
- **Ask the room:** Read the v1 answer. Would you ship it?
- **What goes wrong:** A whole column reading error: the judge is not returning JSON, so print one `metric.reason`. A gate failing where every per-case row passed: a judge error scored zero.

### 22 Observability and incidents

- **Reveal:** Task 3, the chart. From the fifth day a third of the passing answers fail. Latency, cost, and refusal rate never move; only the eval score falls.
- **Ask the room:** A third of the answers just went wrong. Which line moved?
- **What goes wrong:** The eval score line does not fall: the pool has no passing runs. A non-zero failed column: the endpoint times out. Never aim the load test at shared infrastructure.

### 23 Release pipeline

- **Reveal:** Task 4, the thirteen-row table. The naive verdict promotes on every higher rate; the real one holds at forty samples, promotes only when the interval clears zero, and rolls back the slow row.
- **Ask the room:** Candidate passes 85%, baseline 80%, forty samples each. Promote?
- **What goes wrong:** Fewer than two versions in the results: run the eval notebook first. Both gate exit codes 0: rerun with a floor of 0.99.
