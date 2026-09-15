# Agents 101

## Learn | Create | Grow

### Learn
What an agent is: a model with a job description, a toolbox, a budget, and a trace. Tools are a contract of name, docstring, and schema. The loop, built with one call.

### Create
Four questions derived from your charter, run through the agent with middleware that logs and limits calls, and the conversations saved as transcripts for the judge to score.

### Grow
A production harness adds a tool catalogue with auth and audit, persistent traces, and quotas. Tell your team which question called a tool, which did not, and what the trace revealed.

**Estimated time:** 35 minutes
**Reads:** charter, prompts
**Writes:** transcripts

## Plain English first

| Term | Meaning |
|---|---|
| Agent | a model loop that can decide to call tools before answering |
| Tool | a function the model is allowed to ask your system to run |
| Harness | the model, its instructions, its tools, its limits, and its trace |
| Middleware | code around the loop for logging, limits, retries, or guardrails |
| Trace | the step-by-step record of model messages and tool calls |

## What you will do

| Task | What happens |
|---|---|
| 1 | Three tools: search the charter, search earlier prompt outputs, log a request |
| 2 | Build the loop with a system prompt that names each tool |
| 3 | Derive four questions from your charter and run the agent on each |
| 4 | Stream one run and read the trace |
| 5 | Add logging and a model-call limit |
| 6 | Save the transcripts |

## Before you arrive

- List the three lookups your assistant would need to answer real questions, with a one-line description of each; bring the list.
- Building effective agents: https://www.anthropic.com/engineering/building-effective-agents

## Setup

```bash
make setup
uv run jupyter lab      # open 03_Agents_101/Agent_Harness.ipynb
```

Needs `OPENAI_API_KEY` and `LLM_MODEL` in `.env`. No embeddings, no vector store.

## Data files

None in this folder. Reads `charter` and `prompts` from the workspace, writes `transcripts`.
