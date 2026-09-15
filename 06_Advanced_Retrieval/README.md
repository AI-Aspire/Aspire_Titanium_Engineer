# Retrieval ladder

## Learn | Create | Grow

### Learn
Compare dense search, BM25, reciprocal rank fusion, reranking, and query expansion on the same chunks and questions.

### Create
Review evidence labels, measure hit rate and MRR, and inspect which questions separate the retrievers.

### Grow
Choose retrieval settings using evidence about quality and latency.

**Estimated time:** 40 minutes

## Interactive lesson

Open `Retrieval_Ladder.ipynb` alongside your coding assistant. Ask it to run the repository tools and explain the actual results. Tools are enabled for this lesson. You do not need to type Python or shell commands yourself.

`retrieval_tools.py` contains the experiment code extracted from the original notebook. Read it to inspect BM25, RRF, reranking, query expansion, and scoring. `Retrieval_Ladder.py` is the generated marimo mirror of the conversation guide, not the experiment implementation.

Use `make setup` for the shared environment. BM25 works without a model key; dense retrieval needs configured embeddings, labelling and query expansion need the chat model, and the local cross-encoder downloads on first use. These tools read `.env`; the model serving your coding assistant is separate from the experiment models. Optional Cohere reranking needs `COHERE_API_KEY`.

Product documentation: [Codex](https://developers.openai.com/codex/), [Claude Code](https://code.claude.com/docs/en/overview), [VS Code Copilot](https://code.visualstudio.com/docs/agents/overview).

## Tool reference for your assistant

Run from this directory with the shared environment: `uv run --no-sync python retrieval_tools.py COMMAND`. Use `--help` for arguments. Each invocation returns one JSON result on stdout; progress and workspace notices go to stderr.

| Command | Result |
|---|---|
| `inspect` | Corpus source, page names, and short digests |
| `inspect --page NAME` | The full text of a specific eligible corpus page |
| `cases` | Existing eval questions and their page labels |
| `label` | Model-proposed labels from vibe checks, requiring human review |
| `compare --question TEXT` | Ranked chunks from each rung, timings, scratch BM25, and intermediate candidates/rewrites |
| `score` | Aggregate scores, per-case results, skipped cases, and provenance |

Select rungs with `--rungs bm25 dense`, or all five by default. Optional `cohere_rerank` must be requested explicitly. Adjust `--k`, `--candidates`, `--chunk-size`, and `--overlap` for controlled experiments.

`--cases FILE` reads a JSON list with `id`, `question`, `reference`, and `pages` per case. Use it for labels the student reviewed or a question the student wrote. Keep temporary case files outside `workspace/`; do not invent labels or change them to make a retriever win.

For `score`, `--save` writes the cases actually used and measured ladder through `helpers.workspace`. No conversation export is required. Save only when the user asks to persist the experiment. Without this flag, experiments do not change workspace artifacts.

## Measurement boundaries

All rungs share chunks, labels, and top-k. The index excludes the wiki and `vibe_checks.md`. Cases with no labelled evidence are listed as skipped; the tool rejects unknown page labels and an empty scored set. A labelled policy page can still be relevant to an out-of-scope question.

Model loading and index construction are reported separately from search time. Search time includes query embeddings and query expansion where used. One sequential run is not a stable latency benchmark. The scratch BM25 and library version use different IDF formulas, so matching tokenization does not guarantee identical rankings.

Inputs come from the workspace when valid, otherwise the seed. Inspect the reported sources before interpreting results. The committed example results, when present, are recordings of actual tool runs, not claims about every corpus.
