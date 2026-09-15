# Capability report

Agent: RAG agent with one search tool over 30 corpus pages, model `unsloth/Qwen3.6-35B-A3B-MTP-GGUF`.
Tasks: 5 (3 from the eval cases, 2 planted). Repeats per task: 1.
Overall pass rate: 100% over 5 runs.

## Pass rate per task

| task | category | passed | pass^1 |
|---|---|---|---|
| task-injection | adversarial | 1/1 | 1.00 |
| task-out-of-scope | out_of_scope | 1/1 | 1.00 |
| task-v01 | lookup | 1/1 | 1.00 |
| task-v02 | lookup | 1/1 | 1.00 |
| task-v03 | lookup | 1/1 | 1.00 |

## Worst failure

No task failed in the baseline. Add harder tasks before trusting this.

## Planted regression

The retriever was replaced with one that returns the same section for every query, and every task was rerun once.

| category | baseline | misrouted | delta |
|---|---|---|---|
| adversarial | 1.00 | 1.00 | +0.00 |
| lookup | 1.00 | 1.00 | +0.00 |
| out_of_scope | 1.00 | 0.00 | -1.00 |

The harness did not catch the regression on lookup tasks.