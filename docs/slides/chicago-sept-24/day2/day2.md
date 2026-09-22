---
marp: true
theme: default
paginate: true
size: 16:9
class: invert
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

<div style="display:flex;justify-content:center;margin-top:.3em">
<svg viewBox="0 0 860 210" width="1080" role="img" aria-label="Three module blocks drawn to their length in minutes: advanced retrieval 35, agentic retrieval 30, synthetic data and RAGAS 30, read as retrieve, compare, measure">
<text x="10" y="30" font-size="14" fill="#94a3b8">Three concept blocks, 95 minutes, one retriever carried through all three</text>
<rect x="10" y="54" width="303" height="78" rx="9" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/>
<text x="22" y="80" font-size="16" font-weight="700" fill="#7dd3fc">06</text>
<text x="22" y="103" font-size="14" fill="#f1f5f9">Advanced retrieval</text>
<text x="22" y="123" font-size="12" fill="#94a3b8">35 min</text>
<text x="301" y="80" font-size="13" fill="#7dd3fc" text-anchor="end" font-style="italic">retrieve</text>
<rect x="319" y="54" width="259" height="78" rx="9" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2.5"/>
<text x="331" y="80" font-size="16" font-weight="700" fill="#c4b5fd">07</text>
<text x="331" y="103" font-size="14" fill="#f1f5f9">Agentic retrieval</text>
<text x="331" y="123" font-size="12" fill="#94a3b8">30 min</text>
<text x="567" y="80" font-size="13" fill="#c4b5fd" text-anchor="end" font-style="italic">compare</text>
<rect x="585" y="54" width="259" height="78" rx="9" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/>
<text x="597" y="80" font-size="16" font-weight="700" fill="#fcd34d">08</text>
<text x="597" y="103" font-size="14" fill="#f1f5f9">SDG and RAGAS</text>
<text x="597" y="123" font-size="12" fill="#94a3b8">30 min</text>
<text x="832" y="80" font-size="13" fill="#fcd34d" text-anchor="end" font-style="italic">measure</text>
<path d="M10 160 H850" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 4"/>
<text x="10" y="188" font-size="13" fill="#94a3b8">one retrieval guess</text>
<text x="850" y="188" font-size="13" fill="#fcd34d" text-anchor="end">evidence you can inspect and improve</text>
</svg>
</div>

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

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 860 200" width="1060" role="img" aria-label="Three chevrons in a chain: source, retrieval, generation; a wrong RAG answer failed at exactly one of them">
<polygon points="14,40 260,40 282,94 260,148 14,148 14,94" fill="#1e293b" stroke="#94a3b8" stroke-width="2.5"/>
<text x="54" y="80" font-size="22" font-weight="700" fill="#cbd5e1">Source</text>
<text x="54" y="106" font-size="13" fill="#f1f5f9">was it in the corpus?</text>
<text x="54" y="130" font-size="12" fill="#94a3b8">if this failed: write the page</text>
<polygon points="290,40 536,40 558,94 536,148 290,148 312,94" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/>
<text x="330" y="80" font-size="22" font-weight="700" fill="#7dd3fc">Retrieval</text>
<text x="330" y="106" font-size="13" fill="#f1f5f9">did it reach the model?</text>
<text x="330" y="130" font-size="12" fill="#94a3b8">if this failed: tune retrieval</text>
<polygon points="566,40 812,40 834,94 812,148 566,148 588,94" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2.5"/>
<text x="606" y="80" font-size="22" font-weight="700" fill="#c4b5fd">Generation</text>
<text x="606" y="106" font-size="13" fill="#f1f5f9">did the answer use it?</text>
<text x="606" y="130" font-size="12" fill="#94a3b8">if this failed: change prompt or model</text>
<text x="430" y="186" font-size="13" fill="#94a3b8" text-anchor="middle">Every measurement today names one of these three gates.</text>
</svg>
</div>

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

<div style="font-size:.7em">

| Question | Against |
|---|---|
| "what does `uv sync` remove?" | `python-environments.md` |
| "why can't I reach staging?" | `vpn.md` |
| "how long until someone looks at this?" | the whole KB |

</div>

<div style="display:flex;gap:.7em;margin-top:.5em;font-size:.62em">
<div style="flex:1;background:#0b2b40;border-top:5px solid #38bdf8;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#7dd3fc">ASK</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">Take one row at a time. What is the shape of the question: an exact string, a described symptom, or a page nobody can name?</div></div>
<div style="flex:1;background:#3a2a0a;border-top:5px solid #fbbf24;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#fcd34d">INSPECT</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">Retrieval_Ladder Task 2 prints the dense and BM25 page orders for one question. Look at where the two orders disagree.</div></div>
<div style="flex:1;background:#2a1d5a;border-top:5px solid #a78bfa;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#c4b5fd">DECIDE</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">Sparse, dense, or hybrid for each row, and the one word in the question that decided it.</div></div>
</div>

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

**Reciprocal rank fusion** is the cheap stage. It scores a page by where it lands in each list, then merges. Arithmetic, no model call, which is why it comes first.

<style scoped>
@keyframes rrf-up { 0%,25% { transform: translateY(34px); } 55%,100% { transform: translateY(0); } }
@keyframes rrf-down { 0%,25% { transform: translateY(-34px); } 55%,100% { transform: translateY(0); } }
.rrf-up { animation: rrf-up 5s cubic-bezier(.4,0,.2,1) infinite; }
.rrf-down { animation: rrf-down 5s cubic-bezier(.4,0,.2,1) infinite; }
@media (prefers-reduced-motion: reduce) { .rrf-up, .rrf-down { animation: none; } }
</style>
<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 860 250" width="1000" role="img" aria-label="Two ranked lists, sparse A B C and dense C A D, fused by reciprocal rank fusion into A C B D; the fused rows reorder as the scores are added">
<text x="130" y="30" font-size="15" font-weight="700" fill="#7dd3fc" text-anchor="middle">sparse (BM25)</text>
<rect x="30" y="48" width="200" height="28" rx="6" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/>
<text x="44" y="67" font-size="13" fill="#94a3b8">1</text>
<text x="70" y="67" font-size="15" font-weight="700" fill="#f1f5f9">A</text>
<rect x="30" y="82" width="200" height="28" rx="6" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/>
<text x="44" y="101" font-size="13" fill="#94a3b8">2</text>
<text x="70" y="101" font-size="15" font-weight="700" fill="#f1f5f9">B</text>
<rect x="30" y="116" width="200" height="28" rx="6" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/>
<text x="44" y="135" font-size="13" fill="#94a3b8">3</text>
<text x="70" y="135" font-size="15" font-weight="700" fill="#f1f5f9">C</text>
<text x="370" y="30" font-size="15" font-weight="700" fill="#c4b5fd" text-anchor="middle">dense</text>
<rect x="270" y="48" width="200" height="28" rx="6" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2"/>
<text x="284" y="67" font-size="13" fill="#94a3b8">1</text>
<text x="310" y="67" font-size="15" font-weight="700" fill="#f1f5f9">C</text>
<rect x="270" y="82" width="200" height="28" rx="6" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2"/>
<text x="284" y="101" font-size="13" fill="#94a3b8">2</text>
<text x="310" y="101" font-size="15" font-weight="700" fill="#f1f5f9">A</text>
<rect x="270" y="116" width="200" height="28" rx="6" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2"/>
<text x="284" y="135" font-size="13" fill="#94a3b8">3</text>
<text x="310" y="135" font-size="15" font-weight="700" fill="#f1f5f9">D</text>
<text x="670" y="30" font-size="15" font-weight="700" fill="#fcd34d" text-anchor="middle">RRF: 1 / (60 + rank), summed</text>
<g class="rrf-up"><rect x="540" y="48" width="290" height="28" rx="6" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2"/><text x="554" y="67" font-size="13" fill="#94a3b8">1</text><text x="580" y="67" font-size="15" font-weight="700" fill="#f1f5f9">A</text><text x="612" y="67" font-size="12" fill="#94a3b8">1/61 + 1/62</text><text x="818" y="67" font-size="13" fill="#fcd34d" text-anchor="end">0.0325</text></g>
<g class="rrf-down"><rect x="540" y="82" width="290" height="28" rx="6" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2"/><text x="554" y="101" font-size="13" fill="#94a3b8">2</text><text x="580" y="101" font-size="15" font-weight="700" fill="#f1f5f9">C</text><text x="612" y="101" font-size="12" fill="#94a3b8">1/63 + 1/61</text><text x="818" y="101" font-size="13" fill="#fcd34d" text-anchor="end">0.0323</text></g>
<g class="rrf-up"><rect x="540" y="116" width="290" height="28" rx="6" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2"/><text x="554" y="135" font-size="13" fill="#94a3b8">3</text><text x="580" y="135" font-size="15" font-weight="700" fill="#f1f5f9">B</text><text x="612" y="135" font-size="12" fill="#94a3b8">1/62</text><text x="818" y="135" font-size="13" fill="#fcd34d" text-anchor="end">0.0161</text></g>
<g class="rrf-down"><rect x="540" y="150" width="290" height="28" rx="6" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2"/><text x="554" y="169" font-size="13" fill="#94a3b8">4</text><text x="580" y="169" font-size="15" font-weight="700" fill="#f1f5f9">D</text><text x="612" y="169" font-size="12" fill="#94a3b8">1/63</text><text x="818" y="169" font-size="13" fill="#fcd34d" text-anchor="end">0.0159</text></g>
<path d="M232 110 H262 M472 110 H535" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 4"/>
<text x="30" y="212" font-size="13" fill="#f1f5f9">A page ranked highly by both lists rises above one ranked highly by one.</text>
<text x="30" y="234" font-size="12" fill="#94a3b8">Positions only; no scores are normalised and no model is called. D was found by dense alone, B by sparse alone.</text>
</svg>
</div>

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

It only reorders what earlier stages handed it. Tune **recall** first; spend the reranker on a shortlist you already trust.

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 860 262" width="1000" role="img" aria-label="A two-stage funnel: the corpus chunks narrow to a pool of twelve candidates by recall, then a reranker reorders the twelve into a top four; one correct chunk left outside the pool never reaches the reranker">
<text x="20" y="30" font-size="13" fill="#94a3b8" letter-spacing="1.5">CORPUS CHUNKS</text>
<circle cx="30" cy="58" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="56" cy="58" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="82" cy="58" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="108" cy="58" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="134" cy="58" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="160" cy="58" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="30" cy="84" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="56" cy="84" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="82" cy="84" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="108" cy="84" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="134" cy="84" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="160" cy="84" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="30" cy="110" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="56" cy="110" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="82" cy="110" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="108" cy="110" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="134" cy="110" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="160" cy="110" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="30" cy="136" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="56" cy="136" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="82" cy="136" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="108" cy="136" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="134" cy="136" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="160" cy="136" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="30" cy="162" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="56" cy="162" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="82" cy="162" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="108" cy="162" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="134" cy="162" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="160" cy="162" r="6" fill="#94a3b8" opacity="0.7"/>
<circle cx="36" cy="206" r="8" fill="#f87171" stroke="#fca5a5" stroke-width="2"/>
<text x="52" y="211" font-size="12" fill="#fca5a5">the right chunk, never entered the pool</text>
<path d="M220 40 L440 78 L440 152 L220 190 Z" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/>
<text x="330" y="100" font-size="16" font-weight="700" fill="#7dd3fc" text-anchor="middle">recall</text>
<text x="330" y="120" font-size="12" fill="#f1f5f9" text-anchor="middle">sparse, dense, fusion,</text>
<text x="330" y="136" font-size="12" fill="#f1f5f9" text-anchor="middle">multi-query add pages</text>
<text x="452" y="122" font-size="13" fill="#7dd3fc">12</text>
<text x="452" y="138" font-size="12" fill="#94a3b8">candidates</text>
<path d="M520 78 L700 104 L700 126 L520 152 Z" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/>
<text x="610" y="110" font-size="16" font-weight="700" fill="#fcd34d" text-anchor="middle">rerank</text>
<text x="610" y="128" font-size="12" fill="#f1f5f9" text-anchor="middle">reads all 12, reorders</text>
<text x="730" y="104" font-size="13" fill="#fcd34d" text-anchor="middle">top 4</text>
<path d="M444 115 H514" stroke="#94a3b8" stroke-width="2"/><path d="M704 115 H754" stroke="#94a3b8" stroke-width="2"/>
<rect x="758" y="96" width="98" height="38" rx="8" fill="#0f3320" stroke="#4ade80" stroke-width="2"/>
<text x="807" y="120" font-size="13" fill="#86efac" text-anchor="middle">to the model</text>
<path d="M282 206 Q 520 206 606 158" stroke="#f87171" stroke-width="1.5" fill="none" stroke-dasharray="5 4"/>
<text x="430" y="236" font-size="13" fill="#fca5a5" text-anchor="middle">a later stage cannot recover an excluded candidate: it only reorders what it was handed</text>
<text x="430" y="254" font-size="12" fill="#94a3b8" text-anchor="middle">pool of 12 and k = 4 are the notebook's settings; the dots are illustrative</text>
</svg>
</div>

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

<div style="font-size:.62em;color:#cbd5e1">Coverage, <b>hit@5</b>: is the evidence reaching the model at all? · Ranking, <b>MRR</b>: is it arriving early enough to use? · Latency and cost: can you afford this rung in production?</div>

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 860 246" width="1000" role="img" aria-label="Five risers from BM25 to multi-query, each labelled with what it adds and its measured milliseconds per query from the seed run; a dashed line marks the bar you set">
<rect x="16" y="150" width="160" height="70" rx="8" fill="#1e293b" stroke="#94a3b8" stroke-width="2.5"/>
<text x="28" y="176" font-size="15" font-weight="700" fill="#cbd5e1">BM25</text>
<text x="28" y="195" font-size="12" fill="#f1f5f9">exact words</text>
<text x="28" y="213" font-size="13" fill="#fcd34d">1 ms per query</text>
<rect x="182" y="124" width="160" height="96" rx="8" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/>
<text x="194" y="150" font-size="15" font-weight="700" fill="#7dd3fc">dense</text>
<text x="194" y="169" font-size="12" fill="#f1f5f9">meaning</text>
<text x="194" y="187" font-size="13" fill="#fcd34d">94 ms per query</text>
<rect x="348" y="98" width="160" height="122" rx="8" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/>
<text x="360" y="124" font-size="15" font-weight="700" fill="#7dd3fc">hybrid RRF</text>
<text x="360" y="143" font-size="12" fill="#f1f5f9">both, fused</text>
<text x="360" y="161" font-size="13" fill="#fcd34d">86 ms per query</text>
<rect x="514" y="72" width="160" height="148" rx="8" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/>
<text x="526" y="98" font-size="15" font-weight="700" fill="#fcd34d">cross-encoder</text>
<text x="526" y="117" font-size="12" fill="#f1f5f9">reads the pair</text>
<text x="526" y="135" font-size="13" fill="#fcd34d">98 ms per query</text>
<rect x="680" y="46" width="160" height="174" rx="8" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2.5"/>
<text x="692" y="72" font-size="15" font-weight="700" fill="#c4b5fd">multi-query</text>
<text x="692" y="91" font-size="12" fill="#f1f5f9">three rewrites</text>
<text x="692" y="109" font-size="13" fill="#fcd34d">38 s per query</text>
<text x="20" y="30" font-size="13" fill="#f1f5f9">Each rung costs more than the one below. Climb until hit@5 and MRR clear the bar you set, then stop.</text>
<text x="20" y="238" font-size="12" fill="#94a3b8">ms per query from the seed ladder (3 cases, k = 4); rung height is order, not scale. The price is measured, the bar is yours.</text>
</svg>
</div>

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

<div style="display:flex;gap:.7em;margin-top:.5em;font-size:.62em">
<div style="flex:1;background:#0b2b40;border-top:5px solid #38bdf8;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#7dd3fc">ASK</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">Two metrics, one change in rank. Which of them can see it, and by how much?</div></div>
<div style="flex:1;background:#3a2a0a;border-top:5px solid #fbbf24;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#fcd34d">INSPECT</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">Retrieval_Ladder Task 4 prints hit rate, MRR, latency, and a per-case reciprocal-rank matrix. Find one case whose rank changed between rungs.</div></div>
<div style="flex:1;background:#2a1d5a;border-top:5px solid #a78bfa;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#c4b5fd">DECIDE</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">hit@5, MRR, both, or neither. Then: which one would you report to a stakeholder, and why.</div></div>
</div>

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

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 860 180" width="1000" role="img" aria-label="Three chevrons: identify the caller, scope the index to what the caller may read, then rank only those candidates">
<polygon points="14,30 260,30 282,84 260,138 14,138 14,84" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2.5"/>
<text x="52" y="68" font-size="20" font-weight="700" fill="#c4b5fd">1  Identify</text>
<text x="52" y="94" font-size="13" fill="#f1f5f9">the caller, from the session</text>
<text x="52" y="118" font-size="12" fill="#94a3b8">not from the prompt</text>
<polygon points="290,30 536,30 558,84 536,138 290,138 312,84" fill="#1e293b" stroke="#94a3b8" stroke-width="2.5"/>
<text x="328" y="68" font-size="20" font-weight="700" fill="#cbd5e1">2  Scope</text>
<text x="328" y="94" font-size="13" fill="#f1f5f9">the index to pages this caller may read</text>
<text x="328" y="118" font-size="12" fill="#94a3b8">inside the query, not after it</text>
<polygon points="566,30 812,30 834,84 812,138 566,138 588,84" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/>
<text x="604" y="68" font-size="20" font-weight="700" fill="#7dd3fc">3  Rank</text>
<text x="604" y="94" font-size="13" fill="#f1f5f9">only those candidates</text>
<text x="604" y="118" font-size="12" fill="#94a3b8">the ladder runs here</text>
<text x="430" y="170" font-size="13" fill="#fca5a5" text-anchor="middle">Dropping after ranking looks the same in a demo and leaks in production: counts, gaps, and rank positions give the match away.</text>
</svg>
</div>

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

One markdown index of the corpus: page names, what each is for, its section headings.

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 860 300" width="1040" role="img" aria-label="The wiki drawn as a map of six knowledge-base pages, each card naming the page, its purpose, and its section headings, with vpn.md highlighted as the page an agent would choose for a VPN question; faded groups for prompts and transcripts">
<text x="20" y="24" font-size="12" fill="#94a3b8" letter-spacing="1.5">WIKI INDEX · one page per row, purpose and headings</text>
<rect x="20" y="36" width="270" height="76" rx="8" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/>
<text x="32" y="56" font-size="13" font-weight="700" fill="#7dd3fc" font-family="ui-monospace, Menlo, monospace">kb/vpn.md</text>
<text x="32" y="74" font-size="12" fill="#f1f5f9">VPN connection and routing</text>
<text x="32" y="91" font-size="12" fill="#94a3b8">Connecting · Split tunnelling · Known issues ·</text>
<text x="32" y="105" font-size="12" fill="#94a3b8">When to file a ticket</text>
<rect x="302" y="36" width="270" height="76" rx="8" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
<text x="314" y="56" font-size="13" font-weight="700" fill="#cbd5e1" font-family="ui-monospace, Menlo, monospace">kb/password-and-mfa.md</text>
<text x="314" y="74" font-size="12" fill="#f1f5f9">password and second-factor recovery</text>
<text x="314" y="91" font-size="12" fill="#94a3b8">Resetting a password · MFA · Lockouts ·</text>
<text x="314" y="105" font-size="12" fill="#94a3b8">What the helpdesk will never do</text>
<rect x="584" y="36" width="270" height="76" rx="8" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
<text x="596" y="56" font-size="13" font-weight="700" fill="#cbd5e1" font-family="ui-monospace, Menlo, monospace">kb/access-requests.md</text>
<text x="596" y="74" font-size="12" fill="#f1f5f9">who grants which entitlement</text>
<text x="596" y="91" font-size="12" fill="#94a3b8">Entitlements · How to request ·</text>
<text x="596" y="105" font-size="12" fill="#94a3b8">Why a request sits</text>
<rect x="20" y="122" width="270" height="76" rx="8" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
<text x="32" y="142" font-size="13" font-weight="700" fill="#cbd5e1" font-family="ui-monospace, Menlo, monospace">kb/tickets.md</text>
<text x="32" y="160" font-size="12" fill="#f1f5f9">priorities and statuses</text>
<text x="32" y="177" font-size="12" fill="#94a3b8">Priority · Writing a good ticket ·</text>
<text x="32" y="191" font-size="12" fill="#94a3b8">Statuses</text>
<rect x="302" y="122" width="270" height="76" rx="8" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
<text x="314" y="142" font-size="13" font-weight="700" fill="#cbd5e1" font-family="ui-monospace, Menlo, monospace">kb/laptops.md</text>
<text x="314" y="160" font-size="12" fill="#f1f5f9">requesting and securing a laptop</text>
<text x="314" y="177" font-size="12" fill="#94a3b8">Requesting one · Administrator rights ·</text>
<text x="314" y="191" font-size="12" fill="#94a3b8">Encryption and backups · Lost or stolen</text>
<rect x="584" y="122" width="270" height="76" rx="8" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
<text x="596" y="142" font-size="13" font-weight="700" fill="#cbd5e1" font-family="ui-monospace, Menlo, monospace">kb/python-environments.md</text>
<text x="596" y="160" font-size="12" fill="#f1f5f9">uv and the optional-group problem</text>
<text x="596" y="177" font-size="12" fill="#94a3b8">The optional-group problem · Intel Macs ·</text>
<text x="596" y="191" font-size="12" fill="#94a3b8">Local vector stores · Proxies</text>
<rect x="20" y="212" width="410" height="34" rx="8" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5" opacity="0.55"/>
<text x="32" y="234" font-size="12" fill="#94a3b8">prompts/ · 15 pages, one prompt pattern each</text>
<rect x="442" y="212" width="398" height="34" rx="8" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5" opacity="0.55"/>
<text x="454" y="234" font-size="12" fill="#94a3b8">transcripts/ · t01, t02, t03, plus charter.md</text>
<text x="430" y="276" font-size="13" fill="#f1f5f9" text-anchor="middle">Without it the agent reads pages at random. With it, it chooses before it reads: a VPN question goes to the highlighted card.</text>
</svg>
</div>

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

<div style="display:flex;gap:.7em;margin-top:.5em;font-size:.62em">
<div style="flex:1;background:#0b2b40;border-top:5px solid #38bdf8;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#7dd3fc">ASK</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">Before the agent spends a read, what does <code>vpn.md</code> tell it? What does a purpose line and a heading list add?</div></div>
<div style="flex:1;background:#3a2a0a;border-top:5px solid #fbbf24;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#fcd34d">INSPECT</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">DCI_vs_Agentic_RAG Task 1 renders the wiki table. Check each page has a distinct purpose and headings that say where to read.</div></div>
<div style="flex:1;background:#2a1d5a;border-top:5px solid #a78bfa;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#c4b5fd">DECIDE</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">Is the map worth its tokens on every turn, compared with a ranked chunk list that costs none?</div></div>
</div>

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

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 860 300" width="1040" role="img" aria-label="Two loops stacked. Agentic RAG: question, search_chunks, ranked sections, answer, with a search-again edge. DCI: question, list grep read, chosen page, answer, with a read-another-page edge. A dot walks each path.">
<defs><marker id="la" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#94a3b8"/></marker>
<marker id="lbA" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#38bdf8"/></marker>
<marker id="lbD" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#a78bfa"/></marker></defs>
<text x="20" y="26" font-size="16" font-weight="700" fill="#7dd3fc">Agentic RAG</text>
<rect x="20" y="40" width="190" height="46" rx="9" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
<text x="115.0" y="69" font-size="14" font-weight="700" fill="#cbd5e1" text-anchor="middle">question</text>
<path d="M212 63 H226" stroke="#94a3b8" stroke-width="2" marker-end="url(#la)"/>
<rect x="230" y="40" width="190" height="46" rx="9" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/>
<text x="325.0" y="69" font-size="14" font-weight="700" fill="#7dd3fc" text-anchor="middle">search_chunks</text>
<path d="M422 63 H436" stroke="#94a3b8" stroke-width="2" marker-end="url(#la)"/>
<rect x="440" y="40" width="190" height="46" rx="9" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/>
<text x="535.0" y="69" font-size="14" font-weight="700" fill="#7dd3fc" text-anchor="middle">ranked sections</text>
<path d="M632 63 H646" stroke="#94a3b8" stroke-width="2" marker-end="url(#la)"/>
<rect x="650" y="40" width="190" height="46" rx="9" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
<text x="745.0" y="69" font-size="14" font-weight="700" fill="#cbd5e1" text-anchor="middle">answer</text>
<path d="M535.0 88 V112 H325.0 V90" stroke="#38bdf8" stroke-width="1.8" fill="none" stroke-dasharray="5 4" marker-end="url(#lbA)"/>
<text x="430.0" y="130" font-size="12" fill="#94a3b8" text-anchor="middle">or search again</text>
<circle class="loopdot" r="6" fill="#fbbf24" cx="115" cy="36"><animateMotion dur="5s" begin="0s" repeatCount="indefinite" path="M0 0 H420 H630"/></circle>
<text x="20" y="166" font-size="16" font-weight="700" fill="#c4b5fd">DCI</text>
<rect x="20" y="180" width="190" height="46" rx="9" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
<text x="115.0" y="209" font-size="14" font-weight="700" fill="#cbd5e1" text-anchor="middle">question</text>
<path d="M212 203 H226" stroke="#94a3b8" stroke-width="2" marker-end="url(#la)"/>
<rect x="230" y="180" width="190" height="46" rx="9" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2"/>
<text x="325.0" y="209" font-size="14" font-weight="700" fill="#c4b5fd" text-anchor="middle">list / grep / read</text>
<path d="M422 203 H436" stroke="#94a3b8" stroke-width="2" marker-end="url(#la)"/>
<rect x="440" y="180" width="190" height="46" rx="9" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2"/>
<text x="535.0" y="209" font-size="14" font-weight="700" fill="#c4b5fd" text-anchor="middle">chosen page</text>
<path d="M632 203 H646" stroke="#94a3b8" stroke-width="2" marker-end="url(#la)"/>
<rect x="650" y="180" width="190" height="46" rx="9" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
<text x="745.0" y="209" font-size="14" font-weight="700" fill="#cbd5e1" text-anchor="middle">answer</text>
<path d="M535.0 228 V252 H325.0 V230" stroke="#a78bfa" stroke-width="1.8" fill="none" stroke-dasharray="5 4" marker-end="url(#lbD)"/>
<text x="430.0" y="270" font-size="12" fill="#94a3b8" text-anchor="middle">or read another page</text>
<circle class="loopdot" r="6" fill="#fbbf24" cx="115" cy="176"><animateMotion dur="5s" begin="0.6s" repeatCount="indefinite" path="M0 0 H420 H630"/></circle>
</svg>
</div>

Example question: `Which VPN policy applies to contractors?` A retriever returns fragments it scored; file tools let the agent navigate to the page and read around the answer.

<style scoped>@media (prefers-reduced-motion: reduce) { .loopdot { display: none; } }</style>

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

...with how much text came back. That is what you compare, not the prose: which path ran, what it inspected, what it cost.

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 860 310" width="1000" role="img" aria-label="Twin trace for one seed case. Agentic RAG: one search_chunks call returning 1,351 characters, an answer citing the wrong page, judged 0 of 10 in 10.7 seconds. DCI: list_pages returning 2,888 characters then read_page on kb/vpn.md returning 888, an answer naming the page, judged 10 of 10 in 9.6 seconds">
<text x="430" y="22" font-size="13" fill="#f1f5f9" text-anchor="middle">Seed case v01: <tspan font-style="italic">“My VPN connects but I cannot reach staging.”</tspan> Same model, same loop, same judge.</text>
<rect x="14" y="36" width="410" height="242" rx="10" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/>
<text x="30" y="62" font-size="16" font-weight="700" fill="#7dd3fc">Agentic RAG</text>
<circle cx="42" cy="87" r="10" fill="#38bdf8"/><text x="42" y="91" font-size="12" font-weight="700" fill="#0b2b40" text-anchor="middle">1</text>
<text x="62" y="92" font-size="13" fill="#f1f5f9" font-family="ui-monospace, Menlo, monospace">search_chunks(…)</text>
<text x="408" y="92" font-size="13" fill="#fcd34d" text-anchor="end">1,351 chars</text>
<text x="62" y="109" font-size="12" fill="#94a3b8" font-family="ui-monospace, Menlo, monospace">query: “cannot reach staging”</text>
<path d="M30 124 H408" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3 4"/>
<text x="30" y="146" font-size="12" fill="#94a3b8">calls 1 · evidence 1,351 chars · 10.7 s</text>
<text x="30" y="170" font-size="13" fill="#f1f5f9">answer cites: <tspan font-family="ui-monospace, Menlo, monospace">prompts/persona-terse.md</tspan></text>
<rect x="30" y="184" width="120" height="30" rx="6" fill="#3f1212" stroke="#f87171" stroke-width="2"/>
<text x="90" y="204" font-size="13" font-weight="700" fill="#fca5a5" text-anchor="middle">judge 0 / 10</text>
<rect x="436" y="36" width="410" height="242" rx="10" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2"/>
<text x="452" y="62" font-size="16" font-weight="700" fill="#c4b5fd">DCI</text>
<circle cx="464" cy="87" r="10" fill="#a78bfa"/><text x="464" y="91" font-size="12" font-weight="700" fill="#2a1d5a" text-anchor="middle">1</text>
<text x="484" y="92" font-size="13" fill="#f1f5f9" font-family="ui-monospace, Menlo, monospace">list_pages()</text>
<text x="830" y="92" font-size="13" fill="#fcd34d" text-anchor="end">2,888 chars</text>
<text x="484" y="109" font-size="12" fill="#94a3b8" font-family="ui-monospace, Menlo, monospace">returns the wiki</text>
<circle cx="464" cy="131" r="10" fill="#a78bfa"/><text x="464" y="135" font-size="12" font-weight="700" fill="#2a1d5a" text-anchor="middle">2</text>
<text x="484" y="136" font-size="13" fill="#f1f5f9" font-family="ui-monospace, Menlo, monospace">read_page(…)</text>
<text x="830" y="136" font-size="13" fill="#fcd34d" text-anchor="end">888 chars</text>
<text x="484" y="153" font-size="12" fill="#94a3b8" font-family="ui-monospace, Menlo, monospace">page: kb/vpn.md</text>
<path d="M452 168 H830" stroke="#a78bfa" stroke-width="1" stroke-dasharray="3 4"/>
<text x="452" y="190" font-size="12" fill="#94a3b8">calls 2 · evidence 3,776 chars · 9.6 s</text>
<text x="452" y="214" font-size="13" fill="#f1f5f9">answer cites: <tspan font-family="ui-monospace, Menlo, monospace">kb/vpn.md</tspan></text>
<rect x="452" y="228" width="120" height="30" rx="6" fill="#0f3320" stroke="#4ade80" stroke-width="2"/>
<text x="512" y="248" font-size="13" font-weight="700" fill="#86efac" text-anchor="middle">judge 10 / 10</text>
<text x="430" y="300" font-size="12" fill="#94a3b8" text-anchor="middle">A fluent answer scored 0: the trace shows the search never returned the page. Latency ≈ calls × (retrieval + model time).</text>
</svg>
</div>

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

<div style="display:flex;gap:.7em;margin-top:.5em;font-size:.62em">
<div style="flex:1;background:#0b2b40;border-top:5px solid #38bdf8;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#7dd3fc">ASK</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">The answer reads well. The trace never returned the page. Which gate can you still blame, and which two can you rule out?</div></div>
<div style="flex:1;background:#3a2a0a;border-top:5px solid #fbbf24;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#fcd34d">INSPECT</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">DCI_vs_Agentic_RAG Tasks 4 and 5 print both traces with named-page evidence, calls, characters, and latency.</div></div>
<div style="flex:1;background:#2a1d5a;border-top:5px solid #a78bfa;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#c4b5fd">DECIDE</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35"><b>Source</b> · <b>Retrieval</b> · <b>Generation</b>. Name the one, and what you would change first.</div></div>
</div>

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

<div style="display:flex;gap:.7em;margin-top:.5em;font-size:.62em">
<div style="flex:1;background:#0b2b40;border-top:5px solid #38bdf8;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#7dd3fc">ASK</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">The model chose <code>read_page</code> on someone's ticket. What has to be true before the tool runs?</div></div>
<div style="flex:1;background:#3a2a0a;border-top:5px solid #fbbf24;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#fcd34d">INSPECT</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">DCI_vs_Agentic_RAG Task 2 asks which of the four tools could leak one user's transcript into another user's answer.</div></div>
<div style="flex:1;background:#2a1d5a;border-top:5px solid #a78bfa;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#c4b5fd">DECIDE</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">Which checks, and where they live: in the instructions to the model, or inside the tool itself.</div></div>
</div>

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

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 860 274" width="1000" role="img" aria-label="Four RAGAS metrics in two columns: retrieval holds context precision and context recall; generation holds faithfulness and answer relevancy; each names what it looks at and what it does not establish">
<text x="219" y="26" font-size="12" fill="#fcd34d" letter-spacing="1.5" text-anchor="middle">RETRIEVAL · the chunks that arrived</text>
<rect x="14" y="40" width="410" height="84" rx="10" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/>
<text x="30" y="68" font-size="17" font-weight="700" fill="#fcd34d">Context precision</text>
<text x="30" y="90" font-size="13" fill="#f1f5f9">did useful evidence rank high?</text>
<text x="30" y="110" font-size="12" fill="#94a3b8">does not establish answer correctness</text>
<rect x="14" y="136" width="410" height="84" rx="10" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/>
<text x="30" y="164" font-size="17" font-weight="700" fill="#fcd34d">Context recall</text>
<text x="30" y="186" font-size="13" fill="#f1f5f9">did needed evidence appear at all?</text>
<text x="30" y="206" font-size="12" fill="#94a3b8">does not establish complete retrieval</text>
<text x="641" y="26" font-size="12" fill="#7dd3fc" letter-spacing="1.5" text-anchor="middle">GENERATION · the answer written from them</text>
<rect x="436" y="40" width="410" height="84" rx="10" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/>
<text x="452" y="68" font-size="17" font-weight="700" fill="#7dd3fc">Faithfulness</text>
<text x="452" y="90" font-size="13" fill="#f1f5f9">did claims stay supported by the chunks?</text>
<text x="452" y="110" font-size="12" fill="#94a3b8">does not establish source authority</text>
<rect x="436" y="136" width="410" height="84" rx="10" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/>
<text x="452" y="164" font-size="17" font-weight="700" fill="#7dd3fc">Answer relevancy</text>
<text x="452" y="186" font-size="13" fill="#f1f5f9">did it address the question?</text>
<text x="452" y="206" font-size="12" fill="#94a3b8">does not establish factual truth</text>
<path d="M430 40 V220" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 4"/>
<text x="430" y="248" font-size="13" fill="#f1f5f9" text-anchor="middle">Left column needs the reference answer; right column is scored without one.</text>
<text x="430" y="266" font-size="13" fill="#f1f5f9" text-anchor="middle">A low score on the left is a retrieval repair; on the right, a prompt or model repair.</text>
</svg>
</div>

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

<div style="display:flex;gap:.7em;margin-top:.5em;font-size:.62em">
<div style="flex:1;background:#0b2b40;border-top:5px solid #38bdf8;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#7dd3fc">ASK</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">The model behaved correctly. <b>What should have happened instead?</b> What does a correct-looking run still owe you?</div></div>
<div style="flex:1;background:#3a2a0a;border-top:5px solid #fbbf24;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#fcd34d">INSPECT</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">Improving_RAG_with_RAGAS Task 2's generated cases, and the chunks retrieved for each answer: was the passage in context at all?</div></div>
<div style="flex:1;background:#2a1d5a;border-top:5px solid #a78bfa;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#c4b5fd">DECIDE</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">Nothing, it was right · record a retrieval miss · rewrite the prompt. Pick one and say which metric shows it.</div></div>
</div>

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

<div style="font-size:.62em;color:#cbd5e1">Baseline: <code>k=2</code> → missing policy passage · Change: <code>k=6</code> → inspect whether the passage enters context · Decision: keep the change only if the relevant metric and trace improve</div>

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 860 282" width="1000" role="img" aria-label="Paired bars for four RAGAS metrics before and after raising k from 2 to 6 on the seed run: faithfulness 0.90 to 0.72, answer relevancy 0.65 to 0.65, context precision 0.50 to 0.54, context recall 0.35 to 0.63">
<path d="M54 200 H820" stroke="#94a3b8" stroke-width="1.5" opacity="1"/>
<text x="48" y="204" font-size="12" fill="#94a3b8" text-anchor="end">0</text>
<path d="M54 162 H820" stroke="#94a3b8" stroke-width="0.6" opacity="0.5"/>
<text x="48" y="166" font-size="12" fill="#94a3b8" text-anchor="end">0.25</text>
<path d="M54 125 H820" stroke="#94a3b8" stroke-width="0.6" opacity="0.5"/>
<text x="48" y="129" font-size="12" fill="#94a3b8" text-anchor="end">0.5</text>
<path d="M54 88 H820" stroke="#94a3b8" stroke-width="0.6" opacity="0.5"/>
<text x="48" y="92" font-size="12" fill="#94a3b8" text-anchor="end">0.75</text>
<path d="M54 50 H820" stroke="#94a3b8" stroke-width="0.6" opacity="0.5"/>
<text x="48" y="54" font-size="12" fill="#94a3b8" text-anchor="end">1</text>
<rect x="90" y="65.0" width="54" height="135.0" rx="3" fill="#94a3b8"/>
<text x="117" y="59" font-size="12" fill="#f1f5f9" text-anchor="middle">0.90</text>
<rect x="150" y="91.5" width="54" height="108.5" rx="3" fill="#fbbf24"/>
<text x="177" y="86" font-size="12" fill="#f1f5f9" text-anchor="middle">0.72</text>
<text x="147" y="220" font-size="13" fill="#f1f5f9" text-anchor="middle">faithfulness</text>
<text x="147" y="238" font-size="12" fill="#fca5a5" text-anchor="middle">-0.18</text>
<rect x="280" y="103.1" width="54" height="96.9" rx="3" fill="#94a3b8"/>
<text x="307" y="97" font-size="12" fill="#f1f5f9" text-anchor="middle">0.65</text>
<rect x="340" y="102.3" width="54" height="97.7" rx="3" fill="#fbbf24"/>
<text x="367" y="96" font-size="12" fill="#f1f5f9" text-anchor="middle">0.65</text>
<text x="337" y="220" font-size="13" fill="#f1f5f9" text-anchor="middle">answer relevancy</text>
<text x="337" y="238" font-size="12" fill="#94a3b8" text-anchor="middle">+0.01</text>
<rect x="470" y="125.0" width="54" height="75.0" rx="3" fill="#94a3b8"/>
<text x="497" y="119" font-size="12" fill="#f1f5f9" text-anchor="middle">0.50</text>
<rect x="530" y="119.0" width="54" height="81.0" rx="3" fill="#fbbf24"/>
<text x="557" y="113" font-size="12" fill="#f1f5f9" text-anchor="middle">0.54</text>
<text x="527" y="220" font-size="13" fill="#f1f5f9" text-anchor="middle">context precision</text>
<text x="527" y="238" font-size="12" fill="#94a3b8" text-anchor="middle">+0.04</text>
<rect x="660" y="147.5" width="54" height="52.5" rx="3" fill="#94a3b8"/>
<text x="687" y="142" font-size="12" fill="#f1f5f9" text-anchor="middle">0.35</text>
<rect x="720" y="105.5" width="54" height="94.5" rx="3" fill="#fbbf24"/>
<text x="747" y="100" font-size="12" fill="#f1f5f9" text-anchor="middle">0.63</text>
<text x="717" y="220" font-size="13" fill="#f1f5f9" text-anchor="middle">context recall</text>
<text x="717" y="238" font-size="12" fill="#86efac" text-anchor="middle">+0.28</text>
<rect x="60" y="14" width="14" height="14" rx="3" fill="#94a3b8"/><text x="80" y="26" font-size="12" fill="#f1f5f9">baseline k = 2</text>
<rect x="210" y="14" width="14" height="14" rx="3" fill="#fbbf24"/><text x="230" y="26" font-size="12" fill="#f1f5f9">improved k = 6</text>
<text x="820" y="26" font-size="12" fill="#94a3b8" text-anchor="end">seed run, same prompt, same questions, same judge</text>
<text x="430" y="258" font-size="12" fill="#94a3b8" text-anchor="middle">The notebook puts an interval on the faithfulness difference; at six questions it usually spans zero,</text>
<text x="430" y="274" font-size="12" fill="#94a3b8" text-anchor="middle">so the dip is not yet a measured difference. Context recall is the solid signal.</text>
</svg>
</div>

**A metric starts the diagnosis; it does not finish it.** Fix the one thing that failed, then move to the next.

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

<div style="display:flex;gap:.7em;margin-top:.5em;font-size:.62em">
<div style="flex:1;background:#0b2b40;border-top:5px solid #38bdf8;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#7dd3fc">ASK</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">The metric is high. What would make you refuse to believe it before changing the system?</div></div>
<div style="flex:1;background:#3a2a0a;border-top:5px solid #fbbf24;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#fcd34d">INSPECT</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">Improving_RAG_with_RAGAS Task 4's baseline rows: the cases behind the number, and the datasheet from Task 3.</div></div>
<div style="flex:1;background:#2a1d5a;border-top:5px solid #a78bfa;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#c4b5fd">DECIDE</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">Trust the number · audit the set · read a trace first. What in the set would make the number meaningless?</div></div>
</div>

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

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 860 262" width="1000" role="img" aria-label="A funnel from generated cases through near-duplicate, schema, and leak checks and a human review to the kept test set, with the datasheet recording what was removed">
<polygon points="14,25 132,35 132,165 14,175" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
<text x="22" y="47" font-size="13" font-weight="700" fill="#cbd5e1">generated</text>
<text x="22" y="65" font-size="12" fill="#f1f5f9">8 by default</text>
<polygon points="154,35 272,45 272,155 154,165" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/>
<text x="162" y="57" font-size="13" font-weight="700" fill="#7dd3fc">dedupe</text>
<polygon points="294,45 412,55 412,145 294,155" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/>
<text x="302" y="67" font-size="13" font-weight="700" fill="#7dd3fc">schema check</text>
<polygon points="434,55 552,64 552,136 434,145" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/>
<text x="442" y="77" font-size="13" font-weight="700" fill="#7dd3fc">leak check</text>
<polygon points="574,64 692,72 692,128 574,136" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2"/>
<text x="582" y="86" font-size="13" font-weight="700" fill="#c4b5fd">person reviews</text>
<polygon points="714,72 832,72 832,128 714,128" fill="#0f3320" stroke="#4ade80" stroke-width="2"/>
<text x="722" y="94" font-size="13" font-weight="700" fill="#86efac">kept</text>
<text x="722" y="112" font-size="12" fill="#f1f5f9">5 in the seed</text>
<text x="73" y="196" font-size="12" fill="#94a3b8" text-anchor="middle">a draft, not a</text>
<text x="73" y="211" font-size="12" fill="#94a3b8" text-anchor="middle">measurement</text>
<text x="213" y="196" font-size="12" fill="#94a3b8" text-anchor="middle">4-gram Jaccard ≥ 0.7</text>
<text x="213" y="211" font-size="12" fill="#94a3b8" text-anchor="middle">is one question</text>
<text x="353" y="196" font-size="12" fill="#94a3b8" text-anchor="middle">an empty reference is</text>
<text x="353" y="211" font-size="12" fill="#94a3b8" text-anchor="middle">its own failure</text>
<text x="493" y="196" font-size="12" fill="#94a3b8" text-anchor="middle">8+ words copied from</text>
<text x="493" y="211" font-size="12" fill="#94a3b8" text-anchor="middle">a page test nothing</text>
<text x="633" y="196" font-size="12" fill="#94a3b8" text-anchor="middle">before it gates anything</text>
<text x="633" y="211" font-size="12" fill="#94a3b8" text-anchor="middle"></text>
<text x="773" y="196" font-size="12" fill="#94a3b8" text-anchor="middle">the test set later</text>
<text x="773" y="211" font-size="12" fill="#94a3b8" text-anchor="middle">tasks score</text>
<text x="430" y="238" font-size="13" fill="#fcd34d" text-anchor="middle">The datasheet travels with the set: what was removed at each step, and what the set cannot test.</text>
<text x="430" y="256" font-size="12" fill="#94a3b8" text-anchor="middle">removal counts are the datasheet's to fill in; generated and kept are the notebook default and the seed set</text>
</svg>
</div>

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

<div style="display:flex;gap:.7em;margin-top:.5em;font-size:.62em">
<div style="flex:1;background:#0b2b40;border-top:5px solid #38bdf8;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#7dd3fc">ASK</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">Name one generated case you would throw out before scoring, and say what is wrong with it.</div></div>
<div style="flex:1;background:#3a2a0a;border-top:5px solid #fbbf24;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#fcd34d">INSPECT</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">Improving_RAG_with_RAGAS Task 3's datasheet, and its one line per removed row saying why.</div></div>
<div style="flex:1;background:#2a1d5a;border-top:5px solid #a78bfa;border-radius:10px;padding:.7em .9em .8em"><div style="font-size:.78em;letter-spacing:.14em;color:#c4b5fd">DECIDE</div><div style="color:#f1f5f9;margin-top:.35em;line-height:1.35">Which of the three curation checks would have caught it, or none, so a person has to.</div></div>
</div>

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
