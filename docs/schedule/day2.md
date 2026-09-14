# Day 2: retrieval

*Ends with:* five-minute demos per group: the corpus, the retrieval pipeline,
the eval numbers, and one change that measurably helped.

## Goals

- Engineering: RAG, a retrieval ladder, agentic retrieval, synthetic test sets and RAGAS
- Product: product sense and user empathy; who will use this and what they will ask
- Group: a RAG baseline over the group's own artifacts, measured

## Modules

| # | Module | Demo | Reads | Writes |
|---|---|---|---|---|
| 05 | RAG | 30 min | charter, prompts, transcripts, vibe_checks | corpus, baseline_runs |
| 06 | Advanced retrieval | 35 min | corpus, vibe_checks | eval_cases, ladder |
| 07 | Agentic retrieval | 30 min | corpus, eval_cases | wiki, agentic_runs |
| 08 | SDG and RAGAS | 30 min | corpus | testset, ragas_scores |

## Run of show

| Time | Block | Min | What |
|---|---|---|---|
| 9:00 | 🧑‍🏫 | 15 | Feedback on the pitches. What the workspace now holds |
| 9:15 | 🧑‍🏫 | 20 | RAG: dense retrieval plus in-context learning |
| 9:35 | 🧑‍💻 | 30 | Module 05: RAG over your own artifacts |
| 10:05 | 🧑‍🤝‍🧑 | 30 | Build the corpus. Run the baseline |
| 10:35 | ☕ | 15 | |
| 10:50 | 🧑‍🏫 | 15 | The retrieval ladder |
| 11:05 | 🧑‍💻 | 35 | Module 06: BM25, hybrid, rerank, measured |
| 11:40 | 🧑‍🤝‍🧑 | 35 | Draw the RAG diagram. Write eval cases |
| 12:15 | 🍽 | 60 | |
| 1:15 | 🧑‍🏫 | 15 | Agentic retrieval and model-readable wikis |
| 1:30 | 🧑‍💻 | 30 | Module 07: direct corpus interaction versus agentic RAG |
| 2:00 | 🧑‍🏫 | 20 | Synthetic data and RAGAS |
| 2:20 | 🧑‍💻 | 30 | Module 08: generate a test set, measure, change one thing |
| 2:50 | ☕ | 15 | |
| 3:05 | 🧑‍🤝‍🧑 | 60 | Measure your pipeline. Improve one thing. Measure again |
| 4:05 | 🎤 | 45 | Demos, five minutes per group |
| 4:50 | 🧑‍🏫 | 10 | Wrap. `make check-day D=2` |

## Reading

- Retrieval-augmented generation: https://arxiv.org/abs/2005.11401
- BM25: https://www.nowpublishers.com/article/Details/INR-019
- Reciprocal rank fusion: https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf
- 12-factor agents, own your context window: https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md
- In defense of evals: https://www.sh-reya.com/blog/in-defense-ai-evals/
