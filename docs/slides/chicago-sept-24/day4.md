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
Speaker notes: Start with the recurring workplace question: “Why did our support agent fail this access request, and what should we change?” A single prompt can produce a polished answer, but it hides whether the question was understood, whether search was broad enough, and where a claim came from. The notebook unrolls that opaque call into six nodes. Clarify decides whether the question is specific enough; brief states success criteria; plan creates bounded research tasks; research isolates each task; compress reduces findings into an evidence packet; write produces the report. LangGraph supplies the state graph, but the teaching point is the contract between steps. This is an engineering response to context and auditability problems, not proof that more nodes create better research. Check: which boundary would you inspect first when the final answer is wrong? Lab observation: six node updates, one trace event per node, and a query line per research task.
Check understanding: Which boundary would you inspect first when the final answer is wrong?
Lab observation: Notebook cue: six node updates in order and trace events with query, corpus hits, web hits, and gaps.
Sources: [LangGraph graph API](https://docs.langchain.com/oss/python/langgraph/graph-api), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---

# 17 · Make research inspectable · The practical check

- **Ask:** Which boundary would you inspect first when the final answer is wrong?
- **Inspect:** Notebook cue: six node updates in order and trace events with query, corpus hits, web hits, and gaps.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D4-M17-C1B
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Which boundary would you inspect first when the final answer is wrong?
Lab observation: Notebook cue: six node updates in order and trace events with query, corpus hits, web hits, and gaps.
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
Speaker notes: The practical change is not “use the web.” It is to give each research task a narrow query, a bounded number of results, and an explicit handoff. The notebook’s researchers search the rendered corpus and, when Tavily is configured, the web; they extract short source text, reflect on relevance, and retain sources plus gaps. The default path still works with corpus-only evidence. That matters for a workplace assistant whose policy pages and prior traces are often more relevant than the open web. The stopping rule is evidence-based: a task with no source becomes an admitted gap. Do not let a fluent compression step turn an empty result into a fact. Check: what should the report say when all search paths return zero hits? Lab observation: the notebook prints per-task query and corpus/web hit counts.
Check understanding: What should the report say when every search path returns zero hits?
Lab observation: Notebook cue: empty sources are surfaced as gaps; query lines and hit counts appear under research.
Sources: [LangGraph workflows](https://docs.langchain.com/oss/python/langgraph/workflows-agents), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---

# 17 · Research is a bounded loop · The practical check

- **Ask:** What should the report say when every search path returns zero hits?
- **Inspect:** Notebook cue: empty sources are surfaced as gaps; query lines and hit counts appear under research.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D4-M17-C2B
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: What should the report say when every search path returns zero hits?
Lab observation: Notebook cue: empty sources are surfaced as gaps; query lines and hit counts appear under research.
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
Speaker notes: Use a concrete example: “The agent should ask for the device identifier before changing access.” A defensible report should connect that recommendation to a finding, the finding to a source page or search result, and the trace to the query that found it. The notebook prompts the writer to include inline sources and an open-gaps section, then the checkpoint asks the learner to compare citations with the distinct-source list. That is a human inspection cue, not an executable validation assertion. It may reveal an invented citation, but it does not prove that a cited page supports the claim. Provenance answers “where did this come from?”; it does not answer “is the source authoritative or current?” Check: what extra test would you add for support rather than citation presence? Lab observation: inspect the rendered report, distinct sources, and gaps together.
Check understanding: What does a valid citation prove, and what does it still not prove?
Lab observation: Notebook cue: stop if the report cites a source absent from the distinct-sources list.
Sources: [LangGraph workflows](https://docs.langchain.com/oss/python/langgraph/workflows-agents), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---

# 17 · Provenance is part of the answer · The practical check

- **Ask:** What does a valid citation prove, and what does it still not prove?
- **Inspect:** Notebook cue: stop if the report cites a source absent from the distinct-sources list.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D4-M17-C3B
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: What does a valid citation prove, and what does it still not prove?
Lab observation: Notebook cue: stop if the report cites a source absent from the distinct-sources list.
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
Speaker notes: Close by separating prototype maturity from technology choice. The notebook gives us a useful working prototype: typed state, bounded nodes, optional tools, source filtering, a report, and a trace. It is not production readiness. A production research workflow must decide which sources may be searched, whose data may be exposed, how tool failures and retries are handled, how stale evidence is detected, and which eval cases gate changes. The safe stopping rule is often simpler: use the internal corpus only when the question is about internal policy, and do not turn on web search merely because it is available. The bridge is to the capability report from module 09: choose a top failure, research it, then make the resulting risk testable. Check: what permission would you require before enabling web search? Lab observation: compare Tavily enabled with the documented web-off path and inspect open gaps.
Check understanding: What permission would you require before enabling web search?
Lab observation: Notebook cue: compare `TavilySearch` enabled with the documented `web: off` path and inspect open gaps.
Sources: [LangGraph durable execution](https://docs.langchain.com/oss/python/langgraph/durable-execution), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)
-->

---

# 17 · The next step is evidence policy · The practical check

- **Ask:** What permission would you require before enabling web search?
- **Inspect:** Notebook cue: compare `TavilySearch` enabled with the documented `web: off` path and inspect open gaps.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D4-M17-C4B
Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: What permission would you require before enabling web search?
Lab observation: Notebook cue: compare `TavilySearch` enabled with the documented `web: off` path and inspect open gaps.
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
Speaker notes: Return to the workplace question: “Can this assistant safely answer an access request?” A guardrail is not a second vague system prompt. It is a check attached to a boundary with a policy and a defined failure behavior. The notebook first redacts email, phone, SSN, or employee ID without blocking a legitimate request. It then checks scope and prompt injection before the model, and unsupported claims and tone after generation. The OpenAI Agents SDK distinguishes input and output guardrails and exposes tripwire exceptions when a check blocks. Tool guardrails are a separate boundary when the risk is the tool call itself. Check: where would you put a check that prevents an unauthorized account change? Lab observation: `run_guarded` records processed input, stage, blocked state, and tripwire.
Check understanding: Where would you put a check that prevents an unauthorized account change?
Lab observation: Notebook cue: read the stage and tripwire fields for each guarded case.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# 18 · A guardrail is a boundary with a policy · The practical check

- **Ask:** Where would you put a check that prevents an unauthorized account change?
- **Inspect:** Notebook cue: read the stage and tripwire fields for each guarded case.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D4-M18-C1B
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Where would you put a check that prevents an unauthorized account change?
Lab observation: Notebook cue: read the stage and tripwire fields for each guarded case.
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
Speaker notes: Placement is an architectural decision. Input guardrails are not unconditionally before model execution: the SDK can run them in parallel by default. A blocking input check is the mode that completes before the agent starts, which matters for cost and side effects. An output guardrail can stop a final answer, but the model has already spent tokens and may already have used tools. A tool input guardrail is closer to the side effect and can reject or halt the tool call. The notebook deliberately teaches input and output agent guardrails, while its lookup tool remains a simple capability. Do not claim that an output phrase check authorizes an action. Check: which boundary is the strongest place to enforce “the requester is the account holder”? Lab observation: compare input-stage and output-stage tripwires, including the forced unsafe demo agents.
Check understanding: Which boundary should enforce requester authorization, and why?
Lab observation: Notebook cue: forced overclaim and casual agents end at the output stage; input attacks stop earlier.
Sources: [OpenAI guardrail execution modes](https://openai.github.io/openai-agents-python/guardrails/#execution-modes), [Tool guardrails](https://openai.github.io/openai-agents-python/ref/tool_guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# 18 · Placement changes the failure · The practical check

- **Ask:** Which boundary should enforce requester authorization, and why?
- **Inspect:** Notebook cue: forced overclaim and casual agents end at the output stage; input attacks stop earlier.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D4-M18-C2B
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Which boundary should enforce requester authorization, and why?
Lab observation: Notebook cue: forced overclaim and casual agents end at the output stage; input attacks stop earlier.
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
Speaker notes: Connect this module to module 13’s ladder. The off-the-shelf SDK gives lifecycle plumbing and typed outcomes; it does not make the policy detector accurate. The notebook’s scope and injection checks are regex and vocabulary rules, PII is regex redaction, and claims and tone are pattern checks. Those are excellent teaching mechanisms because the result is inspectable. They miss paraphrases, new attack forms, and legitimate wording outside the corpus vocabulary. A classifier or LLM judge may improve coverage, but it adds training or prompt drift, latency, and another failure mode. The stopping rule is empirical: run every case, read false positives first, and keep a guardrail hard-blocking only when the harm of a miss justifies the cost of a false positive. Check: which tone violation should be warn-only? Lab observation: read the matrix, not just the attack count.
Check understanding: Which policy would you make warn-only, and what evidence would change your mind?
Lab observation: Notebook cue: the matrix records five guardrail rows per case and flags uncaught attacks as findings.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# 18 · Cheap rules are useful and brittle · The practical check

- **Ask:** Which policy would you make warn-only, and what evidence would change your mind?
- **Inspect:** Notebook cue: the matrix records five guardrail rows per case and flags uncaught attacks as findings.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D4-M18-C3B
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Which policy would you make warn-only, and what evidence would change your mind?
Lab observation: Notebook cue: the matrix records five guardrail rows per case and flags uncaught attacks as findings.
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
Speaker notes: End with the boundary students most often blur: content safety is not authorization. A guardrail can detect “reset my password” or redact an identifier, but only the application can verify identity, tenant, role, approval, and whether the tool is allowed to mutate state. Module 13's ladder defines the policy layer as deterministic authorisation on the user and the action, never a prompt. This notebook's Grow section points the scope check toward a tenant-aware policy classifier, and its `run_guarded` record keeps the model boundary separate from execution authorization. A useful record includes the case, stage, policy version, reason, and whether the model or tool was reached. This creates a bridge back to evals: every real incident should become a regression case, and every hard block should be reviewed for false positives. Check: what must be true before a password-reset tool can execute? Lab observation: inspect `model_reached`, `stage`, `expected`, and uncaught attack rows.
Check understanding: What must be true before a password-reset tool can execute?
Lab observation: Notebook cue: use the saved `ots_results` fields to separate model boundary from execution authorization.
Sources: [OpenAI Agents SDK tools](https://openai.github.io/openai-agents-python/tools/), [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->

---

# 18 · The system still owns authorization · The practical check

- **Ask:** What must be true before a password-reset tool can execute?
- **Inspect:** Notebook cue: use the saved `ots_results` fields to separate model boundary from execution authorization.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D4-M18-C4B
Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: What must be true before a password-reset tool can execute?
Lab observation: Notebook cue: use the saved `ots_results` fields to separate model boundary from execution authorization.
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
Speaker notes: This optional slide uses Anthropic’s June 2025 engineering case study as a concrete multi-agent research example. Anthropic describes a lead agent delegating parallel research to subagents, then compressing findings; its claimed internal result is vendor-reported and should not be treated as a cohort benchmark. The contribution is an architecture for breadth-first, open-ended questions; the tradeoff is materially higher token use, coordination complexity, and weaker fit for tightly coupled work. Compare that case with this notebook’s six-node single-graph workflow: both expose stages and handoffs, but neither makes sources authoritative. Ask the room whether parallel subagents are justified for an internal access-policy question. Stop when the group names a workload property, cost constraint, and evaluation needed to test the choice.
Check understanding: Which state boundary should stop when sources are empty?
Lab observation: Notebook cue: compare the six node updates with the research trace and open gaps.
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
Speaker notes: This optional slide extends the notebook’s distinction between an answer boundary and an execution boundary. The OpenAI Agents SDK documentation describes tool guardrails that run around function-tool invocation and can allow normal execution, reject content while continuing, or raise an exception to halt. That is a sharper research question than “should we add more moderation?” For an access assistant, a sentence such as “I reset the account” is an output risk, while an unauthorized reset request is a tool-input risk. Ask the room to design one case for each and decide which outcome is appropriate. The notebook does not implement a mutating tool or a real authorization service, so this is a documented extension, not a claimed lab result. Stop when the policy owner and test case are named.
Check understanding: What tool-call condition should halt execution rather than merely warn?
Lab observation: Alignment pending for this extension; the notebook’s confirmed cue is stage-specific tripwire handling.
Sources: [OpenAI tool guardrails](https://openai.github.io/openai-agents-python/ref/tool_guardrails/), [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)
-->
