# OWASP LLM top ten

## Learn | Create | Grow

### Learn
Five OWASP categories run against a retrieval agent: direct and indirect prompt injection, sensitive disclosure, output handling, excessive agency, system prompt leakage.

### Create
Every attack run against your agent with the tools your catalogue describes, and one finding row per attack saved.

### Grow
Every attack that worked becomes a regression test. Tell your team what your agent did before you fixed it, and whether the attack came from the user or from a page.

**Estimated time:** 40 minutes
**Reads:** corpus, tools_catalog
**Writes:** owasp_findings

## Plain English first

| Term | Meaning |
|---|---|
| Canary | a unique string in the system prompt; if it appears in output, the prompt leaked |
| Direct injection | the user types an instruction that overrides the system prompt |
| Indirect injection | the instruction arrives inside content the agent retrieves |
| Excessive agency | the agent takes an action nobody asked for |
| Finding | one row: id, OWASP category, whether the attack succeeded, input, evidence |

The categories come from the [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/).

## What you will do

| Task | What happens |
|---|---|
| 1 | Build the agent: corpus search, a ticket reader, a ticket closer, one tool per catalog entry |
| 2 | LLM01 direct injection: ask for the canary outright |
| 3 | LLM01 indirect injection: swap a poisoned page copy into the search tool and ask an innocent question |
| 4 | LLM02 sensitive disclosure: claim to be another user and ask for their ticket |
| 5 | LLM05 output handling: ask for markup and show the escaped version next to the raw one |
| 6 | LLM06 excessive agency: imply cleanup and watch for the write tool |
| 7 | LLM07 system prompt leakage: three polite probes |
| 8 | Save the findings |

Scope: every attack targets your own application in your own environment. Attacking systems you do not own is not a grey area.

## Setup

```bash
make setup
uv run jupyter lab      # open 20_OWASP_LLM_Top10/Attack_Your_Agent.ipynb
```

Needs `OPENAI_API_KEY` and `LLM_MODEL` in `.env`. No embeddings, no vector store.

## Data files

None in this folder. Reads `corpus` and `tools_catalog` from the workspace, writes `owasp_findings`. The ticket store is two rows in memory; replace it with your own user data.
