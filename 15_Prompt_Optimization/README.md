# DSPy optimizers

ℹ This module needs the `optim` dependency group. Run `make setup-optim` once before opening the notebook.

## Learn | Create | Grow

### Learn
Prompt optimisation as a compile step: a signature, a metric, and optimisers that search for the prompt. BootstrapFewShot, MIPROv2, and GEPA on the same task.

### Create
Training examples from your judge scores and transcripts, agreement with your hand scores as the metric, and the best program saved.

### Grow
Production optimisation reruns when the examples change and records what changed in the prompt. Tell your team which optimiser moved agreement and whether it was worth the calls.

**Estimated time:** 30 minutes
**Reads:** judge_scores, transcripts
**Writes:** dspy_program

## Plain English first

| Term | Meaning |
|---|---|
| Signature | the fields a program takes in and gives out, with one instruction |
| Program | a signature wrapped in a module you can call and save |
| Metric | a function that says whether one prediction was good |
| Optimizer | a search over instructions and demos that raises the metric on training examples |
| Demo | a solved example pasted into the prompt |
| Held-out | examples the optimizer never saw, used to score it honestly |

## What you will do

| Task | What happens |
|---|---|
| 1 | Build examples from the transcripts you scored by hand |
| 2 | Write the judge program and the agreement metric; score the baseline |
| 3 | BootstrapFewShot |
| 4 | MIPROv2 |
| 5 | GEPA, if the installed DSPy has it |
| 6 | Compare, show what each optimizer changed, save the winner |

## Before you arrive

- Score six transcripts from your own assistant by hand on a 0 to 10 scale and keep the sheet; the optimizer trains on them.
- DSPy: https://arxiv.org/abs/2310.03714

## Setup

```bash
make setup-optim
uv run jupyter lab      # open 15_Prompt_Optimization/DSPy_Optimizers.ipynb
```

Needs `OPENAI_API_KEY` and `LLM_MODEL` in `.env`. DSPy caches model calls on disk under its own cache directory, so a rerun is fast.

## Data files

None in this folder. Reads `judge_scores` and `transcripts` from the workspace, writes `dspy_program`.
