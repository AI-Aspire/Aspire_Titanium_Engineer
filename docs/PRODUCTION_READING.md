# Production reading

The five days cover prototyping through a release decision. What comes after,
running a model in production, is covered by *LLMs in Production* (Brousseau
and Sharp, Manning, 2025). The companion code is at
https://github.com/IMJONEZZ/LLMs-in-Production. These chapters pick up where
the course leaves off.

| Topic | Where | Why it matters after the course |
|---|---|---|
| Quantisation and low-rank approximation | chapter 3 | the model that fits the box you have |
| Serving, streaming, flow control | chapter 6 | the endpoint your prototype calls in production |
| Rate limiting and API keys | chapter 6 | what stops one user from taking the service down |
| Rolling updates on Kubernetes | chapter 6 | shipping a new model without downtime |
| Load testing with Locust | chapter 6 | knowing the ceiling before users find it |
| Drift and monitoring with whylogs | chapter 6 | noticing when the corpus and the questions change |
| LoRA, distillation, mixture of experts | chapter 5 | when prompting and retrieval are not enough |
| Speculative decoding, cached embeddings | chapter 12 | latency and cost at scale |
