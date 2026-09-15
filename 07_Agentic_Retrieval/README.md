# DCI vs agentic RAG

## Learn | Create | Grow

### Learn
Two ways for an agent to reach documents: read the pages directly through a model-readable wiki, or call a retriever tool. One loop, two tool sets, and what each one reads.

### Create
A wiki index generated from your corpus, both modes scored over your eval cases, and a table of answer quality, calls, evidence read, and latency per mode.

### Grow
Keep the cheaper mode that passes your questions and write down what kind of question would make you switch. Tell your team one question where the modes diverged.

**Estimated time:** 35 minutes
**Reads:** corpus, eval_cases
**Writes:** wiki, agentic_runs

## Plain English first

| Term | Meaning |
|---|---|
| Wiki | one markdown index of the corpus: page names, what each is for, its sections |
| DCI | direct corpus interaction: the agent lists, searches, and reads pages with file tools |
| Agentic RAG | the agent calls a retriever that returns ranked chunks, and may call it again |
| Trace | the sequence of tool calls a run made, with how much text came back |

## What you will do

| Task | What happens |
|---|---|
| 1 | Build the wiki index from the page headings, with a model-written purpose line per page |
| 2 | Two tool sets: `search_chunks` for RAG; `list_pages`, `grep_wiki`, `read_page` for DCI |
| 3 | One agent loop that logs every call, run on one question both ways |
| 4 | Score every eval case in both modes with your judge and save the runs |
| 5 | Read the summary and the traces, case by case |

## Before you arrive

- Pick one document your product answers from and write its one-line purpose and its section headings by hand; bring the outline.
- 12-factor agents, own your context window: https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md

## Setup

```bash
make setup
uv run jupyter lab      # open 07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb
```

Needs `OPENAI_API_KEY` and `LLM_MODEL` in `.env`. No embeddings; the RAG side uses BM25 so the retriever is local and inspectable.

## Data files

None in this folder. Reads `corpus` and `eval_cases` from the workspace, writes `wiki` and `agentic_runs`.
