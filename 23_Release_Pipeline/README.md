# Release pipeline

## Learn | Create | Grow

### Learn
A release gate as one line in a pipeline, the eight properties of a manifest a platform team greps for, and why a canary at forty samples cannot tell an improvement from luck.

### Create
The gate, the manifest check, and the canary verdict run on your own eval results and written to the workspace, then an authorisation check over your corpus and a deployment checklist with the unknowns marked.

### Grow
A deployment is a conversation with whoever runs the platform. Bring them the manifest and the checklist, and ask what is wrong with them.

**Estimated time:** 40 minutes
**Reads:** deepeval_results, release_decision, eval_cases, trajectories, tools_catalog, corpus
**Writes:** eval_gate, canary_verdict, deploy_checklist

## Plain English first

| Term | Meaning |
|---|---|
| Release gate | a script that reads the eval results and exits non-zero when a metric is under its bar |
| Manifest | the file that tells a cluster how to run the app, and what a security review reads first |
| Canary | a small share of real traffic sent to the new version before the rest |
| Shadow | the new version answers every request but nobody sees its answers |
| Two-proportion interval | the range the difference between two pass rates could really be, given how few samples you have |
| Authorisation | whether this user may read this document, decided before ranking, never after |

## What you will do

| Task | What happens |
|---|---|
| 1 | Compute a pass rate per metric and see the average that hides a failure |
| 2 | Run the same gate as a script and find the one line in the pipeline that calls it |
| 3 | Read a manifest a security review can accept, break one property, watch the check fail |
| 4 | Compare rolling, canary, and shadow, then write a verdict that refuses to promote on noise |
| 5 | Decide who may read what before retrieval, and see why filtering afterwards leaks |
| 6 | Fill the deployment checklist from what the repository already answers, and mark the rest unknown |

## Setup

```bash
make setup
uv run jupyter lab      # open 23_Release_Pipeline/Release_Pipeline.ipynb
```

Runs offline: no model calls. Needs the eval results and release decision in the workspace or the seed.

## Data files

`deploy/k8s.yaml` and `deploy/deploy.yml` are the manifest and the pipeline the notebook reads and checks. Two repository scripts do the checking: `scripts/release_gate.py` and `scripts/check_manifests.py`.
