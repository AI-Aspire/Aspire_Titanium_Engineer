# Improving RAG with RAGAS

## Learn | Create | Grow

### Learn
Why a weak pipeline on purpose, how a synthetic test set is written by hand for one chunk and generated for the rest, and what four RAGAS metrics each measure.

### Create
A test set generated from your corpus, RAGAS scores on your pipeline, one retrieval change, and the scores again.

### Grow
Production teams keep the test set under version control and rerun it on every retrieval change. Tell your team your weakest metric and which way it moved.

**Estimated time:** 35 minutes
**Reads:** corpus
**Writes:** testset, ragas_scores

## Plain English first

| Term | Meaning |
|---|---|
| Synthetic data generation | a model writes questions and reference answers from your pages |
| Faithfulness | share of claims in the answer that the retrieved chunks support |
| Answer relevancy | how directly the answer addresses the question |
| Context precision | whether the chunks the reference needs are retrieved and ranked high |
| Context recall | whether retrieval surfaced what the reference answer needs at all |

## What you will do

| Task | What happens |
|---|---|
| 1 | Index the pages in memory and answer with a deliberately small `k` |
| 2 | One question by hand from one chunk, then a RAGAS test set, saved |
| 3 | Answer every generated question with the weak pipeline |
| 4 | Score faithfulness, answer relevancy, context precision, context recall |
| 5 | Raise `k`, score again, save both rows, chart the change |

## Setup

This module has its own environment because RAGAS pins the LangChain 0.3 line and the rest of the repository runs LangChain 1.x.

```bash
cd 08_SDG_RAGAS && uv sync && uv run jupyter lab      # open Improving_RAG_with_RAGAS.ipynb
```

Needs `OPENAI_API_KEY`, `LLM_MODEL`, and `EMBED_MODEL` in the repository `.env`. Optional: `RAGAS_MODEL` for the judges and `SDG_MODEL` for the generator, with `RAGAS_BASE_URL` if they live on another server. Each falls back to `LLM_MODEL`.

## Data files

None in this folder. Reads `corpus` from the workspace, writes `testset` and `ragas_scores`.
