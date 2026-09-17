---
marp: true
theme: default
paginate: true
size: 16:9
---

# Today: longer horizons, more sources, more ways to be wrong

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
- Marcus asks: did the VPN policy change, and when?
- Keep the trace that shows which KB page was stale.

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
- Watch: Notebook:cell#24 — Task 5 compiles and streams the graph; connect Marcus's stale-policy question to the trace. In the notebook: The report is the product; the trace is how you debug cost, latency, and source quality.
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
- Then: Optional, if someone asks what a real middleware layer looks like in code — there are open-source guardrail middleware projects that sit between the agent and its tools. LINK UNVERIFIED: the author mentioned a Zambelli/forge guardrail repo; the closest match found was antoinezambelli/forge with a Rust port at whit3rabbit/forge-guardrails, neither confirmed as the intended reference. Confirm the URL before naming it in the room.
Sources: [OpenAI Agents SDK tools](https://openai.github.io/openai-agents-python/tools/), [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# Redaction transforms input before generation

- Redaction removes the secret and keeps the legitimate question.
- Record what kind of PII was removed, never its value.
- Deskmate must not leak one user's ticket text into another user's answer.

<!--
Slide ID: D4-M18-C5
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes:
- Say: A transform can preserve a useful request while changing what reaches the model.
- Ask: What evidence would prove the identifier was removed without exposing it?
- Watch: Notebook:cell#16 — Task 3 distinguishes redaction from blocking and records only detected types. In the notebook: Redaction is not an authorization decision and should not be taught as one.
- Then: Connect the transform to Deskmate's cross-user ticket leakage failure before moving to output checks.
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
