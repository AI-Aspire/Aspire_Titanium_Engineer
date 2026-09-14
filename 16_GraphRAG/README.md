# GraphRAG

ℹ This module needs the `graph` dependency group. Run `make setup-graph` once before opening the notebook; it installs spaCy, its small English model, networkx, and rdflib.

## Learn | Create | Grow

### Learn
When a graph earns its cost: the multi-hop hypothesis, a steelman vector baseline, and three ways to build a graph over the same pages, with spaCy, an ontology, and the model.

### Create
A graph over your corpus and trajectories, an answer path from its neighbourhood, a scored comparison on your eval cases, and both saved.

### Grow
Decide from the numbers whether the graph earns its build cost. Bring your team the table, not the feeling.

**Estimated time:** 50 minutes
**Reads:** corpus, trajectories, eval_cases
**Writes:** graph, graph_eval

## Plain English first

| Term | Meaning |
|---|---|
| Triple | subject, relation, object: one fact with the page it came from |
| Knowledge graph | every triple as an edge between two named nodes |
| Entity linking | finding the nodes a question is about |
| k-hop subgraph | every node within k edges of those entry nodes |
| Steelman baseline | the strongest vector retriever you can build, so the graph is measured fairly |
| Reference recall | the share of the reference answer's key terms present in what was retrieved |

## What you will do

| Task | What happens |
|---|---|
| 1 | Load pages and trajectories, split them into semantic chunks |
| 2 | Build the hybrid baseline: dense, BM25, cross-encoder rerank |
| 3 | Build the graph with spaCy and with a hand-written ontology; view it as RDF |
| 4 | Build the graph with the model; compare the three schemas |
| 5 | Answer from the graph neighbourhood and from the baseline |
| 6 | Measure both on your eval cases |
| 7 | Save the best graph and the scores |

## Setup

```bash
make setup-graph
uv run jupyter lab      # open 16_GraphRAG/GraphRAG.ipynb
```

Needs `OPENAI_API_KEY`, `LLM_MODEL`, `EMBED_MODEL`, and optionally `EMBED_BASE_URL` in `.env`. The cross-encoder reranker downloads once; without it the baseline ranks by dense score and says so. Everything is computed in memory; no embedding cache is written.

## Data files

None in this folder. Reads `corpus`, `trajectories`, and `eval_cases` from the workspace, writes `graph` and `graph_eval`.
