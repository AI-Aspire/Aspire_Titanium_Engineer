---
marp: true
theme: default
paginate: true
size: 16:9
class: invert
---

# Today: longer horizons, more sources, more ways to be wrong

<div style="display:flex;justify-content:center;margin-top:.3em">
<svg viewBox="0 0 860 200" width="1080" role="img" aria-label="The five modules of the day drawn to their length in minutes: voice agents 40, prompt optimisation 35, GraphRAG 40, deep research 35, off-the-shelf guardrails 30, 180 minutes in all">
<text x="10" y="34" font-size="14" fill="#94a3b8">Five modules, 180 minutes, each one a loop that runs longer or sees more than the last</text>
<rect x="10" y="60" width="181" height="88" rx="9" fill="#1e293b" stroke="#94a3b8" stroke-width="2.5"/><text x="20" y="84" font-size="15" font-weight="700" fill="#cbd5e1">14</text><text x="20" y="105" font-size="13" fill="#f1f5f9">Voice agents</text><text x="20" y="138" font-size="12" fill="#94a3b8">40 min</text>
<rect x="197" y="60" width="159" height="88" rx="9" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/><text x="207" y="84" font-size="15" font-weight="700" fill="#7dd3fc">15</text><text x="207" y="105" font-size="13" fill="#f1f5f9">Prompt optimisation</text><text x="207" y="138" font-size="12" fill="#94a3b8">35 min</text>
<rect x="362" y="60" width="181" height="88" rx="9" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2.5"/><text x="372" y="84" font-size="15" font-weight="700" fill="#c4b5fd">16</text><text x="372" y="105" font-size="13" fill="#f1f5f9">GraphRAG</text><text x="372" y="138" font-size="12" fill="#94a3b8">40 min</text>
<rect x="549" y="60" width="159" height="88" rx="9" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/><text x="559" y="84" font-size="15" font-weight="700" fill="#fcd34d">17</text><text x="559" y="105" font-size="13" fill="#f1f5f9">Deep research</text><text x="559" y="138" font-size="12" fill="#94a3b8">35 min</text>
<rect x="714" y="60" width="136" height="88" rx="9" fill="#0f3320" stroke="#4ade80" stroke-width="2.5"/><text x="724" y="84" font-size="15" font-weight="700" fill="#86efac">18</text><text x="724" y="105" font-size="13" fill="#f1f5f9">Off-the-shelf</text><text x="724" y="121" font-size="13" fill="#f1f5f9">guardrails</text><text x="724" y="138" font-size="12" fill="#94a3b8">30 min</text>
<path d="M10 164 H850" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 4"/>
<g font-size="12" fill="#94a3b8"><text x="10" y="184">0 min</text><text x="197" y="184">40</text><text x="362" y="184">75</text><text x="549" y="184">115</text><text x="714" y="184">150</text><text x="850" y="184" text-anchor="end">180 min</text></g>
</svg>
</div>

A six-step loop running unsupervised across many sources has a different failure surface than one you watch.

<!--
Slide ID: D4-F1
Module: Framing, before the selected modules
Instructor: Eli, Beric
Type: framing
Minutes: 2
Layout: 02 Agenda
Speaker notes:
- Say: Today the system runs longer, sees more sources, and needs more explicit boundaries.
- Ask: Where would you want a person to see evidence before this loop continues?
- Watch: Notebook:cell#24 shows the streamed research lifecycle; Notebook:cell#16 shows a transform before the model sees input.
- Then: Start cold with the research graph, then carry its trace into the guardrail boundary.
Sources: [17 Deep Research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md), [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
-->

---
# 14 · Voice agents

**A research panel you can hear.** · 40 min

- A planner splits the question, researchers read your corpus, a critic attacks the draft, a judge decides
- Speech is a round trip bolted onto a loop you already understand

<!--
Slide ID: D4-T14
Module: [14 Voice agents](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/14_Voice_Agents/README.md)
Instructor: Eli
Type: transition
Minutes: 0
Layout: 01 Title
Speaker notes:
- Say: Voice is not a new kind of agent. It is two HTTP services either side of the loop you have been building all week.
- Ask: Hold for a beat — this is the hand-off, not content.
- Watch: Name the module and move. The panel roles are the content.
- Then: Straight into the first content slide.
Sources: [Module 14 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/14_Voice_Agents/README.md).
-->
---
# Voice is a round trip, not a new architecture

- **STT:** audio in, a transcript out · **TTS:** a line and a voice name in, audio out
- Both are OpenAI-compatible HTTP services, like every other call this week
- Prove the round trip *first*: synthesize a line, play it, transcribe it back, compare
- Everything between them is the agent loop you already have

<!--
Slide ID: D4-M14-C1
Module: [14 Voice agents](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/14_Voice_Agents/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: The reason to prove the round trip before building anything on it is that speech failures and reasoning failures look identical in a transcript. If you have not confirmed the audio path, every bad answer is ambiguous.
- Ask: A narrated answer comes back wrong. How do you tell a transcription error from a research error?
- Watch: Voice_Deep_Research:cell#9 is Task 1 of 6 — voice in, voice out. In the notebook: two OpenAI-compatible HTTP services do the speech work; prove the round trip before building anything on it.
- Then: Note this is the OpenAI-compatible idea from Monday doing real work — the speech services swap the same way the model does.
Sources: [OpenAI speech to text](https://developers.openai.com/api/docs/guides/speech-to-text), [voice notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/14_Voice_Agents/Voice_Deep_Research.ipynb)
-->
---
# A critic that sends the draft back

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 760 180" width="900" role="img" aria-label="The voice panel loop: a planner splits a question into three angles, three researchers work in parallel, an aggregator drafts, then a critic and judge loop back until the judge passes the draft">
<rect x="10" y="60" width="104" height="50" rx="8" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2.5"/>
<text x="62" y="82" font-size="13" font-weight="700" text-anchor="middle" fill="#c4b5fd">planner</text>
<text x="62" y="99" font-size="10.5" text-anchor="middle" fill="#a78bfa">3 angles</text>
<rect x="148" y="22" width="104" height="30" rx="6" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/>
<text x="200" y="42" font-size="11.5" text-anchor="middle" fill="#7dd3fc">researcher</text>
<rect x="148" y="60" width="104" height="30" rx="6" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/>
<text x="200" y="80" font-size="11.5" text-anchor="middle" fill="#7dd3fc">researcher</text>
<rect x="148" y="98" width="104" height="30" rx="6" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/>
<text x="200" y="118" font-size="11.5" text-anchor="middle" fill="#7dd3fc">researcher</text>
<rect x="286" y="60" width="104" height="50" rx="8" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2.5"/>
<text x="338" y="82" font-size="13" font-weight="700" text-anchor="middle" fill="#c4b5fd">aggregator</text>
<text x="338" y="99" font-size="10.5" text-anchor="middle" fill="#a78bfa">drafts</text>
<rect x="424" y="60" width="90" height="50" rx="8" fill="#3f1212" stroke="#f87171" stroke-width="2.5"/>
<text x="469" y="82" font-size="13" font-weight="700" text-anchor="middle" fill="#fecaca">critic</text>
<text x="469" y="99" font-size="10.5" text-anchor="middle" fill="#fca5a5">attacks</text>
<rect x="548" y="60" width="90" height="50" rx="8" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/>
<text x="593" y="82" font-size="13" font-weight="700" text-anchor="middle" fill="#fcd34d">judge</text>
<text x="593" y="99" font-size="10.5" text-anchor="middle" fill="#fcd34d">pass?</text>
<rect x="668" y="68" width="82" height="34" rx="8" fill="#0f3320" stroke="#4ade80" stroke-width="2.5"/>
<text x="709" y="90" font-size="12.5" font-weight="700" text-anchor="middle" fill="#86efac">answer</text>
<path d="M116 85 H144" stroke="#94a3b8" stroke-width="2" marker-end="url(#va)"/>
<path d="M254 75 H282" stroke="#94a3b8" stroke-width="2" marker-end="url(#va)"/>
<path d="M392 85 H420" stroke="#94a3b8" stroke-width="2" marker-end="url(#va)"/>
<path d="M516 85 H544" stroke="#94a3b8" stroke-width="2" marker-end="url(#va)"/>
<path d="M640 85 H664" stroke="#4ade80" stroke-width="2.5" marker-end="url(#vg)"/>
<path d="M593 114 V140 H338 V114" fill="none" stroke="#f87171" stroke-width="2.5" stroke-dasharray="5 3" marker-end="url(#vr)"/>
<text x="466" y="155" font-size="11.5" text-anchor="middle" fill="#fca5a5" font-style="italic">sent back for a revision · capped rounds</text>
<defs>
<marker id="va" markerWidth="9" markerHeight="9" refX="7.5" refY="3" orient="auto"><path d="M0 0 L7.5 3 L0 6 z" fill="#94a3b8"/></marker>
<marker id="vg" markerWidth="9" markerHeight="9" refX="7.5" refY="3" orient="auto"><path d="M0 0 L7.5 3 L0 6 z" fill="#4ade80"/></marker>
<marker id="vr" markerWidth="9" markerHeight="9" refX="7.5" refY="3" orient="auto"><path d="M0 0 L7.5 3 L0 6 z" fill="#f87171"/></marker>
</defs>
</svg>
</div>

The judge can refuse. That backward edge is the module — and the round cap is what keeps it from running forever.

<!--
Slide ID: D4-M14-C2
Module: [14 Voice agents](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/14_Voice_Agents/README.md)
Instructor: Eli
Type: core
Minutes: 3
Layout: 06 Process steps
Speaker notes:
- Say: Every loop so far ran forward. This one has an edge that goes back: the critic attacks the draft, the judge decides, and a failed draft returns to the aggregator for another round. That is also the first thing that can spin, which is why the cap is part of the design and not a safety afterthought.
- Ask: What would make you cap the rounds at two rather than five?
- Watch: Voice_Deep_Research:cell#24 is Task 5 of 6 — the full narrated session. In the notebook: the orchestrator runs plan, three researchers in parallel, aggregate, then critic and judge until the judge passes the draft or the round cap hits. Every step is an event, and the narrator compresses long events to one spoken line.
- Then: The questions the panel researches are the failing tasks from their own capability report, so the panel is auditing their own agent out loud.
Sources: [voice notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/14_Voice_Agents/Voice_Deep_Research.ipynb)
-->
---
# 15 · Prompt optimisation

**Stop hand-tuning the prompt. Compile it.** · 35 min

- A signature, a metric, and an optimiser that searches for the instruction and the demos
- BootstrapFewShot, MIPROv2, GEPA — on the same task, measured the same way

<!--
Slide ID: D4-T15
Module: [15 Prompt optimisation](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/15_Prompt_Optimization/README.md)
Instructor: Eli
Type: transition
Minutes: 0
Layout: 01 Title
Speaker notes:
- Say: Monday you wrote prompts by hand. This module makes writing them a compile step with a number attached.
- Ask: Hold for a beat — this is the hand-off, not content.
- Watch: Needs the optim dependency group — make setup-optim, once, before the notebook opens.
- Then: Straight into the first content slide.
Sources: [Module 15 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/15_Prompt_Optimization/README.md).
-->
---
# An optimiser is a search, so it needs a bar

<div style="font-size:.8em">A <b>signature</b> is the fields in and out, with one instruction. A <b>metric</b> says whether one prediction was good — here, agreement with <i>your</i> hand scores. Score the un-optimised program on held-out examples <b>first</b>: that number is the bar every optimiser has to beat.</div>

<div style="display:flex;justify-content:center;margin-top:.2em">
<svg viewBox="0 0 860 236" width="960" role="img" aria-label="Bar chart of held-out agreement for the baseline judge and three optimisers from the seed run: baseline, BootstrapFewShot and GEPA all reach one of three, MIPROv2 was skipped, and the dashed baseline bar sits at one of three">
<path d="M90 30 V196 H560" fill="none" stroke="#94a3b8" stroke-width="1.5"/>
<g font-size="12" fill="#94a3b8" text-anchor="end">
<text x="82" y="200">0 of 3</text><text x="82" y="145">1 of 3</text><text x="82" y="89">2 of 3</text><text x="82" y="34">3 of 3</text>
</g>
<g stroke="#334155" stroke-width="1"><path d="M90 140 H560"/><path d="M90 85 H560"/><path d="M90 30 H560"/></g>
<text x="40" y="112" font-size="12" fill="#94a3b8" text-anchor="middle" transform="rotate(-90 40 112)">held-out agreement</text>
<rect x="115" y="140" width="70" height="56" rx="4" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
<rect x="230" y="140" width="70" height="56" rx="4" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/>
<rect x="345" y="30" width="70" height="166" rx="4" fill="none" stroke="#475569" stroke-width="1.5" stroke-dasharray="5 4"/>
<rect x="460" y="140" width="70" height="56" rx="4" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/>
<g font-size="13" fill="#f1f5f9" text-anchor="middle"><text x="150" y="165">33%</text><text x="265" y="165">33%</text><text x="495" y="165">33%</text></g>
<text x="380" y="118" font-size="12" fill="#94a3b8" text-anchor="middle">skipped</text>
<text x="380" y="134" font-size="12" fill="#94a3b8" text-anchor="middle">that run</text>
<g font-size="12" fill="#cbd5e1" text-anchor="middle"><text x="150" y="216">baseline</text><text x="265" y="216">BootstrapFewShot</text><text x="380" y="216">MIPROv2</text><text x="495" y="216">GEPA</text></g>
<path d="M90 140 H560" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="7 4"/>
<text x="96" y="132" font-size="12" font-weight="700" fill="#fcd34d">the bar: baseline, 1 of 3</text>
<rect x="600" y="30" width="250" height="166" rx="10" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/>
<text x="616" y="56" font-size="15" font-weight="700" fill="#fcd34d">Seed run, real numbers</text>
<g font-size="13" fill="#f1f5f9"><text x="616" y="82">3 train, 3 held out</text><text x="616" y="102">agree = within 1 point on 1 to 10</text><text x="616" y="122">nothing cleared the bar</text><text x="616" y="142">winner saved: baseline</text></g>
<text x="616" y="166" font-size="12" fill="#fcd34d">a tie goes to the cheapest program,</text>
<text x="616" y="182" font-size="12" fill="#fcd34d">which is no optimiser at all</text>
</svg>
</div>

Without the baseline, "the optimiser helped" is a feeling. With 3 held-out examples, one disagreement moves the bar by 33 points.

<!--
Slide ID: D4-M15-C1
Module: [15 Prompt optimisation](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/15_Prompt_Optimization/README.md)
Instructor: Eli
Type: core
Minutes: 3
Layout: 06 Process steps
Speaker notes:
- Say: This is measure-before-you-adopt again, now pointed at the prompt itself. The metric here is agreement with the scores you assigned by hand, which means the optimiser is searching for a prompt that judges the way you judge. Held-out matters: examples the optimiser never saw are the only honest score.
- Ask: Your optimised judge agrees with you 90 percent of the time. What have you not yet learned about it?
- Watch: DSPy_Optimizers:cell#12 is Task 2 of 6 — the program and the metric. In the notebook: score the un-optimized program on the held-out examples first, because that number is the bar every optimizer has to beat. DSPy_Optimizers:cell#9 is Task 1, building examples from the transcripts they scored by hand.
- Then: Six hand-scored transcripts is a small training set — say so, and say that it bounds how much any optimiser can claim.
Sources: [DSPy](https://arxiv.org/abs/2310.03714), [optimiser notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/15_Prompt_Optimization/DSPy_Optimizers.ipynb)
-->
---
# DSPy: declare the interface, let it write the prompt

```python
class ScoreAnswer(dspy.Signature):
    """Score a support assistant's answer to a user's question."""   # ← rewritable
    question: str = dspy.InputField()
    response: str = dspy.InputField()
    score:    int = dspy.OutputField(desc="an integer score")


def agreement(example, pred, trace=None) -> bool:
    return abs(as_int(pred.score) - example.score) <= TOL
```

**signature** = the interface · **metric** = the objective · **optimiser** = the search

No prompt string anywhere. `agreement` is the whole objective — the optimiser can only chase what it returns.

<!--
Slide ID: D4-M15-C1A
Module: [15 Prompt optimisation](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/15_Prompt_Optimization/README.md)
Instructor: Eli
Type: core
Minutes: 3
Layout: 04 Lab and code
Speaker notes:
- Say: This is DSPy's whole premise on one slide, and it is worth naming as a framework choice rather than a coding style. You declare the interface — fields in, fields out, one docstring — and you never write the prompt. The metric is an ordinary Python function returning a bool. Then an optimiser searches for the instruction and demos that maximise it. Three parts: signature, metric, optimiser, and the next slide is about the third.
- Ask: The metric allows a tolerance. What does that choice do to what the optimiser learns?
- Watch: Notebook:cell#13 — Task 2 defines the program and the metric. Point at the docstring and at with_instructions: that string is what MIPROv2 and GEPA are allowed to rewrite, which is why the instruction lives in exactly one place. If anyone already uses DSPy, this is the slide to check their intuition against — the framework is familiar to some rooms and completely new to others.
- Then: This is the sharpest version of a point from Monday — the objective you write down is the only thing that gets optimised. A loose tolerance buys agreement cheaply and teaches the judge less.
Sources: [DSPy](https://arxiv.org/abs/2310.03714), [optimiser notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/15_Prompt_Optimization/DSPy_Optimizers.ipynb)
-->
---
# Three optimisers, three things they are allowed to change

| Optimiser | What it changes | Cost |
|---|---|---|
| BootstrapFewShot | demos only — never the instruction | cheapest |
| MIPROv2 | proposes instructions **and** demo sets, keeps the best mix | many more calls |
| GEPA | reads *why* a guess was wrong and rewrites the instruction | needs feedback text |

Read the table as cost against benefit, not as a leaderboard.

<!--
Slide ID: D4-M15-C2
Module: [15 Prompt optimisation](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/15_Prompt_Optimization/README.md)
Instructor: Eli
Type: core
Minutes: 3
Layout: 05 Two column
Speaker notes:
- Say: The useful distinction is what each one is permitted to touch. Bootstrap can only replay what the base program already gets right, so it cannot fix a task the program fails outright. MIPROv2 searches instruction space, which costs calls. GEPA needs a metric that returns feedback text rather than just a number, and it may not be in the installed DSPy — the cell checks and skips cleanly.
- Ask: Which of the three can improve a prompt that currently fails every example?
- Watch: DSPy_Optimizers:cell#16, cell#19, and cell#23 are Tasks 3, 4, and 5 — BootstrapFewShot, MIPROv2, GEPA. In the notebook: bootstrap never changes the instruction and can only replay what the base program already gets right.
- Then: The answer to the Ask is not bootstrap — if nothing passes the metric, it has nothing to harvest as a demo. Then land on cost against benefit and move.
Sources: [DSPy](https://arxiv.org/abs/2310.03714), [optimiser notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/15_Prompt_Optimization/DSPy_Optimizers.ipynb)
-->
---
# 16 · GraphRAG

**When does a graph earn its cost?** · 40 min

- A vector store retrieves what *looks like* the question; a graph retrieves what is *connected* to it
- Built three ways, measured against the strongest vector baseline you can build

<!--
Slide ID: D4-T16
Module: [16 GraphRAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/16_GraphRAG/README.md)
Instructor: Eli
Type: transition
Minutes: 0
Layout: 01 Title
Speaker notes:
- Say: This module is a decision, not a technique tour. The deliverable is a table that says whether the graph was worth building.
- Ask: Hold for a beat — this is the hand-off, not content.
- Watch: Needs the graph dependency group — make setup-graph, once, which installs spaCy, its English model, networkx, and rdflib.
- Then: Straight into the first content slide.
Sources: [Module 16 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/16_GraphRAG/README.md).
-->
---
# The multi-hop hypothesis

Some questions are answered in one page. The interesting ones need **two**:

- a transcript where the agent failed, **and** the knowledge-base page it should have used
- similarity ranking may grab one side strongly and miss the other entirely
- a graph that knows the two are connected can walk from one to the other

That is the hypothesis. The rest of the module tries to falsify it.

<!--
Slide ID: D4-M16-C1
Module: [16 GraphRAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/16_GraphRAG/README.md)
Instructor: Eli
Type: core
Minutes: 3
Layout: 05 Two column
Speaker notes:
- Say: A graph is expensive, so it needs a hypothesis it can fail. This is it: one hop past the words. A question whose answer lives in two documents is where similarity search is structurally weak, because ranking each candidate independently has no way to prefer a pair.
- Ask: Think of a question about your own product whose answer needs two documents — which two?
- Watch: GraphRAG:cell#9 is Task 1 of 7 — the multi-hop hypothesis. In the notebook: a retriever that ranks by similarity may grab one side strongly and miss the other. That is also the question their README asked them to bring.
- Then: Note what a triple is — subject, relation, object, with the page it came from — because the provenance on the edge is what makes a graph answer checkable.
Sources: [graph notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/16_GraphRAG/GraphRAG.ipynb)
-->
---
# How does it *know* two things are related?

Same sections in, a graph out — **only the extractor differs**:

| Extractor | How it decides | Cost | Fails by |
|---|---|---|---|
| **spaCy NER** | two entities share a sentence → one *untyped* edge | cheap | domain-blind |
| **Ontology** | hand-written phrase schema: actors, objects, actions | free at run time | finds only what it anticipated |
| **Model** | reads a section, emits typed triples | one call per section | relation drift |

Structure alone gives you a graph. Only semantics give you a *knowledge* graph.

<!--
Slide ID: D4-M16-C1A
Module: [16 GraphRAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/16_GraphRAG/README.md)
Instructor: Eli
Type: core
Minutes: 4
Layout: 05 Two column
Speaker notes:
- Say: The previous slide claimed a graph knows two things are connected. This is where that claim gets paid for, because knowing is not free and it is not automatic. Three extractors, same input, and the edge means something different in each. spaCy joins any two named entities that appear in one sentence, so an edge means co-occurrence and nothing more. The ontology is a hand-written schema, so an edge means a relationship someone anticipated. The model reads and emits typed triples, so an edge means whatever the model inferred — flexible, and it drifts, because two pages can describe the same relationship with different relation names.
- Ask: Which of the three would you trust to connect a failed trajectory to the knowledge-base page that would have fixed it?
- Watch: GraphRAG:cell#16 is Task 3 of 7 — spaCy and the ontology; cell#20 is Task 4 — the model extractor. In the notebook: same sections in, a graph out, only the extractor differs, and the part that matters when comparing the three is what a node and an edge mean in each. Every graph also gets structural edges from their trajectories: which task each run tried, which tools it called, whether it passed.
- Then: Those structural edges are the honest answer to the Ask — the trajectory-to-task-to-tool edges are known facts from their own workspace, not inferred text, so they are the reliable part of the graph. The extracted edges are the uncertain part.
- Then: If the room has database people, the storage model is worth a beat. Three ways to hold this: recursive queries on a relational table, which is a self-join you already know how to index and tune; a labelled property graph, where attributes hang on nodes and edges and traversal is the primitive; and RDF triples, where every fact is subject-relation-object and the query language reasons over types. This notebook builds triples and views them two ways — networkx for traversal, rdflib serialised to Turtle at cell#18, where the ontology's types show up as rdf:type statements. The choice drives what is cheap: k-hop traversal, or a type-constrained query, or a join plan.
Sources: [graph notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/16_GraphRAG/GraphRAG.ipynb)
-->
---
# Build the steelman, or the comparison is worthless

- The baseline is **not** a toy top-k: dense **+** BM25, unioned, then a cross-encoder rerank
- Same eval cases, same prompt, same answer model — only the retrieved context differs
- Two measures: **reference recall** (structural, free) and **correctness** (a model judge)
- Decide from the table whether the graph earned its build cost

Beat a weak baseline and you have learned nothing except that you built a weak baseline.

<!--
Slide ID: D4-M16-C2
Module: [16 GraphRAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/16_GraphRAG/README.md)
Instructor: Eli
Type: core
Minutes: 3
Layout: 03 Big stats
Speaker notes:
- Say: This is the most transferable habit in the module and it has nothing to do with graphs. If you want to know whether a new technique helps, the thing you compare against has to be the best version of the old one. The notebook calls it a steelman baseline, and it is the full stack from Tuesday — dense, BM25, cross-encoder rerank.
- Ask: What in your own stack have you adopted without measuring it against its strongest alternative?
- Watch: GraphRAG:cell#12 is Task 2 of 7 — the steelman baseline: dense cosine over the chunks, BM25 over the same chunks, the union as a candidate pool, then a local cross-encoder to rerank to the top five. GraphRAG:cell#29 is Task 6, measuring both on their eval cases. Note the one variable that changes: same prompt as the baseline, so the only difference is what goes into the context window.
- Then: Their README says it plainly — bring your team the table, not the feeling. The saved scores are what a release decision reads when someone proposes GraphRAG.
Sources: [graph notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/16_GraphRAG/GraphRAG.ipynb)
-->
---
# 17 · Deep research

**What happens when the loop runs for twenty steps, unwatched?** · 35 min

- A bounded loop over many sources is a different failure surface than one you watch.

<!--
Slide ID: D4-T17
Module: [17 Deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: transition
Minutes: 0
Layout: 01 Title
Speaker notes:
- Say: A bounded loop over many sources is a different failure surface than one you watch. That is what this module is for.
- Ask: Hold for a beat — this is the hand-off, not content.
- Watch: Name the module and who is running it, then move. One breath.
- Then: Straight into the first content slide.
Sources: [Module 17 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md).
-->
---

# What makes it *research*

> "Research work involves open-ended problems where it's very difficult to predict the required steps in advance."
>
> "You can't hardcode a fixed path for exploring complex topics, as the process is inherently dynamic and path-dependent."
>
> — Anthropic, *How we built our multi-agent research system* (2025)

Everything else this week had a fixed shape. Research does not: the second search depends on what the first one returned.

<!--
Slide ID: D4-M17-C0
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 08 Quote
Speaker notes:
- Say: Deep research is the agent application that broke out first, and this is the property that makes it hard. A RAG pipeline has one shape every time: retrieve, rank, answer. Research has no fixed path, because each finding changes what is worth looking for next.
- Ask: Where have you already hit this — a question that changed once you saw the first answer?
- Watch: Hold the room on the second quote. Path-dependent is the engineering word: the sequence of steps is itself an output, not something you can write down in advance. Notebook:cell#9 is Task 1 of 6 — the question and the contracts; it is where the unpredictable path gets pinned down to typed handoffs. In the notebook: each stage passes a typed object to the next, so the workflow is a relay, not a long conversation.
- Then: If the path cannot be fixed in advance, the boundaries between steps are all you can hold to a contract. That is what the next slide unrolls.
Sources: [Anthropic multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), [LangChain Open Deep Research](https://www.langchain.com/blog/open-deep-research)
-->

---

# Make research inspectable

<style scoped>
@media (prefers-reduced-motion: reduce) { .d4-mover { display: none; } }
</style>

<div style="display:flex;justify-content:center;margin-top:.2em">
<svg viewBox="0 0 860 250" width="1040" role="img" aria-label="A six-node state graph from START to END: clarify, brief, plan, research, compress, write. Under each node the typed object it writes; under plan and research the budget that caps them; a trace bar along the bottom with one event per node">
<defs><marker id="d4c1" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#38bdf8"/></marker></defs>
<circle cx="22" cy="100" r="8" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
<text x="22" y="82" font-size="12" fill="#94a3b8" text-anchor="middle">START</text>
<circle cx="838" cy="100" r="8" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
<text x="838" y="82" font-size="12" fill="#94a3b8" text-anchor="middle">END</text>
<g stroke="#38bdf8" stroke-width="2.5" marker-end="url(#d4c1)">
<path d="M30 100 H46"/><path d="M160 100 H176"/><path d="M290 100 H306"/><path d="M420 100 H436"/><path d="M550 100 H566"/><path d="M680 100 H696"/><path d="M810 100 H828"/>
</g>
<g font-size="15" font-weight="700" fill="#7dd3fc" text-anchor="middle">
<rect x="48" y="78" width="112" height="44" rx="9" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/><text x="104" y="105">clarify</text>
<rect x="178" y="78" width="112" height="44" rx="9" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/><text x="234" y="105">brief</text>
<rect x="308" y="78" width="112" height="44" rx="9" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/><text x="364" y="105">plan</text>
<rect x="438" y="78" width="112" height="44" rx="9" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/><text x="494" y="105">research</text>
<rect x="568" y="78" width="112" height="44" rx="9" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/><text x="624" y="105">compress</text>
<rect x="698" y="78" width="112" height="44" rx="9" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/><text x="754" y="105">write</text>
</g>
<text x="430" y="30" font-size="14" fill="#94a3b8" text-anchor="middle">a path you cannot predict: under each node, the typed object it writes and the cap it runs under</text>
<g font-size="12" font-weight="700" fill="#fcd34d" text-anchor="middle">
<text x="104" y="150">ClarificationDecision</text><text x="234" y="168">ResearchBrief</text><text x="364" y="150">ResearchPlan</text><text x="494" y="168">list[ResearchFinding]</text><text x="624" y="150">CompressedDossier</text><text x="754" y="168">FinalReport</text>
</g>
<g font-size="12" fill="#c4b5fd" text-anchor="middle">
<text x="364" y="192">tasks ≤ 6</text><text x="494" y="192">loops per task ≤ 3 · workers ≤ 3</text>
</g>
<rect x="48" y="210" width="762" height="28" rx="6" fill="#3a2a0a" stroke="#fbbf24" stroke-width="1.5"/>
<text x="429" y="229" font-size="13" fill="#fcd34d" text-anchor="middle">trace_events: one event per node, so the trace shows where evidence and uncertainty entered</text>
<circle class="d4-mover" cx="22" cy="100" r="6" fill="#fcd34d"><animateMotion dur="6s" repeatCount="indefinite" path="M0 0 H816" calcMode="linear"/></circle>
</svg>
</div>

A question becomes a brief, plan, findings, dossier, and report. When the final answer fails, the first broken contract is where to look.

> Source: [LangGraph graph API](https://docs.langchain.com/oss/python/langgraph/graph-api)

<!--
Slide ID: D4-M17-C1
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: When the final answer fails, a visible handoff lets us locate the first broken contract.
- Ask: Which boundary would you inspect first when the final answer is wrong?
- Watch: Notebook:cell#9 — Task 1 defines the question and typed contracts that make each handoff inspectable. In the notebook: A trace earns trust only when it preserves the query, hits, and gaps needed to challenge the result.
- Then: Compare the contract boundaries with the trace on the next slide.
Sources: [LangGraph graph API](https://docs.langchain.com/oss/python/langgraph/graph-api), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->
---
# The contract is the handoff

```python
class ResearchBrief(BaseModel):
    question: str
    audience: str
    deliverable: str
    success_criteria: list[str]
    constraints: list[str]

class ResearchConfig(BaseModel):
    max_research_tasks:    int = Field(default=budget(3, 2), ge=1, le=6)
    max_researcher_loops:  int = Field(default=1, ge=1, le=3)
```

A path you cannot predict still has boundaries you can **type** — and ceilings you can **cap**.

<!--
Slide ID: D4-M17-C1A
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 3
Layout: 04 Lab and code
Speaker notes:
- Say: This is the answer to the problem we opened with. You cannot hardcode the path, but you can say exactly what has to be true at each handoff. A brief is not prose — it is five fields, and a stage that cannot fill them has failed early and visibly instead of producing a vague report later.
- Ask: Which of those five fields would you refuse to make optional?
- Watch: Notebook:cell#10 — Task 1 defines the contracts and the budgets together. Point at the ge and le bounds: every loop in an unpredictable process has a ceiling, and le=6 on research tasks is what stops a plan from fanning out forever.
- Then: Note that the budgets sit in the same object as the contracts, on purpose — the shape of the handoff and the cost of the step are one decision.
Sources: [LangGraph graph API](https://docs.langchain.com/oss/python/langgraph/graph-api), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---

# Research is a bounded loop

`plan → parallel research → search → extract → reflect → compress`

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 860 236" width="1000" role="img" aria-label="Left: one researcher's loop of search, extract, reflect, which either loops back with a follow-up query or hands over a finding. Right: four budget gauges from the seed run: research tasks 2 of a cap of 6, loops per task 1 of a cap of 3, corpus hits 6 of 6, web hits 0 because web search was off">
<defs><marker id="d4c2s" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#94a3b8"/></marker><marker id="d4c2a" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#fbbf24"/></marker><marker id="d4c2g" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#4ade80"/></marker></defs>
<text x="20" y="20" font-size="14" fill="#94a3b8">one researcher, one task: corpus first, web only if a key is set</text>
<g font-size="14" font-weight="700" text-anchor="middle">
<rect x="20" y="40" width="100" height="38" rx="8" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/><text x="70" y="64" fill="#7dd3fc">search</text>
<rect x="260" y="40" width="100" height="38" rx="8" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/><text x="310" y="64" fill="#7dd3fc">extract</text>
<rect x="140" y="112" width="100" height="38" rx="8" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2.5"/><text x="190" y="136" fill="#c4b5fd">reflect</text>
<rect x="120" y="190" width="140" height="36" rx="8" fill="#0f3320" stroke="#4ade80" stroke-width="2.5"/><text x="190" y="213" fill="#86efac">finding + gaps</text>
</g>
<path d="M122 59 H256" stroke="#94a3b8" stroke-width="2" marker-end="url(#d4c2s)"/>
<path d="M300 80 L232 112" stroke="#94a3b8" stroke-width="2" marker-end="url(#d4c2s)"/>
<path d="M148 112 L80 80" stroke="#fbbf24" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#d4c2a)"/>
<text x="20" y="134" font-size="12" fill="#fcd34d">follow-up query,</text>
<text x="20" y="148" font-size="12" fill="#fcd34d">while loops remain</text>
<path d="M190 152 V186" stroke="#4ade80" stroke-width="2.5" marker-end="url(#d4c2g)"/>
<text x="204" y="174" font-size="12" fill="#86efac">no follow-up, or budget spent</text>
<text x="620" y="20" font-size="14" fill="#94a3b8" text-anchor="middle">the seed run against its ceilings</text>
<g font-size="12" fill="#cbd5e1">
<text x="420" y="52">research tasks</text><rect x="540" y="40" width="280" height="16" rx="4" fill="#1e293b" stroke="#475569"/><rect x="540" y="40" width="93" height="16" rx="4" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/><text x="828" y="52" fill="#f1f5f9">2</text><text x="633" y="70" fill="#a78bfa" text-anchor="middle">budget 2</text><text x="820" y="70" fill="#94a3b8" text-anchor="end">cap 6</text>
<text x="420" y="100">loops per task</text><rect x="540" y="88" width="280" height="16" rx="4" fill="#1e293b" stroke="#475569"/><rect x="540" y="88" width="93" height="16" rx="4" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/><text x="828" y="100" fill="#f1f5f9">1</text><text x="633" y="118" fill="#a78bfa" text-anchor="middle">budget 1</text><text x="820" y="118" fill="#94a3b8" text-anchor="end">cap 3</text>
<text x="420" y="148">corpus hits</text><rect x="540" y="136" width="280" height="16" rx="4" fill="#1e293b" stroke="#475569"/><rect x="540" y="136" width="280" height="16" rx="4" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2"/><text x="828" y="148" fill="#f1f5f9">6</text><text x="820" y="166" fill="#94a3b8" text-anchor="end">3 per search, 2 searches</text>
<text x="420" y="196">web hits</text><rect x="540" y="184" width="280" height="16" rx="4" fill="none" stroke="#475569" stroke-dasharray="4 3"/><text x="828" y="196" fill="#f1f5f9">0</text><text x="820" y="214" fill="#94a3b8" text-anchor="end">web search off, no key</text>
</g>
<g stroke="#a78bfa" stroke-width="2"><path d="M633 36 V60"/><path d="M633 84 V108"/></g>
</svg>
</div>

<div style="font-size:.78em">Search the corpus first; web search is optional. Parallel tasks cut wall-clock time and add coordination cost. Stop when the budget is spent or the evidence is empty — and an empty result set reaches the report as a gap, not as silence.</div>

<!--
Slide ID: D4-M17-C2
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes:
- Say: A research run needs a stopping rule, or empty searches turn into confident-looking silence.
- Ask: What should the report say when every search path returns zero hits?
- Watch: Notebook:cell#19 — Task 4 runs research and compression while preserving source observations and gaps. In the notebook: Zero hits are a result the report must expose, because silence can be mistaken for support.
- Then: Surface the empty-source case on the next slide and make the gap explicit.
Sources: [LangGraph workflows](https://docs.langchain.com/oss/python/langgraph/workflows-agents), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---

# What happens when a citation is hallucinated?

The report cites a source. The source is real. The claim beside it is not in that source.

**Nothing in the pipeline has failed yet — and the report looks better than an honest one.**

<!--
Slide ID: D4-M17-C3
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 4
Layout: 08 Quote
Speaker notes:
- Say: This is the failure that survives every check we have built so far. A retrieval eval scores whether the right document came back, and it did. A judge scores whether the answer reads well, and it does. The citation is present and the link resolves. The only broken thing is the join between the claim and the source, and that is the one thing none of our measurements looked at.
- Ask: Open the floor and let them work it — take three or four answers before showing the next slide. Push for a mechanism, not a principle: who or what checks the join, and when does it run?
- Watch: Answers usually arrive in this order — have a human review it (does not scale, and reviewers skim), ask the model to check its own citations (same model, same blind spot), then someone lands on re-retrieving the cited span and testing entailment against the claim, which is Anthropic's CitationAgent pattern and what the notebook's trace makes possible. If the room stalls, ask what they would need to have kept in order to check it later. Notebook:cell#27 is Task 6 of 6 — inspect the trace and save the report; it saves sources, open gaps, and the trace summary together, which is the record any of their answers depends on.
- Then: Note which of their answers are guardrails and which are measurements — this is the same split from yesterday's ladder. Then show what the trace has to carry for any of it to be checkable.
Sources: [Anthropic multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---

# Provenance is part of the answer

<div style="display:flex;justify-content:center;margin-top:.2em">
<svg viewBox="0 0 860 250" width="1000" role="img" aria-label="Left: the seed research report with each finding carrying an inline source citation, an open gaps section with three gaps, and a trace line. Right: the source ledger of the four corpus pages the researchers observed, each citation joined to its ledger row, and a dashed red row for any citation that is not in the ledger">
<rect x="10" y="10" width="470" height="212" rx="10" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
<text x="26" y="34" font-size="15" font-weight="700" fill="#cbd5e1">research_report.md</text>
<text x="400" y="34" font-size="12" fill="#94a3b8">the product</text>
<g font-size="13" fill="#f1f5f9">
<text x="26" y="58">Accuracy ≥ 95%: cannot be assessed</text>
<text x="26" y="86">Traceability: JSON contract, reason given</text>
<text x="26" y="114">Scope: inferred from prompt examples</text>
<text x="26" y="142">Empirical void: no eval data anywhere</text>
<text x="26" y="170">Open gaps (3): void · scope · regression, kept through compression</text>
</g>
<g font-size="12" font-weight="700" fill="#fcd34d">
<rect x="358" y="46" width="112" height="16" rx="4" fill="#3a2a0a" stroke="#fbbf24"/><text x="414" y="58" text-anchor="middle">[few-shot-zero.md]</text>
<rect x="296" y="74" width="174" height="16" rx="4" fill="#3a2a0a" stroke="#fbbf24"/><text x="383" y="86" text-anchor="middle">[few-shot-two-examples.md]</text>
<rect x="404" y="102" width="66" height="16" rx="4" fill="#3a2a0a" stroke="#fbbf24"/><text x="437" y="114" text-anchor="middle">[kb/vpn.md]</text>
<rect x="292" y="130" width="178" height="16" rx="4" fill="#3a2a0a" stroke="#fbbf24"/><text x="381" y="142" text-anchor="middle">[meta-prompt-generate.md]</text>
</g>
<path d="M26 186 H464" stroke="#475569" stroke-width="1"/>
<text x="26" y="208" font-size="12" fill="#94a3b8">Trace: 2 tasks · 2 searches · 6 corpus hits · 0 web · 4 extracted · 4 distinct</text>
<rect x="540" y="10" width="310" height="212" rx="10" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/>
<text x="556" y="34" font-size="15" font-weight="700" fill="#fcd34d">source ledger</text>
<text x="834" y="34" font-size="12" fill="#fbbf24" text-anchor="end">what a researcher observed</text>
<g font-size="12" fill="#f1f5f9">
<text x="556" y="58">prompts/few-shot-zero.md</text><text x="834" y="58" fill="#86efac" text-anchor="end">observed</text>
<text x="556" y="86">prompts/few-shot-two-examples.md</text><text x="834" y="86" fill="#86efac" text-anchor="end">observed</text>
<text x="556" y="114">kb/vpn.md</text><text x="834" y="114" fill="#86efac" text-anchor="end">observed</text>
<text x="556" y="142">prompts/meta-prompt-generate.md</text><text x="834" y="142" fill="#86efac" text-anchor="end">observed</text>
</g>
<rect x="552" y="162" width="286" height="44" rx="6" fill="none" stroke="#f87171" stroke-width="1.5" stroke-dasharray="5 4"/>
<text x="695" y="181" font-size="12" fill="#fca5a5" text-anchor="middle">a citation not on this ledger is invented:</text>
<text x="695" y="197" font-size="12" fill="#fca5a5" text-anchor="middle">the writer may cite only what was observed</text>
<g stroke="#fbbf24" stroke-width="1.5" fill="none">
<path d="M470 54 H540"/><path d="M470 82 H540"/><path d="M470 110 H540"/><path d="M470 138 H540"/>
</g>
<text x="430" y="244" font-size="13" fill="#94a3b8" text-anchor="middle">Source paths sit beside the findings, the three gaps survived compression, and the trace says how much research stands behind the report.</text>
</svg>
</div>

Citation presence is not proof that a claim is supported. A report is usable when a reader can retrace it.

<!--
Slide ID: D4-M17-C3A
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 05 Two column
Speaker notes:
- Say: Every answer the room gave needs the same precondition — the source path has to still be sitting beside the finding when you go back to check it. That is why compression drops volume but never drops the gaps.
- Watch: Notebook:cell#27 — Task 6 inspects the trace and saves sources, open gaps, and the report together. In the notebook: A citation is only useful when the retrieved source actually supports the claim it sits beside.
- Then: Third bullet is the answer to what we just brainstormed; say it plainly and move on.
Sources: [LangGraph workflows](https://docs.langchain.com/oss/python/langgraph/workflows-agents), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---

# The next step is evidence policy

- A working prototype has typed boundaries and a readable trace.
- Production also needs source trust, permissions, recovery, and evals.
- A bounded research graph is not automatically production-ready.
- Stop at corpus-only research when web access is not justified.

<!--
Slide ID: D4-M17-C4
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 05 Two column 1
Speaker notes:
- Say: Web search expands reach and risk, so its permission belongs in the design before the key is present.
- Ask: What permission would you require before enabling web search?
- Watch: Notebook:cell#12 — Task 2 separates corpus search from optional web tools and makes the web path explicit. In the notebook: Decide what evidence the agent may consult before enabling a tool that can broaden the claim surface.
- Then: Carry the chosen web permission into the policy decision on the next slide.
Sources: [LangGraph durable execution](https://docs.langchain.com/oss/python/langgraph/durable-execution), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---

# Compile while the graph runs

<div style="display:flex;gap:1.2em;align-items:stretch;margin-top:.2em">
<div style="flex:1.45;background:#0b2b40;border-left:6px solid #38bdf8;border-radius:10px;padding:.6em .9em;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.62em;line-height:1.55;color:#f1f5f9;white-space:pre">graph.stream(state, stream_mode="updates")

<span style="color:#7dd3fc">[clarify]</span>  updated <span style="color:#fcd34d">['clarification', 'trace_events']</span>
<span style="color:#7dd3fc">[brief]</span>    updated <span style="color:#fcd34d">['brief', 'trace_events']</span>
<span style="color:#7dd3fc">[plan]</span>     updated <span style="color:#fcd34d">['tasks', 'trace_events']</span>
<span style="color:#7dd3fc">[research]</span> updated <span style="color:#fcd34d">['findings', 'trace_events']</span>
  <span style="color:#94a3b8">‹task 1›: query='…' corpus=3 web=0</span>
  <span style="color:#94a3b8">‹task 2›: query='…' corpus=3 web=0</span>
<span style="color:#7dd3fc">[compress]</span> updated <span style="color:#fcd34d">['dossier', 'trace_events']</span>
<span style="color:#7dd3fc">[write]</span>    updated <span style="color:#fcd34d">['final_report', 'trace_events']</span></div>
<div style="flex:1;display:flex;flex-direction:column;gap:.5em;font-size:.66em">
<div style="background:#1e293b;border-radius:8px;padding:.5em .8em"><b style="color:#7dd3fc">[node]</b><br>the node that just finished, in lifecycle order</div>
<div style="background:#1e293b;border-radius:8px;padding:.5em .8em"><b style="color:#fcd34d">updated [...]</b><br>the state keys it wrote; every node appends to the trace</div>
<div style="background:#1e293b;border-radius:8px;padding:.5em .8em"><b style="color:#cbd5e1">query lines</b><br>one per research task: where the budget went. Seed run: two tasks, three corpus hits each, web off</div>
<div style="color:#94a3b8;padding:.2em .8em">Query text elided here; the notebook prints it.</div>
</div>
</div>

<div style="font-size:.8em">The writer gets the brief and dossier, not the whole conversation. Keep the trace that shows which source was stale.</div>

<!--
Slide ID: D4-M17-C5
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes:
- Say: Compilation is an observable handoff, not a hidden final model call.
- Ask: Which streamed update would tell you that the research question is drifting?
- Watch: Notebook:cell#24 — Task 5 compiles and streams the graph. The concrete case in their own environment is a stale-policy question — did the VPN policy change, and when — where the trace is what shows which knowledge-base page was out of date. In the notebook: The report is the product; the trace is how you debug cost, latency, and source quality.
- Then: Let the stream finish, then inspect the saved report and its evidence.
Sources: [LangGraph graph API](https://docs.langchain.com/oss/python/langgraph/graph-api), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---
# 18 · Off-the-shelf guardrails

**Do you build the controls, or buy them?** · 30 min

- Someone has already written the PII redactor. What you still own is the policy.

<!--
Slide ID: D4-T18
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: transition
Minutes: 0
Layout: 01 Title
Speaker notes:
- Say: Someone has already written the PII redactor. What you still own is the policy. That is what this module is for.
- Ask: Hold for a beat — this is the hand-off, not content.
- Watch: Name the module and who is running it, then move. One breath.
- Then: Straight into the first content slide.
Sources: [Module 18 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md).
-->
---

# Stop rebuilding the plumbing

You already built the ladder and wrote the cases. Today you attach **someone else's** policies and run your own cases through them.

| Yesterday | Today |
|---|---|
| you wrote each rung | the SDK owns the wiring |
| you called the checks | the runner decides when they run |
| a block was your `if` | a **tripwire** raises a typed exception |

Two things the ladder did not have: a **transform**, which rewrites a request and lets it through, and a library's opinion about where checks belong.

<!--
Slide ID: D4-M18-C1
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 05 Two column
Speaker notes:
- Say: Guardrails are not new today — you built the five rungs yesterday and measured them. What is new is that you stop writing the plumbing. The notebook's own first line: you wrote guardrail cases against your own agent, and this notebook stops rebuilding the plumbing and attaches five policies through the SDK instead.
- Ask: What do you give up when the library owns the wiring?
- Watch: Notebook:cell#24 — Task 5 wires the guarded agent lifecycle: raw prompt, redaction, input guardrails, agent and tool, output guardrails, then an answer or a tripwire. Every stage returns a record, so a case is never a silent failure.
- Then: Redaction is the genuinely new idea — a check that neither allows nor blocks. Hold it for the transform slide rather than explaining it here.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# Placement changes the failure

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 720 200" width="900" role="img" aria-label="Three guardrail placements around the agent loop: before generation on the input, at the tool boundary, and after generation on the output">
<rect x="236" y="62" width="150" height="66" rx="9" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2.5"/>
<text x="311" y="89" font-size="15" font-weight="700" text-anchor="middle" fill="#c4b5fd">the loop</text>
<text x="311" y="110" font-size="12" text-anchor="middle" fill="#a78bfa">model + your code</text>

<rect x="14" y="62" width="150" height="66" rx="9" fill="#3f1212" stroke="#f87171" stroke-width="2.5"/>
<text x="89" y="84" font-size="13.5" font-weight="700" text-anchor="middle" fill="#fecaca">before generation</text>
<text x="89" y="103" font-size="11.5" text-anchor="middle" fill="#fca5a5">scope · injection</text>
<text x="89" y="119" font-size="11" text-anchor="middle" fill="#fca5a5">blocks: nothing runs</text>

<rect x="458" y="62" width="150" height="66" rx="9" fill="#3f1212" stroke="#f87171" stroke-width="2.5"/>
<text x="533" y="84" font-size="13.5" font-weight="700" text-anchor="middle" fill="#fecaca">after generation</text>
<text x="533" y="103" font-size="11.5" text-anchor="middle" fill="#fca5a5">unsupported claims</text>
<text x="533" y="119" font-size="11" text-anchor="middle" fill="#fca5a5">blocks: output withheld</text>

<rect x="236" y="158" width="150" height="38" rx="9" fill="#3a2a0a" stroke="#fbbf24" stroke-width="3"/>
<text x="311" y="175" font-size="13.5" font-weight="700" text-anchor="middle" fill="#fcd34d">tool boundary</text>
<text x="311" y="190" font-size="11" text-anchor="middle" fill="#fbbf24">authorization · side effects</text>

<path d="M166 95 H232" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#p1)"/>
<path d="M388 95 H454" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#p1)"/>
<path d="M311 130 V154" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#p2)"/>
<text x="656" y="99" font-size="12" text-anchor="middle" fill="#cbd5e1" font-style="italic">answer</text>
<defs>
<marker id="p1" markerWidth="10" markerHeight="10" refX="8.5" refY="3" orient="auto"><path d="M0 0 L8.5 3 L0 6 z" fill="#94a3b8"/></marker>
<marker id="p2" markerWidth="10" markerHeight="10" refX="8.5" refY="3" orient="auto"><path d="M0 0 L8.5 3 L0 6 z" fill="#fbbf24"/></marker>
</defs>
</svg>
</div>

No placement can undo a side effect that already happened.

> Source: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/)

<!--
Slide ID: D4-M18-C2
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes:
- Say: The same policy catches different failures depending on whether it runs before generation, at the tool, or after output.
- Ask: Which boundary should enforce requester authorization, and why?
- Watch: Notebook:cell#24 — Task 5 wires input, tool, and output stages into one guarded lifecycle. In the notebook: Authorization belongs at the action boundary because an output block cannot undo a side effect.
- Then: Use the placement choice to frame the boundary comparison on the next slide.
Sources: [OpenAI guardrail execution modes](https://openai.github.io/openai-agents-python/guardrails/#execution-modes), [Tool guardrails](https://openai.github.io/openai-agents-python/ref/tool_guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---
# A "cheap rule" is a named pattern

```python
INJECTION = {
    "ignore instructions": r"ignore\s+(your\s+|all\s+)?(previous|prior|all|above)\s+instructions",
    "prompt extraction": r"(tell|show|give)\s+me\s+your\s+(system\s+)?prompt|...",
    "role override":     r"pretend\s+(you\s+are|to\s+be)|you\s+are\s+now\s+(a|an)\b|...",
    "constraint bypass": r"no\s+(rules|restrictions|guardrails)|jailbreak|developer\s+mode",
}
```

The key is the name. A block reports **which** pattern fired — so the log says `role override`, not `blocked`.

<!--
Slide ID: D4-M18-C3A
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 3
Layout: 04 Lab and code
Speaker notes:
- Say: Worth seeing what a rule rung actually is, because it is less impressive and more useful than people expect — a dict of named regexes. The naming is the engineering decision. Yesterday we said a block nobody can explain gets switched off by the first person it inconveniences; this is how you avoid that, by making the reason a value the code carries rather than a comment.
- Ask: Which of these four would a determined attacker get past first?
- Watch: Notebook:cell#13 — Task 2 writes each policy as a plain function that returns whether it tripped and why, then wraps it for the SDK. The scope check pairs with this one: a request has to share vocabulary with the corpus and match no off-topic pattern.
- Then: Every one of these is paraphraseable, which is the brittleness the previous slide claimed. That is the argument for measuring false negatives on their own case set rather than trusting the list.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# The system still owns authorization

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 860 250" width="1000" role="img" aria-label="Heatmap of six guardrail cases against five guardrails from the seed run: four legitimate cases pass every check, attack g05 trips prompt injection, attack g06 trips scope, and the output checks are not reached for either attack. A sixth dashed column labelled who asked is empty for every case">
<g font-size="12" fill="#cbd5e1" text-anchor="middle">
<text x="185" y="42">scope</text><text x="255" y="42">injection</text><text x="325" y="42">pii</text><text x="395" y="42">claims</text><text x="465" y="42">tone</text>
</g>
<text x="545" y="42" font-size="12" font-weight="700" fill="#c4b5fd" text-anchor="middle">who asked?</text>
<g font-size="12" fill="#cbd5e1">
<text x="60" y="68">g01</text><text x="60" y="96">g02</text><text x="60" y="124">g03</text><text x="60" y="152">g04</text><text x="60" y="180" fill="#fca5a5">g05</text><text x="60" y="208" fill="#fca5a5">g06</text>
</g>
<g font-size="12" fill="#94a3b8"><text x="95" y="68">legit</text><text x="95" y="96">legit</text><text x="95" y="124">legit</text><text x="95" y="152">legit</text><text x="95" y="180" fill="#fca5a5">attack</text><text x="95" y="208" fill="#fca5a5">attack</text></g>
<g fill="#0f3320" stroke="#4ade80" stroke-width="1">
<rect x="152" y="52" width="66" height="24" rx="3"/><rect x="222" y="52" width="66" height="24" rx="3"/><rect x="292" y="52" width="66" height="24" rx="3"/><rect x="362" y="52" width="66" height="24" rx="3"/><rect x="432" y="52" width="66" height="24" rx="3"/>
<rect x="152" y="80" width="66" height="24" rx="3"/><rect x="222" y="80" width="66" height="24" rx="3"/><rect x="292" y="80" width="66" height="24" rx="3"/><rect x="362" y="80" width="66" height="24" rx="3"/><rect x="432" y="80" width="66" height="24" rx="3"/>
<rect x="152" y="108" width="66" height="24" rx="3"/><rect x="222" y="108" width="66" height="24" rx="3"/><rect x="292" y="108" width="66" height="24" rx="3"/><rect x="362" y="108" width="66" height="24" rx="3"/><rect x="432" y="108" width="66" height="24" rx="3"/>
<rect x="152" y="136" width="66" height="24" rx="3"/><rect x="222" y="136" width="66" height="24" rx="3"/><rect x="292" y="136" width="66" height="24" rx="3"/><rect x="362" y="136" width="66" height="24" rx="3"/><rect x="432" y="136" width="66" height="24" rx="3"/>
<rect x="152" y="164" width="66" height="24" rx="3"/><rect x="292" y="164" width="66" height="24" rx="3"/>
<rect x="222" y="192" width="66" height="24" rx="3"/><rect x="292" y="192" width="66" height="24" rx="3"/>
</g>
<g fill="#3f1212" stroke="#f87171" stroke-width="2.5"><rect x="222" y="164" width="66" height="24" rx="3"/><rect x="152" y="192" width="66" height="24" rx="3"/></g>
<g font-size="12" font-weight="700" fill="#fca5a5" text-anchor="middle"><text x="255" y="180">tripwire</text><text x="185" y="208">tripwire</text></g>
<g fill="#1e293b" stroke="#475569" stroke-width="1" stroke-dasharray="3 3"><rect x="362" y="164" width="66" height="24" rx="3"/><rect x="432" y="164" width="66" height="24" rx="3"/><rect x="362" y="192" width="66" height="24" rx="3"/><rect x="432" y="192" width="66" height="24" rx="3"/></g>
<g font-size="12" fill="#94a3b8" text-anchor="middle"><text x="395" y="180">not run</text><text x="465" y="180">not run</text><text x="395" y="208">not run</text><text x="465" y="208">not run</text></g>
<g fill="none" stroke="#a78bfa" stroke-width="1.5" stroke-dasharray="4 3"><rect x="512" y="52" width="66" height="24" rx="3"/><rect x="512" y="80" width="66" height="24" rx="3"/><rect x="512" y="108" width="66" height="24" rx="3"/><rect x="512" y="136" width="66" height="24" rx="3"/><rect x="512" y="164" width="66" height="24" rx="3"/><rect x="512" y="192" width="66" height="24" rx="3"/></g>
<g font-size="12" fill="#c4b5fd" text-anchor="middle"><text x="545" y="68">?</text><text x="545" y="96">?</text><text x="545" y="124">?</text><text x="545" y="152">?</text><text x="545" y="180">?</text><text x="545" y="208">?</text></g>
<g font-size="12" fill="#94a3b8"><rect x="152" y="230" width="12" height="12" rx="2" fill="#0f3320" stroke="#4ade80"/><text x="170" y="240">passed</text><rect x="232" y="230" width="12" height="12" rx="2" fill="#3f1212" stroke="#f87171"/><text x="250" y="240">tripped</text><rect x="316" y="230" width="12" height="12" rx="2" fill="#1e293b" stroke="#475569" stroke-dasharray="3 3"/><text x="334" y="240">blocked at input, never ran</text></g>
<text x="610" y="240" font-size="12" fill="#c4b5fd">no guardrail answers the dashed column</text>
<g font-size="13" fill="#f1f5f9">
<text x="610" y="64">A prompt can describe policy;</text><text x="610" y="82">it cannot enforce permission.</text>
<text x="610" y="110">Results need severity, owner,</text><text x="610" y="128">and audit context.</text>
<text x="610" y="156">Test refusal, escalation, and safe</text><text x="610" y="174">completion, not only blocking.</text>
<text x="610" y="202">Test legitimate requests and</text><text x="610" y="220">attacks together.</text>
</g>
<text x="430" y="22" font-size="13" fill="#94a3b8" text-anchor="middle">Seed run: six cases through five guardrails. Legitimate requests untouched; each attack caught by a different check.</text>
</svg>
</div>

Every one of these lives in **middleware** — between the model and the systems that can act. Who asked, and whether they may, is decided there.

<!--
Slide ID: D4-M18-C4
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 3
Layout: 05 Two column 3
Speaker notes:
- Say: The model asks. Only your system can verify identity and permit the side effect. This is the middleware plug — severity, owner, audit context, and the authorization decision all belong in a layer you own, not in the prompt and not in the library's guardrail function. The SDK gives you the tripwire; it does not know who Priya is or whether she may reset that account.
- Ask: What must be true before a password-reset tool can execute?
- Watch: Notebook:cell#24 — Task 5 places the agent and tool inside the guarded lifecycle, separating execution from model output. In the notebook: A model can request a password reset, but only the system can verify identity and authorize the side effect.
- Then: Note the last two bullets are test design, not enforcement: a suite that only tries attacks cannot tell you what you broke for legitimate users. Same protection-and-friction pair from yesterday's ladder measurements.
- Then: Optional, two open-source middleware layers to name if someone asks what this looks like in code. Agentware (https://github.com/HaikeiLabs/Agentware) is the closer match to these bullets: policy enforcement and audit middleware for agent tool calls, in Go, Python, and TypeScript. Its framing is exactly the owner-and-audit problem — attribution dies at the first delegation hop — so it writes one append-only record per tool call carrying the invoking human subject and the delegation chain. That is the through-line to yesterday's multi-agent module: once a supervisor delegates, the audit row is the only thing that still knows who actually asked. Forge (https://github.com/antoinezambelli/forge) sits at a different layer — a reliability layer for self-hosted LLM tool-calling, with schema validation, rescue parsing for malformed tool calls, retries, and a composable guardrails-middleware mode; it runs as a proxy in front of an OpenAI-compatible endpoint, the same swap-your-provider property this course is built on. A Rust port of it exists at whit3rabbit/forge-guardrails.
Sources: [OpenAI Agents SDK tools](https://openai.github.io/openai-agents-python/tools/), [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# Redaction transforms input before generation

A third option, next to allow and block: **let it through, changed.**

```python
def redact_pii(raw: str) -> Redaction:
    text, found = raw, []
    for label, pat in PII.items():
        if re.search(pat, text):
            found.append(label)
            text = re.sub(pat, f"[{label.upper()}_REDACTED]", text)
    return Redaction(text, found)
```

`found` holds the **kinds** removed — `["email", "phone"]` — never the values.

<!--
Slide ID: D4-M18-C5
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 3
Layout: 04 Lab and code
Speaker notes:
- Say: This is the one genuinely new mechanism in the module. Every control so far was a verdict — allow or block. A transform keeps a legitimate question alive while changing what the model receives, and the user never gets refused for including their own email address.
- Ask: What evidence would prove the identifier was removed without exposing it?
- Watch: Notebook:cell#17 — Task 3 distinguishes redaction from blocking. Point at the return: the Redaction dataclass carries the rewritten text and the list of labels, so the record proves redaction happened without storing the secret. That answers the Ask. In the notebook: this pre-pass is boring and fast on purpose.
- Then: Say clearly that redaction is not an authorization decision and should not be taught as one. In their own environment this is what stops one user's ticket text reaching another user's answer — worth naming as the concrete case, since they will hit it in the notebook.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# Optional: a research loop is a state graph you can resume

- Anthropic’s case delegates breadth-first research to parallel subagents.
- Compare its contribution, cost, and fit with this notebook’s graph.

<!--
Slide ID: D4-M17-R1
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes:
- Say: For a deeper comparison, examine how another research system divides state and parallel work.
- Ask: Which state boundary should stop when sources are empty?
- Watch: Notebook cue: compare the six node updates with the research trace and open gaps.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [Anthropic multi-agent research case study](https://www.anthropic.com/engineering/multi-agent-research-system), [LangGraph graph API](https://docs.langchain.com/oss/python/langgraph/graph-api), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---

# Optional: the tool boundary is the last place to say no

- Agent checks and tool checks protect different boundaries.
- Choose reject, warn, or halt deliberately.
- Test the side effect, not only the wording.

<!--
Slide ID: D4-M18-R1
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes:
- Say: For a deeper comparison, examine the tool boundary where a blocked answer is not enough to protect a side effect.
- Ask: What tool-call condition should halt execution rather than merely warn?
- Watch: Alignment pending for this extension; the notebook’s confirmed cue is stage-specific tripwire handling.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [OpenAI tool guardrails](https://openai.github.io/openai-agents-python/ref/tool_guardrails/), [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# What you can defend on Friday

| Prototype evidence | Production equivalent |
|---|---|
| A trace list in state | Persistent traces with cost per node and a dashboard per run |
| One report saved as markdown | A citation verifier, human review before publish, and versioned reports |
| Regex PII redaction | A DLP or PII service with audit logging and reversible tokens |

What did you choose **not** to ship?

<!--
Slide ID: D4-Z1
Module: Closing, after the selected modules
Instructor: Eli, Beric
Type: closing
Minutes: 2
Layout: 05 Two column 3
Speaker notes:
- Say: These are the boundaries between a working prototype and evidence you can defend.
- Ask: Which unshipped behavior would you want a named owner and regression case for first?
- Watch: Notebook:cell#27 supplies the trace/report row; Notebook:cell#16 supplies the redaction row; both production equivalents are lifted from the notebooks.
- Then: Close on the panel's question: what did you choose not to ship?
Sources: [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->
