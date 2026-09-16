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
