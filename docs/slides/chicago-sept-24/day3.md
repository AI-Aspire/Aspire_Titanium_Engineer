---
marp: true
theme: default
paginate: true
size: 16:9
---
# A useful answer is not enough

`goal → user turns → tool calls → observations → final state`

- A helpdesk answer can sound right and still take the wrong path
- Evaluate the complete trajectory, not only the final sentence

<!--
Slide ID: D3-M09-C1
Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: A useful answer is not enough
- Ask: What evidence would a final answer hide that the trajectory exposes?
- Watch: Run the notebook’s first agent-under-test cell; observe the section count, search_kb call, and answer naming a section.
- Then: Carry the observation into the next exercise.
Sources: [ReAct paper](https://arxiv.org/abs/2210.03629); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)
-->
---
# A useful answer is not enough · The practical check

- **Ask:** What evidence would a final answer hide that the trajectory exposes?
- **Inspect:** Run the notebook’s first agent-under-test cell; observe the section count, search_kb call, and answer naming a section.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M09-C1B
Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: A useful answer is not enough
- Ask: What evidence would a final answer hide that the trajectory exposes?
- Watch: Run the notebook’s first agent-under-test cell; observe the section count, search_kb call, and answer naming a section.
- Then: Carry the observation into the notebook exercise.
Sources: [ReAct paper](https://arxiv.org/abs/2210.03629); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)
-->
---
# Turn a prompt into a testable task

- Hide the success condition from the agent
- Simulate the user’s missing details and patience
- Use deterministic checks for exact facts and judged criteria for meaning
- Score facts, actions, and policy—not just prose

<!--
Slide ID: D3-M09-C2
Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: Turn a prompt into a testable task
- Ask: Which requirement should be deterministic for the VPN task, and which needs judgment?
- Watch: Inspect one generated task row; observe its category, opening, facts, and hidden success condition.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [OpenAI evals build guide](https://github.com/openai/evals/blob/main/docs/build-eval.md); [OpenAI graders reference](https://platform.openai.com/docs/api-reference/graders); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)
-->
---
# Turn a prompt into a testable task · The practical check

- **Ask:** Which requirement should be deterministic for the VPN task, and which needs judgment?
- **Inspect:** Inspect one generated task row; observe its category, opening, facts, and hidden success condition.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M09-C2B
Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes:
- Say: Turn a prompt into a testable task
- Ask: Which requirement should be deterministic for the VPN task, and which needs judgment?
- Watch: Inspect one generated task row; observe its category, opening, facts, and hidden success condition.
- Then: Carry the observation into the notebook exercise.
Sources: [OpenAI evals build guide](https://github.com/openai/evals/blob/main/docs/build-eval.md); [OpenAI graders reference](https://platform.openai.com/docs/api-reference/graders); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)
-->
---
# Reliability lives across runs

- One run is a sample, not a reliability claim
- Use pass rate and pass^k for repeated tasks
- Compare the shape of failures across repeated runs
- Plant a regression and verify the harness moves

<!--
Slide ID: D3-M09-C3
Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: Reliability lives across runs
- Ask: Why can pass^k be much lower than pass rate without either metric being wrong?
- Watch: Run repeated tasks and the planted regression; compare lookup-category movement with out-of-scope and injection categories.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [$\tau$-bench](https://arxiv.org/abs/2406.12045); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)
-->
---
# Reliability lives across runs · The practical check

- **Ask:** Why can pass^k be much lower than pass rate without either metric being wrong?
- **Inspect:** Run repeated tasks and the planted regression; compare lookup-category movement with out-of-scope and injection categories.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M09-C3B
Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: Reliability lives across runs
- Ask: Why can pass^k be much lower than pass rate without either metric being wrong?
- Watch: Run repeated tasks and the planted regression; compare lookup-category movement with out-of-scope and injection categories.
- Then: Carry the observation into the notebook exercise.
Sources: [$\tau$-bench](https://arxiv.org/abs/2406.12045); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)
-->
---
# Stop on evidence, not confidence

- Keep the worst trace beside the score
- Gate changes to prompts, tools, and retrieval
- A score without the trace can hide the first incorrect step
- Stop when coverage and known-failure bars are met

> “If you are not running repeated evals on your agents, you are not measuring behavior—you are observing randomness.” — SoyPete Tech

<!--
Slide ID: D3-M09-C4
Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes:
- Say: Stop on evidence, not confidence
- Ask: What must be reproducible before you call an agent change ready to ship?
- Watch: Read the printed capability report and locate the worst failure and planted-regression result.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [OpenAI evals](https://evals.openai.com/); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)
-->
---
# Stop on evidence, not confidence · The practical check

- **Ask:** What must be reproducible before you call an agent change ready to ship?
- **Inspect:** Read the printed capability report and locate the worst failure and planted-regression result.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M09-C4B
Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes:
- Say: Stop on evidence, not confidence
- Ask: What must be reproducible before you call an agent change ready to ship?
- Watch: Read the printed capability report and locate the worst failure and planted-regression result.
- Then: Carry the observation into the notebook exercise.
Sources: [OpenAI evals](https://evals.openai.com/); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)
-->
---
# Research: from traces to state

- ReAct made tool interaction part of the task
- τ-bench evaluates user, policy, tools, and end state
- Open question: does the oracle match support reality?

<!--
Slide ID: D3-M09-R1
Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
Instructor: Eli
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes:
- Say: Research: from traces to state
- Ask: What does tau-bench add beyond checking the agent’s final sentence?
- Watch: Compare the notebook’s current text/fact checks with its Grow suggestion to assert external state.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [ReAct](https://arxiv.org/abs/2210.03629); [$\tau$-bench](https://arxiv.org/abs/2406.12045); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)
-->
---
# Memory is restored context

- The model call ends; the harness can persist state
- Useful memory improves continuity across sessions
- Memory is selected context, not a hidden model faculty
- Wrong memory creates confident, stale answers

<!--
Slide ID: D3-M10-C1
Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 05 Two column
Speaker notes:
- Say: Memory is restored context
- Ask: Where does the remembered Mac fact live between the two model calls?
- Watch: Run the naive memory demonstration; observe the same-session answer versus the fresh-session “I do not know.”
- Then: The harness must choose what to persist and what to place back into the next prompt.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Memory is restored context · The practical check

- **Ask:** Where does the remembered Mac fact live between the two model calls?
- **Inspect:** Run the naive memory demonstration; observe the same-session answer versus the fresh-session “I do not know.”
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M10-C1B
Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: Memory is restored context
- Ask: Where does the remembered Mac fact live between the two model calls?
- Watch: Run the naive memory demonstration; observe the same-session answer versus the fresh-session “I do not know.”
- Then: Carry the observation into the notebook exercise.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Give each memory a job

| Memory | Example | Why it exists |
|---|---|---|
| Procedural | “Ask for the device before reset” | Rules and instructions |
| Semantic | “Finance uses split tunnel” | Durable facts |
| Episodic | “We tried reset yesterday” | What happened |
| Working | “The current error is 401” | What this turn needs |

Every memory needs scope, ownership, and a retention rule.

<!--
Slide ID: D3-M10-C2
Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 04 Icon cards 1
Speaker notes:
- Say: Give each memory a job
- Ask: Which memory type should preserve the tool call that actually ran?
- Watch: Inspect the named output and verify its provenance.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Give each memory a job · The practical check

- **Ask:** Which memory type should preserve the tool call that actually ran?
- **Inspect:** Read the notebook’s three-kind implementation and identify the procedural, semantic, episodic, and working layers in the assembled prompt.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M10-C2B
Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes:
- Say: Give each memory a job
- Ask: Which memory type should preserve the tool call that actually ran?
- Watch: Inspect the named output and verify its provenance.
- Then: Carry the observation into the notebook exercise.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Budget memory deliberately

- Protect instructions and recent turns
- Drop low-relevance recalled facts first
- Compact old turns, but keep raw recovery

<!--
Slide ID: D3-M10-C3
Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 07 Big stats 1
Speaker notes:
- Say: Budget memory deliberately
- Ask: Which tier does the notebook drop first, and which two tiers does it protect?
- Watch: Compare the 6,000- and 120-token breakdowns, then observe compacted=True and raw retrieval of ticket 48213.
- Then: Carry the observation into the next exercise.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Budget memory deliberately · The practical check

- **Ask:** Which tier does the notebook drop first, and which two tiers does it protect?
- **Inspect:** Compare the 6,000- and 120-token breakdowns, then observe compacted=True and raw retrieval of ticket 48213.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M10-C3B
Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: Budget memory deliberately
- Ask: Which tier does the notebook drop first, and which two tiers does it protect?
- Watch: Compare the 6,000- and 120-token breakdowns, then observe compacted=True and raw retrieval of ticket 48213.
- Then: Carry the observation into the notebook exercise.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Remember less, govern better

- Supersede stale facts and delete when required
- Scope memory by user or tenant
- Test truthfulness, staleness, and leakage

<!--
Slide ID: D3-M10-C4
Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: Remember less, govern better
- Ask: What test detects a memory store that leaks one user’s ticket into another user’s session?
- Watch: Run the supersede-on-subject check and the leakage test; observe stale facts being rejected and user stores kept separate.
- Then: Carry the observation into the next exercise.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Remember less, govern better · The practical check

- **Ask:** What test detects a memory store that leaks one user’s ticket into another user’s session?
- **Inspect:** Run the supersede-on-subject check and the leakage test; observe stale facts being rejected and user stores kept separate.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M10-C4B
Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes:
- Say: Remember less, govern better
- Ask: What test detects a memory store that leaks one user’s ticket into another user’s session?
- Watch: Run the supersede-on-subject check and the leakage test; observe stale facts being rejected and user stores kept separate.
- Then: Carry the observation into the notebook exercise.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Research: memory as a managed resource

- Context windows remain a bounded active workspace
- Paging can extend usable history without erasing raw evidence
- Open question: how should privacy and deletion shape recall?

<!--
Slide ID: D3-M10-R1
Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
Instructor: Beric
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes:
- Say: Research: memory as a managed resource
- Ask: What does virtual context management move, and what remains fixed?
- Watch: Compare the notebook’s raw archive plus summary with the paper’s tiered-context idea.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [MemGPT paper](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Recap: model inside a harness

`user → harness → model → proposed tool call → authorization → tool → observation → harness`

- The model generates; the harness controls
- The trace records what the system actually did
- State and policy sit outside the model

<!--
Slide ID: D3-M11-C1
Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: Recap: model inside a harness
- Ask: Which component actually executes search_kb?
- Watch: Compare this boundary with the Six Ways capability catalogue and the search_kb call and trace shown in module 09.
- Then: Carry the observation into the next exercise.
Sources: [Module 11 README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md); [Six Ways notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/Six_Ways.ipynb); [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture)
-->
---
# Recap: model inside a harness · The practical check

- **Ask:** Which component actually executes search_kb?
- **Inspect:** Compare this boundary with the Six Ways capability catalogue and the search_kb call and trace shown in module 09.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M11-C1B
Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: Recap: model inside a harness
- Ask: Which component actually executes search_kb?
- Watch: Compare this boundary with the Six Ways capability catalogue and the search_kb call and trace shown in module 09.
- Then: Carry the observation into the notebook exercise.
Sources: [Module 11 README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md); [Six Ways notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/Six_Ways.ipynb); [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture)
-->
---
# State makes recovery explicit

- A state graph names checkpoints and failure paths
- Retries need idempotency, not optimism
- Recovery must distinguish safe retries from repeated side effects
- Approval gates precede consequential writes

<!--
Slide ID: D3-M11-C2
Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes:
- Say: State makes recovery explicit
- Ask: Where should authorization live if the model asks to reset a password?
- Watch: Inspect the named output and verify its provenance.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [ReAct](https://arxiv.org/abs/2210.03629); [module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
-->
---
# State makes recovery explicit · The practical check

- **Ask:** Where should authorization live if the model asks to reset a password?
- **Inspect:** Module 11 notebook cue: compare the tool, skill, MCP, sub-agent, code-mode, and manifest traces; inspect what enters context and the recorded call count/context size.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M11-C2B
Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes:
- Say: State makes recovery explicit
- Ask: Where should authorization live if the model asks to reset a password?
- Watch: Inspect the named output and verify its provenance.
- Then: Carry the observation into the notebook exercise.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [ReAct](https://arxiv.org/abs/2210.03629); [module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
-->
---
# Tools, MCP, and skills have different jobs

- Tool, skill, MCP, and sub-agent expose different boundaries
- Code mode runs capability logic; a manifest describes an API
- Choose an interface by ownership, auth, context, call count, and failure behavior
- Interfaces do not grant permission; review and scope every capability

<!--
Slide ID: D3-M11-C3
Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 04 Icon cards 2
Speaker notes:
- Say: Tools, MCP, and skills have different jobs
- Ask: Which job belongs to a tool, an MCP connection, and a skill?
- Watch: Inspect the named output and verify its provenance.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [ReAct](https://arxiv.org/abs/2210.03629); [$\tau$-bench](https://arxiv.org/abs/2406.12045); [module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
-->
---
# Tools, MCP, and skills have different jobs · The practical check

- **Ask:** Which job belongs to a tool, an MCP connection, and a skill?
- **Inspect:** Module 11 notebook cue: edit the capability catalogue and compare two mechanisms for one lookup; inspect ownership, auth, call count, and context size.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M11-C3B
Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: Tools, MCP, and skills have different jobs
- Ask: Which job belongs to a tool, an MCP connection, and a skill?
- Watch: Inspect the named output and verify its provenance.
- Then: Carry the observation into the notebook exercise.
Sources: [ReAct](https://arxiv.org/abs/2210.03629); [$\tau$-bench](https://arxiv.org/abs/2406.12045); [module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
-->
---
# Budget and evidence define the stop

- Bound turns, tools, tokens, time, and money
- Checkpoint evidence distinguishes done from unknown
- A stop condition is part of the architecture, not an afterthought
- Stop, verify, or escalate when recovery is unsafe

<!--
Slide ID: D3-M11-C4
Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: Budget and evidence define the stop
- Ask: Which of the six boxes would be invisible in a final-answer-only test?
- Watch: Module 11 notebook cue: read the six-row `tools_catalog` output and compare the two mechanisms selected for the group's lookup.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [Module 11 README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md); [Six Ways notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/Six_Ways.ipynb); [Module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
-->
---
# Budget and evidence define the stop · The practical check

- **Ask:** Which of the six boxes would be invisible in a final-answer-only test?
- **Inspect:** Module 11 notebook cue: read the six-row `tools_catalog` output and compare the two mechanisms selected for the group's lookup.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M11-C4B
Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes:
- Say: Budget and evidence define the stop
- Ask: Which of the six boxes would be invisible in a final-answer-only test?
- Watch: Module 11 notebook cue: read the six-row `tools_catalog` output and compare the two mechanisms selected for the group's lookup.
- Then: Carry the observation into the notebook exercise.
Sources: [Module 11 README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md); [Six Ways notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/Six_Ways.ipynb); [Module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
-->
---
# Research: durable state for long-running work

- Graphs make state and recovery points explicit
- Long runs need checkpoints and observable progress
- Case studies are guidance, not universal proof

<!--
Slide ID: D3-M11-R1
Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
Instructor: Rohit
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes:
- Say: Research: durable state for long-running work
- Ask: What does the benchmark evaluate that a model-only architecture cannot represent?
- Watch: Inspect the named output and verify its provenance.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [LangGraph: Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph); [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents); [module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
-->
---
# Guardrails sit at choke points

- Instructions influence; independent controls constrain
- Gate input, tools, and output for different failures
- A guardrail can block a behavior, but it does not grant permission
- Authorization belongs to policy, not prose

<!--
Slide ID: D3-M13-C1
Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: Guardrails sit at choke points
- Ask: Why is a prompt instruction not enough to authorize a password reset?
- Watch: Run case-set creation; observe benign transcript inputs alongside planted attacks and expected allow/block labels.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework); [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Guardrails sit at choke points · The practical check

- **Ask:** Why is a prompt instruction not enough to authorize a password reset?
- **Inspect:** Run case-set creation; observe benign transcript inputs alongside planted attacks and expected allow/block labels.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M13-C1B
Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: Guardrails sit at choke points
- Ask: Why is a prompt instruction not enough to authorize a password reset?
- Watch: Run case-set creation; observe benign transcript inputs alongside planted attacks and expected allow/block labels.
- Then: Carry the observation into the notebook exercise.
Sources: [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework); [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Choose the cheapest sufficient rung

| Control | Good at | Trade-off |
|---|---|---|
| Exact rule | Known patterns | Brittle coverage |
| Classifier | Paraphrases and categories | Threshold tuning |
| Judge | Open-ended meaning | Cost and calibration |

- Each rung adds latency or false-positive risk
- No rung replaces authorization or testing

<!--
Slide ID: D3-M13-C2
Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 07 Big stats 1
Speaker notes:
- Say: Choose the cheapest sufficient rung
- Ask: Which rung is best for an exact card-number pattern, and why?
- Watch: Run the constrained-decoding demo and rules/classifier comparison; observe kept tokens, rule latency, and disagreements.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [JSONSchemaBench constrained-decoding study](https://arxiv.org/abs/2501.10868); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Choose the cheapest sufficient rung · The practical check

- **Ask:** Which rung is best for an exact card-number pattern, and why?
- **Inspect:** Run the constrained-decoding demo and rules/classifier comparison; observe kept tokens, rule latency, and disagreements.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M13-C2B
Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes:
- Say: Choose the cheapest sufficient rung
- Ask: Which rung is best for an exact card-number pattern, and why?
- Watch: Run the constrained-decoding demo and rules/classifier comparison; observe kept tokens, rule latency, and disagreements.
- Then: Carry the observation into the notebook exercise.
Sources: [JSONSchemaBench constrained-decoding study](https://arxiv.org/abs/2501.10868); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Measure protection and friction

- Coverage without false positives is misleading
- Latency belongs in the release decision
- Test both harmful requests and legitimate requests that resemble them
- Real benign inputs are part of the test set

<!--
Slide ID: D3-M13-C3
Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 05 Two column 3
Speaker notes:
- Say: Measure protection and friction
- Ask: Why must false positives appear beside attack coverage?
- Watch: Compare the notebook’s rungs table; observe attacks caught, false positives, and mean milliseconds for each rung.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [NIST AI RMF GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Measure protection and friction · The practical check

- **Ask:** Why must false positives appear beside attack coverage?
- **Inspect:** Compare the notebook’s rungs table; observe attacks caught, false positives, and mean milliseconds for each rung.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M13-C3B
Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: Measure protection and friction
- Ask: Why must false positives appear beside attack coverage?
- Watch: Compare the notebook’s rungs table; observe attacks caught, false positives, and mean milliseconds for each rung.
- Then: Carry the observation into the notebook exercise.
Sources: [NIST AI RMF GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Stop safely and record why

- Cheapest first; stop at the first block
- Fail closed on guardrail errors
- Log the stage, reason, and owner for every blocked request
- Keep policy authorization outside text checks

<!--
Slide ID: D3-M13-C4
Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes:
- Say: Stop safely and record why
- Ask: What happens when one rung raises an exception?
- Watch: Run the full ladder; observe the stopped_at rung, ran list, false-positive summary, and saved ladder_results artifact.
- Then: Carry the observation into the next exercise.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [InjecAgent](https://arxiv.org/abs/2403.02691); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Stop safely and record why · The practical check

- **Ask:** What happens when one rung raises an exception?
- **Inspect:** Run the full ladder; observe the stopped_at rung, ran list, false-positive summary, and saved ladder_results artifact.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M13-C4B
Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes:
- Say: Stop safely and record why
- Ask: What happens when one rung raises an exception?
- Watch: Run the full ladder; observe the stopped_at rung, ran list, false-positive summary, and saved ladder_results artifact.
- Then: Carry the observation into the notebook exercise.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [InjecAgent](https://arxiv.org/abs/2403.02691); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Research: untrusted context can steer action

- Retrieved text is data, not authority
- Tool authorization must survive model mistakes
- Turn every incident into a regression case

<!--
Slide ID: D3-M13-R1
Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
Instructor: Rohit
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes:
- Say: Research: untrusted context can steer action
- Ask: Which boundary can still protect the tool if the retrieved text fools the model?
- Watch: Run the notebook’s planted injection through the ladder and inspect which rung catches it; do not infer security from one pass.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [InjecAgent](https://arxiv.org/abs/2403.02691); [NIST AI RMF GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
