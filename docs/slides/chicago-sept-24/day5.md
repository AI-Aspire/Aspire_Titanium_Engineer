---
marp: true
theme: default
paginate: true
size: 16:9
---

# Show one working application flow

- Start with the workplace question and user goal.
- Show the smallest end-to-end path that works.
- Point to the artifact or trace that proves each step.
- Show what the demonstration does not yet prove.

<!--
Slide ID: D5-E1
Module: Evidence preparation
Instructor: Course team
Type: evidence
Minutes: 0
Layout: 09 Lab and code
Speaker notes:
- Say: Show one working application flow
- Ask: What artifact proves the demonstrated path worked?
- Watch: Use existing workspace artifacts; do not fabricate scores, traces, or conclusions.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [Titanium Engineer README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/README.md), [Workspace contract](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/WORKSPACE.md), [Trajectory evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)
-->

---

# Compare against the simplest baseline

| | Baseline | Current path |
|---|---|---|
| Same question | ✓ | ✓ |
| Evidence and success condition | Same | Same |
| Compare | Quality · cost · latency · failure shape | Quality · cost · latency · failure shape |

Name the case where the extra mechanism was not worth it.

<!--
Slide ID: D5-E2
Module: Evidence preparation
Instructor: Course team
Type: evidence
Minutes: 0
Layout: 05 Two column
Speaker notes:
- Say: Compare against the simplest baseline
- Ask: Which comparison row is your stopping rule?
- Watch: Point to the relevant saved artifact or mark the comparison as unmeasured.
- Then: Check: which row would change your decision if it got worse in the next run?
Sources: [Titanium Engineer README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/README.md), [Reading guide](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/READING_GUIDE.md), [Retrieval ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)
-->

---

# Explain architecture and one failure

- Draw model, tools, state, controls, and trace boundaries.
- Replay the failure at the step where it began.
- Separate a bug, a limitation, and an unmeasured risk.
- Label each conclusion as reproduced, suspected, or unmeasured.

<!--
Slide ID: D5-E3
Module: Evidence preparation
Instructor: Course team
Type: evidence
Minutes: 0
Layout: 09 Lab and code 1
Speaker notes:
- Say: Explain architecture and one failure
- Ask: At which boundary did the failure first become observable?
- Watch: Trace the claim to a real notebook output or mark it as pending.
- Then: Then replay one failure from the first incorrect step.
Sources: [OpenAI Agents SDK agents](https://openai.github.io/openai-agents-python/agents/), [LangGraph graph API](https://docs.langchain.com/oss/python/langgraph/graph-api), [Workspace contract](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/WORKSPACE.md), [Agents 101 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb)
-->

---

# Make the next decision explicit

| Decision | Evidence needed | Owner |
|---|---|---|
| Ship | The release bar is met | Named approver |
| Measure next | A specific gap, case, or metric | Named investigator |
| Stop | Complexity or risk is not justified | Product owner |

Record the remaining risk and what result would reverse the decision.

<!--
Slide ID: D5-E4
Module: Evidence preparation
Instructor: Course team
Type: evidence
Minutes: 0
Layout: 07 Big stats
Speaker notes:
- Say: Make the next decision explicit
- Ask: What exact result would reverse your decision?
- Watch: Decision must cite measured evidence or clearly state that it remains pending.
- Then: “Continue” means the demonstrated path cleared a stated bar and has a next controlled change.
Sources: [Titanium Engineer README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/README.md), [Demo scorecard](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/project/DEMO_SCORECARD.md), [Trajectory evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)
-->

---

# Optional modules: five ways to defend the thing you built

**Pick by the question you cannot answer yet.** · each stands alone

| Module | The question it answers | Time |
|---|---|---|
| 19 Responsible AI | what could go wrong, and who owns it? | 25m |
| 20 OWASP LLM top 10 | what happens when someone attacks it? | 35m |
| 21 DeepEval | does the new version actually beat the old one? | 35m |
| 22 Observability | how would you find out in production? | 35m |
| 23 Release pipeline | what stops a bad version from shipping? | 35m |

<!--
Slide ID: D5-T19
Module: Optional instruction, modules 19-23
Instructor: Course team
Type: transition
Minutes: 0
Layout: 02 Agenda
Speaker notes:
- Say: These are optional and independent — none depends on another, and each reads artifacts the week already wrote. Choose by the gap you feel rather than working down the list.
- Ask: Which of those five questions would you least want to be asked on Friday?
- Watch: Every one of these reads from the workspace, so a group that skipped a Create act will fall back to the seed. That is fine, and check_workspace will say so.
- Then: Straight into whichever the room picks.
Sources: [Titanium Engineer README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/README.md)
-->

---

# A risk register is derived, not drafted

Four NIST functions, each answered by **an artifact you already produced**:

| Function | Rows come from |
|---|---|
| Map | the charter's "where it will be wrong" bullets |
| Measure | judges with a low mean, and RAGAS faithfulness and pass rates |
| Manage | attacks no guardrail rung blocked |
| Govern | rubric aspects with **no** judge — the gaps |

Plain Python over the workspace. Every row gets an owner, or it is not a row.

<!--
Slide ID: D5-M19-C1
Module: [19 Responsible AI](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/19_Responsible_AI/README.md)
Instructor: Course team
Type: core
Minutes: 3
Layout: 05 Two column
Speaker notes:
- Say: The reason this module is twenty-five minutes and not a workshop is that the register is derived. You are not brainstorming risks in a room; you are reading them out of what the week measured. That is also what makes it defensible on Friday — every row points at an artifact.
- Ask: Which of the four functions will produce your longest list, and what does that tell you?
- Watch: Notebook Tasks 1 through 5 build the rows in that order, and Task 5 puts an owner on every row. The Govern rows are the interesting ones: they come from rubric aspects with no judge, which means the register names what you never measured.
- Then: A row with no owner is a note, not a risk. Say that plainly — it is the whole argument for doing this as a table rather than a discussion.
Sources: [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), [risk register notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/19_Responsible_AI/README.md)
-->

---

# The attack does not have to come from the user

- **Direct** injection: ask for the canary outright
- **Recombined:** prefixes × bodies × suffixes — one attack, many surfaces
- **Indirect:** a *poisoned page* in the corpus, and an innocent question
- Also: a poisoned **tool description**, where the canary shows up in the call arguments

Retrieved text and tool metadata are inputs too. Every attack that worked becomes a regression test.

<!--
Slide ID: D5-M20-C1
Module: [20 OWASP LLM top ten](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/20_OWASP_LLM_Top10/README.md)
Instructor: Course team
Type: core
Minutes: 4
Layout: 06 Process steps
Speaker notes:
- Say: The move worth carrying out of this module is the indirect case. Most people picture prompt injection as a hostile user typing something clever. Here a page in your own corpus carries the payload, and the user's question is innocent — which means your retrieval step is an attack surface, and so is a tool description you copied from somewhere.
- Ask: If the payload is in a knowledge-base page, which of this week's controls would catch it?
- Watch: Tasks 2 through 9 run the five categories: direct, recombined, and indirect injection, sensitive disclosure by claiming to be another user, output handling, excessive agency where cleanup is implied and the write tool fires, and system prompt leakage both by probe and by poisoned tool description.
- Then: The answer to the Ask is day 3's optional slide — retrieved text is data, never authority — plus the guardrail at the tool boundary. Neither is a prompt instruction. Then land the regression-test point: an attack you fixed without a test is an attack you will ship again.
Sources: [OWASP LLM top ten](https://genai.owasp.org/llm-top-10/), [OWASP notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/20_OWASP_LLM_Top10/README.md)
-->

---

# Two versions, same cases, three metrics each

- v1 is prompt-only; v2 retrieves over the corpus — **the only difference**
- Read every eval case *before* any model runs
- Gate **per metric**, not on an average
- Fingerprint the case set, so the decision records what it was measured against

A release decision written from numbers, not from the demo that happened to work.

<!--
Slide ID: D5-M21-C1
Module: [21 DeepEval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/21_DeepEval/README.md)
Instructor: Course team
Type: core
Minutes: 3
Layout: 05 Two column
Speaker notes:
- Say: This is the comparison discipline from Tuesday applied to a release. Two versions differing in exactly one thing, the same cases, the same judge on your own endpoint. Reading the cases first is deliberate: once you have seen a score you cannot un-see it when deciding whether the case was fair.
- Ask: Your average score improves and one metric drops. Ship or hold?
- Watch: Task 1 reads every case before any model runs; Task 7 fingerprints the case set and gates v2 per metric. The fingerprint is what stops a decision from outliving the cases that justified it.
- Then: Hold — that is the setup for module 23, whose first task is literally the average that hides a failure.
Sources: [DeepEval](https://deepeval.com/docs/getting-started), [DeepEval notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/21_DeepEval/README.md)
-->

---

# Three of the four metrics cannot see a quality regression

Plant one: from day five, **a third of passing answers now fail.** Nothing else changes.

| Metric | Does it move? |
|---|---|
| p50 / p95 latency | no |
| cost per request | no |
| refusal rate | no |
| **eval score on traffic** | **yes** |

A tracing dashboard that only records success shows a healthy system during an outage.

<!--
Slide ID: D5-M22-C1
Module: [22 Observability and incidents](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/22_Observability/README.md)
Instructor: Course team
Type: core
Minutes: 4
Layout: 03 Big stats
Speaker notes:
- Say: The notebook is explicit that these are not the standard four — they are the four an LLM application needs. And it plants a regression to make the point undeniable: a third of good answers go bad, and three of your four charts stay flat. The one that moves is the only one that costs money to collect, which is exactly why teams skip it.
- Ask: Which of your four would you have to build before launch, and who runs it?
- Watch: Task 3 builds the week and plants the regression from day five. Task 1 is the span itself — a dictionary with a start time, a duration, and a parent — and the context manager records whether or not the work succeeded, because instrumentation that only records success shows a healthy dashboard during an outage.
- Then: Tell them the span mapping matters too: their dictionary says tokens_in and the rest of the world says gen_ai.usage.input_tokens, so Task 2 is what makes their traces readable by tools they have not bought yet.
Sources: [OpenTelemetry GenAI conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/), [observability notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/22_Observability/README.md)
-->

---

# Say the detection lag out loud

- You cannot score every request. Score a **sample** each day and watch the series
- The detector: fires when the last three days average **2.5 standard deviations** below everything before
- Run it and watch it fire **a day late**
- The gap between the regression starting and the alert is a number you can promise

Sophisticated change detection exists and is rarely why teams miss this. Not looking is.

<!--
Slide ID: D5-M22-C2
Module: [22 Observability and incidents](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/22_Observability/README.md)
Instructor: Course team
Type: core
Minutes: 3
Layout: 06 Process steps
Speaker notes:
- Say: The honest deliverable here is not the detector, it is the lag. You will watch it fire a day after the regression began, and that day is what you owe your team as a commitment rather than an embarrassment. A number you can state beats a dashboard you hope someone is watching.
- Ask: What is the longest detection lag your product could survive?
- Watch: Task 4 writes detect_drift, runs it on the eval score, then on p95 latency with the sign flipped so a rise reads as a drop, and asks which fires. The notebook's line is worth quoting: sophisticated change detection exists and is rarely why teams miss this; not looking is.
- Then: Task 6 is where data boundaries arrive with teeth — if questions contain customer data and the tracing backend keeps request bodies for ninety days, you have made a ninety-day copy of customer data in a system nobody classified. So the saved spans are redacted, with question_len in place of the question.
Sources: [observability notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/22_Observability/README.md)
-->

---

# A canary at forty samples cannot tell a win from luck

- A rolling update answers one question: does it start and stay up — **a worse model passes that**
- A canary sends a slice of real traffic; a shadow copies traffic and discards the replies
- Both give you a pass rate on a *sample*, and a sample of forty moves around
- So: latency is a hard gate, too few samples is a **hold**, then a two-proportion 95% interval decides

A release decision that lives in a notebook is a wish. A gate is a script that exits non-zero.

<!--
Slide ID: D5-M23-C1
Module: [23 Release pipeline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/23_Release_Pipeline/README.md)
Instructor: Course team
Type: core
Minutes: 4
Layout: 03 Big stats
Speaker notes:
- Say: This is the statistical honesty the whole week has been building toward. Forty samples feels like evidence and is not; the interval on the difference of two proportions will straddle zero, and a verdict that promotes anyway is promoting noise. The three-part rule is the deliverable — hard gate on latency, hold on sample size, interval after that.
- Ask: At your real request volume, how long would a canary at five percent of traffic need to run before the interval could clear zero?
- Watch: Task 4 compares rolling, canary, and shadow and writes the verdict from scratch. Task 1 is the average that hides a failure, which is the direct sequel to module 21's per-metric gate.
- Then: The Ask is the notebook's own question, and for most products the honest answer is that shadowing offline is the only workable option — which is a real architectural consequence of a statistics fact.
Sources: [release pipeline notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/23_Release_Pipeline/README.md)
-->

---

# Filtering after you rank is a leak

- Decide who may read what **before** retrieval, never after
- Filter-after-rank means the ranker already saw documents this user may not
- Eight properties of a manifest a platform team greps for — break one, watch the check fail
- Fill the deployment checklist from what the repo answers, and mark the rest **unknown**

The unknowns are the useful part. They are the questions only your platform team can close.

<!--
Slide ID: D5-M23-C2
Module: [23 Release pipeline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/23_Release_Pipeline/README.md)
Instructor: Course team
Type: core
Minutes: 3
Layout: 06 Process steps
Speaker notes:
- Say: Authorisation before ranking is the same point day 2 made about filtering the candidate set, now with the release consequence attached. If the ranker has already scored a document this user cannot see, the scores themselves carry information out — and top-k over a filtered list is not the same as filtering a top-k.
- Ask: Who signs the checklist rows you have to mark unknown?
- Watch: Task 5 decides who may read what before retrieval and shows why filtering afterwards leaks. Task 3 reads a manifest a security review can accept, then breaks one property so the check fails. Task 6 fills the checklist from what the repository already answers.
- Then: Marking a row unknown is the honest end of the week. An unknown with a name next to it is a plan; an unknown with no name is how a prototype quietly becomes production.
Sources: [release pipeline notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/23_Release_Pipeline/README.md)
-->
