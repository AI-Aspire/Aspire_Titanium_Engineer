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

# 17 · Make research inspectable

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

# 17 · Research is a bounded loop

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

# 17 · Provenance is part of the answer

- Keep source paths beside findings, not in a hidden log.
- Compress context without deleting gaps.
- Citation presence is not proof that a claim is supported.
- A report is usable when a reader can retrace it.

<!--
Slide ID: D4-M17-C3
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 05 Two column
Speaker notes:
- Say: A reader should be able to retrace every finding before acting on the report.
- Ask: What does a valid citation prove, and what does it still not prove?
- Watch: Notebook:cell#27 — Task 6 inspects the trace and saves sources, open gaps, and the report together. In the notebook: A citation is only useful when the retrieved source actually supports the claim it sits beside.
- Then: Test the citation-to-source link on the next slide.
Sources: [LangGraph workflows](https://docs.langchain.com/oss/python/langgraph/workflows-agents), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---

# 17 · The next step is evidence policy

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

# 17 · Compile while the graph runs

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

# 18 · A guardrail is a boundary with a policy

- Input guardrails gate the model boundary on the blocking path.
- Transforms change what proceeds; blocks stop a run.
- Tool checks protect execution and side effects, not only text.
- Output guardrails protect what the user receives.
- **Fail closed:** block when the check fires. Fail open warns and continues.

<!--
Slide ID: D4-M18-C1
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: A guardrail without a stated policy is a hope with a log line.
- Ask: Where would you put a check that prevents an unauthorized account change?
- Watch: Notebook:cell#24 — Task 5 wires the guarded agent lifecycle from raw prompt through tripwires and answer. In the notebook: A guardrail is a boundary with a policy
- Then: It then checks scope and prompt injection before the model, and unsupported claims and tone after generation.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# 18 · Placement changes the failure

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

# 18 · Cheap rules are useful and brittle

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

# 18 · The system still owns authorization

- A prompt can describe policy; it cannot enforce permission.
- Guardrail results need severity, owner, and audit context.
- Test refusal, escalation, and safe completion—not only blocking.
- Test legitimate requests and attacks together.

<!--
Slide ID: D4-M18-C4
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 05 Two column 3
Speaker notes:
- Say: The model asks. Only your system can verify identity and permit the side effect.
- Ask: What must be true before a password-reset tool can execute?
- Watch: Notebook:cell#24 — Task 5 places the agent and tool inside the guarded lifecycle, separating execution from model output. In the notebook: A model can request a password reset, but only the system can verify identity and authorize the side effect.
- Then: Carry the authorization distinction into the model-boundary check on the next slide.
Sources: [OpenAI Agents SDK tools](https://openai.github.io/openai-agents-python/tools/), [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# 18 · Redaction transforms input before generation

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

# Optional research · State graphs for research

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

# Optional research · Guardrails at the tool boundary

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
