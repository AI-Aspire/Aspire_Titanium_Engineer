# Day 4: advanced prototyping, instructors' pick

*Ends with:* no pitches. Every group runs the modules the instructors chose
and decides, per technique, whether it earns a place in the prototype.

The instructors pick from the menu below, usually four modules, based on what
the cohort's projects need. Anything not picked stays available on day 5.

## Goals

- Engineering: the techniques the cohort's prototypes call for, each measured before it is adopted
- Product: product-market fit; which of these the users would notice
- Group: a written decision per technique in `project/DECISIONS.md`

## Menu

| # | Module | Demo | Reads | Writes | Pick it when |
|---|---|---|---|---|---|
| 14 | Voice agents | 40 min | capability_report | voice_sessions | users will speak to the product |
| 15 | Prompt optimisation | 35 min | judge_scores, vibe_checks | dspy_program | a prompt is the bottleneck and there is a metric to optimise |
| 16 | GraphRAG | 40 min | corpus, trajectories | graph, graph_eval | questions span entities and relations, not passages |
| 17 | Deep research | 35 min | capability_report | research_report | answers need many sources and a report, not a reply |
| 18 | Off-the-shelf guardrails | 30 min | guardrail_cases | ots_results | the ladder from day 3 is going to production |
| 19 | Responsible AI | 25 min | everything | risk_register | the prototype will face a review board |
| 20 | OWASP LLM top 10 | 35 min | corpus, tools_catalog | owasp_findings | the agent has tools and reads untrusted text |
| 21 | DeepEval | 35 min | eval_cases, trajectories | deepeval_results, release_decision | a release decision is due |
| 22 | Observability and incidents | 40 min | trajectories, eval_cases, corpus | traces, load_test, monitoring | someone will have to run it and be woken by it |
| 23 | Release pipeline | 40 min | deepeval_results, eval_cases, trajectories, tools_catalog | eval_gate, canary_verdict, deploy_checklist | it is going anywhere near production |

Modules 19 to 23 are the release-readiness set. Pick from them when a
cohort is heading for a demo or a pilot; 22 and 23 are what running it for
real needs.

## Shape of the day

Each slot is a short lecture and one module from the menu, followed by group
time to decide where it fits.

| Time | Block | Min | What |
|---|---|---|---|
| 9:00 | 🧑‍🏫 | 15 | How to assess a technique in an hour |
| 9:15 | 🧑‍🏫 🧑‍💻 | 60 | Slot one: lecture and module |
| 10:15 | 🧑‍🤝‍🧑 | 20 | Where it fits, if anywhere |
| 10:35 | ☕ | 15 | |
| 10:50 | 🧑‍🏫 🧑‍💻 | 60 | Slot two: lecture and module |
| 11:50 | 🧑‍🤝‍🧑 | 25 | Where it fits, if anywhere |
| 12:15 | 🍽 | 60 | |
| 1:15 | 🧑‍🏫 🧑‍💻 | 60 | Slot three: lecture and module |
| 2:15 | 🧑‍🤝‍🧑 | 20 | Where it fits, if anywhere |
| 2:35 | ☕ | 15 | |
| 2:50 | 🧑‍🏫 🧑‍💻 | 60 | Slot four: lecture and module |
| 3:50 | 🧑‍🤝‍🧑 | 55 | Product-market fit check. Decisions in `project/DECISIONS.md`. Build |
| 4:45 | 🧑‍🏫 | 15 | What day 5 offers. Wrap. `make check-day D=4` |

## Reading

- DSPy: https://arxiv.org/abs/2310.03714
- How we built our multi-agent research system: https://www.anthropic.com/engineering/multi-agent-research-system
- The AI guardrails index: https://www.guardrailsai.com/blog/introducing-the-ai-guardrails-index
- NIST AI risk management framework: https://www.nist.gov/itl/ai-risk-management-framework
- OWASP top 10 for LLM applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- DeepEval: https://docs.confident-ai.com
- The product-market fit framework: https://pmarchive.com/guide_to_startups_part4.html
