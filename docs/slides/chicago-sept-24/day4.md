---
marp: true
theme: default
paginate: true
size: 16:9
---

# Today: longer horizons, more sources, more ways to be wrong

- 14 Voice agents · 40m
- 15 Prompt optimisation · 35m
- 16 GraphRAG · 40m
- 17 Deep research · 35m
- 18 Off-the-shelf guardrails · 30m
- A six-step loop running unsupervised across many sources has a different failure surface than one you watch.

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
<rect x="10" y="60" width="104" height="50" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.5"/>
<text x="62" y="82" font-size="13" font-weight="700" text-anchor="middle" fill="#5b21b6">planner</text>
<text x="62" y="99" font-size="10.5" text-anchor="middle" fill="#6d28d9">3 angles</text>
<rect x="148" y="22" width="104" height="30" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
<text x="200" y="42" font-size="11.5" text-anchor="middle" fill="#075985">researcher</text>
<rect x="148" y="60" width="104" height="30" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
<text x="200" y="80" font-size="11.5" text-anchor="middle" fill="#075985">researcher</text>
<rect x="148" y="98" width="104" height="30" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
<text x="200" y="118" font-size="11.5" text-anchor="middle" fill="#075985">researcher</text>
<rect x="286" y="60" width="104" height="50" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.5"/>
<text x="338" y="82" font-size="13" font-weight="700" text-anchor="middle" fill="#5b21b6">aggregator</text>
<text x="338" y="99" font-size="10.5" text-anchor="middle" fill="#6d28d9">drafts</text>
<rect x="424" y="60" width="90" height="50" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2.5"/>
<text x="469" y="82" font-size="13" font-weight="700" text-anchor="middle" fill="#7f1d1d">critic</text>
<text x="469" y="99" font-size="10.5" text-anchor="middle" fill="#b91c1c">attacks</text>
<rect x="548" y="60" width="90" height="50" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/>
<text x="593" y="82" font-size="13" font-weight="700" text-anchor="middle" fill="#92400e">judge</text>
<text x="593" y="99" font-size="10.5" text-anchor="middle" fill="#92400e">pass?</text>
<rect x="668" y="68" width="82" height="34" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2.5"/>
<text x="709" y="90" font-size="12.5" font-weight="700" text-anchor="middle" fill="#166534">answer</text>
<path d="M116 85 H144" stroke="#94a3b8" stroke-width="2" marker-end="url(#va)"/>
<path d="M254 75 H282" stroke="#94a3b8" stroke-width="2" marker-end="url(#va)"/>
<path d="M392 85 H420" stroke="#94a3b8" stroke-width="2" marker-end="url(#va)"/>
<path d="M516 85 H544" stroke="#94a3b8" stroke-width="2" marker-end="url(#va)"/>
<path d="M640 85 H664" stroke="#16a34a" stroke-width="2.5" marker-end="url(#vg)"/>
<path d="M593 114 V140 H338 V114" fill="none" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="5 3" marker-end="url(#vr)"/>
<text x="466" y="155" font-size="11.5" text-anchor="middle" fill="#b91c1c" font-style="italic">sent back for a revision · capped rounds</text>
<defs>
<marker id="va" markerWidth="9" markerHeight="9" refX="7.5" refY="3" orient="auto"><path d="M0 0 L7.5 3 L0 6 z" fill="#94a3b8"/></marker>
<marker id="vg" markerWidth="9" markerHeight="9" refX="7.5" refY="3" orient="auto"><path d="M0 0 L7.5 3 L0 6 z" fill="#16a34a"/></marker>
<marker id="vr" markerWidth="9" markerHeight="9" refX="7.5" refY="3" orient="auto"><path d="M0 0 L7.5 3 L0 6 z" fill="#dc2626"/></marker>
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

- A **signature** is the fields in and out, with one instruction
- A **metric** says whether one prediction was good — here, agreement with *your* hand scores
- Score the un-optimised program on held-out examples **first**
- That number is the bar every optimiser has to beat

Without the baseline, "the optimiser helped" is a feeling.

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

- A question becomes a brief, plan, findings, evidence packet, and report.
- Each boundary has a typed contract and a budget.
- The graph makes each handoff inspectable.
- The trace shows where evidence and uncertainty entered.

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

- Search the corpus first; web search is optional.
- Parallel work can reduce wall-clock time while increasing coordination cost.
- Stop when the budget is spent or evidence is empty.

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

- Keep source paths beside findings, not in a hidden log.
- Compress context without deleting gaps.
- Citation presence is not proof that a claim is supported.
- A report is usable when a reader can retrace it.

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

- The writer gets the brief and dossier, not the whole conversation.
- Stream node updates and research queries as they happen.
- Each line names the node that finished and the state it wrote.
- Keep the trace that shows which source was stale.

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
<rect x="236" y="62" width="150" height="66" rx="9" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.5"/>
<text x="311" y="89" font-size="15" font-weight="700" text-anchor="middle" fill="#5b21b6">the loop</text>
<text x="311" y="110" font-size="12" text-anchor="middle" fill="#6d28d9">model + your code</text>

<rect x="14" y="62" width="150" height="66" rx="9" fill="#fee2e2" stroke="#dc2626" stroke-width="2.5"/>
<text x="89" y="84" font-size="13.5" font-weight="700" text-anchor="middle" fill="#7f1d1d">before generation</text>
<text x="89" y="103" font-size="11.5" text-anchor="middle" fill="#b91c1c">scope · injection</text>
<text x="89" y="119" font-size="11" text-anchor="middle" fill="#b91c1c">blocks: nothing runs</text>

<rect x="458" y="62" width="150" height="66" rx="9" fill="#fee2e2" stroke="#dc2626" stroke-width="2.5"/>
<text x="533" y="84" font-size="13.5" font-weight="700" text-anchor="middle" fill="#7f1d1d">after generation</text>
<text x="533" y="103" font-size="11.5" text-anchor="middle" fill="#b91c1c">unsupported claims</text>
<text x="533" y="119" font-size="11" text-anchor="middle" fill="#b91c1c">blocks: output withheld</text>

<rect x="236" y="158" width="150" height="38" rx="9" fill="#fef3c7" stroke="#d97706" stroke-width="3"/>
<text x="311" y="175" font-size="13.5" font-weight="700" text-anchor="middle" fill="#92400e">tool boundary</text>
<text x="311" y="190" font-size="11" text-anchor="middle" fill="#b45309">authorization · side effects</text>

<path d="M166 95 H232" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#p1)"/>
<path d="M388 95 H454" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#p1)"/>
<path d="M311 130 V154" stroke="#d97706" stroke-width="2.5" marker-end="url(#p2)"/>
<text x="656" y="99" font-size="12" text-anchor="middle" fill="#475569" font-style="italic">answer</text>
<defs>
<marker id="p1" markerWidth="10" markerHeight="10" refX="8.5" refY="3" orient="auto"><path d="M0 0 L8.5 3 L0 6 z" fill="#94a3b8"/></marker>
<marker id="p2" markerWidth="10" markerHeight="10" refX="8.5" refY="3" orient="auto"><path d="M0 0 L8.5 3 L0 6 z" fill="#d97706"/></marker>
</defs>
</svg>
</div>

No placement can undo a side effect that already happened.

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

# Cheap rules are useful and brittle

| Mechanism | Strength | Risk |
|---|---|---|
| Regex | Fast and explainable | Misses paraphrases |
| Classifier | Broader language coverage | Threshold and drift |
| LLM judge | Interprets open-ended cases | Cost and calibration |

- False positives decide whether a control survives.
- Test legitimate requests alongside attacks.

<!--
Slide ID: D4-M18-C3
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: Cheap rules catch the obvious cases and quietly miss the rest — so read the uncaught column.
- Ask: Which policy would you make warn-only, and what evidence would change your mind?
- Watch: Notebook:cell#31 — Task 7 runs every case and saves one tripwire result per guardrail row. In the notebook: A control is only as credible as the legitimate requests and attacks it handles without hiding its misses.
- Then: Inspect the uncaught cases on the next slide before choosing warn-only behavior.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
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

- A prompt can describe policy; it cannot enforce permission.
- Guardrail results need severity, owner, and audit context.
- Test refusal, escalation, and safe completion — not only blocking.
- Test legitimate requests and attacks together.

Every one of these lives in **middleware** — between the model and the systems that can act.

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
