# Retrieval ladder

## Learn | Create | Grow

### Learn
A ladder of retrievers on the same questions: dense, BM25 written from scratch, fusion with RRF, a cross-encoder reranker, multi-query. What each rung adds and what it costs.

### Create
Eval cases labelled with the pages that hold the evidence, a scored table of hit rate and MRR per rung over your corpus, and a permission filter that runs inside the query rather than after it.

### Grow
Ship the cheapest rung that clears your bar and write down which question type needs the expensive one. In production the bar is measured on every change, not once.

**Estimated time:** 45 minutes
**Reads:** corpus, vibe_checks
**Writes:** eval_cases, ladder

## Plain English first

| Term | Meaning |
|---|---|
| Dense search | find text with a similar meaning, not necessarily the same words |
| BM25 | find text with the same words, ranked by how rare and how frequent they are |
| RRF | combine two ranked lists by adding `1 / (60 + rank)` from each, no tuning |
| Cross-encoder | a model that reads the question and a candidate together and scores the pair |
| Multi-query | ask the question several ways so one awkward phrasing does not hide the evidence |
| Hit rate | share of questions where any top result came from a labelled page |
| MRR | mean of one over the rank of the first correct result |

## What you will do

| Task | What happens |
|---|---|
| 1 | Label each vibe check with the pages that hold its evidence and save the eval cases |
| 2 | BM25 from scratch, then `rank_bm25`, then dense search over the same chunks |
| 3 | Fuse with RRF, rerank with a cross-encoder, expand the query |
| 4 | Score every rung on hit rate and MRR, chart it, save the ladder |
| 5 | Tag every chunk with a group and compare dropping after ranking with filtering inside the query |

## Before you arrive

- Write five questions your users ask and, for each, name the document that holds the answer; bring the sheet.
- Reciprocal rank fusion: https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf

## Setup

```bash
make setup
uv run jupyter lab      # open 06_Advanced_Retrieval/Retrieval_Ladder.ipynb
```

Needs `OPENAI_API_KEY`, `LLM_MODEL`, and `EMBED_MODEL` in `.env`. The cross-encoder `cross-encoder/ms-marco-MiniLM-L-6-v2` downloads from the Hugging Face hub on first use. Set `COHERE_API_KEY` to add a hosted reranker as an extra rung; it is optional.

## Data files

None in this folder. Reads `corpus` and `vibe_checks` from the workspace, writes `eval_cases` and `ladder`. The vector index is in memory and rebuilt each run.
