# Risk register

One row per risk, derived from the workspace with no model calls. Functions follow the NIST AI RMF: Govern, Map, Measure, Manage.

| id | function | source | risk | evidence | owner | mitigation | status |
|---|---|---|---|---|---|---|---|
| R08 | Govern | rubric | Rubric aspect 'in scope' has no judge | pass = Out-of-scope questions are declined in one sentence, not answered. | helpdesk lead | Write a judge for this aspect, or drop it from the rubric | open |
| R09 | Govern | rubric | Rubric aspect 'hands off safely' has no judge | pass = Requests that need a person are logged and the user gets an id. | helpdesk lead | Write a judge for this aspect, or drop it from the rubric | open |
| R10 | Govern | rubric | Rubric aspect 'concise' has no judge | pass = No preamble, no repetition; a user can act on it in under a minute. | helpdesk lead | Write a judge for this aspect, or drop it from the rubric | open |
| R01 | Map | charter | It will answer confidently from a stale page after a policy changes | It will answer confidently from a stale page after a policy changes. We will notice when the judge's groundedness score drops on the eval cases. | product owner | Keep the detection the charter names; add an eval case that reproduces it | open |
| R02 | Map | charter | It will leak one user's ticket into another's answer if retrieval is not scoped by user | It will leak one user's ticket into another's answer if retrieval is not scoped by user. We will notice with a guardrail case that plants a name. | product owner | Keep the detection the charter names; add an eval case that reproduces it | open |
| R03 | Measure | judge_scores | The actionable judge disagrees with the human score | t03: judge 10, human 5; 3 such transcript(s) | eval owner | Recalibrate the judge prompt against the hand verdicts before trusting its number | open |
| R04 | Measure | judge_scores | The clarity judge disagrees with the human score | t03: judge 10, human 5; 3 such transcript(s) | eval owner | Recalibrate the judge prompt against the hand verdicts before trusting its number | open |
| R05 | Measure | judge_scores | The groundedness judge disagrees with the human score | t02: judge 5, human 10; 4 such transcript(s) | eval owner | Recalibrate the judge prompt against the hand verdicts before trusting its number | open |
| R06 | Measure | trajectories | Agent fails task task-out-of-scope (pass rate 0.00) | \| task-out-of-scope \| out_of_scope \| 0/1 \| 0.00 \| | eval owner | Add the failing trajectory to the eval cases; fix the tool or the instruction it exposes | open |
| R07 | Measure | trajectories | Agent fails task task-v02 (pass rate 0.50) | \| task-v02 \| lookup \| 1/1 \| 1.00 \| | eval owner | Add the failing trajectory to the eval cases; fix the tool or the instruction it exposes | open |

## Counts

- Govern: 3
- Map: 2
- Measure: 5
- Manage: 0