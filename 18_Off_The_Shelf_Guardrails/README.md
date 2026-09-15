# Off-the-shelf guardrails

## Learn | Create | Grow

### Learn
Library guardrails on an SDK agent: scope and prompt-injection checks on input, PII redaction as a transform, unsupported-claim and tone checks on output. What each is good for.

### Create
Every guardrail run over your case set, results per case per guardrail, and a decision about which fail closed, which warn, and which are too brittle to keep.

### Grow
Say what each guardrail stops and what it does not. Tell your team which case tripped a guardrail you did not expect and which attack walked through.

**Estimated time:** 35 minutes
**Reads:** guardrail_cases, corpus
**Writes:** ots_results

## Plain English first

| Term | Meaning |
|---|---|
| Input guardrail | a check on the request before the model runs |
| Output guardrail | a check on the answer before the user sees it |
| Transform | a rewrite of the request that lets it through, such as redaction |
| Tripwire | the flag that stops the run and raises a typed exception |
| Fail closed | block when the check fires; fail open means warn and continue |

## What you will do

| Task | What happens |
|---|---|
| 1 | One lookup tool over the corpus; read the cases |
| 2 | Scope and prompt-injection input guardrails |
| 3 | PII redaction as a transform |
| 4 | Unsupported-claim and tone output guardrails |
| 5 | Wire the protected agent and run four cases |
| 6 | Force the output tripwires with two unsafe demo agents |
| 7 | Run every case and save the matrix |

## Before you arrive

- List the kinds of personal data your users might paste into a question, with one made-up example of each; bring the list.
- Guardrails in the OpenAI Agents SDK: https://openai.github.io/openai-agents-python/guardrails/

## Setup

```bash
make setup
uv run jupyter lab      # open 18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb
```

Needs `OPENAI_API_KEY` and `LLM_MODEL` in `.env`. With `OPENAI_BASE_URL` set, the SDK uses the chat completions API; against api.openai.com it uses the responses API.

## Data files

None in this folder. Reads `guardrail_cases` and `corpus` from the workspace, writes `ots_results`.
