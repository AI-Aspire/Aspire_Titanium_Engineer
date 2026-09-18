---
marp: true
theme: default
paginate: true
size: 16:9
class: invert
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

- Yesterday: a question, a prompt, an agent, and a first RAG baseline
- Today: retrieval choices, and evidence for which one is better

When a RAG answer is wrong, one of three gates failed:

**Source** — was it in the corpus? · **Retrieval** — did it reach the model? · **Generation** — did the answer use it?
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
- Watch: These three gates are from day 1 and every measurement today names one of them. Say them once here so the diagnostic questions later land.
- Then: Start with the measurement question, not the metric name.
Sources: [Day 2 schedule](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/schedule/day2.md); [Module 05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md).
-->

---
# Worth watching: Typesafe.ai

Launched this year. **"Composable AI: Build Prod, Not God."**

> "The bottleneck isn't raw intelligence. It's that today's intelligence is hard to build on."
>
> "Intelligence today is like **databases before SQL**: powerful, but every use is bespoke."

Their bet: a model built to be *invoked by software*, not chatted with — so a smart decision becomes as dependable as a database query. First model: **Jev**.

<!--
Slide ID: D2-M06-R0
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: optional
Minutes: 2
Layout: 08 Quote
Speaker notes:
- Say: One slide on something brand new, because it names the gap this whole day is about. Their claim is that the models are already smart enough and the missing piece is being able to build on them — to bury one five layers deep in a system and trust it.
- Ask: Rhetorical — no answer needed, just plant it.
- Watch: The databases-before-SQL line is the one worth repeating. Nobody who built databases imagined Google; they made a lower-level capability dependable enough to layer on. Their argument is that safety is a precondition for layering: you let a component run unattended if it is reliable, and you only build on top of it if it is trustworthy.
- Then: Say plainly that the course does not use this — it launched recently and is here as context. Then land the connection: today is about making retrieval dependable enough to build on, which is the same problem at a smaller scale. Everything after this slide is how you get there — measure it, then choose the cheapest rung that clears the bar.
Sources: [Typesafe.ai manifesto](https://typesafe.ai/manifesto)
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
- Watch: Work the arithmetic on screen; these are illustrative ranks, not cohort results. The "not found" case contributes zero to both, which is what makes recall the first thing to fix. Retrieval_Ladder:cell#22 is Task 4 of 5 — Score the ladder.
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
# The wiki is the map that makes choosing possible

One markdown index of the corpus — page names, what each is for, its section headings:

| Page | Purpose | Headings |
|---|---|---|
| `vpn.md` | VPN connection and routing | connecting · split tunnelling · known issues |
| `password-and-mfa.md` | password and second-factor recovery | reset · MFA · lockouts |

Without it the agent reads pages at random. With it, it chooses before it reads.

<!--
Slide ID: D2-M07-C1
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 05 Two column
Speaker notes:
- Say: A file tool without a map is a guess. The wiki is what turns the next call into a decision.
- Ask: A page index costs tokens on every turn. What does that buy that a ranked chunk list does not?
- Watch: The skeleton is built from the headings by hand; the model writes each one-line purpose. DCI_vs_Agentic_RAG:cell#9 is Task 1 of 5 — Build the wiki.
- Then: Purpose and headings are the clues — which is what the next question turns on. Note the wiki is Task 1 in the notebook, before either interface exists.
Sources: [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Why store page purpose and headings instead of only filenames?

<!--
Slide ID: D2-M07-C1B
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
Slide ID: D2-M07-C1A
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: A filename is an identifier; a purpose line is a routing decision.
- Ask: Rhetorical — answer it from the two rows they just saw.
- Watch: Point to the visible evidence and the notebook artifact. DCI_vs_Agentic_RAG:cell#12 is Task 2 of 5 — Two corpus interfaces.
- Then: They have the map now. Next: the two interfaces it makes a choice between.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---
# A retrieval interface is what the agent can ask for

The corpus does not change. **The interface is what the agent gets access to:**

| Interface | The agent calls | Gets back |
|---|---|---|
| **Agentic RAG** | a retriever | ranked chunks it did not choose |
| **DCI** — direct corpus interaction | file tools: list, search, read | whole pages it picked |

Same corpus, same question, different evidence path.
<!--
Slide ID: D2-M07-C2
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 06 Process steps
Speaker notes:
- Say: The corpus is fixed all day. What changes is what the agent is allowed to ask for.
- Ask: Say the full name once — direct corpus interaction — then use DCI for the rest of the module.
- Watch: The notebook puts it plainly: the question is what interface the agent gets to the corpus — a retriever returning ranked chunks, or file tools that list, search and read pages. DCI_vs_Agentic_RAG:cell#12 is Task 2 of 5 — Two corpus interfaces.
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
Slide ID: D2-M07-C2X
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
# Change only the retrieval interface

- Hold the **model, questions, agent loop, and scoring** constant — vary the interface alone.

<!--
Slide ID: D2-M07-C2A
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: One variable. Everything else is a control.
- Ask: Take answers from two tables before revealing; the wrong answers are the teachable ones.
- Watch: Change two things and a difference in the result cannot be attributed to either. Same discipline as module 06's ladder: one variable per comparison, or the number means nothing. DCI_vs_Agentic_RAG:cell#16 is Task 3 of 5 — One loop for both.
- Then: One variable per comparison. Next: what the agent can actually see before its first read.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---
# DCI is retrieval through tool calls

The agent gets file tools, not a search endpoint:

```text
list_pages()              → the wiki: every page, purpose, headings
grep_wiki("split tunnel") → matching lines, with page and line number
read_page("vpn.md")       → the whole page, headings and all
```

Three tools, no search endpoint. It chooses what to open, so it can read around an answer instead of taking scored fragments.

<!--
Slide ID: D2-M07-C3
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 09 Lab and code
Speaker notes:
- Say: Retrieval stops being an endpoint you call and becomes a set of tools the agent decides between.
- Ask: Rhetorical — name the three tools, then point back at the wiki they opened on.
- Watch: These are the real tool names in the notebook. DCI_vs_Agentic_RAG:cell#12 is Task 2 of 5 — Two corpus interfaces.
- Then: Choosing only works because they already have the map. list_pages returns that wiki — say so explicitly, it closes the loop.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242), [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---
# A trace is the sequence of tool calls a run made

...with how much text came back. That is what you compare — not the prose.

| The trace shows | What it tells you |
|---|---|
| `search_chunks → 3 hits` | which evidence path ran, and how much came back |
| `read_page(vpn.md)` | the page actually inspected |
| `calls=2 · latency=1.8s` | what the path cost |

Cost follows the path: **latency ≈ calls × (retrieval + model time)**. One polished answer can hide a failed search.

<!--
Slide ID: D2-M07-C4
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 05 Two column 1
Speaker notes:
- Say: Define it once: a trace is the sequence of tool calls a run made, with how much text came back. Everything else today reads off one.
- Ask: Rhetorical — set it up, then use the next slide's question for the room.
- Watch: Tasks 4–5 print answer scores, named-page evidence, calls, characters, latency, and both traces. DCI_vs_Agentic_RAG:cell#16 is Task 3 of 5 — One loop for both.
- Then: Now put the comparison to the room on the next slide.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---
# The trace shows no relevant page. Which gate failed?

**Source** · **Retrieval** · **Generation**
<!--
Slide ID: D2-M07-C4B
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
Slide ID: D2-M07-C4A
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
Slide ID: D2-M07-C5
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
Slide ID: D2-M07-C5B
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
Slide ID: D2-M07-C5A
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
# Direct corpus interaction widens the search interface

- Fixed top-k can discard clues before the model reasons over them
- DCI trades broader access for calls, latency, and controls
- Test the interface on your own traces before routing questions to it

> [Direct Corpus Interaction (2026)](https://arxiv.org/abs/2605.05242)

<!--
Slide ID: D2-M07-R1
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes:
- Say: Optional — skip if the room is behind. The paper's claim is about interface width, not a guarantee for your corpus.
- Ask: What evidence would falsify the claim that DCI is worth its extra calls for our questions?
- Watch: Alignment is present through the notebook’s controlled two-mode comparison; no cohort score is assumed.
- Then: Optional extra: offer it as reading rather than teaching it if time is short.
Sources: [Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->

---
# 08 · Synthetic data and RAGAS

**You have a retriever. Where do the test cases come from?** · 30 min

- Modules 06 and 07 compared retrievers on cases that already existed
- Module 08 generates the cases, then decides which ones count

<!--
Slide ID: D2-T08
Module: [08 SDG and RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: transition
Minutes: 0
Layout: 01 Title
Speaker notes:
- Say: Every measurement so far assumed a test set. This module builds one, and then argues about whether to trust it.
- Ask: Hold for a beat — this is the hand-off, not content.
- Watch: Generation is the easy half. Curation is where the work is.
- Then: Straight into what a generated case looks like.
Sources: [Module 08 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md).
-->
---
# A generated case carries its provenance

**Provenance** = where a case came from: its origin, so a reviewer can check it.

Source row, from `access-requests.md`:
`warehouse-write | write access to the warehouse | the data platform lead and your manager`

| The generated case | |
|---|---|
| Question | "Who approves warehouse write access?" |
| Reference answer | "The data platform lead and your manager." |
| **Provenance** | `access-requests.md`, the entitlements table row above |

Generated means *proposed*. Provenance is what lets review reject it.
<!--
Slide ID: D2-M08-C1
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 06 Process steps
Speaker notes:
- Say: Provenance is just origin — where this case came from. Say it plainly, because the whole curation argument rests on it.
- Ask: Rhetorical — with the passage on screen, ask what you would check to decide the case is fair.
- Watch: The row is real — `warehouse-write` needs two approvers, which is what makes it a good case: an answer naming only one is wrong in a checkable way. Improving_RAG_with_RAGAS:cell#13 is Task 2 of 6 — Generate the test set.
- Then: Without provenance a reviewer is guessing. With it, rejecting a bad case takes seconds.
Sources: [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---
# No provenance, no rejection

- A case without a source page is an **assertion**, not a test.

A reviewer cannot disprove a plausible-sounding question that names no origin — so it ships, and it measures nothing.
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
# Why one score is not enough

A single "quality: 7/10" cannot tell you what to fix.

| The failure | What you would change |
|---|---|
| The page was never in the corpus | write the page |
| It was there, retrieval missed it | tune retrieval |
| Retrieved, but the answer ignored it | change the prompt or model |

Same low score, three different repairs. **You need a metric per gate.**

<!--
Slide ID: D2-M08-C2Y
Module: [08 SDG and RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 05 Two column
Speaker notes:
- Say: This is the argument for four metrics instead of one number: a single score tells you something is wrong and nothing about where.
- Ask: Audience — a score drops from 8 to 5. What is your first move? The honest answer is you cannot know yet.
- Watch: These are the three gates from this morning, now with a metric attached to each. Improving_RAG_with_RAGAS:cell#25 is Task 5 of 6 — Measure with RAGAS.
- Then: So here are the four RAGAS metrics, and which gate each one watches.
Sources: [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/), [local RAGAS notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---
# Four RAGAS metrics, four different questions

| Metric | Looks at | Does **not** establish |
|---|---|---|
| Context precision | did useful evidence rank high? | answer correctness |
| Context recall | did needed evidence appear at all? | complete retrieval |
| Faithfulness | did claims stay supported? | source authority |
| Answer relevancy | did it address the question? | factual truth |

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
# One answer, three different verdicts

The page says **"the data platform lead and your manager."**
The answer says **"your manager approves it."**

| Metric | Verdict |
|---|---|
| Context recall | **pass** — the right row was retrieved |
| Faithfulness | **fail** — it dropped an approver the passage names |
| Answer relevancy | **pass** — it did answer who approves |

An answer can be relevant and still be unfaithful. One score cannot tell you which.
<!--
Slide ID: D2-M08-C2E
Module: [08 SDG and RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 05 Two column
Speaker notes:
- Say: This is the case that justifies four metrics instead of one score.
- Ask: Audience — which metric would a single "quality" number have hidden here? All three.
- Watch: Same entitlements row as the provenance slide, so the room already knows the ground truth. Dropping one of two approvers is a faithfulness failure that a single quality score would hide. Improving_RAG_with_RAGAS:cell#25 is Task 5 of 6 — Measure with RAGAS.
- Then: A high score on the wrong metric is how a bad answer ships.
Sources: [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/), [local RAGAS notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---
# The passage never arrived and the model said "I do not know."

**What should have happened instead?**
<!--
Slide ID: D2-M08-C2B
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 05 Two column 2
Speaker notes:
- Say: The model behaved correctly. So what does a correct-looking run owe you?
- Ask: Audience — push past "nothing, it was right". The system should have told you retrieval came back empty.
- Watch: Put the named artifact on screen and trace where its values came from. Improving_RAG_with_RAGAS:cell#13 is Task 2 of 6 — Generate the test set.
- Then: Reveal it — the honest refusal is right, and it still has to be visible as a retrieval miss.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)
-->
---
# This is why you measure: to detect, then remediate

- The refusal was correct. **The system still owed you a recorded retrieval miss.**

| | |
|---|---|
| Without per-gate metrics | a fluent "I do not know" looks like success |
| With context recall | the miss is visible, and you know to fix retrieval |

Measurement is not grading the answer. It is **detecting which part failed so it can be repaired** — that is what makes the system reliable rather than lucky.
<!--
Slide ID: D2-M08-C2A
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: This is the reliability argument, not a scoring argument. Metrics exist to localise a failure so you can act on it.
- Ask: Audience — how many silent retrieval misses would it take to erode trust in the product? One, if it is the question someone escalated.
- Watch: Point to the visible evidence and the notebook artifact. Improving_RAG_with_RAGAS:cell#13 is Task 2 of 6 — Generate the test set.
- Then: Detect, localise, repair. The rest of the module is about keeping the instrument honest enough to do that.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)
-->
---
# The agent has to survive a bare error code

`VPN-4312` and *"my vpn is broken again"* are the same intent in different clothes.

| Your test set holds | It can detect failure on |
|---|---|
| polished questions only | polished questions |
| **bare codes, terse phrasing, mixed sources** | what users actually type |

A well-formed test set cannot see the failure on the terse one. **The set decides which failures are visible at all.**

<!--
Slide ID: D2-M08-C3T
Module: [08 SDG and RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 05 Two column
Speaker notes:
- Say: Generated questions come out fluent and well-formed. Real ones arrive as three characters and a complaint.
- Ask: Audience — what does your own helpdesk queue actually look like? Nobody types a well-formed question.
- Watch: This is why the generator needs varied personas: a set of polished questions measures a product nobody uses. Improving_RAG_with_RAGAS:cell#18 is Task 3 of 6 — Curate the test set before you trust it.
- Then: So curation is not only removing bad cases — it is checking the set covers how people really ask.
Sources: [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/), [local RAGAS notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---

# Stop when the diagnosis is actionable

Baseline: `k=2` → missing policy passage
Change: `k=4` → inspect whether the passage enters context
Decision: keep the change only if the relevant metric and trace improve

**A metric starts the diagnosis; it does not finish it.**

Evaluate what failed, fix that one thing, then move to the next. The score is the trigger, not the work.

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

A **test set** is a set of eval cases: a question, the reference answer, and its provenance. Generated cases are *drafts*.

- Check the source passage and the expected answer
- Remove unsupported or duplicate cases
- Have a person review the set before it gates anything
- Record a **datasheet**: counts and caveats that travel with the set — what was removed, and what it cannot test

**Measurement begins with a defensible case.**
<!--
Slide ID: D2-M08-C5
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 04 Icon cards
Speaker notes:
- Say: Same artifact you met in module 06 as eval cases — here you are generating them, so they need review before they gate anything.
- Ask: Which generated Deskmate case would you remove before scoring?
- Watch: Distinguish an unsupported policy question from a real system failure.
- Then: A case asking about a policy the corpus never had is not a product failure. That is the next slide.
Sources: Notebook:cell#18; [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->

---
# What is an example of a bad eval case?

<!--
Slide ID: D2-M08-C5A
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Open it to the room. You are listening for the shapes, not one right answer.
- Ask: Audience — collect three or four before commenting. Expect: no source in the corpus, a duplicate, an ambiguous question, a reference answer that is itself wrong, a question the product never promised to answer.
- Watch: Every example the room gives is something curation has to catch. Improving_RAG_with_RAGAS:cell#18 is Task 3 of 6 — Curate the test set before you trust it.
- Then: A synthetic question can be fluent, plausible, and still test nothing you promised. Record the review decision and gate only on the curated set.
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
