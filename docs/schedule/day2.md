# Day 2: retrieval and agent evals

*Ends with:* five-minute demos per group: the retrieval pipeline, the eval
numbers, one change that measurably helped, and the first capability report
for the group's agent.

## Goals

- Engineering: a retrieval ladder, agentic retrieval, synthetic test sets and RAGAS, agent evals from simulated trajectories
- Product: product sense and user empathy; who will use this and what they will ask
- Group: a measured RAG pipeline and an agent with a capability report

## Modules

| # | Module | Demo | Reads | Writes |
|---|---|---|---|---|
| 06 | Advanced retrieval | 35 min | corpus, vibe_checks | eval_cases, ladder |
| 07 | Agentic retrieval | 30 min | corpus, eval_cases | wiki, agentic_runs |
| 08 | SDG and RAGAS | 30 min | corpus | testset, ragas_scores |
| 09 | Agent evals | 35 min | corpus, eval_cases | tasks, trajectories, capability_report |

## Run of show

| Time | Block | Min | What |
|---|---|---|---|
| 9:00 | 🧑‍🏫 | 15 | Feedback on the pitches. What the workspace now holds |
| 9:15 | 🧑‍🏫 | 15 | The retrieval ladder |
| 9:30 | 🧑‍💻 | 35 | Module 06: BM25, hybrid, rerank, measured |
| 10:05 | 🧑‍🤝‍🧑 | 30 | Draw the RAG diagram. Write eval cases |
| 10:35 | ☕ | 15 | |
| 10:50 | 🧑‍🏫 | 15 | Agentic retrieval and model-readable wikis |
| 11:05 | 🧑‍💻 | 30 | Module 07: direct corpus interaction versus agentic RAG |
| 11:35 | 🧑‍🏫 | 15 | Synthetic data and RAGAS |
| 11:50 | 🧑‍💻 | 30 | Module 08: generate a test set, measure, change one thing |
| 12:20 | 🍽 | 60 | |
| 1:20 | 🧑‍🤝‍🧑 | 40 | Measure your pipeline. Improve one thing. Measure again |
| 2:00 | 🧑‍🏫 | 20 | Agent evals: tasks, trajectories, pass rates |
| 2:20 | 🧑‍💻 | 35 | Module 09: simulate and score trajectories |
| 2:55 | ☕ | 15 | |
| 3:10 | 🧑‍🤝‍🧑 | 45 | Write three scenarios. Run the harness. Prepare the demo |
| 3:55 | 🎤 | 45 | Demos, five minutes per group |
| 4:40 | 🧑‍🏫 | 20 | Wrap. `make check-day D=2` |

## Reading

- BM25: https://www.nowpublishers.com/article/Details/INR-019
- Reciprocal rank fusion: https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf
- 12-factor agents, own your context window: https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md
- In defense of evals: https://www.sh-reya.com/blog/in-defense-ai-evals/
- RAGAS: https://docs.ragas.io
