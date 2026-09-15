# The guardrail ladder

## Learn | Create | Grow

### Learn
A guardrail ladder from scratch: constrained decoding on recorded logits, a regex rung, a classifier trained in numpy, an LLM judge, and a policy table. What each rung costs, catches, and guarantees.

### Create
A case set of benign inputs from your transcripts plus planted attacks, every rung run over it failing closed, and coverage next to false positives per rung saved.

### Grow
Ship cheapest-first: the rungs that clear your coverage bar at your latency budget. Tell your team which rung you left out and what it would cost.

**Estimated time:** 45 minutes
**Reads:** transcripts
**Writes:** guardrail_cases, ladder_results

## Plain English first

| Term | Meaning |
|---|---|
| Rung | one guardrail mechanism; each costs more and catches more than the one below |
| Constrained decoding | masking illegal tokens before sampling, so a bad output is unreachable |
| False positive | a legitimate input the guardrail blocks; the number that decides whether it survives |
| Fail closed | when a rung raises, the ladder blocks rather than allows |
| Policy layer | deterministic authorisation on the user and the action, never a prompt |

## What you will do

| Task | What happens |
|---|---|
| 1 | Build the case set: first user turns from your transcripts plus planted attacks |
| 2 | Rung 0: constrain a recorded distribution to an allowed set and read the kept mass |
| 3 | Rung 1: four regexes, timed in microseconds |
| 4 | Rung 2: train a logistic-regression classifier in numpy and compare it with the rules |
| 5 | Rung 3: an LLM judge with a one-word verdict, timed |
| 6 | Rung 4: a policy table over roles, decided in microseconds without reading the text |
| 7 | Run every rung on every case, failing closed, report coverage beside false positives, assemble the ladder, and save the results |

## Before you arrive

- Write down three requests your assistant must refuse and two that look similar but must pass; bring all five.
- Efficient guided generation for large language models: https://arxiv.org/abs/2307.09702

## Setup

```bash
make setup
uv run jupyter lab      # open 13_Guardrails_101/Guardrail_Ladder.ipynb
```

Needs `OPENAI_API_KEY` and `LLM_MODEL` in `.env` for the judge rung. The other rungs run with no network.

## Data files

| File | Purpose |
|---|---|
| `data/logits_small.npz` | top-200 logits and token ids at two positions, recorded from a small open-weights model |
| `data/logits_small_meta.json` | the prompt, the model name, and the vocabulary for those token ids |

Reads `transcripts` from the workspace, writes `guardrail_cases` and `ladder_results`.
