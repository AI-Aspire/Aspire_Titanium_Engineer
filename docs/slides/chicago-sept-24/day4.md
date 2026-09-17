---
marp: true
theme: default
paginate: true
size: 16:9
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
- Say: Make research inspectable
- Ask: Which boundary would you inspect first when the final answer is wrong?
- Watch: Notebook cue: six node updates in order and trace events with query, corpus hits, web hits, and gaps.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [LangGraph graph API](https://docs.langchain.com/oss/python/langgraph/graph-api), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---

# Trace the query and the hits
- **Ask:** Which boundary would you inspect first when the final answer is wrong?
- **Inspect:** Notebook cue: six node updates in order and trace events with query, corpus hits, web hits, and gaps.
- **Decide:** If the trace does not show the query and the hits, the research is not inspectable.

<!--
Slide ID: D4-M17-C1B
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: Make research inspectable
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Notebook cue: six node updates in order and trace events with query, corpus hits, web hits, and gaps.
- Then: If the trace does not show the query and the hits, the research is not inspectable.
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
- Say: Research is a bounded loop
- Ask: What should the report say when every search path returns zero hits?
- Watch: Notebook cue: empty sources are surfaced as gaps; query lines and hit counts appear under research.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [LangGraph workflows](https://docs.langchain.com/oss/python/langgraph/workflows-agents), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---

# Surface empty sources as gaps
- **Ask:** What should the report say when every search path returns zero hits?
- **Inspect:** Notebook cue: empty sources are surfaced as gaps; query lines and hit counts appear under research.
- **Decide:** Surface empty sources as gaps; silence reads as evidence.

<!--
Slide ID: D4-M17-C2B
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes:
- Say: Research is a bounded loop
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Notebook cue: empty sources are surfaced as gaps; query lines and hit counts appear under research.
- Then: Surface empty sources as gaps; silence reads as evidence.
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
- Say: Provenance is part of the answer
- Ask: What does a valid citation prove, and what does it still not prove?
- Watch: Notebook cue: stop if the report cites a source absent from the distinct-sources list.
- Then: Carry the observation into the next exercise.
Sources: [LangGraph workflows](https://docs.langchain.com/oss/python/langgraph/workflows-agents), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---

# Every citation traces to a source
- **Ask:** What does a valid citation prove, and what does it still not prove?
- **Inspect:** Notebook cue: stop if the report cites a source absent from the distinct-sources list.
- **Decide:** Refuse a citation you cannot trace to a retrieved source.

<!--
Slide ID: D4-M17-C3B
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: Provenance is part of the answer
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Notebook cue: stop if the report cites a source absent from the distinct-sources list.
- Then: Refuse a citation you cannot trace to a retrieved source.
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
- Say: The next step is evidence policy
- Ask: What permission would you require before enabling web search?
- Watch: Notebook cue: compare `TavilySearch` enabled with the documented `web: off` path and inspect open gaps.
- Then: Carry the observation into the next exercise.
Sources: [LangGraph durable execution](https://docs.langchain.com/oss/python/langgraph/durable-execution), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---

# Decide the evidence policy first
- **Ask:** What permission would you require before enabling web search?
- **Inspect:** Notebook cue: compare `TavilySearch` enabled with the documented `web: off` path and inspect open gaps.
- **Decide:** Decide the evidence policy before the tool is enabled, not after.

<!--
Slide ID: D4-M17-C4B
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes:
- Say: The next step is evidence policy
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Notebook cue: compare `TavilySearch` enabled with the documented `web: off` path and inspect open gaps.
- Then: Decide the evidence policy before the tool is enabled, not after.
Sources: [LangGraph durable execution](https://docs.langchain.com/oss/python/langgraph/durable-execution), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---

# 18 · A guardrail is a boundary with a policy

- Input checks gate the model boundary on the blocking path.
- Transforms change what proceeds; blocks stop a run.
- Tool checks protect execution and side effects, not only text.
- Output checks protect what the user receives.

<!--
Slide ID: D4-M18-C1
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: A guardrail is a boundary with a policy
- Ask: Where would you put a check that prevents an unauthorized account change?
- Watch: Notebook cue: read the stage and tripwire fields for each guarded case.
- Then: It then checks scope and prompt injection before the model, and unsupported claims and tone after generation.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# Read the stage and the tripwire
- **Ask:** Where would you put a check that prevents an unauthorized account change?
- **Inspect:** Notebook cue: read the stage and tripwire fields for each guarded case.
- **Decide:** State the policy and the stage together; a boundary without a policy is a hope.

<!--
Slide ID: D4-M18-C1B
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: A guardrail is a boundary with a policy
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Notebook cue: read the stage and tripwire fields for each guarded case.
- Then: State the policy and the stage together; a boundary without a policy is a hope.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# 18 · Placement changes the failure

| Placement | Primary protection | If it blocks |
|---|---|---|
| Before generation | Scope, injection, sensitive input | No model or tool run |
| After generation | Unsupported claims, tone, format | Output is withheld |
| Tool boundary | Authorization and side effects | Tool call is rejected |

No placement can undo a side effect that already happened.

<!--
Slide ID: D4-M18-C2
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes:
- Say: Placement changes the failure
- Ask: Which boundary should enforce requester authorization, and why?
- Watch: Notebook cue: forced overclaim and casual agents end at the output stage; input attacks stop earlier.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [OpenAI guardrail execution modes](https://openai.github.io/openai-agents-python/guardrails/#execution-modes), [Tool guardrails](https://openai.github.io/openai-agents-python/ref/tool_guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# Input stage or output stage
- **Ask:** Which boundary should enforce requester authorization, and why?
- **Inspect:** Notebook cue: forced overclaim and casual agents end at the output stage; input attacks stop earlier.
- **Decide:** Choose placement by which failure you can afford — input, output, or action.

<!--
Slide ID: D4-M18-C2B
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes:
- Say: Placement changes the failure
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Notebook cue: forced overclaim and casual agents end at the output stage; input attacks stop earlier.
- Then: Choose placement by which failure you can afford — input, output, or action.
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
- Say: Cheap rules are useful and brittle
- Ask: Which policy would you make warn-only, and what evidence would change your mind?
- Watch: Notebook cue: the matrix records five guardrail rows per case and flags uncaught attacks as findings.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# Check the uncaught column
- **Ask:** Which policy would you make warn-only, and what evidence would change your mind?
- **Inspect:** Notebook cue: the matrix records five guardrail rows per case and flags uncaught attacks as findings.
- **Decide:** Cheap rules first, but log what they miss; brittleness only shows in the uncaught column.

<!--
Slide ID: D4-M18-C3B
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: Cheap rules are useful and brittle
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Notebook cue: the matrix records five guardrail rows per case and flags uncaught attacks as findings.
- Then: Cheap rules first, but log what they miss; brittleness only shows in the uncaught column.
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
- Say: The system still owns authorization
- Ask: What must be true before a password-reset tool can execute?
- Watch: Notebook cue: use the saved `ots_results` fields to separate model boundary from execution authorization.
- Then: Carry the observation into the next exercise.
Sources: [OpenAI Agents SDK tools](https://openai.github.io/openai-agents-python/tools/), [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# Model boundary or system authorization
- **Ask:** What must be true before a password-reset tool can execute?
- **Inspect:** Notebook cue: use the saved `ots_results` fields to separate model boundary from execution authorization.
- **Decide:** The system authorizes the action, never the model's request.

<!--
Slide ID: D4-M18-C4B
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes:
- Say: The system still owns authorization
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Notebook cue: use the saved `ots_results` fields to separate model boundary from execution authorization.
- Then: The system authorizes the action, never the model's request.
Sources: [OpenAI Agents SDK tools](https://openai.github.io/openai-agents-python/tools/), [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
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
- Say: Optional research · State graphs for research
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
- Say: Optional research · Guardrails at the tool boundary
- Ask: What tool-call condition should halt execution rather than merely warn?
- Watch: Alignment pending for this extension; the notebook’s confirmed cue is stage-specific tripwire handling.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [OpenAI tool guardrails](https://openai.github.io/openai-agents-python/ref/tool_guardrails/), [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->
