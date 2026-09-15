# RAG with LangChain

## Learn | Create | Grow

### Learn
The retrieval gap, what pasting the whole corpus costs per call, then retrieval as three moves: embed, find the nearest chunks, paste them in. From scratch in thirty lines, rebuilt with a splitter, an embeddings endpoint, and a vector store.

### Create
A corpus rendered from your charter, prompts, transcripts, and vibe checks, indexed locally, and a baseline answer saved for every vibe check.

### Grow
Production retrieval means structure-aware chunking, incremental re-indexing, hybrid search, and faithfulness checks in CI. Show your team the vibe check that retrieval fixed.

**Estimated time:** 35 minutes
**Reads:** charter, prompts, transcripts, vibe_checks
**Writes:** corpus, baseline_runs

## Plain English first

| Term | Meaning |
|---|---|
| Corpus | the markdown pages rendered from your charter, prompts, transcripts, and vibe checks |
| Chunk | a slice of a page small enough to embed and retrieve on its own |
| Embedding | a vector that puts texts with similar meaning close together |
| Retriever | the piece that turns a question into the chunks closest to it |
| Chain | question to retriever to prompt to model to text, in one call |

## What you will do

| Task | What happens |
|---|---|
| 1 | Ask one vibe check with no source text and see the gap |
| 2 | Paste the whole corpus into the prompt, time the first token, and see what ordering does to a prefix cache |
| 3 | RAG from scratch: chunk, embed, rank by cosine, paste into the prompt |
| 4 | The same pipeline in LangChain with a splitter, embeddings, and local Qdrant |
| 5 | Wire it into a chain and answer the same question from the corpus |
| 6 | Change `k` and compare two answers to one question |
| 7 | Answer every vibe check and save the baseline runs with their contexts |

## Before you arrive

- Collect ten pages of the documents your product would answer from, as markdown or plain text, and bring the folder.
- Retrieval-augmented generation: https://arxiv.org/abs/2005.11401

## Setup

```bash
make setup
uv run jupyter lab      # open 05_RAG/RAG_with_LangChain.ipynb
```

Needs `OPENAI_API_KEY`, `LLM_MODEL`, and `EMBED_MODEL` in `.env`. The index is an embedded Qdrant folder at the repository root, `.qdrant_local/`, which later notebooks reuse. It is single-writer: shut down this kernel before another notebook opens it.

## Data files

None in this folder. Reads `charter`, `prompts`, `transcripts`, and `vibe_checks` from the workspace, writes `corpus` and `baseline_runs`.
