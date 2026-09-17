---
marp: true
theme: default
paginate: true
size: 16:9
---

# Today: making retrieval measurable

- 06 Advanced retrieval — 35m
- 07 Agentic retrieval — 30m
- 08 SDG and RAGAS — 30m

<!--
Day 2 delivery map from the supplied formal schedule:
- 08:15–08:30: evaluation foundation before the evals notebook demo.
- 09:15–09:30: RAG foundation before the retrieval blocks.
- 09:45–10:05: Module 06 concept introduction; the 10:05 demo owns notebook mechanics.
- Module 07 is selected in the instructor matrix but has no explicit clock slot in the supplied schedule. Keep its concept block ready, but confirm whether it is taught inside the retrieval block or moved to another day.
- 11:30–12:00: Module 08 concept introduction; Beric's 12:00 demo owns notebook mechanics.
-->

# Today: making the agent's evidence trustworthy

06 Advanced retrieval · 35m  ·  07 Agentic retrieval · 30m  ·  08 SDG and RAGAS · 30m

<!--
Slide ID: D2-F0
Module: Day 2 foundation
Instructor: Miriah
Type: framing
Minutes: 2
Layout: 02 Agenda
Speaker notes:
- Say: Today we turn one retrieval guess into evidence we can inspect and improve.
- Ask: Which part of the journey needs evidence before your group can defend it?
- Watch: Keep the three module blocks as one progression: retrieve, compare, measure.
- Then: Yesterday's framing remains the starting point; now move into the day-2 questions.
Sources: Notebook:cell#27; [Day 2 schedule](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/schedule/day2.md); [Module 06 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md).
-->

---

# From a prototype to a measured retrieval system

- Yesterday: a question, prompt, agent, and first RAG baseline
- Today: evidence, retrieval choices, and repeatable measurement
- Deliverable: explain what changed and what the evidence says

<!--
Slide ID: D2-F1
Module: Day 2 foundation
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 01 Title
Speaker notes:
- Say: Yesterday you got an answer. Today you find out whether it was luck.
- Ask: What did yesterday's prototype leave uncertain?
- Watch: Groups name one uncertainty before choosing a retrieval technique.
- Then: Start with the measurement question, not the metric name.
Sources: [Day 2 schedule](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/schedule/day2.md); [Module 05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md).
-->

---
# Three kinds of retrieval, named

| | Matches on | Finds `VPN-4312` | Finds "remote access" |
|---|---|---|---|
| **Sparse** (BM25) | exact words | yes | no |
| **Dense** (embeddings) | meaning | often not | yes |
| **Hybrid** | both, then fuse | yes | yes |

Example question: `VPN-4312 fails after a password reset` — it needs both signals.

<!--
Slide ID: D2-M06-C1
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 05 Two column
Speaker notes:
- Say: An exact code and a vague description are different search problems; one retriever cannot be good at both.
- Ask: Which part of the question would dense retrieval risk blurring, and which part would BM25 preserve?
- Watch: Retrieval_Ladder Task 2 prints dense and scratch/library BM25 orders for one question; compare the disagreement. Retrieval_Ladder:cell#9 is Task 1 of 5 — Label the evidence.
- Then: A reranker is a later model that reads the question and candidate passage together to reorder a shortlist.
Sources: [Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/); [Lucene BM25Similarity](https://lucene.apache.org/core/9_12_1/core/org/apache/lucene/search/similarities/BM25Similarity.html); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---
# Which method would you use for each question?

| Question | Against |
|---|---|
| "what does `uv sync` remove?" | `python-environments.md` |
| "why can't I reach staging?" | `vpn.md` |
| "how long until someone looks at this?" | the whole KB |

<!--
Slide ID: D2-M06-C1B
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 04 Icon cards
Speaker notes:
- Say: Three real pages from the course corpus. The question shape, not the topic, decides the method.
- Ask: Audience — take one row at a time. Row three is the interesting one: nobody knows which page answers it.
- Watch: `uv sync` is a literal string on the page. "reach staging" never appears — the page says split tunnelling. The third question is answered by a priority table in `tickets.md` that the user cannot name. Retrieval_Ladder:cell#12 is Task 2 of 5 — Dense and sparse.
- Then: Reveal it — exact strings are sparse, described symptoms are dense, and unknown-page is hybrid.
Sources: [Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/); [Lucene BM25Similarity](https://lucene.apache.org/core/9_12_1/core/org/apache/lucene/search/similarities/BM25Similarity.html); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---
# Exact strings are sparse; descriptions are dense

- **`uv sync`** → sparse. It is a literal token on the page.
- **"reach staging"** → dense. The page says *split tunnelling*, never those words.
- **unknown page** → hybrid. You cannot predict which arrives.

The two signals surface different candidates, so the set differs before any ranking happens.
<!--
Slide ID: D2-M06-C1A
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Hybrid is the default precisely because you cannot know the question shape in advance.
- Ask: Take answers from two tables before revealing; the wrong answers are the teachable ones.
- Watch: Point to the visible evidence and the notebook artifact. Retrieval_Ladder:cell#9 is Task 1 of 5 — Label the evidence.
- Then: Which raises the next question: once you have two ranked lists, how do you merge them?
Sources: [Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/); [Lucene BM25Similarity](https://lucene.apache.org/core/9_12_1/core/org/apache/lucene/search/similarities/BM25Similarity.html); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---
# Fusion: merging two ranked lists

Retrieval is **two stages with separate budgets** — cheap candidate generation, then expensive inspection.

**Reciprocal rank fusion** is the cheap stage. It scores a page by where it lands in each list, then merges:

```text
sparse:  [A, B, C]      a page ranked highly by BOTH
dense:   [C, A, D]      rises above one ranked highly by one
         ──────────
RRF:     [A, C, B, D]
```

Arithmetic — no model call. That is why it comes first.

<!--
Slide ID: D2-M06-C2
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 06 Process steps
Speaker notes:
- Say: Fusion is the cheapest thing on the ladder: it is arithmetic over two orderings, with no model in the loop.
- Ask: If the correct passage never enters the fused shortlist, can reranking recover it?
- Watch: Retrieval_Ladder Task 3 prints the fused list and cross-encoder order; inspect how many candidates reach the reranker. Retrieval_Ladder:cell#12 is Task 2 of 5 — Dense and sparse.
- Then: Now the expensive rung — a reranker that actually reads the passages.
Sources: [Dense Passage Retrieval for Open-Domain Question Answering](https://aclanthology.org/2020.emnlp-main.550/), [Reciprocal rank fusion paper](https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf), [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---
# A reranker reads the passage, not just the score

Fusion never opens a page — it merges positions. A **cross-encoder reranker** does read:

| Stage | Sees | Cost |
|---|---|---|
| Sparse / dense | the query, the index | one search |
| Fusion (RRF) | two orderings | arithmetic |
| **Reranker** | query **and** passage text, together | one model call per candidate |

So a reranker is accurate and expensive — you run it on a shortlist, never the corpus.

<!--
Slide ID: D2-M06-C2B
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 05 Two column 2
Speaker notes:
- Say: This is the first rung that costs a model call, and it is the first that actually reads the text.
- Ask: Now the room can answer the next slide's question. Ask it before advancing.
- Watch: Retrieval_Ladder Task 3 prints the fused list and cross-encoder order; inspect how many candidates reach the reranker. Retrieval_Ladder:cell#12 is Task 2 of 5 — Dense and sparse.
- Then: Pose it directly: if the right page is not in the shortlist, can the reranker rescue it?
Sources: [Reciprocal rank fusion paper](https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---
# A reranker cannot recover what was never retrieved

**If the right page is absent from the shortlist, the reranker cannot find it.**

It only reorders what earlier stages handed it. So:

- Tune **recall** first — sparse, dense, fusion, multi-query
- Spend the reranker on a shortlist you already trust

<!--
Slide ID: D2-M06-C2A
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Every later stage is a reordering. Recall is the only stage that can add a page.
- Ask: Take answers from two tables before revealing; the wrong answers are the teachable ones.
- Watch: Point to the visible evidence and the notebook artifact. Retrieval_Ladder:cell#12 is Task 2 of 5 — Dense and sparse.
- Then: Tie the answer to the notebook artifact before moving on.
Sources: [Reciprocal rank fusion paper](https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---
# Multi-query: ask the same thing three ways

One phrasing searches one neighbourhood. **Multi-query** rewrites the question and searches with each:

```text
original:   How do I restore VPN access?
rewrite A:  VPN password reset procedure
rewrite B:  remote access account locked
```

Each rewrite retrieves its own list; the results are fused. It helps only when a rewrite surfaces a page the original missed — new source IDs, not a longer list.

<!--
Slide ID: D2-M06-C3
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 06 Process steps 1
Speaker notes:
- Say: Multi-query is a recall move: it buys coverage by paying for extra searches, not by ranking better.
- Ask: What evidence would show that a rewrite changed coverage rather than merely added duplicates?
- Watch: Retrieval_Ladder Task 3 prints three rewrites and one list per retriever; compare per-case reciprocal ranks in Task 4. Retrieval_Ladder:cell#17 is Task 3 of 5 — Fuse, rerank, expand.
- Then: Watch the source IDs when this runs — repeated IDs mean you paid for nothing.
Sources: [Iterative query generation for multi-hop QA](https://aclanthology.org/D19-1261/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---
# Two ways to measure a retriever

Ranks of the correct page across three questions: `[2, 8, not found]`

| Metric | Asks | On this example |
|---|---|---|
| **hit@5** | did it land in the top 5 at all? | `1/3` — only rank 2 qualifies |
| **MRR** | how *early* did it land? | `(1/2 + 1/8 + 0) / 3` |

hit@5 is a pass/fail cutoff. MRR rewards being early. Illustrative numbers, not cohort results.

<!--
Slide ID: D2-M06-C4
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 07 Big stats
Speaker notes:
- Say: Two metrics, two different questions — and a rung can improve one while leaving the other flat.
- Ask: Rank 8 contributes 1/8 to MRR and nothing to hit@5. Which metric would you report to a stakeholder, and why?
- Watch: Work the arithmetic on screen. The "not found" case contributes zero to both, which is what makes recall the first thing to fix. Retrieval_Ladder:cell#22 is Task 4 of 5 — Score the ladder.
- Then: Now the choosing rule, on the next slide.
Sources: [Lucene BM25Similarity](https://lucene.apache.org/core/9_12_1/core/org/apache/lucene/search/similarities/BM25Similarity.html), [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---
# Choose the cheapest rung that clears the bar

| Signal | What it decides |
|---|---|
| Coverage — **hit@5** | is the evidence reaching the model at all? |
| Ranking — **MRR** | is it arriving early enough to use? |
| Latency and cost | can you afford this rung in production? |

Add a rung only when the cheaper one misses your bar. Then stop.

<!--
Slide ID: D2-M06-C4X
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 04 Icon cards
Speaker notes:
- Say: The ladder is not a checklist to complete. Each rung has to earn its latency.
- Ask: A reranker lifts MRR but hit@5 does not move. Did the rung earn its cost?
- Watch: The answer is usually no — if coverage did not change, a cheaper stage was already finding the page. Retrieval_Ladder:cell#22 is Task 4 of 5 — Score the ladder.
- Then: The last rung is the one nobody measures: filtering before you rank.
Sources: [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# A correct page moves from rank 4 to rank 2. Which metric improves?

<!--
Slide ID: D2-M06-C4B
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes:
- Say: Choose the cheapest rung that clears the bar
- Ask: Which evidence would change your conclusion?
- Watch: Retrieval_Ladder Task 4 prints hit rate, MRR, latency, and a per-case reciprocal-rank matrix; use the matrix to choose one rung. Retrieval_Ladder:cell#22 is Task 4 of 5 — Score the ladder.
- Then: Reveal it — “A correct page moves from rank 4 to rank 2”.
Sources: [DPR retrieval formulation](https://aclanthology.org/2020.emnlp-main.550/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---
# A correct page moves from rank 4 to rank 2

**MRR improves. hit@5 does not move.**

| | rank 4 | rank 2 |
|---|---|---|
| hit@5 — inside the top 5? | yes | yes → **no change** |
| MRR — how early? | `1/4` | `1/2` → **doubles** |

Both ranks already cleared the cutoff, so a coverage metric cannot see the improvement. Pick the metric that answers your question before you report a win.
<!--
Slide ID: D2-M06-C4A
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: A real improvement that one of your two metrics is blind to — which is why you report both.
- Ask: Reverse it: what change would move hit@5 but leave MRR flat? Finding a page that was previously missing entirely.
- Watch: Point to the visible evidence and the notebook artifact. Retrieval_Ladder:cell#22 is Task 4 of 5 — Score the ladder.
- Then: Coverage and ranking are different claims. The last rung in this module is the one that affects neither.
Sources: [DPR retrieval formulation](https://aclanthology.org/2020.emnlp-main.550/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---
# Filter before you rank

A helpdesk agent gets: *"Why can't I reach the staging database from the VPN?"*

The KB holds pages for every team, plus other people's tickets. So:

1. Identify the caller
2. Scope the index to the pages that caller may read
3. Rank only those candidates

**Retrieval is not an authorisation check.**
<!--
Slide ID: D2-M06-C5
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 06 Process steps
Speaker notes:
- Say: A strong ranker can still return the wrong user's evidence.
- Ask: Where in the pipeline would you attach the caller's identity?
- Watch: Use Priya's staging-database question and Marcus's helpdesk scope as the contrast.
- Then: Make the ordering explicit: authorize, filter, rank.
Sources: Notebook:cell#27; [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->

---
# 07 · Agentic retrieval

**Who decides how to search — you, or the agent?** · 30 min

- Module 06 tuned a pipeline you control
- Module 07 hands the search itself to the agent

<!--
Slide ID: D2-T07
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: transition
Minutes: 0
Layout: 01 Title
Speaker notes:
- Say: Everything so far was a pipeline with fixed stages. Now the agent chooses its own next move.
- Ask: Hold for a beat — this is the hand-off, not content.
- Watch: The trade is control for adaptability, and the cost is that no two runs look the same.
- Then: Straight into the two interfaces.
Sources: [Module 07 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md).
-->
---
# Two ways to give an agent the corpus

| Interface | First move | What it can inspect next |
|---|---|---|
| **Agentic RAG** — calls a retriever | rank matching chunks | another query, or a new result set |
| **DCI** — direct corpus interaction | list and search *pages* | headings, the full page, neighbouring sections |

Same question, different evidence path.

<!--
Slide ID: D2-M07-C1
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 06 Process steps
Speaker notes:
- Say: Retrieval is not one design. Choosing the interface is choosing what the agent can discover.
- Ask: What stays constant in the notebook comparison, and what is deliberately changed?
- Watch: DCI_vs_Agentic_RAG setup defines both modes and keeps model, loop, questions, and scoring the same. DCI_vs_Agentic_RAG:cell#9 is Task 1 of 5 — Build the wiki.
- Then: Hold this until the notebook block, where the numbers appear.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---
# The loop shape differs

```text
Agentic RAG:  question → search_chunks → ranked sections → answer or search again

DCI:          question → list/search/read → chosen page → answer or search again
```

Example question: `Which VPN policy applies to contractors?`

A retriever returns fragments it scored. File tools let the agent navigate to the page and read around the answer.

<!--
Slide ID: D2-M07-C1X
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 06 Process steps
Speaker notes:
- Say: The difference is what the agent can do after its first look.
- Ask: For a policy question that spans two sections, which loop gets you the whole answer?
- Watch: DCI can read neighbouring sections; a chunk retriever returns only what it scored. DCI_vs_Agentic_RAG:cell#12 is Task 2 of 5 — Two corpus interfaces.
- Then: Holding everything else constant is what makes the comparison mean anything.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242), [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---
# To compare the two interfaces fairly, what must stay the same?
<!--
Slide ID: D2-M07-C1B
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 04 Icon cards
Speaker notes:
- Say: A comparison is only a comparison if one thing varies. Ask what that one thing should be.
- Ask: Let the room list what to hold fixed before you reveal. Most name the model and forget the scoring.
- Watch: DCI_vs_Agentic_RAG setup defines both modes and keeps model, loop, questions, and scoring the same. DCI_vs_Agentic_RAG:cell#9 is Task 1 of 5 — Build the wiki.
- Then: Then show how short the list of things that may vary actually is.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---
# Change only the retrieval interface

- Hold the **model, questions, agent loop, and scoring** constant — vary the interface alone.

Change two things and a difference in the result cannot be attributed to either. This is the same discipline as module 06's ladder: one variable per comparison, or the number means nothing.
<!--
Slide ID: D2-M07-C1A
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: One variable. Everything else is a control.
- Ask: Take answers from two tables before revealing; the wrong answers are the teachable ones.
- Watch: Point to the visible evidence and the notebook artifact. DCI_vs_Agentic_RAG:cell#9 is Task 1 of 5 — Build the wiki.
- Then: With the comparison fixed, the next question is what the agent can actually see.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---
# DCI is retrieval through tool calls

The agent gets file tools, not a search endpoint:

```text
list_pages()          → what exists
read_page("vpn.md")   → the whole page, headings and all
search_chunks(query)  → the Agentic RAG path, for contrast
```

The **wiki** is one markdown index of the corpus — page names, what each is for, its section headings:

| Page | Purpose | Headings |
|---|---|---|
| `vpn.md` | VPN connection and routing | connecting · split tunnelling · known issues |
| `password-and-mfa.md` | password and second-factor recovery | reset · MFA · lockouts |

Without it the agent reads pages at random. With it, it chooses before it reads.
<!--
Slide ID: D2-M07-C2
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 06 Process steps 1
Speaker notes:
- Say: Retrieval stops being an endpoint you call and becomes a set of tools the agent decides between.
- Ask: A page index costs tokens on every turn. What does that buy you that a ranked chunk list does not?
- Watch: The wiki skeleton is built from the headings by hand; the model writes each one-line purpose. DCI_vs_Agentic_RAG:cell#9 is Task 1 of 5 — Build the wiki.
- Then: The map is what makes the next tool call a choice rather than a guess.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Why store page purpose and headings instead of only filenames?

<!--
Slide ID: D2-M07-C2B
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 05 Two column 2
Speaker notes:
- Say: Let the agent navigate a persistent map
- Ask: Why does DCI need a map before it receives a question?
- Watch: Task 1 renders a wiki table; inspect whether each page has a distinct purpose and useful headings. DCI_vs_Agentic_RAG:cell#12 is Task 2 of 5 — Two corpus interfaces.
- Then: Reveal it — “Filenames do not say what is inside”.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---
# Filenames do not say what is inside

- A filename is an identifier. **Purpose and headings are navigable clues.**

`vpn.md` tells the agent nothing about which section covers contractors. "contractor remote access · reset · device · escalation" tells it where to read — before it spends a read on the whole page.
<!--
Slide ID: D2-M07-C2A
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: A filename is an identifier; a purpose line is a routing decision.
- Ask: Rhetorical — answer it yourself; the room has not seen a wiki entry yet.
- Watch: Point to the visible evidence and the notebook artifact. DCI_vs_Agentic_RAG:cell#12 is Task 2 of 5 — Two corpus interfaces.
- Then: The map is what turns the next tool call into a choice.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---
# Why compare traces, not answers

| The trace shows | What it tells you |
|---|---|
| `search_chunks → 3 hits` | which evidence path ran, and how much came back |
| `read_page(vpn.md)` | the page actually inspected |
| `calls=2 · latency=1.8s` | what the path cost |
| answer + source IDs | whether the synthesis used the evidence |

Cost is a function of the path: **latency ≈ calls × (retrieval + model time)**. Two calls at 0.9s is not the same product as six.

One polished answer can hide a failed search path.
<!--
Slide ID: D2-M07-C3
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 05 Two column 1
Speaker notes:
- Say: An answer is one sample of the output. The trace is the whole run, including what it cost.
- Ask: Rhetorical — set it up, then use the next slide's question for the room.
- Watch: Tasks 4–5 print answer scores, named-page evidence, calls, characters, latency, and both traces. DCI_vs_Agentic_RAG:cell#16 is Task 3 of 5 — One loop for both.
- Then: Now put the comparison to the room on the next slide.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---
# The trace shows no relevant page. Which gate failed?

**Source** · **Retrieval** · **Generation**
<!--
Slide ID: D2-M07-C3B
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 07 Big stats
Speaker notes:
- Say: Same three gates from day 1, now read off a trace instead of guessed at.
- Ask: Audience — put it to the room. It is a genuine diagnostic, and the wrong answer is instructive.
- Watch: Tasks 4–5 print answer scores, named-page evidence, calls, characters, latency, and both traces. DCI_vs_Agentic_RAG:cell#16 is Task 3 of 5 — One loop for both.
- Then: Reveal it — the trace tells you which two gates you can rule out.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---
# Retrieval, and the trace proves it

- The page never entered the context, so **Generation never had it to use.**

| Gate | What the trace says |
|---|---|
| Source | the page exists in the corpus — not this |
| **Retrieval** | it was never returned — **this one** |
| Generation | it answered from what it was given — not this |

A trace rules gates out. Without one you would be rewriting the prompt.
<!--
Slide ID: D2-M07-C3A
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: This is what a trace buys you: it eliminates two of the three gates before you change anything.
- Ask: Audience — they have the three gates from module 06, so put it to the room.
- Watch: Point to the visible evidence and the notebook artifact. DCI_vs_Agentic_RAG:cell#16 is Task 3 of 5 — One loop for both.
- Then: Fix retrieval. The prompt is the last thing to touch.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---
# DCI trades access for exposure

`read_page` can open **any** page the agent names. A chunk retriever only ever returns what it scored.

| | Agent can reach | Risk it creates |
|---|---|---|
| Agentic RAG | scored chunks | narrow — and may miss context |
| **DCI** | any page it can list | a transcript, a ticket, another team's doc |

That is the trade: broader raw access produces better answers on structural questions, and a larger blast radius on everything else.
<!--
Slide ID: D2-M07-C4
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 05 Two column 2
Speaker notes:
- Say: DCI's advantage and its risk are the same property: the agent can reach more.
- Ask: Rhetorical — set up the next slide, which asks what has to be checked first.
- Watch: The notebook says DCI earns its extra calls when page structure or exact identifiers matter, and that it gives the model broader raw access. DCI_vs_Agentic_RAG:cell#24 is Task 5 of 5 — Inspect the difference.
- Then: So the question is not whether to allow the tool, but what runs before it.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Before read_page("jordan-ticket.md"), what must the system check?

<!--
Slide ID: D2-M07-C4B
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes:
- Say: Stop at the smallest safe interface
- Ask: What must be checked before a DCI read_page call on a user transcript?
- Watch: Task 2’s notebook question explicitly asks which tool could leak a transcript and what to check on the caller. DCI_vs_Agentic_RAG:cell#20 is Task 4 of 5 — Score every case.
- Then: Reveal it — “The system checks, not the model”.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---
# The system checks, not the model

- Before any `read_page`: **caller identity, page permission, and purpose.**

The model chose the next tool, but choosing is not authorising. Put the check inside the tool — instructions to the model are not a control.
<!--
Slide ID: D2-M07-C4A
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Choosing a tool is not the same as being allowed to run it.
- Ask: Audience — most rooms say 'permission' and stop; push for identity and purpose.
- Watch: Point to the visible evidence and the notebook artifact. DCI_vs_Agentic_RAG:cell#20 is Task 4 of 5 — Score every case.
- Then: The check belongs in the tool, where the model cannot talk its way past it.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Inspect the difference

Deskmate asks the same agent the split-tunnel question through two corpus interfaces.

| Interface | Evidence to compare |
|---|---|
| chunk retriever | ranked section and source ID |
| direct corpus tools | page path and exact menu heading |

**The answer is not the whole trace.**

<!--
Slide ID: D2-M07-C5
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 05 Two column
Speaker notes:
- Say: Compare the evidence path when the same agent sees two interfaces.
- Ask: Which trace field would let Marcus audit the exact menu path?
- Watch: Keep the question fixed so only the corpus interface changes.
- Then: Move from a polished answer to the evidence each mode actually inspected.
Sources: Notebook:cell#24; [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->

---

# Which trace would show that Deskmate found the exact split-tunnel menu path?

<!--
Slide ID: D2-M07-C5B
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 07 Big stats
Speaker notes:
- Say: Ask for the observable difference, not a preference for one interface.
- Ask: What would you put side by side before accepting the answer?
- Watch: Listen for source IDs, page reads, and the exact evidence text.
- Then: Reveal the answer and connect it to the notebook's comparison trace.
Sources: Notebook:cell#24; [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->

---
# A trace names the evidence; prose does not

- Compare **the page path, the quoted heading, and the calls used** — not the wording.

Two interfaces can produce near-identical prose while inspecting entirely different evidence. Only one of them can show you where the answer came from.
<!--
Slide ID: D2-M07-C5A
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Prose is the one part of a run you cannot audit.
- Ask: Rhetorical — lands the point that led into the trace comparison.
- Watch: Tie exact menu-path evidence to the user's question, not to call count alone.
- Then: This is why the notebook saves traces, not just answers.
Sources: Notebook:cell#24; [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->

---

# Research: direct corpus interaction widens the search interface

- Fixed top-k can discard clues before reasoning
- DCI trades broader access for calls, latency, and controls
- Test the interface on local traces before routing to it

<!--
Slide ID: D2-M07-R1
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes:
- Say: Optional: giving the agent file-like access changes what it can discover, and what it can reach.
- Ask: What evidence would falsify the claim that DCI is worth its extra calls for our questions?
- Watch: Alignment is present through the notebook’s controlled two-mode comparison; no cohort score is assumed.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->

---

# 08 · Synthetic data makes failures testable

Source passage: `VPN access requires manager approval after two failed resets.`

Generated candidate:
- Question: “What happens after two failed resets?”
- Reference: “Manager approval is required.”
- Provenance: source page and quoted passage

**Generated means proposed. Review decides whether it becomes a test.**

<!--
Slide ID: D2-M08-C1
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 06 Process steps
Speaker notes:
- Say: You cannot test a failure you have no case for — so generate the cases, then review them.
- Ask: Which source artifact would let a reviewer reject a synthetic question as unsupported?
- Watch: Put the named artifact on screen and trace where its values came from. Improving_RAG_with_RAGAS:cell#9 is Task 1 of 6 — A weak pipeline on purpose.
- Then: Hold this until the notebook block, where the numbers appear.
Sources: [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---

# What source artifact lets a reviewer reject an unsupported case?

<!--
Slide ID: D2-M08-C1B
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 04 Icon cards
Speaker notes:
- Say: Synthetic data makes failures testable
- Ask: Which source artifact would let a reviewer reject a synthetic question as unsupported?
- Watch: Put the named artifact on screen and trace where its values came from. Improving_RAG_with_RAGAS:cell#9 is Task 1 of 6 — A weak pipeline on purpose.
- Then: Reveal it — “Provenance is what makes rejection possible”.
Sources: [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---
# Provenance is what makes rejection possible

- Every generated case carries **its source page, the passage, and the generation record.**

Without them a reviewer can only guess whether a case is supported. With them, rejecting a bad case takes seconds.
<!--
Slide ID: D2-M08-C1A
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: A generated case without a source is an assertion, not a test.
- Ask: Audience — ask what they would need to throw a case out; they will name the source.
- Watch: Point to the visible evidence and the notebook artifact. Improving_RAG_with_RAGAS:cell#9 is Task 1 of 6 — A weak pipeline on purpose.
- Then: Provenance is what lets a human reject one quickly.
Sources: [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---

# Metrics answer different diagnostic questions

| Metric | Looks at | Does not establish |
|---|---|---|
| Context precision | Did useful evidence rank high? | Answer correctness |
| Context recall | Did needed evidence appear? | Complete retrieval |
| Faithfulness | Did claims stay supported? | Source authority |
| Answer relevancy | Did the response address the question? | Factual truth |

Worked example: retrieved text says “manager approval”; answer says “automatic approval.”
- Context precision: did the needed passage rank high?
- Faithfulness: did the answer follow the passage?
- Answer relevancy: did it answer the question?

**One answer can be relevant but unfaithful.**

<!--
Slide ID: D2-M08-C2
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 07 Big stats
Speaker notes:
- Say: Context recall and faithfulness fail for different reasons and demand different repairs.
- Ask: If the correct passage is missing but the model says “I don’t know,” which retrieval lens is still failing?
- Watch: Put the named artifact on screen and trace where its values came from. Improving_RAG_with_RAGAS:cell#13 is Task 2 of 6 — Generate the test set.
- Then: Hand into “Metrics answer different diagnostic questions · Question”.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)
-->
---

# If the passage is missing but the model says “I do not know,” what failed?

<!--
Slide ID: D2-M08-C2B
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 05 Two column 2
Speaker notes:
- Say: Metrics answer different diagnostic questions
- Ask: If the correct passage is missing but the model says “I don’t know,” which retrieval lens is still failing?
- Watch: Put the named artifact on screen and trace where its values came from. Improving_RAG_with_RAGAS:cell#13 is Task 2 of 6 — Generate the test set.
- Then: Reveal it — “Context recall failed, not the answer”.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)
-->
---
# Context recall failed, not the answer

- The evidence never reached the context, so **retrieval failed** — the model behaved correctly.

A fluent "I do not know" looks like good behaviour and hides a retrieval bug. Separate the two metrics before deciding what to repair.
<!--
Slide ID: D2-M08-C2A
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: The model did the right thing and the system still failed. Both can be true.
- Ask: Audience — this one usually splits the room, which is the useful moment.
- Watch: Point to the visible evidence and the notebook artifact. Improving_RAG_with_RAGAS:cell#13 is Task 2 of 6 — Generate the test set.
- Then: Name the gate before you choose a repair.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)
-->
---

# Review synthetic cases as measurement assets

Candidate A: “What happens after two failed resets?” — supported
Candidate B: “Who is the CEO of the vendor?” — unsupported by the page
Candidate C: duplicate wording — remove before scoring

**Curation protects the measurement set from synthetic noise.**

<!--
Slide ID: D2-M08-C3
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 04 Icon cards
Speaker notes:
- Say: A generated test set is a measurement instrument. Review it before it gates anything.
- Ask: Which dimension would expose a system that succeeds on polished questions but fails on terse error-code queries?
- Watch: Module 08 notebook cue: inspect deduplication, schema validation, quoted-page checks, the datasheet, and the kept/removed counts. Improving_RAG_with_RAGAS:cell#18 is Task 3 of 6 — Curate the test set before you trust it.
- Then: Curate once, then compare two system versions on the same set.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---

# Which case set exposes failure on terse error-code queries?

<!--
Slide ID: D2-M08-C3B
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 07 Big stats
Speaker notes:
- Say: Review synthetic cases as measurement assets
- Ask: Which dimension would expose a system that succeeds on polished questions but fails on terse error-code queries?
- Watch: Module 08 notebook cue: inspect deduplication, schema validation, quoted-page checks, the datasheet, and the kept/removed counts. Improving_RAG_with_RAGAS:cell#18 is Task 3 of 6 — Curate the test set before you trust it.
- Then: Reveal it — “Test on the questions users actually type”.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---
# Test on the questions users actually type

- A set with **varied wording, bare error codes, and mixed source types** — not only polished questions.

`VPN-4312` and "my vpn is broken again" are the same intent in different clothes. A set of well-formed questions cannot see the failure on the terse one.
<!--
Slide ID: D2-M08-C3A
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Your test set decides which failures are visible at all.
- Ask: Rhetorical — the example does the work; no need to poll.
- Watch: Point to the visible evidence and the notebook artifact. Improving_RAG_with_RAGAS:cell#18 is Task 3 of 6 — Curate the test set before you trust it.
- Then: Build the varied set first; the score comes after.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---

# Stop when the diagnosis is actionable

Baseline: `k=2` → missing policy passage
Change: `k=4` → inspect whether the passage enters context
Decision: keep the change only if the relevant metric and trace improve

**A metric starts the diagnosis; it does not finish it.**

> “Evals are not validation, they are development.” — SoyPete Tech

<!--
Slide ID: D2-M08-C4
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 05 Two column 3
Speaker notes:
- Say: Stop measuring when you know which component to change, not when the number looks good.
- Ask: What would make you reject a high metric score before changing the system?
- Watch: Put the named artifact on screen and trace where its values came from. Improving_RAG_with_RAGAS:cell#21 is Task 4 of 6 — Run the baseline over the test set.
- Then: Hold this until the notebook block, where the numbers appear.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---

# What would make you reject a high score?

<!--
Slide ID: D2-M08-C4B
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes:
- Say: Stop when the diagnosis is actionable
- Ask: What would make you reject a high metric score before changing the system?
- Watch: Put the named artifact on screen and trace where its values came from. Improving_RAG_with_RAGAS:cell#21 is Task 4 of 6 — Run the baseline over the test set.
- Then: Reveal it — “Audit the asset, not the number”.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---
# Audit the asset, not the number

- Reject a high score when the set has **unsupported cases, duplicates, narrow coverage, or a trace that contradicts it.**

The score is only as good as the set that produced it. A weak measurement asset makes a strong number meaningless.
<!--
Slide ID: D2-M08-C4A
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: A number inherits the weakness of the set behind it.
- Ask: Audience — a good one for the room; it is the Friday panel's question.
- Watch: Point to the visible evidence and the notebook artifact. Improving_RAG_with_RAGAS:cell#21 is Task 4 of 6 — Run the baseline over the test set.
- Then: This is the question Friday's panel will ask about your own numbers.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---

# Curate the test set before you trust it

Generated cases are drafts. A case asking about a policy the KB never had is not a Deskmate failure.

- Check the source passage and expected answer
- Remove unsupported or duplicate cases
- Have a person review the set before it gates anything
- Record a **datasheet**: the counts and caveats that travel with the set — what was removed, and what it cannot test

**Measurement begins with a defensible case.**

<!--
Slide ID: D2-M08-C5
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 04 Icon cards
Speaker notes:
- Say: Synthetic generation expands coverage, but it does not decide what counts.
- Ask: Which generated Deskmate case would you remove before scoring?
- Watch: Distinguish an unsupported policy question from a real system failure.
- Then: Put human review before any eval gate.
Sources: Notebook:cell#18; [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->

---

# A generated case asks about a policy absent from the KB. Should it score Deskmate?

<!--
Slide ID: D2-M08-C5B
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 05 Two column 2
Speaker notes:
- Say: Ask whether the case tests the product or the generator's imagination.
- Ask: What evidence would make this case valid for the helpdesk corpus?
- Watch: Look for a quoted source passage, expected answer, and review decision.
- Then: Reveal the answer and connect it to the notebook's curation checks.
Sources: Notebook:cell#18; [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->

---
# A case with no source tests nothing

- Remove it. **A question the corpus cannot answer cannot measure the product.**

A synthetic question can be fluent, plausible, and still test nothing you promised. Record the review decision, and gate only on the curated set.
<!--
Slide ID: D2-M08-C5A
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Fluent and plausible is not the same as testable.
- Ask: Rhetorical — but pause; someone usually argues it tests refusal, which is a separate case.
- Watch: Keep human review distinct from changing the system to pass a case.
- Then: Record the decision, then gate only on the curated set.
Sources: Notebook:cell#18; [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->

---

# Research: RAG evaluation needs multiple lenses

- Separate retrieval, context use, and answer quality
- Reference-free still requires calibrated measurement
- Use metrics to decide what trace or case to inspect next

<!--
Slide ID: D2-M08-R1
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes:
- Say: Optional: one score cannot separate a retrieval failure from a generation failure.
- Ask: Which part of the RAG pipeline would remain invisible if we reported only answer relevancy?
- Watch: Put the named artifact on screen and trace where its values came from.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [RAGAS: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/)
-->

---

# Where retrieval goes in production

| What we built | Production equivalent |
|---|---|
| An in-memory index rebuilt each run | A persistent index with incremental updates |
| Every page visible to every call | Per-user authorisation on list, search, and read |
| A datasheet printed in a cell | A datasheet committed beside the test set and reviewed before it gates anything |

<!--
Slide ID: D2-Z1
Module: Day 2 close
Instructor: Miriah
Type: closing
Minutes: 2
Layout: 05 Two column
Speaker notes:
- Say: These are the production equivalents named by today's three notebooks.
- Ask: Which prototype row would create the most serious Deskmate risk if left unchanged?
- Watch: Keep the rows verbatim; do not turn them into a new recommendation list.
- Then: Hand the group back to its charter and the evidence it will measure.
Sources: Notebook:cell#34; Notebook:cell#30; Notebook:cell#36; [Module 06 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb); [Module 07 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
