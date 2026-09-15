# Observability and incidents

## Learn | Create | Grow

### Learn
A span from scratch and the convention names it maps onto, the four metrics an LLM application needs, a planted quality regression that three of them cannot see, and a drift detector with a stated lag.

### Create
A real load test against your endpoint, the redacted traces of one instrumented request, and a monitoring file with the four metrics, the drift rule, and what may be logged.

### Grow
Production scores sampled traffic through the eval harness, not only latency. Bring your team the detection lag you can promise and the incident you would find out about last.

**Estimated time:** 40 minutes
**Reads:** trajectories, eval_cases, corpus
**Writes:** traces, load_test, monitoring

## Plain English first

| Term | Meaning |
|---|---|
| Span | one timed unit of work with a parent, so timings form a tree |
| p95 latency | the time 95% of requests beat; the mean hides the slow tail |
| Refusal rate | the share of requests the assistant declined |
| Eval score on traffic | your eval harness run over a sample of real requests, the only metric that sees a silent quality drop |
| Drift | a metric moving away from its own history; the detector says how far and how fast |
| Saturation | the concurrency past which more callers add wait, not throughput |

## What you will do

| Task | What happens |
|---|---|
| 1 | Write a `span` context manager, instrument retrieve, generate, and check, and print the tree for one request |
| 2 | Map the generate span onto the OpenTelemetry GenAI attribute names and compare the model asked for with the model that answered |
| 3 | Simulate a week of traffic shaped by your trajectories, plant a quality regression, and chart the four metrics |
| 4 | Write `detect_drift`, see it fire a day late, and state the lag as a commitment |
| 5 | Load test the configured endpoint at rising concurrency and save throughput and latency |
| 6 | Save the redacted traces and write the monitoring file |

## Before you arrive

- Time ten requests to your model endpoint with curl and note the slowest one, not the average.
- OpenTelemetry GenAI semantic conventions: https://github.com/open-telemetry/semantic-conventions-genai

## Setup

```bash
make setup
uv run jupyter lab      # open 22_Observability/Observability_and_Incidents.ipynb
```

Needs `OPENAI_API_KEY` and `LLM_MODEL` in `.env`. No embeddings, no vector store. The load test sends a few dozen short requests at rising concurrency to that endpoint, so do not point it at shared infrastructure without asking.

## Data files

None in this folder. Reads `trajectories`, `eval_cases`, and `corpus` from the workspace, writes `traces`, `load_test`, and `monitoring`.
