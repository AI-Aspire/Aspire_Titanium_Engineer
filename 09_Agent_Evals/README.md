# Trajectory evals

## Learn | Create | Grow

### Learn
Agent evals as tasks with a goal and a hidden success condition, a simulated user that only reveals what it is asked, and scoring over the whole trajectory rather than the last message.

### Create
Every task run more than once with pass^k, a planted regression to prove the harness catches it, and a capability report written from your own agent's runs.

### Grow
Production agent evals run on every change to the prompt, tools, or retriever, and the capability report is what a release manager reads. Bring your team the worst failure.

**Estimated time:** 45 minutes
**Reads:** corpus, eval_cases
**Writes:** tasks, trajectories, capability_report

## Plain English first

| Term | Meaning |
|---|---|
| Task | a goal for the agent plus a success condition the agent never sees |
| Trajectory | the whole conversation: user turns, tool calls, and replies |
| Simulated user | a model playing a persona that reveals details only when asked |
| pass^k | the chance that all k repeats of a task succeed |
| Planted regression | a deliberate break used to prove the harness can see one |

## What you will do

| Task | What happens |
|---|---|
| 1 | Build the agent under test with one keyword search tool over the corpus |
| 2 | Compose tasks from your eval cases and add two planted ones |
| 3 | Simulate the user and record a full trajectory |
| 4 | Score the trajectory programmatically and with a judge |
| 5 | Run every task k times and compute pass^k |
| 6 | Plant a regression and check the harness catches it |
| 7 | Write the capability report |

## Setup

```bash
make setup
uv run jupyter lab      # open 09_Agent_Evals/Trajectory_Evals.ipynb
```

Needs `OPENAI_API_KEY` and `LLM_MODEL` in `.env`. No embeddings, no vector store.

## Data files

None in this folder. Reads `corpus` and `eval_cases` from the workspace, writes `tasks`, `trajectories`, and `capability_report`.
