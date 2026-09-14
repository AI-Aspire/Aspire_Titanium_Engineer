# Release decision: HOLD

Model `unsloth/Qwen3.6-35B-A3B-MTP-GGUF`, 2 eval cases, three DeepEval metrics per case, bar 80% of cases passing every metric.

| version | pass rate | failing tests |
|---|---|---|
| v1 | 0% | v01, v02 |
| v2 | 50% | v01 |

Judge errors: 0

## Why

Hold because v2 pass rate 50% is under the bar of 80%.

## Failing metrics on v2

- v01 correctness 0.4: The response correctly identifies the routing setting and offers to open a ticket as required. However, it omits the specific menu path needed to locate this setting, which is a direct requirement in the expected output that would change how the user proceeds. While the additional [...]