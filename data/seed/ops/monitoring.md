# Monitoring

Request path: keyword retrieval over 30 corpus pages plus one call to `unsloth/Qwen3.6-35B-A3B-MTP-GGUF`.

## The four metrics

| metric | current value | where it comes from |
|---|---|---|
| p50 / p95 latency | 33688 ms / 39053 ms | measured: the load test at concurrency 1 |
| cost per request | $0.00112 | lookup: 2240 tokens from one measured request at $0.0005 per 1k tokens |
| refusal rate | 60% | from your trajectories: 5 harness runs, not live traffic |
| eval score on traffic | 100% | from your trajectories: the harness pass rate, not live traffic yet |

## Drift rule

`detect_drift(window=3, tolerance=2.5)` over the daily eval score on sampled traffic.
On a planted 35% drop it fired 1 day(s) after the regression began. Commitment: a drop that size is noticed within about 2 days; a smaller one takes longer or is never seen.

## Load

| concurrency | requests | failed | req/s | p50 ms | p95 ms |
|---|---|---|---|---|---|
| 1 | 2 | 0 | 0.03 | 33688 | 39053 |
| 2 | 4 | 0 | 0.041 | 47351 | 50038 |

From 1 to 2 concurrent callers, throughput moved +37% and p50 latency moved +41%. Past the level where throughput flattens, extra callers buy wait, not work: rate limit before you scale.

## What may be logged

Safe to log: duration, status, token counts, model requested and model served, retrieval hits, question length, eval score.

Not safe: the question, the answer, retrieved section text, names inside any of them.

A redacted span:

```json
{"span": "request", "ms": 54412.2, "status": "ok", "id": "7d52ad30", "parent": null, "question_len": 43}
```
