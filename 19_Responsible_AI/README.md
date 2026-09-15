# Responsible AI

## Learn | Create | Grow

### Learn
The NIST AI risk management framework as four functions, Govern, Map, Measure, Manage, and how each one is answered by an artifact you already produced.

### Create
A risk register with one row per risk, derived by plain Python from your workspace, rendered as a table and saved.

### Grow
A register is only useful if someone owns each row. Tell your team which row surprised you and which risk has no evidence behind it yet.

**Estimated time:** 25 minutes
**Reads:** charter, rubric, judge_scores, ragas_scores, trajectories, capability_report, guardrail_cases, ladder_results, owasp_findings
**Writes:** risk_register

## Plain English first

| Term | Meaning |
|---|---|
| Govern | who is accountable and what the rules are |
| Map | where the system could go wrong, in its context |
| Measure | showing a risk with a number from a test |
| Manage | the decision and action taken on a measured risk |
| Register | one table, one row per risk, with evidence and an owner |

`NIST_AI_RMF.md` in this folder explains the four functions in a page.

## What you will do

| Task | What happens |
|---|---|
| 1 | Map rows from the charter's "where it will be wrong" bullets |
| 2 | Measure rows from judges with a low mean or a gap to your hand score |
| 3 | Measure rows from RAGAS faithfulness and agent pass rates |
| 4 | Manage rows from attacks no guardrail rung blocked, plus OWASP findings if present |
| 5 | Govern rows from rubric aspects with no judge; owners on every row |
| 6 | Render the table and save the register |

## Setup

```bash
make setup
uv run jupyter lab      # open 19_Responsible_AI/NIST_Risk_Register.ipynb
```

Runs offline. No key, no model, no network. Reads only the workspace, with the seed as fallback.

## Data files

None in this folder. Reads nine artifacts from the workspace and writes `risk_register`.
