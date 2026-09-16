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
Speaker notes:
- Say: Exact terms and related meanings need different signals
- Ask: Which part of the question would dense retrieval risk blurring, and which part would BM25 preserve?
- Watch: Retrieval_Ladder Task 2 prints dense and scratch/library BM25 orders for one question; compare the disagreement.
- Then: A reranker is a later model that reads the question and candidate passage together to reorder a shortlist.
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
Speaker notes:
- Say: Exact terms and related meanings need different signals
- Ask: Which part of the question would dense retrieval risk blurring, and which part would BM25 preserve?
- Watch: Retrieval_Ladder Task 2 prints dense and scratch/library BM25 orders for one question; compare the disagreement.
- Then: Carry the observation into the notebook exercise.
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
Speaker notes:
- Say: Fuse ranks, then spend judgment carefully
- Ask: If the correct passage never enters the fused shortlist, can reranking recover it?
- Watch: Retrieval_Ladder Task 3 prints the fused list and cross-encoder order; inspect how many candidates reach the reranker.
- Then: Carry the observation into the next exercise.
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
Speaker notes:
- Say: Fuse ranks, then spend judgment carefully
- Ask: If the correct passage never enters the fused shortlist, can reranking recover it?
- Watch: Retrieval_Ladder Task 3 prints the fused list and cross-encoder order; inspect how many candidates reach the reranker.
- Then: Carry the observation into the notebook exercise.
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
Speaker notes:
- Say: Ask the question more than once
- Ask: What evidence would show that a rewrite changed coverage rather than merely added duplicates?
- Watch: Retrieval_Ladder Task 3 prints three rewrites and one list per retriever; compare per-case reciprocal ranks in Task 4.
- Then: Use the answer to decide whether to clarify or continue.
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
Speaker notes:
- Say: Ask the question more than once
- Ask: What evidence would show that a rewrite changed coverage rather than merely added duplicates?
- Watch: Retrieval_Ladder Task 3 prints three rewrites and one list per retriever; compare per-case reciprocal ranks in Task 4.
- Then: Carry the observation into the notebook exercise.
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
Speaker notes:
- Say: Choose the cheapest rung that clears the bar
- Ask: Which evidence would change your conclusion?
- Watch: Retrieval_Ladder Task 4 prints hit rate, MRR, latency, and a per-case reciprocal-rank matrix; use the matrix to choose one rung.
- Then: Use the answer to decide whether to clarify or continue.
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
Speaker notes:
- Say: Choose the cheapest rung that clears the bar
- Ask: Which evidence would change your conclusion?
- Watch: Retrieval_Ladder Task 4 prints hit rate, MRR, latency, and a per-case reciprocal-rank matrix; use the matrix to choose one rung.
- Then: Carry the observation into the notebook exercise.
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
Speaker notes:
- Say: Research: retrieval is a two-stage design
- Ask: Which claim from the paper is about a benchmark setup rather than a guarantee for our corpus?
- Watch: Alignment pending for optional research discussion; use the notebook’s dense-versus-BM25 comparison as the local bridge.
- Then: Skip if time is short; offer as optional stretch or research.
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
Speaker notes:
- Say: Retrieval becomes an interface choice
- Ask: What stays constant in the notebook comparison, and what is deliberately changed?
- Watch: DCI_vs_Agentic_RAG setup defines both modes and keeps model, loop, questions, and scoring the same.
- Then: Carry the observation into the next exercise.
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
Speaker notes:
- Say: Retrieval becomes an interface choice
- Ask: What stays constant in the notebook comparison, and what is deliberately changed?
- Watch: DCI_vs_Agentic_RAG setup defines both modes and keeps model, loop, questions, and scoring the same.
- Then: Carry the observation into the notebook exercise.
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
Speaker notes:
- Say: Let the agent navigate a persistent map
- Ask: Why does DCI need a map before it receives a question?
- Watch: Task 1 renders a wiki table; inspect whether each page has a distinct purpose and useful headings.
- Then: Carry the observation into the next exercise.
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
Speaker notes:
- Say: Let the agent navigate a persistent map
- Ask: Why does DCI need a map before it receives a question?
- Watch: Task 1 renders a wiki table; inspect whether each page has a distinct purpose and useful headings.
- Then: Carry the observation into the notebook exercise.
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
Speaker notes:
- Say: Compare traces, not just answers
- Ask: What trace field distinguishes an evidence miss from a generation miss?
- Watch: Tasks 4–5 print answer scores, named-page evidence, calls, characters, latency, and both traces.
- Then: Carry the observation into the next exercise.
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
Speaker notes:
- Say: Compare traces, not just answers
- Ask: What trace field distinguishes an evidence miss from a generation miss?
- Watch: Tasks 4–5 print answer scores, named-page evidence, calls, characters, latency, and both traces.
- Then: Carry the observation into the notebook exercise.
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
Speaker notes:
- Say: Stop at the smallest safe interface
- Ask: What must be checked before a DCI read_page call on a user transcript?
- Watch: Task 2’s notebook question explicitly asks which tool could leak a transcript and what to check on the caller.
- Then: Use the answer to decide whether to clarify or continue.
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
Speaker notes:
- Say: Stop at the smallest safe interface
- Ask: What must be checked before a DCI read_page call on a user transcript?
- Watch: Task 2’s notebook question explicitly asks which tool could leak a transcript and what to check on the caller.
- Then: Carry the observation into the notebook exercise.
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
Speaker notes:
- Say: Research: direct corpus interaction widens the search interface
- Ask: What evidence would falsify the claim that DCI is worth its extra calls for our questions?
- Watch: Alignment is present through the notebook’s controlled two-mode comparison; no cohort score is assumed.
- Then: Skip if time is short; offer as optional stretch or research.
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
Speaker notes:
- Say: Synthetic data makes failures testable
- Ask: Which source artifact would let a reviewer reject a synthetic question as unsupported?
- Watch: Inspect the named output and verify its provenance.
- Then: Carry the observation into the next exercise.
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
Speaker notes:
- Say: Synthetic data makes failures testable
- Ask: Which source artifact would let a reviewer reject a synthetic question as unsupported?
- Watch: Inspect the named output and verify its provenance.
- Then: Carry the observation into the notebook exercise.
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
Speaker notes:
- Say: Metrics answer different diagnostic questions
- Ask: If the correct passage is missing but the model says “I don’t know,” which retrieval lens is still failing?
- Watch: Inspect the named output and verify its provenance.
- Then: Use the answer to decide whether to clarify or continue.
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
Speaker notes:
- Say: Metrics answer different diagnostic questions
- Ask: If the correct passage is missing but the model says “I don’t know,” which retrieval lens is still failing?
- Watch: Inspect the named output and verify its provenance.
- Then: Carry the observation into the notebook exercise.
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
Speaker notes:
- Say: Review synthetic cases as measurement assets
- Ask: Which dimension would expose a system that succeeds on polished questions but fails on terse error-code queries?
- Watch: Module 08 notebook cue: inspect deduplication, schema validation, quoted-page checks, the datasheet, and the kept/removed counts.
- Then: Curate once, then compare two system versions on the same set.
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
Speaker notes:
- Say: Review synthetic cases as measurement assets
- Ask: Which dimension would expose a system that succeeds on polished questions but fails on terse error-code queries?
- Watch: Module 08 notebook cue: inspect deduplication, schema validation, quoted-page checks, the datasheet, and the kept/removed counts.
- Then: Carry the observation into the notebook exercise.
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
Speaker notes:
- Say: Stop when the diagnosis is actionable
- Ask: What would make you reject a high metric score before changing the system?
- Watch: Inspect the named output and verify its provenance.
- Then: Carry the observation into the next exercise.
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
Speaker notes:
- Say: Stop when the diagnosis is actionable
- Ask: What would make you reject a high metric score before changing the system?
- Watch: Inspect the named output and verify its provenance.
- Then: Carry the observation into the notebook exercise.
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
Speaker notes:
- Say: Research: RAG evaluation needs multiple lenses
- Ask: Which part of the RAG pipeline would remain invisible if we reported only answer relevancy?
- Watch: Inspect the named output and verify its provenance.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [RAGAS: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/)
-->

- Separate retrieval, context use, and answer quality
- Reference-free still requires calibrated measurement
- Use metrics to decide what trace or case to inspect next
