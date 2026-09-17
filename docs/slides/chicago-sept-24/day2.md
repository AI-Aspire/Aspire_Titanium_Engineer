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

# Today: making the agent's evidence trustworthy

06 Advanced retrieval · 35m  ·  07 Agentic retrieval · 30m  ·  08 SDG and RAGAS · 30m

Day 1's retriever was one hand-picked guess; today measures and improves it.

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
- Watch: Groups identify input, expected behavior, and evidence in one case. Vibe_Checks_LLM_Judge:cell#12 is Task 2 of 9 — Write the vibe checks.
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
- Watch: Learners separate retrieval failure from answer-generation failure. Vibe_Checks_LLM_Judge:cell#9 is Task 1 of 9 — Write the rubric.
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
- Watch: Learners name a reference, rubric, and disagreement case. Vibe_Checks_LLM_Judge:cell#25 is Task 5 of 9 — Build a strict judge.
- Then: Show the trace and the judge output side by side in the notebook.
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
- Watch: Learners connect each case to a failure hypothesis and artifact. Vibe_Checks_LLM_Judge:cell#12 is Task 2 of 9 — Write the vibe checks.
- Then: Use the saved case in the judge demo.
Sources: [Module 04 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md); [Machine Learning Yearning](https://github.com/ajaymache/machine-learning-yearning/blob/master/full%20book/machine-learning-yearning.pdf).
-->

---

# What evidence should a reusable eval record?

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
- Watch: Listen for prompt, context, output, rubric, and version. Dev_Environment:cell#16 is Task 3 of 8 — Initialise your workspace.
- Then: Reveal the answer, then tie it to the evals notebook on screen.
Sources: [Module 01 Dev Environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Machine Learning Yearning](https://github.com/ajaymache/machine-learning-yearning/blob/master/full%20book/machine-learning-yearning.pdf).
-->
---

# Six fields, and why each one earns its place

| Field | Without it you cannot… |
|---|---|
| Question | rerun the case |
| Prompt | tell a prompt change from a model change |
| Evidence | tell a retrieval failure from a generation one |
| Answer | see what actually happened |
| Rubric result | compare two runs |
| Model / version | explain why last week's score differed |

A score without its inputs cannot explain a change.

<!--
Slide ID: D2-F5A
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: Take answers from the room first, then reveal. Most rooms name question and answer, and stop there.
- Ask: Push on the two people usually miss — evidence and model/version. Ask what they would do if a score dropped and they had neither.
- Watch: These are the fields the workspace artifacts already carry, which is why later notebooks can score a run they did not produce. Dev_Environment:cell#16 is Task 3 of 8 — Initialise your workspace.
- Then: The evals notebook scores exactly these fields, so the record is the contract between today and Wednesday.
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
- Watch: Learners point to source coverage, retrieval, context use, or answer use. RAG_with_LangChain:cell#9 is Task 1 of 7 — See the gap.
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
- Watch: Learners distinguish chunks and embeddings from ranked context. RAG_with_LangChain:cell#17 is Task 3 of 7 — RAG from scratch.
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
- Watch: Learners name a different remedy for each gate. RAG_with_LangChain:cell#24 is Task 5 of 7 — Wire it into a chain.
- Then: Use the gates to understand advanced retrieval.
Sources: [RAG](https://arxiv.org/abs/2005.11401); [Module 05 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md).
-->

---

# Which failure gate would you inspect first?

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
- Watch: Learners use the table instead of treating every miss as a prompt problem. RAG_with_LangChain:cell#24 is Task 5 of 7 — Wire it into a chain.
- Then: Reveal the answer, then carry it into the advanced-retrieval ladder.
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
- Watch: Point to the visible evidence and the notebook artifact. RAG_with_LangChain:cell#24 is Task 5 of 7 — Wire it into a chain.
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

# Which retriever protects VPN-4312? Which connects “remote access”?

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
- Watch: Retrieval_Ladder Task 2 prints dense and scratch/library BM25 orders for one question; compare the disagreement. Retrieval_Ladder:cell#9 is Task 1 of 5 — Label the evidence.
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
- Watch: Point to the visible evidence and the notebook artifact. Retrieval_Ladder:cell#9 is Task 1 of 5 — Label the evidence.
- Then: Tie the answer to the notebook artifact before moving on.
Sources: [Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/); [Lucene BM25Similarity](https://lucene.apache.org/core/9_12_1/core/org/apache/lucene/search/similarities/BM25Similarity.html); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# Fuse ranks, then spend judgment carefully

`20 candidates → RRF top 10 → reranker top 5 → context top 3`

<svg viewBox="0 0 700 145" width="900" role="img" aria-label="Retrieval ladder sequence from sparse and dense candidates through fusion and reranking to context">
<g text-anchor="middle">
<rect x="12" y="40" width="142" height="54" rx="9" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/>
<text x="83" y="63" font-size="14" font-weight="700" fill="#92400e">sparse</text>
<text x="83" y="81" font-size="11.5" fill="#b45309">exact terms</text>
<rect x="190" y="40" width="142" height="54" rx="9" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.5"/>
<text x="261" y="63" font-size="14" font-weight="700" fill="#5b21b6">dense</text>
<text x="261" y="81" font-size="11.5" fill="#6d28d9">related meaning</text>
<rect x="368" y="40" width="142" height="54" rx="9" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/>
<text x="439" y="63" font-size="14" font-weight="700" fill="#075985">fuse</text>
<text x="439" y="81" font-size="11.5" fill="#0369a1">RRF shortlist</text>
<rect x="546" y="40" width="142" height="54" rx="9" fill="#f8fafc" stroke="#94a3b8" stroke-width="2.5"/>
<text x="617" y="63" font-size="14" font-weight="700" fill="#334155">rerank</text>
<text x="617" y="81" font-size="11.5" fill="#475569">context top 3</text>
<path d="M156 67 H184" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#ladder-a)"/>
<path d="M334 67 H362" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#ladder-a)"/>
<path d="M512 67 H540" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#ladder-a)"/>
</g>
<defs><marker id="ladder-a" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#94a3b8"/></marker></defs>
</svg>

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
- Say: Fusion is cheap and mechanical. A reranker costs a model call per candidate — spend it last.
- Ask: If the correct passage never enters the fused shortlist, can reranking recover it?
- Watch: Retrieval_Ladder Task 3 prints the fused list and cross-encoder order; inspect how many candidates reach the reranker. Retrieval_Ladder:cell#12 is Task 2 of 5 — Dense and sparse.
- Then: Carry the observation into the next exercise.
Sources: [Reciprocal rank fusion paper](https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# If the correct page is absent from the top 10, can the reranker find it?

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
- Watch: Retrieval_Ladder Task 3 prints the fused list and cross-encoder order; inspect how many candidates reach the reranker. Retrieval_Ladder:cell#12 is Task 2 of 5 — Dense and sparse.
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
- Watch: Point to the visible evidence and the notebook artifact. Retrieval_Ladder:cell#12 is Task 2 of 5 — Dense and sparse.
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
- Say: One phrasing finds one neighbourhood. Asking twice is how you find the pages a single query missed.
- Ask: What evidence would show that a rewrite changed coverage rather than merely added duplicates?
- Watch: Retrieval_Ladder Task 3 prints three rewrites and one list per retriever; compare per-case reciprocal ranks in Task 4. Retrieval_Ladder:cell#17 is Task 3 of 5 — Fuse, rerank, expand.
- Then: Hand into “Ask the question more than once · Question”.
Sources: [Iterative query generation for multi-hop QA](https://aclanthology.org/D19-1261/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# Did the rewrites find new pages or repeat the same pages?

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
- Watch: Retrieval_Ladder Task 3 prints three rewrites and one list per retriever; compare per-case reciprocal ranks in Task 4. Retrieval_Ladder:cell#17 is Task 3 of 5 — Fuse, rerank, expand.
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
- Watch: Point to the visible evidence and the notebook artifact. Retrieval_Ladder:cell#17 is Task 3 of 5 — Fuse, rerank, expand.
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
- Say: Every rung adds latency and a new way to be wrong. Add one only when the numbers demand it.
- Ask: Which evidence would change your conclusion?
- Watch: Retrieval_Ladder Task 4 prints hit rate, MRR, latency, and a per-case reciprocal-rank matrix; use the matrix to choose one rung. Retrieval_Ladder:cell#22 is Task 4 of 5 — Score the ladder.
- Then: Hand into “Choose the cheapest rung that clears the bar · Question”.
Sources: [DPR retrieval formulation](https://aclanthology.org/2020.emnlp-main.550/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
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
- Watch: Point to the visible evidence and the notebook artifact. Retrieval_Ladder:cell#22 is Task 4 of 5 — Score the ladder.
- Then: Tie the answer to the notebook artifact before moving on.
Sources: [DPR retrieval formulation](https://aclanthology.org/2020.emnlp-main.550/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->
---

# Filter before you rank

Deskmate receives Priya's question: “Why can't I reach the staging database from the VPN?”

- Identify the caller first
- Scope the KB to that user's allowed pages
- Rank only the permitted candidates

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

# Deskmate has Priya's caller identity and a mixed KB. What is the first retrieval operation?

<!--
Slide ID: D2-M06-C5B
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 05 Two column 2
Speaker notes:
- Say: Ask learners to name the boundary before they name a ranking method.
- Ask: Which artifact would reveal that a result belonged to Marcus rather than Priya?
- Watch: Listen for caller-scoped candidate construction, not a post-answer apology.
- Then: Reveal the answer and connect it to the notebook's group filter.
Sources: Notebook:cell#27; [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->

---

# Authorize the candidate set, then rank it

- **Answer:** Filter the KB by Priya's allowed group before dense, sparse, or hybrid ranking.
- **Why:** Ranking an unscoped index can surface Marcus's tickets to Priya.
- **Next step:** Log the caller, filter, and returned source IDs for each Deskmate answer.

<!--
Slide ID: D2-M06-C5A
Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: The access boundary comes before retrieval quality.
- Ask: What should Marcus be able to audit after a result is returned?
- Watch: Name cross-user ticket leakage as the failure, not merely a poor relevance score.
- Then: Carry the authorization boundary into the next module's corpus interfaces.
Sources: Notebook:cell#27; [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
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
- Say: Optional: retrieval is recall then precision — two stages with different jobs.
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
| **Agentic RAG** — calls a retriever | rank matching chunks | another query or result set |
| **DCI** — direct corpus interaction | list/search pages | headings, full page, neighboring sections |

**Same question; different evidence path.**

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

# What stays constant in the comparison: the model, questions, and scoring—or the tool set?

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
- Watch: DCI_vs_Agentic_RAG setup defines both modes and keeps model, loop, questions, and scoring the same. DCI_vs_Agentic_RAG:cell#9 is Task 1 of 5 — Build the wiki.
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
- Watch: Point to the visible evidence and the notebook artifact. DCI_vs_Agentic_RAG:cell#9 is Task 1 of 5 — Build the wiki.
- Then: Tie the answer to the notebook artifact before moving on.
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

- Separate retrieval, context use, and answer quality
- Reference-free still requires calibrated measurement
- Use metrics to decide what trace or case to inspect next

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
