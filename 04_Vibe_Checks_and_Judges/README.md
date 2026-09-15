# Vibe checks and judges

## Learn | Create | Grow

### Learn
Why a deliberate vibe check comes before a model judge: a written rubric, your own verdicts, one line of reasoning each. Then two scorers that cannot judge at all, to fix the floor and the ceiling any judge sits between.

### Create
A rubric and vibe checks for your product, three judges run over your transcripts, your hand scores attached, a table of where the judges disagree with each other and with you, and an interval on every agreement number.

### Grow
Production evals use a separate judge model, human calibration on a sample, and release thresholds. Bring your team one disagreement and say which evidence you trusted.

**Estimated time:** 35 minutes
**Reads:** charter, transcripts
**Writes:** rubric, vibe_checks, judge_scores

## What you will do

| Task | What happens |
|---|---|
| 1 | Write the rubric: five aspects, one pass definition each |
| 2 | Write vibe checks: inputs with what a good answer must contain |
| 3 | Judge the transcripts by hand |
| 4 | Two dumb baselines, echo and oracle, to fix the floor and ceiling of agreement |
| 5 | Build a strict judge with validation and a retry |
| 6 | Three judges: groundedness, actionability, clarity |
| 7 | Score everything and save the record |
| 8 | Sort by disagreement and read the rationales |
| 9 | Put a 95% interval on each agreement and on a judge-versus-judge gap at several sample sizes |

The distinction that matters: an answer can be grounded, actionable, or clear. Those overlap, and they are not the same measurement.

## Before you arrive

- Score five answers from any assistant you use by hand, pass, mixed, or fail, with one line of reasoning each; keep the sheet.
- Judging LLM-as-a-judge with MT-Bench and Chatbot Arena: https://arxiv.org/abs/2306.05685

## Setup

```bash
make setup
uv run jupyter lab      # open 04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb
```

Needs `OPENAI_API_KEY` and `LLM_MODEL` in `.env`. The judge uses the same model unless you change `JUDGE_MODEL` in the setup cell.

## Data files

None in this folder. Reads `charter` and `transcripts` from the workspace, writes `rubric`, `vibe_checks`, and `judge_scores`.
