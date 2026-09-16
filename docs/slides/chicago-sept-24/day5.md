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
Speaker notes: This is a demonstration format, not a production hosting requirement. Choose one recurring internal question and show the user-visible journey from input to answer. Keep the scope narrow enough that the audience can follow the actual mechanism: prompt, retrieval or tool call, returned observation, final answer, and any guardrail or evaluation record. Use the group’s real workspace artifacts where they exist; do not substitute a polished screenshot for a run. If the system is not reliable, say so and show the failure path. The audience should leave knowing what is working today and what evidence supports that statement. Check: can a viewer identify the exact artifact that proves the answer was grounded or the task passed? Lab observation: report only artifacts the notebooks actually generated.
Check understanding: What artifact proves the demonstrated path worked?
Lab observation: Use existing workspace artifacts; do not fabricate scores, traces, or conclusions.
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
Speaker notes: A comparison makes the engineering decision visible. Use the simplest credible baseline available: no context versus pasted context, dense versus hybrid retrieval, DCI versus agentic RAG, one run versus repeated trajectory evaluation, or unguarded versus guarded output. Keep the question and success condition constant. Do not claim that the newer path wins everywhere; the notebook exercises explicitly ask learners to inspect per-case matrices, disagreement, latency, and false positives. The most valuable comparison may be a non-win that tells the team to stop paying for an extra rung. Check: which row would change your decision if it got worse in the next run? Lab observation: use measured workspace artifacts when present and label any missing comparison as an open gap.
Check understanding: Which comparison row is your stopping rule?
Lab observation: Point to the relevant saved artifact or mark the comparison as unmeasured.
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
Speaker notes: The audience needs an explanation they can challenge. Draw the system boundary plainly: the model proposes; the application executes permitted tools; state and memory determine what context returns; guardrails inspect defined boundaries; the trace records what happened. Then replay one failure from the first incorrect step. If retrieval returned the wrong page, that is different from a judge mis-scoring a good answer. If memory leaked between users, that is different from a missing retention policy. Call each one by its evidence status: reproduced, suspected, or not measured. This keeps a working prototype honest without turning the session into a code review. Check: where did the failure first become observable? Lab observation: use actual trace, ladder, trajectory, or guardrail rows; no invented root cause.
Check understanding: At which boundary did the failure first become observable?
Lab observation: Trace the claim to a real notebook output or mark it as pending.
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
Speaker notes: End with a decision, not a generic future-work list. “Continue” means the demonstrated path cleared a stated bar and has a next controlled change. “Measure” means the evidence is insufficient, so name the missing case, metric, or trace and who will collect it. “Stop” means the added complexity, risk, or cost is not justified by the current result. None of these decisions requires the prototype to be hosted in production. The outcome is a working evaluated application: it documents observed behavior on tested cases and makes remaining uncertainty visible. Include one residual risk even when continuing; an uncaught attack, stale memory, weak retrieval case, or judge disagreement is useful evidence. Check: what exact result would reverse your decision? Lab observation: tie the decision to existing artifacts and unresolved gaps.
Check understanding: What exact result would reverse your decision?
Lab observation: Decision must cite measured evidence or clearly state that it remains pending.
Sources: [Titanium Engineer README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/README.md), [Demo scorecard](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/project/DEMO_SCORECARD.md), [Trajectory evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)
-->
