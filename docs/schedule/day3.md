# Day 3: agents in practice

*Ends with:* four-minute pitches per group: the agent, its harness, its
capability report, and the guardrail cases it must pass.

## Goals

- Engineering: agent evals from simulated trajectories, memory, six ways to call a capability, multi-agent, a guardrail ladder
- Group: an agent over the group's corpus with a capability report and a first guardrail

## Modules

| # | Module | Demo | Reads | Writes |
|---|---|---|---|---|
| 09 | Agent evals | 35 min | corpus, eval_cases | tasks, trajectories, capability_report |
| 10 | Agent memory | 30 min | trajectories | memory, episodes |
| 11 | Agent architecture | 35 min | eval_cases, trajectories | tools_catalog |
| 12 | Multi-agent | 30 min | capability_report, ragas_scores | multi_agent_report |
| 13 | Guardrails 101 | 30 min | transcripts | guardrail_cases, ladder_results |

## Run of show

| Time | Block | Min | What |
|---|---|---|---|
| 9:00 | 🧑‍🏫 | 15 | Feedback on the demos |
| 9:15 | 🧑‍🏫 | 20 | Agent evals: tasks, trajectories, pass rates |
| 9:35 | 🧑‍💻 | 35 | Module 09: simulate and score trajectories |
| 10:10 | 🧑‍🤝‍🧑 | 30 | Write three scenarios. Run the harness |
| 10:40 | ☕ | 15 | |
| 10:55 | 🧑‍🏫 | 15 | Memory: what to keep, where |
| 11:10 | 🧑‍💻 | 30 | Module 10: three kinds of memory |
| 11:40 | 🧑‍🤝‍🧑 | 35 | Wire one kind of memory into your agent |
| 12:15 | 🍽 | 60 | |
| 1:15 | 🧑‍🏫 | 20 | Six ways to call a function |
| 1:35 | 🧑‍💻 | 35 | Module 11: tool, skill, MCP server, sub-agent |
| 2:10 | 🧑‍🏫 | 15 | Multi-agent patterns |
| 2:25 | 🧑‍💻 | 30 | Module 12: a report generator with LangGraph |
| 2:55 | ☕ | 15 | |
| 3:10 | 🧑‍🏫 | 15 | Guardrails 101 |
| 3:25 | 🧑‍💻 | 30 | Module 13: the guardrail ladder |
| 3:55 | 🧑‍🤝‍🧑 | 30 | Final infrastructure diagram. Guardrail cases |
| 4:25 | 🎤 | 30 | Pitches, four minutes per group |
| 4:55 | 🧑‍🏫 | 5 | Wrap. `make check-day D=3` |

## Reading

- Context engineering in agents: https://docs.langchain.com/oss/python/langchain/context-engineering
- Thinking in LangGraph: https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph
- Model Context Protocol: https://www.anthropic.com/news/model-context-protocol
- Agent skills: https://claude.com/blog/skills
- Effective harnesses for long-running agents: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
