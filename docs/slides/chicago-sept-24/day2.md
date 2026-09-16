---
marp: true
theme: default
paginate: true
size: 16:9
---

# 06 · Exact terms and related meanings need different signals

- Word matching preserves exact terms, rarity, and length signals
- Meaning search connects related wording through embeddings
- Hybrid retrieval keeps both exact codes and related meanings in view
- A ranked candidate is evidence to inspect, not proof

<!--
Slide ID: D2-M06-C1
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 05 Two column
Speaker notes: Start with an internal helpdesk question such as “What is the approval path for ERR-4017?” The exact code and the paraphrase “approval path” create different retrieval clues. Sparse search means matching words in the query and passages; BM25 is one widely used scoring formula that accounts for term frequency, rarity, and document length. Dense search means comparing learned vector representations, so related wording can meet even when tokens differ. Neither score is a relevance proof: both only produce candidates. A reranker is a later model that reads the question and candidate passage together to reorder a shortlist. The retrieval notebook compares dense and BM25 over the same chunks and questions, after page-level evidence labels are corrected. Explain the trajectory from one dense retriever to a measured ladder: preserve the questions and inspect where evidence first appears. The practical stop is the cheapest rung that clears the task bar.
Check understanding: Which part of the question would dense retrieval risk blurring, and which part would BM25 preserve?
Lab observation: Retrieval_Ladder Task 2 prints dense and scratch/library BM25 orders for one question; compare the disagreement.
Sources: [Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/); [Lucene BM25Similarity](https://lucene.apache.org/core/9_12_1/core/org/apache/lucene/search/similarities/BM25Similarity.html); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# 06 · Exact terms and related meanings need different signals · The practical check

- **Ask:** Which part of the question would dense retrieval risk blurring, and which part would BM25 preserve?
- **Inspect:** Retrieval_Ladder Task 2 prints dense and scratch/library BM25 orders for one question; compare the disagreement.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D2-M06-C1B
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Which part of the question would dense retrieval risk blurring, and which part would BM25 preserve?
Lab observation: Retrieval_Ladder Task 2 prints dense and scratch/library BM25 orders for one question; compare the disagreement.
Sources: [Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/); [Lucene BM25Similarity](https://lucene.apache.org/core/9_12_1/core/org/apache/lucene/search/similarities/BM25Similarity.html); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->

- Word matching preserves exact terms, rarity, and length signals
- Meaning search connects related wording through embeddings
- Hybrid retrieval keeps both exact codes and related meanings in view
- A ranked candidate is evidence to inspect, not proof
---

# Fuse ranks, then spend judgment carefully

- RRF fuses rank positions, not incomparable raw scores
- Reranking reads the query and each candidate together
- Retrieve broadly before spending compute on deeper judgment
- A later stage cannot recover an excluded candidate

<!--
Slide ID: D2-M06-C2
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes: Use the same helpdesk question and show that BM25 may find an error code while dense retrieval finds a policy paraphrase. Their raw scores are not safely comparable because each system has its own scale. Reciprocal rank fusion combines rank positions, using a contribution such as 1/(60 + rank) in this notebook, so an item appearing near the top in both lists rises without score calibration. A reranker is a later, more expensive judge of the question and each candidate together; it can reorder only what entered its candidate pool. The sequence matters: retrieve broadly enough, fuse complementary lists, then rerank a bounded shortlist. The 2009 RRF paper motivates rank-level fusion; it does not guarantee an improvement on this corpus. Treat any gain as a measured result.
Check understanding: If the correct passage never enters the fused shortlist, can reranking recover it?
Lab observation: Retrieval_Ladder Task 3 prints the fused list and cross-encoder order; inspect how many candidates reach the reranker.
Sources: [Reciprocal rank fusion paper](https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# Fuse ranks, then spend judgment carefully · The practical check

- **Ask:** If the correct passage never enters the fused shortlist, can reranking recover it?
- **Inspect:** Retrieval_Ladder Task 3 prints the fused list and cross-encoder order; inspect how many candidates reach the reranker.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D2-M06-C2B
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: If the correct passage never enters the fused shortlist, can reranking recover it?
Lab observation: Retrieval_Ladder Task 3 prints the fused list and cross-encoder order; inspect how many candidates reach the reranker.
Sources: [Reciprocal rank fusion paper](https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->

- RRF fuses rank positions, not incomparable raw scores
- Reranking reads the query and each candidate together
- Retrieve broadly before spending compute on deeper judgment
- A later stage cannot recover an excluded candidate
---

# Ask the question more than once

- Multi-query covers alternative wording around one intent
- Rewrites can drift, duplicate noise, and add latency
- Fusion helps only when the paths find meaningfully different evidence
- Keep the original question and inspect each candidate path

<!--
Slide ID: D2-M06-C3
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes: Multi-query retrieval is query expansion around the same intent. For “How do I regain access after a locked account?”, rewrites might use “unlock account,” “account lockout recovery,” and the exact internal procedure name. Different wording can expose different lexical or semantic matches, especially for sparse clues. But every rewrite can also drift, duplicate noise, or increase latency. The notebook makes this trade-off visible by generating three rewrites, retrieving for each, and fusing the results. Keep the user question as the anchor and record the rewrites, candidates, and final context. Do not present expansion as a universal upgrade. A useful stopping rule is: add rewrites only when a labelled failure class improves enough to justify extra calls and review burden.
Check understanding: What evidence would show that a rewrite changed coverage rather than merely added duplicates?
Lab observation: Retrieval_Ladder Task 3 prints three rewrites and one list per retriever; compare per-case reciprocal ranks in Task 4.
Sources: [Iterative query generation for multi-hop QA](https://aclanthology.org/D19-1261/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# Ask the question more than once · The practical check

- **Ask:** What evidence would show that a rewrite changed coverage rather than merely added duplicates?
- **Inspect:** Retrieval_Ladder Task 3 prints three rewrites and one list per retriever; compare per-case reciprocal ranks in Task 4.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D2-M06-C3B
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: What evidence would show that a rewrite changed coverage rather than merely added duplicates?
Lab observation: Retrieval_Ladder Task 3 prints three rewrites and one list per retriever; compare per-case reciprocal ranks in Task 4.
Sources: [Iterative query generation for multi-hop QA](https://aclanthology.org/D19-1261/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->

- Multi-query covers alternative wording around one intent
- Rewrites can drift, duplicate noise, and add latency
- Fusion helps only when the paths find meaningfully different evidence
- Keep the original question and inspect each candidate path
---

# Choose the cheapest rung that clears the bar

| Signal | Question it answers | Use it for |
|---|---|---|
| Hit rate | Did relevant evidence enter top-K? | Coverage |
| MRR | How early did the first relevant result appear? | Ranking |
| Latency and cost | What does this rung consume? | Shipping decision |

**Stop:** choose the least expensive rung that clears the task bar.

<!--
Slide ID: D2-M06-C4
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: Define the measurement before looking at averages. Hit rate asks whether any top-K chunk came from a labelled evidence page. MRR asks how early the first relevant chunk appears: rank one contributes 1 and rank four contributes 0.25. The notebook also records latency, because an expensive rung is not free. Read the per-case matrix, not only the aggregate table: one question may justify a reranker while the rest do not. The notebook’s production lesson is to ship the cheapest rung that clears a bar and document which question type needs the expensive one. Scores depend on evidence labels and cutoff K; they do not prove the generated answer is correct. Stop when the observed failure is resolved, not when the ladder looks impressive.
Check understanding: Which metric would move when the right passage rises from rank eight to rank two, even if it was already inside the cutoff?
Lab observation: Retrieval_Ladder Task 4 prints hit rate, MRR, latency, and a per-case reciprocal-rank matrix; use the matrix to choose one rung.
Sources: [DPR retrieval formulation](https://aclanthology.org/2020.emnlp-main.550/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# Choose the cheapest rung that clears the bar · The practical check

- **Ask:** Which metric would move when the right passage rises from rank eight to rank two, even if it was already inside the cutoff?
- **Inspect:** Retrieval_Ladder Task 4 prints hit rate, MRR, latency, and a per-case reciprocal-rank matrix; use the matrix to choose one rung.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D2-M06-C4B
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Which metric would move when the right passage rises from rank eight to rank two, even if it was already inside the cutoff?
Lab observation: Retrieval_Ladder Task 4 prints hit rate, MRR, latency, and a per-case reciprocal-rank matrix; use the matrix to choose one rung.
Sources: [DPR retrieval formulation](https://aclanthology.org/2020.emnlp-main.550/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->

| Signal | Question it answers | Use it for |
|---|---|---|
| Hit rate | Did relevant evidence enter top-K? | Coverage |
| MRR | How early did the first relevant result appear? | Ranking |
| Latency and cost | What does this rung consume? | Shipping decision |

**Stop:** choose the least expensive rung that clears the task bar.
---

# Research: retrieval is a two-stage design

<!--
Slide ID: D2-M06-R1
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes: Use Karpukhin and colleagues’ 2020 Dense Passage Retrieval paper as the research anchor. Its contribution is a dual-encoder dense retriever trained from question-passage pairs, presented as a practical alternative to sparse retrieval for open-domain question answering. The important trajectory for this course is architectural: a retriever selects a small candidate context and a reader examines it more deeply. The paper’s benchmark findings are not a promise about an internal helpdesk corpus, its labels, or its embedding endpoint. Ask learners to identify which assumption transfers and which does not. Dense retrieval supplies a complementary signal; it does not eliminate exact identifiers, chunking problems, authorization, or evaluation. The current engineering question is interface and budget: which candidate-generation and inspection stages fit the task?
Check understanding: Which claim from the paper is about a benchmark setup rather than a guarantee for our corpus?
Lab observation: Alignment pending for optional research discussion; use the notebook’s dense-versus-BM25 comparison as the local bridge.
Sources: [Dense Passage Retrieval for Open-Domain Question Answering](https://aclanthology.org/2020.emnlp-main.550/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->

- Dense retrieval complements sparse matching
- Candidate generation and deep inspection are separate budgets
- Transfer the architecture, not unverified benchmark outcomes

---

# 07 · Retrieval becomes an interface choice

`question → search_chunks → ranked sections → answer or search again`

`question → list/search/read → chosen page → answer or search again`

- Both interfaces let the agent choose its next request
- The interface changes recovery, cost, and access risk

<!--
Slide ID: D2-M07-C1
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes: Hold the model, loop, questions, and scorer constant. Change only the document interface. Agentic RAG gives the model a BM25-backed search_chunks tool that returns ranked sections; the agent can call it again with a new query. Direct corpus interaction, or DCI, gives file tools that list pages, search the wiki, and read a whole page; the agent can choose its next request there too. In both modes, the model proposes a tool call, while application code executes and authorizes it. The retriever’s ranking determines which candidates come back; it does not control the agent’s sequence. For an internal helpdesk question involving an exact policy code and a second page, the interface changes what can be recovered after the first miss. The broader interface also raises authorization, logging, and cost obligations.
Check understanding: What stays constant in the notebook comparison, and what is deliberately changed?
Lab observation: DCI_vs_Agentic_RAG setup defines both modes and keeps model, loop, questions, and scoring the same.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# 07 · Retrieval becomes an interface choice · The practical check

- **Ask:** What stays constant in the notebook comparison, and what is deliberately changed?
- **Inspect:** DCI_vs_Agentic_RAG setup defines both modes and keeps model, loop, questions, and scoring the same.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D2-M07-C1B
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: What stays constant in the notebook comparison, and what is deliberately changed?
Lab observation: DCI_vs_Agentic_RAG setup defines both modes and keeps model, loop, questions, and scoring the same.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->

`question → search_chunks → ranked sections → answer or search again`

`question → list/search/read → chosen page → answer or search again`

- Both interfaces let the agent choose its next request
- The interface changes recovery, cost, and access risk
---

# Let the agent navigate a persistent map

- The wiki maps pages to purposes and headings
- DCI can search a clue, then read its surrounding page
- Search and read are separate actions with separate failure points
- Navigation artifacts need freshness, ownership, and access controls

<!--
Slide ID: D2-M07-C2
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes: A raw corpus is not automatically navigable, but DCI does not inherently require a wiki. This notebook provides one as a navigation aid: a Markdown index containing page names, a purpose line, and section headings. The model proposes the purpose from a digest and the learner corrects it. The wiki is a persistent navigation artifact, not a query-time answer and not a replacement for source pages. In a helpdesk example, the agent can use the map to find an access policy page, inspect a matching line, then read surrounding context. That trajectory can preserve local context better than a single top-k slice, but it also exposes more of the corpus if tools are not scoped. The useful direction is maintained navigation with ownership, freshness, and link checks; DCI can also operate with other corpus maps or search aids.
Check understanding: Why does DCI need a map before it receives a question?
Lab observation: Task 1 renders a wiki table; inspect whether each page has a distinct purpose and useful headings.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Let the agent navigate a persistent map · The practical check

- **Ask:** Why does DCI need a map before it receives a question?
- **Inspect:** Task 1 renders a wiki table; inspect whether each page has a distinct purpose and useful headings.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D2-M07-C2B
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Why does DCI need a map before it receives a question?
Lab observation: Task 1 renders a wiki table; inspect whether each page has a distinct purpose and useful headings.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->

- The wiki maps pages to purposes and headings
- DCI can search a clue, then read its surrounding page
- Search and read are separate actions with separate failure points
- Navigation artifacts need freshness, ownership, and access controls
---

# Compare traces, not just answers

- Trace the tool path, evidence volume, latency, and answer
- Separate wrong evidence from bad synthesis
- One polished answer can hide a failed search path
- Route by measured question type, not a universal winner

<!--
Slide ID: D2-M07-C3
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 05 Two column 1
Speaker notes: A fluent final answer hides the route that produced it. The notebook records tool sequence, characters of evidence read, latency, and a short answer for each mode. Then its judge scores each answer against the eval-case reference and records whether the answer named a labelled evidence page. Use a divergence question: did the weaker mode retrieve the wrong evidence, or retrieve the right evidence and synthesize badly? That separates interface failure from generation failure. DCI may earn extra calls when evidence is split across pages or exact identifiers matter; agentic BM25 RAG may be sufficient for a question mapped to one or two sections. These are hypotheses to test locally, not universal winners. Keep caller identity and tool authorization outside the language model’s discretion.
Check understanding: What trace field distinguishes an evidence miss from a generation miss?
Lab observation: Tasks 4–5 print answer scores, named-page evidence, calls, characters, latency, and both traces.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Compare traces, not just answers · The practical check

- **Ask:** What trace field distinguishes an evidence miss from a generation miss?
- **Inspect:** Tasks 4–5 print answer scores, named-page evidence, calls, characters, latency, and both traces.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D2-M07-C3B
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: What trace field distinguishes an evidence miss from a generation miss?
Lab observation: Tasks 4–5 print answer scores, named-page evidence, calls, characters, latency, and both traces.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->

- Trace the tool path, evidence volume, latency, and answer
- Separate wrong evidence from bad synthesis
- One polished answer can hide a failed search path
- Route by measured question type, not a universal winner
---

# Stop at the smallest safe interface

- Route by question shape and measured trace cost
- Authorize every corpus tool for the caller
- No evidence means stop or escalate; it does not mean guess
- Stop on sufficient evidence, bounded turns, and a passing answer

<!--
Slide ID: D2-M07-C4
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes: The notebook’s production lesson is a routing rule: keep the cheaper mode that passes the questions and document what triggers a switch. Add safety to that rule. A DCI tool must be read-only, scoped to an authorized corpus, and checked against caller identity before list, search, or read. A turn limit prevents repeated calls; evidence characters and latency make the cost visible. At runtime, the agent can stop when the available evidence supports an answer, when no progress is being made, when the budget is exhausted, or when permission is missing. A reference answer is an evaluation aid, not a runtime requirement. An agent that reads more pages can still answer incorrectly or leak another user’s transcript, so inspect the trace before widening access.
Check understanding: What must be checked before a DCI read_page call on a user transcript?
Lab observation: Task 2’s notebook question explicitly asks which tool could leak a transcript and what to check on the caller.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Stop at the smallest safe interface · The practical check

- **Ask:** What must be checked before a DCI read_page call on a user transcript?
- **Inspect:** Task 2’s notebook question explicitly asks which tool could leak a transcript and what to check on the caller.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D2-M07-C4B
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: What must be checked before a DCI read_page call on a user transcript?
Lab observation: Task 2’s notebook question explicitly asks which tool could leak a transcript and what to check on the caller.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->

- Route by question shape and measured trace cost
- Authorize every corpus tool for the caller
- No evidence means stop or escalate; it does not mean guess
- Stop on sufficient evidence, bounded turns, and a passing answer
---

# Research: direct corpus interaction widens the search interface

<!--
Slide ID: D2-M07-R1
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes: The DCI paper is the research hook for this module. It argues that a fixed similarity interface compresses corpus access into a top-k decision before reasoning, which can be a bottleneck for exact lexical constraints, sparse clue conjunctions, local context checks, and iterative hypotheses. Its proposed interface lets an agent use general terminal tools over the raw corpus without an embedding model, vector index, or retrieval API. Present this as a research claim with a scope: the paper studies benchmark and agentic-search settings, while our notebook compares two local interfaces on a small, labelled corpus. The engineering trade is not semantic retrieval versus intelligence. It is interface resolution versus efficiency, with authorization and observability becoming more important as access broadens.
Check understanding: What evidence would falsify the claim that DCI is worth its extra calls for our questions?
Lab observation: Alignment is present through the notebook’s controlled two-mode comparison; no cohort score is assumed.
Sources: [Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->

- Fixed top-k can discard clues before reasoning
- DCI trades broader access for calls, latency, and controls
- Test the interface on local traces before routing to it

---

# 08 · Synthetic data makes failures testable

- Generate questions, reference answers, and provenance from sources
- Start with a concrete failure hypothesis
- Synthetic cases are candidates for review, not ground truth
- Review every candidate before it becomes an eval case

<!--
Slide ID: D2-M08-C1
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes: Synthetic data generation here means using source documents and a model to propose evaluation cases: questions, reference answers, evidence labels, and metadata. It does not mean stochastic gradient descent. The motivation is coverage: a few friendly questions will not expose exact-token, multi-page, terse, or ambiguous failures. Start from a failure hypothesis—“the code is buried,” “the answer needs two pages,” or “the user omits the product name”—then generate a case that can test it. A generated case is a candidate, not truth. Review its grounding, clarity, representative wording, and intended difficulty before using it to compare retrievers or agents. Preserve provenance so a reviewer can find the source passage and understand why the case exists.
Check understanding: Which source artifact would let a reviewer reject a synthetic question as unsupported?
Lab observation: Module 08 notebook cue: build a small-k baseline, then generate candidate questions and references from the corpus. Inspect the generated rows before curation.
Sources: [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---

# 08 · Synthetic data makes failures testable · The practical check

- **Ask:** Which source artifact would let a reviewer reject a synthetic question as unsupported?
- **Inspect:** Module 08 notebook cue: build a small-k baseline, then generate candidate questions and references from the corpus. Inspect the generated rows before curation.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D2-M08-C1B
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Which source artifact would let a reviewer reject a synthetic question as unsupported?
Lab observation: Module 08 notebook cue: build a small-k baseline, then generate candidate questions and references from the corpus. Inspect the generated rows before curation.
Sources: [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->

- Generate questions, reference answers, and provenance from sources
- Start with a concrete failure hypothesis
- Synthetic cases are candidates for review, not ground truth
- Review every candidate before it becomes an eval case
---

# Metrics answer different diagnostic questions

| Metric | Looks at | Does not establish |
|---|---|---|
| Context precision | Whether retrieved material is useful | Answer correctness |
| Context recall | Whether needed material appeared | Complete retrieval |
| Faithfulness | Whether claims follow supplied context | Source authority |
| Answer relevancy | Whether the response addresses the question | Factual truth |

<!--
Slide ID: D2-M08-C2
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: Keep four lenses distinct and name their inputs. Context recall uses reference-answer information and retrieved context to ask whether needed information was recovered. Context precision uses the retrieved context, with relevance judgments, to ask whether the list is focused. Faithfulness uses the answer and supplied context to ask whether claims are supported. Answer relevancy uses the question and answer to ask whether the response addresses the request. Correctness is not the same as relevance: a response can discuss the right topic while stating a wrong procedure, and correctness needs a trusted reference or reviewed evidence. A retrieval failure can lower recall while the model remains faithful to what it saw. RAGAS introduced a reference-free framework for several dimensions, but model-based metrics remain instruments: inspect examples, calibrate, and never treat one score as ground truth.
Check understanding: If the correct passage is missing but the model says “I don’t know,” which retrieval lens is still failing?
Lab observation: Module 08 notebook cue: score faithfulness, answer relevancy, context precision, and context recall, then inspect the metric rows and values.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)
-->
---

# Metrics answer different diagnostic questions · The practical check

- **Ask:** If the correct passage is missing but the model says “I don’t know,” which retrieval lens is still failing?
- **Inspect:** Module 08 notebook cue: score faithfulness, answer relevancy, context precision, and context recall, then inspect the metric rows and values.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D2-M08-C2B
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: If the correct passage is missing but the model says “I don’t know,” which retrieval lens is still failing?
Lab observation: Module 08 notebook cue: score faithfulness, answer relevancy, context precision, and context recall, then inspect the metric rows and values.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)
-->

| Metric | Looks at | Does not establish |
|---|---|---|
| Context precision | Whether retrieved material is useful | Answer correctness |
| Context recall | Whether needed material appeared | Complete retrieval |
| Faithfulness | Whether claims follow supplied context | Source authority |
| Answer relevancy | Whether the response addresses the question | Factual truth |
---

# Review synthetic cases as measurement assets

- Vary topic, persona, query style, and reasoning depth
- Label evidence for both single-hop and multi-hop cases
- Keep a human-reviewed holdout set for comparison
- Hold a reviewed set constant when comparing systems

<!--
Slide ID: D2-M08-C3
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes: Coverage is a design choice, not a random side effect of generation. Vary topic, persona, query style, and reasoning depth. Include single-hop cases where one passage contains the answer and multi-hop cases where several passages must be connected. For an internal helpdesk corpus, a compliance lead may ask which obligation applies, an engineer may ask what to implement, and a terse user may provide only an error code. Add noisy but plausible phrasing without inventing policy. Reviewers should check that the reference answer is supported, the evidence labels are sufficient, the question is clear, and the difficulty is intentional. Curate once, then compare two system versions on the same set. Otherwise the metric change may be a test-set change.
Check understanding: Which dimension would expose a system that succeeds on polished questions but fails on terse error-code queries?
Lab observation: Module 08 notebook cue: inspect deduplication, schema validation, quoted-page checks, the datasheet, and the kept/removed counts.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---

# Review synthetic cases as measurement assets · The practical check

- **Ask:** Which dimension would expose a system that succeeds on polished questions but fails on terse error-code queries?
- **Inspect:** Module 08 notebook cue: inspect deduplication, schema validation, quoted-page checks, the datasheet, and the kept/removed counts.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D2-M08-C3B
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Which dimension would expose a system that succeeds on polished questions but fails on terse error-code queries?
Lab observation: Module 08 notebook cue: inspect deduplication, schema validation, quoted-page checks, the datasheet, and the kept/removed counts.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->

- Vary topic, persona, query style, and reasoning depth
- Label evidence for both single-hop and multi-hop cases
- Keep a human-reviewed holdout set for comparison
- Hold a reviewed set constant when comparing systems
---

# Stop when the diagnosis is actionable

- Turn a metric pattern into one testable change
- Reject ungrounded, duplicated, or unreviewed synthetic cases
- No single score diagnoses the whole retrieval-and-answer system
- Treat scores as observations to inspect, not thresholds

> “Evals are not validation, they are development.” — SoyPete Tech

<!--
Slide ID: D2-M08-C4
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 05 Two column 3
Speaker notes: A useful evaluation cycle ends with a decision, not a dashboard. Form a failure hypothesis, generate and review cases, run the same cases through the system, inspect metric patterns and traces, then choose one change to test. Stop when the evidence identifies the next action: change chunking, increase candidate depth, add a reranker, constrain a tool, or revise the answer instruction. Synthetic cases can contain source leakage, unsupported references, duplicated wording, or judge bias. RAGAS-style metrics can disagree because they measure different properties and may depend on model judgments. Module 08 now implements a weak small-k pipeline, candidate generation and curation, four metrics, and a k comparison with an interval on the faithfulness difference. Those outputs are still observations to inspect, not universal thresholds.
Check understanding: What would make you reject a high metric score before changing the system?
Lab observation: Module 08 notebook cue: compare the saved baseline and improved rows, chart the delta, and read the interval before interpreting the change. Do not invent a cohort result.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---

# Stop when the diagnosis is actionable · The practical check

- **Ask:** What would make you reject a high metric score before changing the system?
- **Inspect:** Module 08 notebook cue: compare the saved baseline and improved rows, chart the delta, and read the interval before interpreting the change. Do not invent a cohort result.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D2-M08-C4B
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: What would make you reject a high metric score before changing the system?
Lab observation: Module 08 notebook cue: compare the saved baseline and improved rows, chart the delta, and read the interval before interpreting the change. Do not invent a cohort result.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->

- Turn a metric pattern into one testable change
- Reject ungrounded, duplicated, or unreviewed synthetic cases
- No single score diagnoses the whole retrieval-and-answer system
- Treat scores as observations to inspect, not thresholds

> “Evals are not validation, they are development.” — SoyPete Tech
---

# Research: RAG evaluation needs multiple lenses

<!--
Slide ID: D2-M08-R1
Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
Instructor: Beric
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes: The RAGAS paper is the optional research anchor. Its contribution is a reference-free framework intended to assess several dimensions of retrieval-augmented generation rather than collapse the pipeline into one end-to-end score. Use it to explain the origin of the metric distinction, then state the limit clearly: reference-free does not mean assumption-free or human-free. The framework relies on model judgments and prompts, so evaluators still need examples, calibration, and disagreement review. The paper’s experiments do not establish a universal threshold for an internal helpdesk system. The course translation is practical: pair metric outputs with retrieved context, answer claims, source provenance, and known failure cases. If the metric cannot change what you inspect or test next, it is not yet a useful diagnostic.
Check understanding: Which part of the RAG pipeline would remain invisible if we reported only answer relevancy?
Lab observation: Module 08 notebook cue: use the produced datasheet and scores as evidence, while checking the curation decisions that produced the test set.
Sources: [RAGAS: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/)
-->

- Separate retrieval, context use, and answer quality
- Reference-free still requires calibrated measurement
- Use metrics to decide what trace or case to inspect next
