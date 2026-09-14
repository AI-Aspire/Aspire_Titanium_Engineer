# Release decision: HOLD

Model `unsloth/Qwen3.6-35B-A3B-MTP-GGUF`, 2 eval cases, three DeepEval metrics per case, bar 80% of cases passing every metric.

| version | pass rate | failing tests |
|---|---|---|
| v1 | 50% | v01 |
| v2 | 0% | v01, v02 |

Judge errors: 0

## Why

Hold because v2 pass rate 0% is under the bar of 80%; v2 scores below v1.

## Failing metrics on v2

- v01 correctness 0.4: The response identifies a routing setting ('split tunnel settings') and offers to open a ticket, satisfying parts of the expected output. However, it omits the required 'menu path' specified in the test case parameters. This failure to include the menu path violates Step 2 and Step 3, which [...]
- v02 correctness 0.0: The actual output completely fails to address the expected requirements, as it does not name the entitlement, identify the approver, or state the expected wait time. Instead, it merely states that the instructions are missing from the provided pages, resulting in a total omission of the [...]