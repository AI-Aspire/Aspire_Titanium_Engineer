# Deployment checklist

30 questions: 7 answered by the repository, 9 partly, 14 unknown. An unknown stays on the list until a person answers it.

## Compute

| # | question | status | answer | source |
|---|---|---|---|---|
| 1 | Where do internal apps run, and who owns that cluster? | unknown |  |  |
| 2 | What does the app need: CPU, memory, a GPU? | answered | requests 250m CPU and 512Mi memory; no GPU, the model runs behind a self-hosted endpoint (OPENAI_BASE_URL is set) | deploy/k8s.yaml |
| 3 | Is the app stateless? | partly | the conversation lives in st.session_state, in the process; two replicas need sticky sessions or a store | project/app/app.py |
| 4 | What is the health endpoint? | answered | /_stcore/health, Streamlit's own route, used by both probes | deploy/k8s.yaml |

## Images

| # | question | status | answer | source |
|---|---|---|---|---|
| 5 | Is there an internal registry, and what is the image called? | partly | registry.example.internal/demo-app:0.1.0 is a placeholder until the registry has a name | deploy/k8s.yaml |
| 6 | Is there a base image you must start from? | unknown |  |  |
| 7 | Must an image be scanned or signed before it may run? | unknown |  |  |

## Identity

| # | question | status | answer | source |
|---|---|---|---|---|
| 8 | How do users authenticate? | partly | the app has no login of its own; a gateway must terminate SSO in front of it and forward the identity | project/app/app.py |
| 9 | Is the service reachable except through the gateway? | unknown |  |  |
| 10 | How does the app authenticate outward, to the model? | answered | an API key read from .env by helpers.config, taken from a Secret on the cluster | helpers/config.py |
| 11 | Is workload identity available, or is it secrets? | unknown |  |  |

## Secrets

| # | question | status | answer | source |
|---|---|---|---|---|
| 12 | Where do secrets live today? | answered | .env at the repository root, loaded by helpers.config | helpers/config.py |
| 13 | Where will they live on the cluster? | answered | the Secret demo-app-secrets, injected with envFrom, never in the image | deploy/k8s.yaml |
| 14 | How are they rotated, and who can read them? | unknown |  |  |

## Network

| # | question | status | answer | source |
|---|---|---|---|---|
| 15 | Can the app reach the internet, and through a proxy? | unknown |  |  |
| 16 | What does the app call? | partly | the model at a self-hosted endpoint (OPENAI_BASE_URL is set); the tools catalog names 3 outward capabilities: mcp_server.py (mcp), ask_trajectory_analyst (sub-agent), eval-lookup-api (utcp) | tools_catalog |
| 17 | What is on the egress allowlist, and who adds to it? | unknown |  |  |
| 18 | Which network is it in, and what can it reach internally? | unknown |  |  |

## Data

| # | question | status | answer | source |
|---|---|---|---|---|
| 19 | What classification may this app process? | unknown |  |  |
| 20 | May data leave the region? | unknown |  |  |
| 21 | How long may prompts and responses be kept? | partly | the workspace already keeps 10 full trajectories with no retention rule | trajectories |
| 22 | Is there a DLP scan on egress? | unknown |  |  |

## Models

| # | question | status | answer | source |
|---|---|---|---|---|
| 23 | Is there an approved internal model endpoint? | partly | today unsloth/Qwen3.6-35B-A3B-MTP-GGUF at a self-hosted endpoint (OPENAI_BASE_URL is set); whether it is approved is a question for the platform team | .env |
| 24 | May you download open weights, and from where? | unknown |  |  |
| 25 | What licence does the model carry, and who signs off on it? | unknown |  |  |

## Legacy

| # | question | status | answer | source |
|---|---|---|---|---|
| 26 | What must this integrate with, and who owns it? | partly | Look up an eval case or a trajectory by id or by question | tools_catalog |
| 27 | Is it real-time or batch? | answered | real-time: 31 tool calls made at request time across 10 trajectories | trajectories |

## Process

| # | question | status | answer | source |
|---|---|---|---|---|
| 28 | Who approves a deployment? | partly | the saved decision says 'Release decision: HOLD'; nobody is named | release_decision |
| 29 | What review gates a deployment? | answered | release_gate.py and check_manifests.py in the Gate step; both exit 1 to stop the job | deploy/deploy.yml |
| 30 | What is the rollback, and who is on call? | partly | kubectl rollout undo to the previous tag in the Deploy step; on call is unknown | deploy/deploy.yml |
