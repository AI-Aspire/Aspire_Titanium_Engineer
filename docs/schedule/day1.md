# Day 1: prototype and retrieve

*Ends with:* four-minute pitches per group: the problem, the users, two
prompt-only prototypes, a first agent, and a RAG baseline over the group's
own artifacts.

## Goals

- Engineering: dev environment, prompt patterns, a first agent, vibe checks and an LLM judge, RAG
- Product: a concrete problem worth solving, a product vision, where evals will matter
- Group: a charter in `project/CHARTER.md`, a corpus, and a pitch

## Modules

| # | Module | Demo | Reads | Writes |
|---|---|---|---|---|
| 01 | Dev environment | 30 min | | manifest, charter |
| 02 | Prompt patterns | 30 min | charter | prompts |
| 03 | Agents 101 | 35 min | charter, prompts | transcripts |
| 04 | Vibe checks and judges | 30 min | transcripts | rubric, vibe_checks, judge_scores |
| 05 | RAG | 30 min | charter, prompts, transcripts, vibe_checks | corpus, baseline_runs |

## Run of show

| Time | Block | Min | What |
|---|---|---|---|
| 9:00 | 🎤 | 15 | Welcome, how the week works, the course eats itself |
| 9:15 | 🧑‍🏫 | 20 | PoC, MVP, production. The project brief |
| 9:35 | 🧑‍💻 | 30 | Module 01: dev environment and workspace |
| 10:05 | 🧑‍🤝‍🧑 | 25 | Form groups. Write the charter |
| 10:30 | ☕ | 15 | |
| 10:45 | 🧑‍🏫 | 15 | Prompt patterns |
| 11:00 | 🧑‍💻 | 30 | Module 02: prompt patterns |
| 11:30 | 🧑‍🤝‍🧑 | 20 | Two prompt-only prototypes of your idea |
| 11:50 | 🧑‍🏫 | 15 | Agents 101 |
| 12:05 | 🍽 | 60 | |
| 1:05 | 🧑‍💻 | 35 | Module 03: a first agent harness |
| 1:40 | 🧑‍🤝‍🧑 | 20 | An agent prototype and a workflow diagram |
| 2:00 | 🧑‍🏫 | 15 | Vibe checks versus evals |
| 2:15 | 🧑‍💻 | 30 | Module 04: vibe checks and an LLM judge |
| 2:45 | ☕ | 15 | |
| 3:00 | 🧑‍🏫 | 15 | RAG: dense retrieval plus in-context learning |
| 3:15 | 🧑‍💻 | 30 | Module 05: RAG over your own artifacts |
| 3:45 | 🧑‍🤝‍🧑 | 30 | Write a rubric. Vibe-check both prototypes. Build the corpus and run the baseline. Prepare the pitch |
| 4:15 | 🎤 | 35 | Pitches, four minutes per group |
| 4:50 | 🧑‍🏫 | 10 | Wrap. Everyone runs `make check-day D=1` |

## Reading

- Chain of thought prompting: https://arxiv.org/abs/2201.11903
- Self-refine: https://arxiv.org/abs/2303.17651
- The LLM application stack: https://a16z.com/emerging-architectures-for-llm-applications/
- Retrieval-augmented generation: https://arxiv.org/abs/2005.11401
