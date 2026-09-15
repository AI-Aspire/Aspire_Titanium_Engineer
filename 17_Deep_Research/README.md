# Unroll deep research

## Learn | Create | Grow

### Learn
Deep research unrolled into six nodes: clarify, brief, plan, research, compress, write. Typed contracts between them and a trace you can read.

### Create
A report on the top failure mode in your capability report, researched over your corpus with optional web search, and saved with its trace.

### Grow
In production the trace is how you defend the report. Tell your team which boundary did the most work and one gap the report admitted.

**Estimated time:** 35 minutes
**Reads:** capability_report, corpus
**Writes:** research_report

## Plain English first

| Term | Meaning |
|---|---|
| Brief | the question rewritten as a target with success criteria |
| Plan | independent research tasks, each with a search query |
| Researcher | one task run in isolation: search, extract, reflect, hand over a finding |
| Compression | the findings reduced to a dossier the writer can hold |
| Trace | one event per node, so you can see where the budget went |

## What you will do

| Task | What happens |
|---|---|
| 1 | Derive the question from the top failure mode; define the contracts and budgets |
| 2 | Build the corpus search and extract tools; add Tavily when a key is set |
| 3 | Clarify, brief, and plan nodes |
| 4 | Research and compress nodes |
| 5 | Compile the graph and stream a run |
| 6 | Read the trace and save the report |

## Before you arrive

- Write down the one failure of your assistant you would most like explained, and the three sources you would check first.
- Open deep research: https://www.langchain.com/blog/open-deep-research

## Setup

```bash
make setup
uv run jupyter lab      # open 17_Deep_Research/Unroll_Deep_Research.ipynb
```

Needs `OPENAI_API_KEY` and `LLM_MODEL` in `.env`. `TAVILY_API_KEY` is optional; without it the researchers read only your corpus.

## Data files

None in this folder. Reads `capability_report` and `corpus` from the workspace, writes `research_report`.
