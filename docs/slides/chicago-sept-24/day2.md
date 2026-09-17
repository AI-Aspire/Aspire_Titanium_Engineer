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

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 700 150" width="900" role="img" aria-label="Sparse retrieval preserves exact VPN code terms while dense retrieval connects related remote access wording, and hybrid keeps both candidate sets">
<g text-anchor="middle">
<rect x="18" y="38" width="190" height="58" rx="9" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/>
<text x="113" y="63" font-size="15" font-weight="700" fill="#92400e">sparse / BM25</text>
<text x="113" y="82" font-size="12" fill="#b45309">VPN-4312</text>
<rect x="255" y="38" width="190" height="58" rx="9" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.5"/>
<text x="350" y="63" font-size="15" font-weight="700" fill="#5b21b6">dense</text>
<text x="350" y="82" font-size="12" fill="#6d28d9">remote access</text>
<rect x="492" y="38" width="190" height="58" rx="9" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/>
<text x="587" y="63" font-size="15" font-weight="700" fill="#075985">hybrid</text>
<text x="587" y="82" font-size="12" fill="#0369a1">both candidate signals</text>
<path d="M210 67 H250" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#dense-sparse-a)"/>
<path d="M447 67 H487" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#dense-sparse-a)"/>
</g>
<defs><marker id="dense-sparse-a" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#94a3b8"/></marker></defs>
</svg>
</div>

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
# Which method would you use for each source?

| Source | What a question about it looks like |
|---|---|
| `tickets.jsonl` | "what happened with T-1001?" — exact IDs |
| `vpn.md` | "why can't I reach staging?" — described, not named |
| the whole KB | a user who does not know which page they need |

<!--
Slide ID: D2-M06-C1B
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 04 Icon cards
Speaker notes:
- Say: Take each row in turn. The answer is in the naming: exact identifiers are a sparse problem, described symptoms are a dense one.
- Ask: Push on row three — most rooms say hybrid, and the reason matters: you do not know in advance which kind of question arrives.
- Watch: Retrieval_Ladder Task 2 prints dense and scratch/library BM25 orders for one question; compare the disagreement. Retrieval_Ladder:cell#9 is Task 1 of 5 — Label the evidence.
- Then: Reveal the answer, then tie it to the notebook artifact on screen.
Sources: [Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/); [Lucene BM25Similarity](https://lucene.apache.org/core/9_12_1/core/org/apache/lucene/search/similarities/BM25Similarity.html); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---
# Exact IDs are sparse; described symptoms are dense

- `tickets.jsonl` → **sparse**. `T-1001` is a token, not a meaning.
- `vpn.md` → **dense**. "cannot reach staging" never says "split tunnel".
- the whole KB → **hybrid**. You cannot predict which arrives.

The two signals surface different passages, so the candidate set differs before any ranking happens.
<!--
Slide ID: D2-M06-C1A
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Reveal the answer and why it matters
- Ask: What would change if the answer were different?
- Watch: Point to the visible evidence and the notebook artifact. Retrieval_Ladder:cell#9 is Task 1 of 5 — Label the evidence.
- Then: Hybrid is the default precisely because the question shape is not knowable in advance.
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
- Ask: What would change if the answer were different?
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
- Then: Reveal the answer, then tie it to the notebook artifact on screen.
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
- Then: Carry the observation into the next exercise.
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
- Ask: What would change if the answer were different?
- Watch: Point to the visible evidence and the notebook artifact. DCI_vs_Agentic_RAG:cell#9 is Task 1 of 5 — Build the wiki.
- Then: With the comparison fixed, the next question is what the agent can actually see.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Let the agent navigate a persistent map

| Page | Purpose | Headings |
|---|---|---|
| `vpn.md` | contractor remote access | reset · device · escalation |
| `mfa.md` | second-factor recovery | lost phone · backup code |

This index is the **wiki**: it helps the agent choose **which page to read** before it reads the whole page.

<!--
Slide ID: D2-M07-C2
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 06 Process steps 1
Speaker notes:
- Say: An index of what exists lets the agent choose before it reads, instead of reading to find out.
- Ask: Why does DCI need a map before it receives a question?
- Watch: Task 1 renders a wiki table; inspect whether each page has a distinct purpose and useful headings. DCI_vs_Agentic_RAG:cell#12 is Task 2 of 5 — Two corpus interfaces.
- Then: Carry the observation into the next exercise.
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
- Then: Reveal the answer, then tie it to the notebook artifact on screen.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Clues before the agent reads a page
- **Answer:** They give the agent navigable clues before it reads a page.
- **Why:** Filenames alone do not explain which page or section is relevant.
- **Next step:** Inspect what the agent sees before its first read, not after.

<!--
Slide ID: D2-M07-C2A
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Reveal the answer and why it matters
- Ask: What would change if the answer were different?
- Watch: Point to the visible evidence and the notebook artifact. DCI_vs_Agentic_RAG:cell#12 is Task 2 of 5 — Two corpus interfaces.
- Then: Tie the answer to the notebook artifact before moving on.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Compare traces, not just answers

| Trace | What it tells us |
|---|---|
| `search_chunks → 3 hits` | evidence path and volume |
| `read_page(vpn.md)` | page actually inspected |
| `calls=2, latency=1.8s` | cost of the path |
| answer + source IDs | whether synthesis used evidence |

One polished answer can hide a failed search path.

<!--
Slide ID: D2-M07-C3
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 05 Two column 1
Speaker notes:
- Say: Two agents can reach the same answer by paths of very different quality.
- Ask: What trace field distinguishes an evidence miss from a generation miss?
- Watch: Tasks 4–5 print answer scores, named-page evidence, calls, characters, latency, and both traces. DCI_vs_Agentic_RAG:cell#16 is Task 3 of 5 — One loop for both.
- Then: Carry the observation into the next exercise.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# No relevant page appears in the trace. Is that a generation or evidence failure?

<!--
Slide ID: D2-M07-C3B
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 07 Big stats
Speaker notes:
- Say: Compare traces, not just answers
- Ask: What trace field distinguishes an evidence miss from a generation miss?
- Watch: Tasks 4–5 print answer scores, named-page evidence, calls, characters, latency, and both traces. DCI_vs_Agentic_RAG:cell#16 is Task 3 of 5 — One loop for both.
- Then: Reveal the answer, then tie it to the notebook artifact on screen.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Evidence failure comes first
- **Answer:** Evidence failure first; inspect the search path before changing the prompt.
- **Why:** No relevant page means the answer had nothing reliable to synthesize.
- **Next step:** Read the search path first; the prompt is the last thing to change.

<!--
Slide ID: D2-M07-C3A
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Reveal the answer and why it matters
- Ask: What would change if the answer were different?
- Watch: Point to the visible evidence and the notebook artifact. DCI_vs_Agentic_RAG:cell#16 is Task 3 of 5 — One loop for both.
- Then: Tie the answer to the notebook artifact before moving on.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Stop at the smallest safe interface

`caller → authorization check → list/search/read → evidence → answer`

- A tool can be useful and still be too powerful
- No evidence means stop or escalate; it does not mean guess
- Stop on sufficient evidence, bounded turns, or human escalation

<!--
Slide ID: D2-M07-C4
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 05 Two column 2
Speaker notes:
- Say: More capability is more attack surface. Take the smallest interface that passes.
- Ask: What must be checked before a DCI read_page call on a user transcript?
- Watch: Task 2’s notebook question explicitly asks which tool could leak a transcript and what to check on the caller. DCI_vs_Agentic_RAG:cell#20 is Task 4 of 5 — Score every case.
- Then: Hand into “Stop at the smallest safe interface · Question”.
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
- Then: Reveal the answer, then tie it to the notebook artifact on screen.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Identity, permission, and purpose
- **Answer:** Caller identity, page permission, and purpose—not just the model request.
- **Why:** The system owns authorization even when the model chooses the next tool.
- **Next step:** Put the check in the tool, not in the instructions to the model.

<!--
Slide ID: D2-M07-C4A
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Reveal the answer and why it matters
- Ask: What would change if the answer were different?
- Watch: Point to the visible evidence and the notebook artifact. DCI_vs_Agentic_RAG:cell#20 is Task 4 of 5 — Score every case.
- Then: Tie the answer to the notebook artifact before moving on.
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

# The winning trace names the evidence

- **Answer:** Compare the retrieved source or page path, the quoted menu heading, and the calls used.
- **Why:** Two interfaces can produce similar prose while inspecting different evidence.
- **Next step:** Keep the same split-tunnel case and inspect both traces before routing future questions.

<!--
Slide ID: D2-M07-C5A
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: A comparison is useful only when the evidence path is visible.
- Ask: Which difference would matter if both answers scored equally?
- Watch: Tie exact menu-path evidence to the user's question, not to call count alone.
- Then: Carry the inspection habit into measurement and curation.
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
- Then: Carry the observation into the next exercise.
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
- Then: Reveal the answer, then tie it to the notebook artifact on screen.
Sources: [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---

# Provenance on every generated case
- **Answer:** The source page, passage, and generation record.
- **Why:** Provenance lets a reviewer reject unsupported or distorted candidates.
- **Next step:** Keep provenance on every generated case, or a reviewer cannot reject one.

<!--
Slide ID: D2-M08-C1A
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Reveal the answer and why it matters
- Ask: What would change if the answer were different?
- Watch: Point to the visible evidence and the notebook artifact. Improving_RAG_with_RAGAS:cell#9 is Task 1 of 6 — A weak pipeline on purpose.
- Then: Tie the answer to the notebook artifact before moving on.
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
- Then: Reveal the answer, then tie it to the notebook artifact on screen.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)
-->
---

# Context recall, not answer quality
- **Answer:** Context recall; the needed evidence never reached the context.
- **Why:** A fluent “I do not know” can still hide a retrieval failure.
- **Next step:** Separate the two metrics before deciding what to repair.

<!--
Slide ID: D2-M08-C2A
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Reveal the answer and why it matters
- Ask: What would change if the answer were different?
- Watch: Point to the visible evidence and the notebook artifact. Improving_RAG_with_RAGAS:cell#13 is Task 2 of 6 — Generate the test set.
- Then: Tie the answer to the notebook artifact before moving on.
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
- Then: Reveal the answer, then tie it to the notebook artifact on screen.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---

# Varied wording beats polished questions
- **Answer:** A set with varied wording, codes, and source types—not only polished questions.
- **Why:** The test set determines which failures can be seen.
- **Next step:** Build the varied set first; it decides which failures you can even see.

<!--
Slide ID: D2-M08-C3A
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Reveal the answer and why it matters
- Ask: What would change if the answer were different?
- Watch: Point to the visible evidence and the notebook artifact. Improving_RAG_with_RAGAS:cell#18 is Task 3 of 6 — Curate the test set before you trust it.
- Then: Tie the answer to the notebook artifact before moving on.
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
- Then: Carry the observation into the next exercise.
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
- Then: Reveal the answer, then tie it to the notebook artifact on screen.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---

# Audit the test set, not the score
- **Answer:** Unsupported cases, duplicates, a narrow test set, or a trace that contradicts the score.
- **Why:** A high score is not useful when the measurement asset is weak.
- **Next step:** Audit the test set before you defend the score it produced.

<!--
Slide ID: D2-M08-C4A
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Reveal the answer and why it matters
- Ask: What would change if the answer were different?
- Watch: Point to the visible evidence and the notebook artifact. Improving_RAG_with_RAGAS:cell#21 is Task 4 of 6 — Run the baseline over the test set.
- Then: Tie the answer to the notebook artifact before moving on.
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

# Human review makes the test set count

- **Answer:** Remove the unsupported case; it cannot measure Deskmate behavior without a source in the KB.
- **Why:** A synthetic question can be fluent, plausible, and still test nothing the product promises.
- **Next step:** Record the review decision and gate only on the curated set.

<!--
Slide ID: D2-M08-C5A
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: The test set is a measurement asset with an owner and a review boundary.
- Ask: What would Marcus want recorded before trusting a regression result?
- Watch: Keep human review distinct from changing the system to pass a case.
- Then: Close by connecting curation to the production table's reviewed gate.
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
