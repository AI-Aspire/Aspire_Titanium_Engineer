# Three kinds of memory

## Learn | Create | Grow

### Learn
Three kinds of memory in one loop: episodic, semantic, working. What each stores, where it lives, the test that catches its failure, and how compaction keeps a budget.

### Create
Episodes written from your trajectories, a long-term store you can read, and a MEMORY.md distilled from your own agent's runs.

### Grow
Production memory is per user, scoped, and forgets on purpose. Show your team one assembled prompt's token breakdown and what was compacted.

**Estimated time:** 45 minutes
**Reads:** trajectories
**Writes:** episodes, memory

## Plain English first

| Term | Meaning |
|---|---|
| Episodic memory | what happened: one summary per agent run, written from the trace |
| Semantic memory | distilled facts in a long-term store, recalled by similarity |
| Working memory | whatever the assembler puts in the prompt this turn |
| Compaction | condensing old turns into a summary while keeping the raw text retrievable |
| Root set | the instructions and the recent turns; never trimmed |

## What you will do

| Task | What happens |
|---|---|
| 1 | See a naive buffer forget between sessions |
| 2 | Write episodes from your trajectories and check them against the trace |
| 3 | Build a markdown long-term store with embedding recall and supersede-on-subject |
| 4 | Assemble working memory under a token budget and read the breakdown |
| 5 | Compact a long session and answer from the summary |
| 6 | Extract facts at session end and recall them in a fresh session |
| 7 | Write MEMORY.md |

## Setup

```bash
make setup
uv run jupyter lab      # open 10_Agent_Memory/Three_Kinds_of_Memory.ipynb
```

Needs `OPENAI_API_KEY`, `LLM_MODEL`, and an embeddings endpoint (`EMBED_MODEL`, and `EMBED_BASE_URL` if it differs) in `.env`. Uses `openai`, `tiktoken`, and `numpy` from the root environment; no vector store.

## Data files

None in this folder. The memory store the notebook writes goes to a temporary directory whose path is printed in the setup cell. Reads `trajectories` from the workspace, writes `episodes` and `memory`.
