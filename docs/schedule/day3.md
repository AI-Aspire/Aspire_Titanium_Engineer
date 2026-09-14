# Day 3: agents in practice

*Ends with:* four-minute pitches per group: the agent, its memory, how each
capability is called, and the guardrail cases it must pass.

## Goals

- Engineering: memory, six ways to call a capability, multi-agent, a guardrail ladder
- Group: an agent over the group's corpus with a final infrastructure diagram and a first guardrail

## Modules

| # | Module | Demo | Reads | Writes |
|---|---|---|---|---|
| 10 | Agent memory | 30 min | trajectories | memory, episodes |
| 11 | Agent architecture | 35 min | eval_cases, trajectories | tools_catalog |
| 12 | Multi-agent | 30 min | capability_report, ragas_scores | multi_agent_report |
| 13 | Guardrails 101 | 30 min | transcripts | guardrail_cases, ladder_results |

## Run of show

| Time | Block | Min | What |
|---|---|---|---|
| 9:00 | 🧑‍🏫 | 15 | Feedback on the demos |
| 9:15 | 🧑‍🏫 | 15 | Memory: what to keep, where |
| 9:30 | 🧑‍💻 | 30 | Module 10: three kinds of memory |
| 10:00 | 🧑‍🤝‍🧑 | 35 | Wire one kind of memory into your agent |
| 10:35 | ☕ | 15 | |
| 10:50 | 🧑‍🏫 | 20 | Six ways to call a function |
| 11:10 | 🧑‍💻 | 35 | Module 11: tool, skill, MCP server, sub-agent |
| 11:45 | 🧑‍🤝‍🧑 | 30 | Pick the mechanism for each capability in your prototype |
| 12:15 | 🍽 | 60 | |
| 1:15 | 🧑‍🏫 | 15 | Multi-agent patterns |
| 1:30 | 🧑‍💻 | 30 | Module 12: a report generator with LangGraph |
| 2:00 | 🧑‍🤝‍🧑 | 30 | Split one job across two agents, or decide not to |
| 2:30 | ☕ | 15 | |
| 2:45 | 🧑‍🏫 | 15 | Guardrails 101 |
| 3:00 | 🧑‍💻 | 30 | Module 13: the guardrail ladder |
| 3:30 | 🧑‍🤝‍🧑 | 45 | Final infrastructure diagram. Guardrail cases. Prepare the pitch |
| 4:15 | 🎤 | 35 | Pitches, four minutes per group |
| 4:50 | 🧑‍🏫 | 10 | Wrap. `make check-day D=3` |

## Reading

- Context engineering in agents: https://docs.langchain.com/oss/python/langchain/context-engineering
- Thinking in LangGraph: https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph
- Model Context Protocol: https://www.anthropic.com/news/model-context-protocol
- Agent skills: https://claude.com/blog/skills
- Effective harnesses for long-running agents: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
