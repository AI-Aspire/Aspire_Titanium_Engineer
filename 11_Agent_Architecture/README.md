# Six ways to give an agent a capability

## Learn | Create | Grow

### Learn
One capability six ways: a tool, a skill folder, an MCP server, a sub-agent, a code-mode runtime, a manifest-described API. What reaches the model in each, and what breaks first.

### Create
A catalogue that says when to use each mechanism, written for the one lookup your prototype needs most and saved to your workspace.

### Grow
Production picks a mechanism per capability by ownership, auth, and what enters context. Tell your team, for two mechanisms on one question, the call count and context size.

**Estimated time:** 45 minutes
**Reads:** eval_cases, trajectories
**Writes:** tools_catalog

## Plain English first

| Term | Meaning |
|---|---|
| Tool | a function with a JSON schema that the model may ask your loop to run |
| Skill | a folder with instructions and a script; the harness reads the instructions and runs the script |
| MCP server | a separate process that exposes tools over the Model Context Protocol |
| Sub-agent | a whole separate agent the main agent delegates to |
| Code mode | the model writes a small program; a runtime executes it |
| UTCP | a manifest that describes an API you already run, so a client can call it directly |

## What you will do

| Task | What happens |
|---|---|
| 1 | A tool: the lookup as a function with a schema and a loop |
| 2 | A skill: the same lookup as a folder the harness shells out to |
| 3 | An MCP server: discover the tools from a subprocess and call them |
| 4 | A sub-agent: a coordinator delegates to a trajectory analyst |
| 5 | Code mode: the model writes a program; a validated runtime runs it |
| 6 | UTCP: a manifest describes the API; the client calls it directly |
| 7 | Write the catalogue |

## Setup

```bash
make setup
uv run jupyter lab      # open 11_Agent_Architecture/Six_Ways.ipynb
```

Needs `OPENAI_API_KEY` and `LLM_MODEL` in `.env`, and a model that supports tool calling. Uses the `mcp` package from the root environment.

## Files in this folder

| File | Purpose |
|---|---|
| `eval_lookup.py` | the lookup as plain Python, shared by the server and the skill |
| `mcp_server.py` | the MCP server the notebook launches over stdio |
| `skills/case_lookup/` | the skill: `SKILL.md` plus `run.py` |

To run the server on its own: `uv run python mcp_server.py` from this folder. It must print nothing to stdout except protocol messages.

## Data files

None. Reads `eval_cases` and `trajectories` from the workspace, writes `tools_catalog`.
