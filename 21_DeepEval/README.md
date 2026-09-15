# DeepEval

## Learn | Create | Grow

### Learn
A release decision as pass/fail evidence: a contract of eval cases, two versions of the assistant, and three metrics per case with a judge on your own endpoint.

### Create
Both versions run over your eval cases, one result row per metric, and a release decision written from the numbers.

### Grow
Rerun before the demo and read the decision aloud. Bring your team one pass and one failure and say which metric caught it.

**Estimated time:** 40 minutes
**Reads:** eval_cases, corpus
**Writes:** deepeval_results, release_decision

## Plain English first

| Term | Meaning |
|---|---|
| Eval case | a question and the reference answer a correct reply must match |
| Answer relevancy | did the answer address the question without drifting |
| Faithfulness | did the answer stay inside the retrieved pages |
| G-Eval | a judge prompt with your own steps, here scoring correctness against the reference |
| Release decision | ship or hold, with the case set fingerprinted and the failing metric named |

## What you will do

| Task | What happens |
|---|---|
| 1 | Read every eval case before any model runs |
| 2 | v1: a prompt-only answerer |
| 3 | v2: a retrieval agent over the corpus with `create_agent` |
| 4 | Answer every case with both versions, keeping the retrieval context |
| 5 | A DeepEval judge over your endpoint and three metrics |
| 6 | Score every run and save the result rows |
| 7 | Fingerprint the case set, gate v2 per metric, and save the release decision |

## Setup

```bash
make setup
uv run jupyter lab      # open 21_DeepEval/Release_Decision.ipynb
```

Needs `OPENAI_API_KEY` and `LLM_MODEL` in `.env`. DeepEval runs locally with no account. Each metric makes one to four judge calls per run, so six cases and two versions is around fifty model calls.

## Data files

None in this folder. Reads `eval_cases` and `corpus` from the workspace, writes `deepeval_results` and `release_decision`.
