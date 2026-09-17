---
marp: true
theme: default
paginate: true
size: 16:9
---

<!--
Day 2 delivery map from the supplied formal schedule:
- 08:15–08:30: evaluation foundation before the evals notebook demo.
- 09:15–09:30: RAG foundation before the retrieval blocks.
- 09:45–10:05: Module 06 concept introduction; the 10:05 demo owns notebook mechanics.
- Module 07 is selected in the instructor matrix but has no explicit clock slot in the supplied schedule. Keep its concept block ready, but confirm whether it is taught inside the retrieval block or moved to another day.
- 11:30–12:00: Module 08 concept introduction; Beric's 12:00 demo owns notebook mechanics.
-->

# Day 2 · From a prototype to a measured retrieval system

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
- Say: Turn yesterday's prototype into a measured system
- Ask: What did yesterday's prototype leave uncertain?
- Watch: Groups name one uncertainty before choosing a retrieval technique.
- Then: Start with the measurement question, not the metric name.
Sources: [Day 2 schedule](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/schedule/day2.md); [Module 05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md).
-->

---

# An eval repeats the question with a pass condition

| Part | Example for an access question |
|---|---|
| Input | “How do I restore VPN access?” |
| Expected behavior | Name the current procedure and next safe step |
| Evidence | Source page, answer, and decision boundary |

**An eval is a development instrument:** it tells us what to change next.

<!--
Slide ID: D2-F2
Module: [04 Vibe Checks and Judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Miriah
Type: core
Minutes: 2
Layout: 05 Two column
Speaker notes:
- Say: A successful answer is not yet a test
- Ask: What must be saved so another run can be compared fairly?
- Watch: Groups identify input, expected behavior, and evidence in one case.
- Then: Use the case to decide what the evaluator should inspect.
Sources: [Module 04 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [In Defense of Evals](https://www.sh-reya.com/blog/in-defense-ai-evals/).
-->

---

# Score the behavior you need to improve

| If the failure is… | Inspect… |
|---|---|
| The answer missed the right page | retrieval coverage and rank |
| The page was present but ignored | grounding and faithfulness |
| The answer used the page but missed the task | answer correctness and completeness |

**A score is useful only when it points to a next experiment.**

<!--
Slide ID: D2-F3
Module: [04 Vibe Checks and Judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Miriah
Type: core
Minutes: 2
Layout: 05 Two column 1
Speaker notes:
- Say: Diagnose the failure before selecting a score
- Ask: Which row changes if the correct page never entered the prompt?
- Watch: Learners separate retrieval failure from answer-generation failure.
- Then: Carry that distinction into the RAG pipeline.
Sources: [Module 04 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md); [RAGAS metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/).
-->

---

# LLM-as-a-judge is a reviewer, not an oracle

`answer + rubric + reference → judge → score + reason → human spot-check`

- Narrow rubric: “Does it name the approved next step?”
- Useful output: score, reason, and case to inspect
- Boundary: agreement between models is not proof of truth

<!--
Slide ID: D2-F4
Module: [04 Vibe Checks and Judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Miriah
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: A judge applies a narrow rubric to a saved case
- Ask: What would you check by hand before trusting the judge?
- Watch: Learners name a reference, rubric, and disagreement case.
- Then: Beric will show the trace and judge output in the notebook.
Sources: [Module 04 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM-as-a-judge limitations](https://arxiv.org/abs/2306.05685).
-->

---

# An eval case needs a reason to exist

| Failure hypothesis | Case that tests it | Evidence to inspect |
|---|---|---|
| policy is missing | ask about a newly changed rule | source coverage |
| retrieval misses codes | use a terse error code | ranked pages |
| answer overclaims | include an out-of-scope request | refusal or escalation |

**A larger test set is not automatically a better test set.**

<!--
Slide ID: D2-F4B
Module: [04 Vibe Checks and Judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Miriah
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: Every eval case should test a known uncertainty
- Ask: Which failure would this case expose?
- Watch: Learners connect each case to a failure hypothesis and artifact.
- Then: Use the saved case in the judge demo.
Sources: [Module 04 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md); [Machine Learning Yearning](https://github.com/ajaymache/machine-learning-yearning/blob/master/full%20book/machine-learning-yearning.pdf).
-->

---

# Quick check · Question: what would you record?

- **Question:** What evidence should a reusable eval record?

<!--
Slide ID: D2-F5
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah
Type: core
Minutes: 1
Layout: 07 Big stats
Speaker notes:
- Say: Ask the question before revealing the answer
- Ask: Which record lets you locate the failing step?
- Watch: Listen for prompt, context, output, rubric, and version.
- Then: Beric reveals the answer and connects it to the evals notebook.
Sources: [Module 01 Dev Environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Machine Learning Yearning](https://github.com/ajaymache/machine-learning-yearning/blob/master/full%20book/machine-learning-yearning.pdf).
-->
---

# What the record has to contain
- **Answer:** Save the question, prompt, evidence, answer, rubric result, and model/version.
- **Why:** Without inputs and evidence, a score cannot explain a change.
- **Next step:** Carry this record forward — the evals notebook scores exactly these fields.

<!--
Slide ID: D2-F5A
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Reveal the answer and why it matters
- Ask: What would change if the answer were different?
- Watch: Point to the visible evidence and the notebook artifact.
- Then: Tie the answer to the notebook artifact before moving on.
Sources: [Module 01 Dev Environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Machine Learning Yearning](https://github.com/ajaymache/machine-learning-yearning/blob/master/full%20book/machine-learning-yearning.pdf).
-->

---

# RAG answers a question with selected evidence

`question → retrieve passages → add context → generate answer → inspect sources`

- The model supplies language; the corpus supplies task-specific facts
- Retrieval changes the request context, not the model weights
- A retrieved passage is evidence to inspect, not automatic truth

<!--
Slide ID: D2-F6
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Miriah
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: RAG is a question-to-evidence pipeline
- Ask: At which arrow could the correct fact be lost?
- Watch: Learners point to source coverage, retrieval, context use, or answer use.
- Then: Define the preparation and per-question steps.
Sources: [RAG](https://arxiv.org/abs/2005.11401); [Module 05 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb).
-->

---

# Prepare once; retrieve for each question

| Before the question | For each question |
|---|---|
| split pages into chunks | represent the question |
| store searchable metadata | rank candidate chunks |
| keep source IDs and versions | assemble context and answer |

**The index is prepared work. Retrieval is a repeated decision.**

<!--
Slide ID: D2-F7
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Miriah
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes:
- Say: Separate index preparation from question-time retrieval
- Ask: Which step happens once, and which repeats for every user question?
- Watch: Learners distinguish chunks and embeddings from ranked context.
- Then: Show why changing k or the retriever changes the evidence.
Sources: [Module 05 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [Context assembly notes](https://github.com/soypete/ctx-eng-book/blob/main/research/context-assembly-pipeline-patterns.md).
-->

---

# RAG has three failure gates

1. **Source:** Did the corpus contain the current answer?
2. **Retrieval:** Did the right passage reach the context?
3. **Generation:** Did the answer use the passage correctly?

**Same symptom, different fix:** add the missing source, change retrieval, or revise the answer contract.

<!--
Slide ID: D2-F8
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Miriah
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: Diagnose the gate before changing the system
- Ask: If the page exists but never enters context, which gate failed?
- Watch: Learners name a different remedy for each gate.
- Then: Use the gates to understand advanced retrieval.
Sources: [RAG](https://arxiv.org/abs/2005.11401); [Module 05 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md).
-->

---

# Quick check · Question: locate the miss

- **Question:** Which failure gate would you inspect first?

<!--
Slide ID: D2-F9
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Miriah
Type: core
Minutes: 1
Layout: 05 Two column 2
Speaker notes:
- Say: Make the failure location visible
- Ask: Which observation would justify changing the retriever?
- Watch: Learners use the table instead of treating every miss as a prompt problem.
- Then: Eli reveals the answer and connects it to advanced retrieval.
Sources: [Module 05 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [RAG failure analysis](https://arxiv.org/abs/2005.11401).
-->
---

# Which gate lost the evidence
- **Answer:** Source coverage, retrieval, or generation, depending on where the evidence disappeared.
- **Why:** Each gate points to a different engineering change.
- **Next step:** Name the gate before you change code; each one points at different work.

<!--
Slide ID: D2-F9A
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Miriah
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Reveal the answer and why it matters
- Ask: What would change if the answer were different?
- Watch: Point to the visible evidence and the notebook artifact.
- Then: Tie the answer to the notebook artifact before moving on.
Sources: [Module 05 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [RAG failure analysis](https://arxiv.org/abs/2005.11401).
-->
---

# 06 · Exact terms and related meanings need different signals

- **BM25:** keeps exact codes, names, and rare terms visible
- **Dense:** connects “remote access” with “VPN connection”
- **Hybrid:** keeps both signals before deeper ranking

Example question: `VPN-4312 fails after a password reset`

| Retriever | Likely strength |
|---|---|
| BM25 | exact `VPN-4312` |
| Dense | related “remote access” guidance |
| Hybrid | both clues in the candidate set |

<!--
Slide ID: D2-M06-C1
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 05 Two column
Speaker notes:
- Say: Exact terms and related meanings need different signals
- Ask: Which part of the question would dense retrieval risk blurring, and which part would BM25 preserve?
- Watch: Retrieval_Ladder Task 2 prints dense and scratch/library BM25 orders for one question; compare the disagreement.
- Then: A reranker is a later model that reads the question and candidate passage together to reorder a shortlist.
Sources: [Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/); [Lucene BM25Similarity](https://lucene.apache.org/core/9_12_1/core/org/apache/lucene/search/similarities/BM25Similarity.html); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# 06 · Exact terms and related meanings need different signals · Question

- **Question:** Which retriever protects VPN-4312? Which connects “remote access”?

<!--
Slide ID: D2-M06-C1B
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 04 Icon cards
Speaker notes:
- Say: Exact terms and related meanings need different signals
- Ask: Which part of the question would dense retrieval risk blurring, and which part would BM25 preserve?
- Watch: Retrieval_Ladder Task 2 prints dense and scratch/library BM25 orders for one question; compare the disagreement.
- Then: Reveal the answer, then tie it to the notebook artifact on screen.
Sources: [Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/); [Lucene BM25Similarity](https://lucene.apache.org/core/9_12_1/core/org/apache/lucene/search/similarities/BM25Similarity.html); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# BM25 keeps the code, dense widens the net
- **Answer:** BM25 protects the exact code; dense search broadens the meaning.
- **Why:** The two signals expose different candidate passages.
- **Next step:** In the notebook, read the two orders side by side before judging either.

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
- Watch: Point to the visible evidence and the notebook artifact.
- Then: Tie the answer to the notebook artifact before moving on.
Sources: [Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/); [Lucene BM25Similarity](https://lucene.apache.org/core/9_12_1/core/org/apache/lucene/search/similarities/BM25Similarity.html); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# Fuse ranks, then spend judgment carefully

`20 candidates → RRF top 10 → reranker top 5 → context top 3`

- **Cheap first:** gather candidates with multiple signals
- **Expensive later:** let a cross-encoder compare question + passage
- **Hard limit:** a reranker cannot recover a passage that was never retrieved

<!--
Slide ID: D2-M06-C2
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 06 Process steps
Speaker notes:
- Say: Fuse ranks, then spend judgment carefully
- Ask: If the correct passage never enters the fused shortlist, can reranking recover it?
- Watch: Retrieval_Ladder Task 3 prints the fused list and cross-encoder order; inspect how many candidates reach the reranker.
- Then: Carry the observation into the next exercise.
Sources: [Reciprocal rank fusion paper](https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# Fuse ranks, then spend judgment carefully · Question

- **Question:** If the correct page is absent from the top 10, can the reranker find it?

<!--
Slide ID: D2-M06-C2B
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 05 Two column 2
Speaker notes:
- Say: Fuse ranks, then spend judgment carefully
- Ask: If the correct passage never enters the fused shortlist, can reranking recover it?
- Watch: Retrieval_Ladder Task 3 prints the fused list and cross-encoder order; inspect how many candidates reach the reranker.
- Then: Reveal the answer, then tie it to the notebook artifact on screen.
Sources: [Reciprocal rank fusion paper](https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# A reranker cannot recover what was never retrieved
- **Answer:** No. A reranker cannot recover a candidate absent from the shortlist.
- **Why:** Later stages only reorder what earlier stages retrieved.
- **Next step:** So tune recall first, then spend a reranker on the shortlist you trust.

<!--
Slide ID: D2-M06-C2A
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Reveal the answer and why it matters
- Ask: What would change if the answer were different?
- Watch: Point to the visible evidence and the notebook artifact.
- Then: Tie the answer to the notebook artifact before moving on.
Sources: [Reciprocal rank fusion paper](https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# Ask the question more than once

- Original: `How do I restore VPN access?`
- Rewrite A: `VPN password reset procedure`
- Rewrite B: `remote access account locked`

Multi-query helps only when the rewrites expose different useful evidence.

<!--
Slide ID: D2-M06-C3
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 06 Process steps 1
Speaker notes:
- Say: Ask the question more than once
- Ask: What evidence would show that a rewrite changed coverage rather than merely added duplicates?
- Watch: Retrieval_Ladder Task 3 prints three rewrites and one list per retriever; compare per-case reciprocal ranks in Task 4.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [Iterative query generation for multi-hop QA](https://aclanthology.org/D19-1261/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# Ask the question more than once · Question

- **Question:** Did the rewrites find new pages or repeat the same pages?

<!--
Slide ID: D2-M06-C3B
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 07 Big stats
Speaker notes:
- Say: Ask the question more than once
- Ask: What evidence would show that a rewrite changed coverage rather than merely added duplicates?
- Watch: Retrieval_Ladder Task 3 prints three rewrites and one list per retriever; compare per-case reciprocal ranks in Task 4.
- Then: Reveal the answer, then tie it to the notebook artifact on screen.
Sources: [Iterative query generation for multi-hop QA](https://aclanthology.org/D19-1261/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# New IDs mean new coverage
- **Answer:** New source IDs show changed coverage; repeated IDs show duplicated evidence.
- **Why:** More results are not the same as more useful evidence.
- **Next step:** Watch the source IDs, not the result count, when you add a rung.

<!--
Slide ID: D2-M06-C3A
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Reveal the answer and why it matters
- Ask: What would change if the answer were different?
- Watch: Point to the visible evidence and the notebook artifact.
- Then: Tie the answer to the notebook artifact before moving on.
Sources: [Iterative query generation for multi-hop QA](https://aclanthology.org/D19-1261/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# Choose the cheapest rung that clears the bar

| Signal | Question it answers | Use it for |
|---|---|---|
| Hit rate | Did relevant evidence enter top-K? | Coverage |
| MRR | How early did the first relevant result appear? | Ranking |
| Latency and cost | What does this rung consume? | Shipping decision |

**Stop:** choose the least expensive rung that clears the task bar.

Illustrative ranks for three questions: `[2, 8, not found]`

`hit@5 = 1/3` · `MRR = (1/2 + 1/8 + 0) / 3`

The numbers show how to reason about a ladder; they are not cohort results.

<!--
Slide ID: D2-M06-C4
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 07 Big stats
Speaker notes:
- Say: Choose the cheapest rung that clears the bar
- Ask: Which evidence would change your conclusion?
- Watch: Retrieval_Ladder Task 4 prints hit rate, MRR, latency, and a per-case reciprocal-rank matrix; use the matrix to choose one rung.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [DPR retrieval formulation](https://aclanthology.org/2020.emnlp-main.550/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# Choose the cheapest rung that clears the bar · Question

- **Question:** A correct page moves from rank 4 to rank 2. Which metric improves?

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
- Then: Reveal the answer, then tie it to the notebook artifact on screen.
Sources: [DPR retrieval formulation](https://aclanthology.org/2020.emnlp-main.550/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# MRR sees rank, hit@5 sees the cutoff
- **Answer:** MRR improves; hit@5 stays the same when both ranks are inside the cutoff.
- **Why:** MRR sees exact rank; hit@5 sees whether the result crossed the cutoff.
- **Next step:** Pick the metric that answers your question before you report a win.

<!--
Slide ID: D2-M06-C4A
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Reveal the answer and why it matters
- Ask: What would change if the answer were different?
- Watch: Point to the visible evidence and the notebook artifact.
- Then: Tie the answer to the notebook artifact before moving on.
Sources: [DPR retrieval formulation](https://aclanthology.org/2020.emnlp-main.550/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
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

Example question: `Which VPN policy applies to contractors?`

| Interface | First move | What it can inspect next |
|---|---|---|
| Retriever | rank matching chunks | another query or result set |
| Direct corpus | list/search pages | headings, full page, neighboring sections |

**Same question; different evidence path.**

<!--
Slide ID: D2-M07-C1
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 06 Process steps
Speaker notes:
- Say: Retrieval becomes an interface choice
- Ask: What stays constant in the notebook comparison, and what is deliberately changed?
- Watch: DCI_vs_Agentic_RAG setup defines both modes and keeps model, loop, questions, and scoring the same.
- Then: Carry the observation into the next exercise.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# 07 · Retrieval becomes an interface choice · Question

- **Question:** What stays constant in the comparison: the model, questions, and scoring—or the tool set?

<!--
Slide ID: D2-M07-C1B
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 04 Icon cards
Speaker notes:
- Say: Retrieval becomes an interface choice
- Ask: What stays constant in the notebook comparison, and what is deliberately changed?
- Watch: DCI_vs_Agentic_RAG setup defines both modes and keeps model, loop, questions, and scoring the same.
- Then: Reveal the answer, then tie it to the notebook artifact on screen.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Change one thing: the retrieval interface
- **Answer:** Keep the model, questions, loop, and scoring constant; change only the retrieval interface.
- **Why:** Otherwise the comparison cannot explain which change caused the result.
- **Next step:** Hold everything else fixed in the notebook, or the comparison says nothing.

<!--
Slide ID: D2-M07-C1A
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Reveal the answer and why it matters
- Ask: What would change if the answer were different?
- Watch: Point to the visible evidence and the notebook artifact.
- Then: Tie the answer to the notebook artifact before moving on.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Let the agent navigate a persistent map

| Page | Purpose | Headings |
|---|---|---|
| `vpn.md` | contractor remote access | reset · device · escalation |
| `mfa.md` | second-factor recovery | lost phone · backup code |

The map helps the agent choose **which page to read** before it reads the whole page.

<!--
Slide ID: D2-M07-C2
Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 06 Process steps 1
Speaker notes:
- Say: Let the agent navigate a persistent map
- Ask: Why does DCI need a map before it receives a question?
- Watch: Task 1 renders a wiki table; inspect whether each page has a distinct purpose and useful headings.
- Then: Carry the observation into the next exercise.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Let the agent navigate a persistent map · Question

- **Question:** Why store page purpose and headings instead of only filenames?

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
- Watch: Task 1 renders a wiki table; inspect whether each page has a distinct purpose and useful headings.
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
- Watch: Point to the visible evidence and the notebook artifact.
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
- Say: Compare traces, not just answers
- Ask: What trace field distinguishes an evidence miss from a generation miss?
- Watch: Tasks 4–5 print answer scores, named-page evidence, calls, characters, latency, and both traces.
- Then: Carry the observation into the next exercise.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Compare traces, not just answers · Question

- **Question:** No relevant page appears in the trace. Is that a generation or evidence failure?

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
- Watch: Tasks 4–5 print answer scores, named-page evidence, calls, characters, latency, and both traces.
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
- Watch: Point to the visible evidence and the notebook artifact.
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
- Say: Stop at the smallest safe interface
- Ask: What must be checked before a DCI read_page call on a user transcript?
- Watch: Task 2’s notebook question explicitly asks which tool could leak a transcript and what to check on the caller.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
---

# Stop at the smallest safe interface · Question

- **Question:** Before read_page("jordan-ticket.md"), what must the system check?

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
- Watch: Point to the visible evidence and the notebook artifact.
- Then: Tie the answer to the notebook artifact before moving on.
Sources: [DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)
-->
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
- Say: Synthetic data makes failures testable
- Ask: Which source artifact would let a reviewer reject a synthetic question as unsupported?
- Watch: Put the named artifact on screen and trace where its values came from.
- Then: Carry the observation into the next exercise.
Sources: [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---

# 08 · Synthetic data makes failures testable · Question

- **Question:** What source artifact lets a reviewer reject an unsupported case?

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
- Watch: Put the named artifact on screen and trace where its values came from.
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
- Watch: Point to the visible evidence and the notebook artifact.
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
- Say: Metrics answer different diagnostic questions
- Ask: If the correct passage is missing but the model says “I don’t know,” which retrieval lens is still failing?
- Watch: Put the named artifact on screen and trace where its values came from.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)
-->
---

# Metrics answer different diagnostic questions · Question

- **Question:** If the passage is missing but the model says “I do not know,” what failed?

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
- Watch: Put the named artifact on screen and trace where its values came from.
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
- Watch: Point to the visible evidence and the notebook artifact.
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
- Say: Review synthetic cases as measurement assets
- Ask: Which dimension would expose a system that succeeds on polished questions but fails on terse error-code queries?
- Watch: Module 08 notebook cue: inspect deduplication, schema validation, quoted-page checks, the datasheet, and the kept/removed counts.
- Then: Curate once, then compare two system versions on the same set.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---

# Review synthetic cases as measurement assets · Question

- **Question:** Which case set exposes failure on terse error-code queries?

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
- Watch: Module 08 notebook cue: inspect deduplication, schema validation, quoted-page checks, the datasheet, and the kept/removed counts.
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
- Watch: Point to the visible evidence and the notebook artifact.
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
- Say: Stop when the diagnosis is actionable
- Ask: What would make you reject a high metric score before changing the system?
- Watch: Put the named artifact on screen and trace where its values came from.
- Then: Carry the observation into the next exercise.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
---

# Stop when the diagnosis is actionable · Question

- **Question:** What would make you reject a high score?

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
- Watch: Put the named artifact on screen and trace where its values came from.
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
- Watch: Point to the visible evidence and the notebook artifact.
- Then: Tie the answer to the notebook artifact before moving on.
Sources: [RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)
-->
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
- Watch: Put the named artifact on screen and trace where its values came from.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [RAGAS: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/)
-->

- Separate retrieval, context use, and answer quality
- Reference-free still requires calibrated measurement
- Use metrics to decide what trace or case to inspect next
