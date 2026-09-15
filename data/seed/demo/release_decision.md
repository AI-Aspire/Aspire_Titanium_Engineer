# Release decision: HOLD

Model `unsloth/Qwen3.6-35B-A3B-MTP-GGUF`, 2 eval cases, case set `6c8177c751fd`, three DeepEval metrics per case.

| version | pass rate | failing tests |
|---|---|---|
| v1 | 50% | v01 |
| v2 | 0% | v01, v02 |

## Gate on v2, mean score per metric

| metric | minimum | v1 | v2 | delta | gate |
|---|---|---|---|---|---|
| answer_relevancy | 0.70 | 1.00 | 1.00 | +0.00 | pass |
| faithfulness | 0.80 | 1.00 | 1.00 | +0.00 | pass |
| correctness | 0.70 | 0.60 | 0.25 | -0.35 | FAIL |

Gate: failed on correctness. Comparison v1 to v2: same case set. Judge errors: 0.

## Why

Hold because the gate failed on correctness; v2 regressed on correctness by more than 0.05.

## Failing metrics on v2

- v01 correctness 0.5: The response correctly identifies the routing setting ('split tunneling') and offers to open a ticket, satisfying parts of the expected output. However, it fails to provide the specific menu path for accessing these settings, which is explicitly required by the expected output. This omission [...]
- v02 correctness 0.0: The actual output fails to provide the entitlement name, approver, or expected wait time as required by the expected output. Instead, it explicitly states that the information is missing from the provided pages, resulting in a complete failure to meet the evaluation criteria.