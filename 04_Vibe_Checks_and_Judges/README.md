# Vibe checks and judges

## Learn | Create | Grow

### Learn
Why a deliberate vibe check comes before a model judge: a written rubric, your own verdicts, one line of reasoning each. Then how a strict judge is built and validated.

### Create
A rubric and vibe checks for your product, three judges run over your transcripts, your hand scores attached, and a table of where the judges disagree with each other and with you.

### Grow
Production evals use a separate judge model, human calibration on a sample, and release thresholds. Bring your team one disagreement and say which evidence you trusted.

**Estimated time:** 30 minutes
**Reads:** charter, transcripts
**Writes:** rubric, vibe_checks, judge_scores

## What you will do

| Task | What happens |
|---|---|
| 1 | Write the rubric: five aspects, one pass definition each |
| 2 | Write vibe checks: inputs with what a good answer must contain |
| 3 | Judge the transcripts by hand |
| 4 | Build a strict judge with validation and a retry |
| 5 | Three judges: groundedness, actionability, clarity |
| 6 | Score everything and save the record |
| 7 | Sort by disagreement and read the rationales |

The distinction that matters: an answer can be grounded, actionable, or clear. Those overlap, and they are not the same measurement.

## Setup

```bash
make setup
uv run jupyter lab      # open 04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb
```

Needs `OPENAI_API_KEY` and `LLM_MODEL` in `.env`. The judge uses the same model unless you change `JUDGE_MODEL` in the setup cell.

## Data files

None in this folder. Reads `charter` and `transcripts` from the workspace, writes `rubric`, `vibe_checks`, and `judge_scores`.
