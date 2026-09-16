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
Module: [09 Agent evals](../../../09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes: Start with the recurring question: “Why can’t I access the VPN?” A final answer can sound plausible while the agent searched the wrong article, skipped a needed clarification, or violated a support policy. An agent eval therefore treats the task as a goal plus a hidden success condition, then records the whole trajectory. The model, permitted search tool, observations, user follow-ups, and stop signal all matter. This is the shift from testing a single string to testing behavior in context. ReAct established the reason/action/observation pattern; trajectory evals apply that systems view to testing. Ask: where would you locate “searched the knowledge base” and “asked for the employee’s operating system”? The notebook cue is a section count, a search_kb call, and a short answer naming a section. The diagram’s end-state assertion is proposed, not implemented locally; this lab checks text facts and tool use, while state assertions appear in Grow. Stop when the trace is inspectable, not when the prose merely sounds good.
Check understanding: What evidence would a final answer hide that the trajectory exposes?
Lab observation: Run the notebook’s first agent-under-test cell; observe the section count, search_kb call, and answer naming a section.
Sources: [ReAct paper](https://arxiv.org/abs/2210.03629); [trajectory-evals notebook](../../../09_Agent_Evals/Trajectory_Evals.ipynb)
-->
---
# A useful answer is not enough · The practical check

- **Ask:** What evidence would a final answer hide that the trajectory exposes?
- **Inspect:** Run the notebook’s first agent-under-test cell; observe the section count, search_kb call, and answer naming a section.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M09-C1B
Module: [09 Agent evals](../../../09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: What evidence would a final answer hide that the trajectory exposes?
Lab observation: Run the notebook’s first agent-under-test cell; observe the section count, search_kb call, and answer naming a section.
Sources: [ReAct paper](https://arxiv.org/abs/2210.03629); [trajectory-evals notebook](../../../09_Agent_Evals/Trajectory_Evals.ipynb)
-->
---
# Turn a prompt into a testable task

- Hide the success condition from the agent
- Simulate the user’s missing details and patience
- Use deterministic checks for exact facts and judged criteria for meaning
- Score facts, actions, and policy—not just prose

<!--
Slide ID: D3-M09-C2
Module: [09 Agent evals](../../../09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes: Define the eval harness as the infrastructure that assembles tasks, runs the agent and simulated user, captures tool calls, and scores the result. A task is richer than a prompt: it includes a goal, persona, opening message, details the user reveals only when asked, and a success condition the agent never sees. The simulator makes missing information consequential. For the VPN question, the agent should ask for the platform before giving platform-specific steps. Use two complementary scorers: deterministic checks for facts and required tool behavior, and a rubric-based judge for supported, useful, policy-aligned answers. Neither is magic. Keyword checks can reward parroting; a judge can forgive a missing exact fact. The notebook’s planted out-of-scope and prompt-injection tasks make those boundaries visible. Ask which assertion belongs in code rather than in a judge prompt. Stop when each critical behavior has an observable assertion.
Check understanding: Which requirement should be deterministic for the VPN task, and which needs judgment?
Lab observation: Inspect one generated task row; observe its category, opening, facts, and hidden success condition.
Sources: [OpenAI evals build guide](https://github.com/openai/evals/blob/main/docs/build-eval.md); [OpenAI graders reference](https://platform.openai.com/docs/api-reference/graders); [trajectory-evals notebook](../../../09_Agent_Evals/Trajectory_Evals.ipynb)
-->
---
# Turn a prompt into a testable task · The practical check

- **Ask:** Which requirement should be deterministic for the VPN task, and which needs judgment?
- **Inspect:** Inspect one generated task row; observe its category, opening, facts, and hidden success condition.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M09-C2B
Module: [09 Agent evals](../../../09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Which requirement should be deterministic for the VPN task, and which needs judgment?
Lab observation: Inspect one generated task row; observe its category, opening, facts, and hidden success condition.
Sources: [OpenAI evals build guide](https://github.com/openai/evals/blob/main/docs/build-eval.md); [OpenAI graders reference](https://platform.openai.com/docs/api-reference/graders); [trajectory-evals notebook](../../../09_Agent_Evals/Trajectory_Evals.ipynb)
-->
---
# Reliability lives across runs

- One run is a sample, not a reliability claim
- Use pass rate and pass^k for repeated tasks
- Compare the shape of failures across repeated runs
- Plant a regression and verify the harness moves

<!--
Slide ID: D3-M09-C3
Module: [09 Agent evals](../../../09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: One run is a sample, especially when a model user rephrases the request or the agent chooses a different tool path. If a task succeeds with probability p, pass^k asks how often all k attempts succeed; it exposes inconsistency that an average pass rate can hide. In this notebook, three repeats use the same configured model, agent, simulated user, and judge, so they reveal sampling variability within this harness—not broad confidence, independence, or production reliability. The planted regression returns the same first section for every query. Lookup tasks should move; out-of-scope and injection tasks may hold. That differential is evidence this harness responds to one known behavior change, not proof that it measures all behavior. Ask what a zero delta would mean. Stop when a failure becomes a reproducible task.
Check understanding: Why can pass^k be much lower than pass rate without either metric being wrong?
Lab observation: Run repeated tasks and the planted regression; compare lookup-category movement with out-of-scope and injection categories.
Sources: [$\tau$-bench](https://arxiv.org/abs/2406.12045); [trajectory-evals notebook](../../../09_Agent_Evals/Trajectory_Evals.ipynb)
-->
---
# Reliability lives across runs · The practical check

- **Ask:** Why can pass^k be much lower than pass rate without either metric being wrong?
- **Inspect:** Run repeated tasks and the planted regression; compare lookup-category movement with out-of-scope and injection categories.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M09-C3B
Module: [09 Agent evals](../../../09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Why can pass^k be much lower than pass rate without either metric being wrong?
Lab observation: Run repeated tasks and the planted regression; compare lookup-category movement with out-of-scope and injection categories.
Sources: [$\tau$-bench](https://arxiv.org/abs/2406.12045); [trajectory-evals notebook](../../../09_Agent_Evals/Trajectory_Evals.ipynb)
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
Module: [09 Agent evals](../../../09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes: Close on the artifact a release manager can act on: a capability report with model and agent identity, per-task pass rate and pass^k, the worst failure, the turn where it first went wrong, and the planted-regression result. The report should preserve disagreement between deterministic checks and judges instead of collapsing it into one reassuring number. A useful stopping rule is evidence-based: stop iterating when the task set covers the intended capability, the release bar is met, and known failures have regression cases. If the cost or permissions make an agent unnecessary, stop and use a simpler workflow. The notebook writes capability_report from actual runs; it does not claim production readiness. Ask learners to name the first observable assertion they would add for VPN support. Their answer belongs in the notebook’s Your turn section, not in this deck.
Check understanding: What must be reproducible before you call an agent change ready to ship?
Lab observation: Read the printed capability report and locate the worst failure and planted-regression result.
Sources: [OpenAI evals](https://evals.openai.com/); [trajectory-evals notebook](../../../09_Agent_Evals/Trajectory_Evals.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)
-->
---
# Stop on evidence, not confidence · The practical check

- **Ask:** What must be reproducible before you call an agent change ready to ship?
- **Inspect:** Read the printed capability report and locate the worst failure and planted-regression result.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M09-C4B
Module: [09 Agent evals](../../../09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: What must be reproducible before you call an agent change ready to ship?
Lab observation: Read the printed capability report and locate the worst failure and planted-regression result.
Sources: [OpenAI evals](https://evals.openai.com/); [trajectory-evals notebook](../../../09_Agent_Evals/Trajectory_Evals.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)
-->
---
# Research: from traces to state

- ReAct made tool interaction part of the task
- τ-bench evaluates user, policy, tools, and end state
- Open question: does the oracle match support reality?

<!--
Slide ID: D3-M09-R1
Module: [09 Agent evals](../../../09_Agent_Evals/README.md)
Instructor: Eli
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes: Optional research: compare ReAct and tau-bench without treating either as a universal recipe. ReAct’s contribution is the interleaving of reasoning traces and actions so external observations can update the plan. Tau-bench adds dynamic user interaction, domain tools, policy guidelines, end-state evaluation, and pass^k. Those are different scopes: a prompting pattern is not an end-to-end release harness, and a benchmark result is not a guarantee for an internal helpdesk. Invite investigation into state-based assertions: did the agent actually create or update the ticket, rather than merely say that it did? The notebook currently scores tool use and text-level facts, then asks learners to move toward state assertions in Grow. The research question is whether the simulator and oracle represent the real support workflow closely enough to make a release decision. Stop research when the comparison changes a concrete assertion or task.
Check understanding: What does tau-bench add beyond checking the agent’s final sentence?
Lab observation: Compare the notebook’s current text/fact checks with its Grow suggestion to assert external state.
Sources: [ReAct](https://arxiv.org/abs/2210.03629); [$\tau$-bench](https://arxiv.org/abs/2406.12045); [trajectory-evals notebook](../../../09_Agent_Evals/Trajectory_Evals.ipynb)
-->
---
# Memory is restored context

- The model call ends; the harness can persist state
- Useful memory improves continuity across sessions
- Memory is selected context, not a hidden model faculty
- Wrong memory creates confident, stale answers

<!--
Slide ID: D3-M10-C1
Module: [10 Memory](../../../10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 05 Two column
Speaker notes: A model does not remember a previous call by itself. The harness must choose what to persist and what to place back into the next prompt. Use the recurring VPN question: in session one, the user says they are on a Mac and belong to Finance; in session two, “the VPN still fails” should not force needless repetition, but only if the memory is scoped to that user and current enough. Define persistence as state that outlives the process that created it. Then name the risk: bad memory is worse than no memory because it creates confident continuity around a stale or wrong fact. The notebook begins with a naive buffer and a fresh session to make the gap observable. Memory is an application design, not a hidden model faculty. Ask which fact is safe to remember and which is merely transient. Stop before storing anything whose future value is unclear.
Check understanding: Where does the remembered Mac fact live between the two model calls?
Lab observation: Run the naive memory demonstration; observe the same-session answer versus the fresh-session “I do not know.”
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](../../../10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Memory is restored context · The practical check

- **Ask:** Where does the remembered Mac fact live between the two model calls?
- **Inspect:** Run the naive memory demonstration; observe the same-session answer versus the fresh-session “I do not know.”
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M10-C1B
Module: [10 Memory](../../../10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Where does the remembered Mac fact live between the two model calls?
Lab observation: Run the naive memory demonstration; observe the same-session answer versus the fresh-session “I do not know.”
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](../../../10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
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
Module: [10 Memory](../../../10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 04 Icon cards 1
Speaker notes: The local notebook teaches three kinds of memory: episodic, semantic, and working. Episodic memory records what happened in a run; semantic memory stores durable facts recalled when relevant; working memory is what the assembler places in the current prompt. The VPN example makes the distinction concrete: “we tried reset and search_kb” is episodic, “Finance uses split tunnel” may be semantic, and the current error belongs in working memory. Treat procedural instructions—identity, constraints, skills, and response policy—as a separate persistence dimension that can be implemented in a harness; it is not one of the notebook’s three memory kinds and is not universally always loaded. Retrieval can select a memory; it does not make the memory true. Ask learners to classify “the user prefers concise steps” and “the ticket number from last week.” Stop when ownership, scope, and retention are explicit.
Check understanding: Which memory type should preserve the tool call that actually ran?
Lab observation: Read the notebook’s three-kind implementation and identify the procedural, semantic, episodic, and working layers in the assembled prompt.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](../../../10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Give each memory a job · The practical check

- **Ask:** Which memory type should preserve the tool call that actually ran?
- **Inspect:** Read the notebook’s three-kind implementation and identify the procedural, semantic, episodic, and working layers in the assembled prompt.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M10-C2B
Module: [10 Memory](../../../10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Which memory type should preserve the tool call that actually ran?
Lab observation: Read the notebook’s three-kind implementation and identify the procedural, semantic, episodic, and working layers in the assembled prompt.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](../../../10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Budget memory deliberately

- Protect instructions and recent turns
- Drop low-relevance recalled facts first
- Compact old turns, but keep raw recovery

<!--
Slide ID: D3-M10-C3
Module: [10 Memory](../../../10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 07 Big stats 1
Speaker notes: Working memory is a budgeted assembly problem. The notebook stacks procedural instructions, recalled semantic memories, an episodic summary, and recent turns. When the budget is small, it drops the least relevant recalled memory first and protects the root set and newest turns. When a conversation grows, compaction condenses older turns while archiving raw text so a ticket number can still be recovered. This is a design choice, not a law: another product may protect an approval record or a safety constraint ahead of recency. The failure to watch is silent loss—an instruction or identifier disappears and the answer remains fluent. Use the VPN ticket number as the invariant. Ask what must never be trimmed in a support product. Stop compaction when the summary no longer preserves the facts needed for the next decision; retrieve the raw turn instead.
Check understanding: Which tier does the notebook drop first, and which two tiers does it protect?
Lab observation: Compare the 6,000- and 120-token breakdowns, then observe compacted=True and raw retrieval of ticket 48213.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](../../../10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Budget memory deliberately · The practical check

- **Ask:** Which tier does the notebook drop first, and which two tiers does it protect?
- **Inspect:** Compare the 6,000- and 120-token breakdowns, then observe compacted=True and raw retrieval of ticket 48213.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M10-C3B
Module: [10 Memory](../../../10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Which tier does the notebook drop first, and which two tiers does it protect?
Lab observation: Compare the 6,000- and 120-token breakdowns, then observe compacted=True and raw retrieval of ticket 48213.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](../../../10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Remember less, govern better

- Supersede stale facts and delete when required
- Scope memory by user or tenant
- Test truthfulness, staleness, and leakage

<!--
Slide ID: D3-M10-C4
Module: [10 Memory](../../../10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes: Memory needs governance as much as retrieval. Capture only facts that can improve a future decision; review them for truth, ownership, and sensitivity; supersede or expire stale values; delete on request; and isolate stores by user or tenant. The notebook tests a changed team fact by retiring the old subject record, then asks learners to run a two-user leakage test with different ticket numbers. Those tests are more valuable than a polished “remembered you” demo. A production design should retain lineage for important decisions and make the write path observable. A stopping rule is intentional forgetfulness: if the fact is not durable, scoped, and useful, do not write it. Ask whether a ticket number, device model, or temporary outage symptom belongs in long-term memory. Their answers should be argued from product need and risk, not inferred here.
Check understanding: What test detects a memory store that leaks one user’s ticket into another user’s session?
Lab observation: Run the supersede-on-subject check and the leakage test; observe stale facts being rejected and user stores kept separate.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](../../../10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Remember less, govern better · The practical check

- **Ask:** What test detects a memory store that leaks one user’s ticket into another user’s session?
- **Inspect:** Run the supersede-on-subject check and the leakage test; observe stale facts being rejected and user stores kept separate.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M10-C4B
Module: [10 Memory](../../../10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: What test detects a memory store that leaks one user’s ticket into another user’s session?
Lab observation: Run the supersede-on-subject check and the leakage test; observe stale facts being rejected and user stores kept separate.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](../../../10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Research: memory as a managed resource

- Context windows remain a bounded active workspace
- Paging can extend usable history without erasing raw evidence
- Open question: how should privacy and deletion shape recall?

<!--
Slide ID: D3-M10-R1
Module: [10 Memory](../../../10_Agent_Memory/README.md)
Instructor: Beric
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes: Optional research: MemGPT describes virtual context management inspired by operating-system memory tiers. Define a token as the model’s text-processing unit used to count context and budget prompt space; token counts vary by tokenizer and are not characters. Define an oracle as the trusted reference for whether a task’s intended state or answer is correct. MemGPT’s contribution is architectural: move information between a constrained active context and slower memory under explicit control. That is a useful origin for the notebook’s budget and compaction ideas, not proof that every product should adopt the same design. Compare it with an internal helpdesk, where privacy, deletion, recency, and auditability may dominate recall breadth. Stop investigation when it cannot change a retention or leakage test.
Check understanding: What does virtual context management move, and what remains fixed?
Lab observation: Compare the notebook’s raw archive plus summary with the paper’s tiered-context idea.
Sources: [MemGPT paper](https://arxiv.org/abs/2310.08560); [memory notebook](../../../10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Recap: model inside a harness

`user → harness → model → proposed tool call → authorization → tool → observation → harness`

- The model generates; the harness controls
- The trace records what the system actually did
- State and policy sit outside the model

<!--
Slide ID: D3-M11-C1
Module: [11 Architecture](../../../11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes: Keep the recap concise: a model generates an output from supplied context; a harness surrounds it with tools, state, policy, and control flow. The Module 11 notebook compares six ways to expose one lookup capability: a tool, skill folder, MCP server, sub-agent, code-mode runtime, and manifest-described API. The model may propose a lookup, but the harness validates the interface, executes the permitted call, returns the observation, and controls the next transition. For “Why can’t I access the VPN?”, a read-only search may be automatic while a password reset must pause for identity and approval. Do not imply that one mechanism wins universally. Ask learners to point to the executor and the approval boundary. Stop the recap once those responsibilities are named; the architecture work is about state, capability interfaces, and recovery.
Check understanding: Which component actually executes search_kb?
Lab observation: Compare this boundary with the Six Ways capability catalogue and the search_kb call and trace shown in module 09.
Sources: [Module 11 README](../../../11_Agent_Architecture/README.md); [Six Ways notebook](../../../11_Agent_Architecture/Six_Ways.ipynb); [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture)
-->
---
# Recap: model inside a harness · The practical check

- **Ask:** Which component actually executes search_kb?
- **Inspect:** Compare this boundary with the Six Ways capability catalogue and the search_kb call and trace shown in module 09.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M11-C1B
Module: [11 Architecture](../../../11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Which component actually executes search_kb?
Lab observation: Compare this boundary with the Six Ways capability catalogue and the search_kb call and trace shown in module 09.
Sources: [Module 11 README](../../../11_Agent_Architecture/README.md); [Six Ways notebook](../../../11_Agent_Architecture/Six_Ways.ipynb); [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture)
-->
---
# State makes recovery explicit

- A state graph names checkpoints and failure paths
- Retries need idempotency, not optimism
- Recovery must distinguish safe retries from repeated side effects
- Approval gates precede consequential writes

<!--
Slide ID: D3-M11-C2
Module: [11 Architecture](../../../11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes: Move from the recap to stateful control flow. Represent the support run as explicit states such as clarify, search, propose, approval-required, execute, verify, and escalate. A checkpoint records enough durable state to resume without guessing what completed. A retry policy must distinguish a safe read from a write that may have succeeded; idempotency means repeating the same request does not create a second side effect, usually through a stable request key or operation check. Put human approval immediately before a consequential action, and make approval part of the state transition rather than a sentence the model can claim. The harness owns timeouts, retry counts, and trace events. Ask which transition follows a lost response from password-reset. Stop retrying when the operation is non-idempotent or evidence is ambiguous; verify or escalate.
Check understanding: Where should authorization live if the model asks to reset a password?
Lab observation: Module 11 notebook cue: compare the tool, skill, MCP, sub-agent, code-mode, and manifest traces; inspect what enters context and the recorded call count/context size.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [ReAct](https://arxiv.org/abs/2210.03629); [module alignment](module-alignment.md)
-->
---
# State makes recovery explicit · The practical check

- **Ask:** Where should authorization live if the model asks to reset a password?
- **Inspect:** Module 11 notebook cue: compare the tool, skill, MCP, sub-agent, code-mode, and manifest traces; inspect what enters context and the recorded call count/context size.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M11-C2B
Module: [11 Architecture](../../../11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Where should authorization live if the model asks to reset a password?
Lab observation: Module 11 notebook cue: compare the tool, skill, MCP, sub-agent, code-mode, and manifest traces; inspect what enters context and the recorded call count/context size.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [ReAct](https://arxiv.org/abs/2210.03629); [module alignment](module-alignment.md)
-->
---
# Tools, MCP, and skills have different jobs

- Tool, skill, MCP, and sub-agent expose different boundaries
- Code mode runs capability logic; a manifest describes an API
- Choose an interface by ownership, auth, context, call count, and failure behavior
- Interfaces do not grant permission; review and scope every capability

<!--
Slide ID: D3-M11-C3
Module: [11 Architecture](../../../11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 04 Icon cards 2
Speaker notes: Now separate capability interfaces from instructions. A tool is an executable capability with typed inputs and a result, such as read_ticket or search_kb. MCP is a protocol for an AI application to connect to servers that expose capabilities such as tools and resources; the protocol does not itself grant authorization. A skill packages repeatable know-how—instructions, examples, resources, and sometimes scripts—for how to perform a kind of work. A skill can tell an agent how to prepare a support brief; a tool can fetch the ticket; an MCP server can provide a standardized connection to that tool and resource. None of the three is automatically trusted. Review third-party code, scope permissions, and keep the policy gate in the harness. Ask which interface belongs to “look up VPN status” and which belongs to “write a weekly incident brief.” Stop when each job has a clear owner.
Check understanding: Which job belongs to a tool, an MCP connection, and a skill?
Lab observation: Module 11 notebook cue: edit the capability catalogue and compare two mechanisms for one lookup; inspect ownership, auth, call count, and context size.
Sources: [ReAct](https://arxiv.org/abs/2210.03629); [$\tau$-bench](https://arxiv.org/abs/2406.12045); [module alignment](module-alignment.md)
-->
---
# Tools, MCP, and skills have different jobs · The practical check

- **Ask:** Which job belongs to a tool, an MCP connection, and a skill?
- **Inspect:** Module 11 notebook cue: edit the capability catalogue and compare two mechanisms for one lookup; inspect ownership, auth, call count, and context size.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M11-C3B
Module: [11 Architecture](../../../11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Which job belongs to a tool, an MCP connection, and a skill?
Lab observation: Module 11 notebook cue: edit the capability catalogue and compare two mechanisms for one lookup; inspect ownership, auth, call count, and context size.
Sources: [ReAct](https://arxiv.org/abs/2210.03629); [$\tau$-bench](https://arxiv.org/abs/2406.12045); [module alignment](module-alignment.md)
-->
---
# Budget and evidence define the stop

- Bound turns, tools, tokens, time, and money
- Checkpoint evidence distinguishes done from unknown
- A stop condition is part of the architecture, not an afterthought
- Stop, verify, or escalate when recovery is unsafe

<!--
Slide ID: D3-M11-C4
Module: [11 Architecture](../../../11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: Finish with operational limits rather than another definition. Set budgets for model turns, tool calls, wall-clock time, tokens, and money. Every transition should emit evidence: the input, selected capability, validated arguments, observation, checkpoint, approval decision, and final status. Recovery must distinguish “not attempted,” “completed,” and “unknown because the response was lost.” The Module 11 catalogue adds a decision aid: choose a mechanism by ownership, authentication, what enters context, and failure behavior. The VPN assistant can stop after verified resolution, after a bounded number of failed attempts with escalation, or when permission is missing. A successful demo is not production evidence; release needs repeatable evals, current context, authorization, monitoring, and accountable ownership. Ask which evidence would make a retry safe. Stop the concept lesson when the team can name the capability owner, budget, approval, and escalation.
Check understanding: Which of the six boxes would be invisible in a final-answer-only test?
Lab observation: Module 11 notebook cue: read the six-row `tools_catalog` output and compare the two mechanisms selected for the group's lookup.
Sources: [Module 11 README](../../../11_Agent_Architecture/README.md); [Six Ways notebook](../../../11_Agent_Architecture/Six_Ways.ipynb); [Module alignment](module-alignment.md)
-->
---
# Budget and evidence define the stop · The practical check

- **Ask:** Which of the six boxes would be invisible in a final-answer-only test?
- **Inspect:** Module 11 notebook cue: read the six-row `tools_catalog` output and compare the two mechanisms selected for the group's lookup.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M11-C4B
Module: [11 Architecture](../../../11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Which of the six boxes would be invisible in a final-answer-only test?
Lab observation: Module 11 notebook cue: read the six-row `tools_catalog` output and compare the two mechanisms selected for the group's lookup.
Sources: [Module 11 README](../../../11_Agent_Architecture/README.md); [Six Ways notebook](../../../11_Agent_Architecture/Six_Ways.ipynb); [Module alignment](module-alignment.md)
-->
---
# Research: durable state for long-running work

- Graphs make state and recovery points explicit
- Long runs need checkpoints and observable progress
- Case studies are guidance, not universal proof

<!--
Slide ID: D3-M11-R1
Module: [11 Architecture](../../../11_Agent_Architecture/README.md)
Instructor: Rohit
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes: Optional research: read LangGraph’s “Thinking in LangGraph” as a framework explanation of stateful graphs, checkpoints, and human-in-the-loop recovery, then compare Anthropic’s long-running-agent harness case study. Their contribution is practical architecture guidance: make progress durable, separate phases, and give a resumed run explicit state and tests. They are not controlled evidence that one framework or harness is best for every support workflow. The useful question is where a VPN run can pause safely: after clarification, after retrieval, before an approved write, or after verification. Bring the discussion back to idempotency, bounded retries, and evidence of completed side effects. The Module 11 notebook supplies a capability-comparison lab; these sources extend it into recovery and long-running work. Stop research when the case study changes one checkpoint or recovery assertion.
Check understanding: What does the benchmark evaluate that a model-only architecture cannot represent?
Lab observation: Module 11 notebook cue: compare the six capability mechanisms first; use this optional reading to propose one recovery assertion for the chosen mechanism.
Sources: [LangGraph: Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph); [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents); [module alignment](module-alignment.md)
-->
---
# Guardrails sit at choke points

- Instructions influence; independent controls constrain
- Gate input, tools, and output for different failures
- A guardrail can block a behavior, but it does not grant permission
- Authorization belongs to policy, not prose

<!--
Slide ID: D3-M13-C1
Module: [13 Guardrails 101](../../../13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes: A guardrail is an independently enforced, testable policy that inspects, transforms, blocks, pauses, or escalates. “Do not reset passwords without approval” in a system prompt is an instruction; the tool gate that checks identity and approval is a guardrail. Use the recurring VPN question to distinguish harmless help from a consequential reset. Input checks can reject out-of-scope requests or redact unnecessary PII. Tool checks validate arguments and authorization immediately before execution. Output checks can catch unsupported claims or sensitive content before release. A policy layer maps user identity and requested action to permission; it is not a prompt and should not be inferred from text. The notebook’s ladder starts from cases drawn from transcripts plus planted attacks. Ask where the reset approval check belongs. Stop a request at the first sufficient choke point and fail closed if the check raises.
Check understanding: Why is a prompt instruction not enough to authorize a password reset?
Lab observation: Run case-set creation; observe benign transcript inputs alongside planted attacks and expected allow/block labels.
Sources: [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework); [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [guardrail notebook](../../../13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Guardrails sit at choke points · The practical check

- **Ask:** Why is a prompt instruction not enough to authorize a password reset?
- **Inspect:** Run case-set creation; observe benign transcript inputs alongside planted attacks and expected allow/block labels.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M13-C1B
Module: [13 Guardrails 101](../../../13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Why is a prompt instruction not enough to authorize a password reset?
Lab observation: Run case-set creation; observe benign transcript inputs alongside planted attacks and expected allow/block labels.
Sources: [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework); [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [guardrail notebook](../../../13_Guardrails_101/Guardrail_Ladder.ipynb)
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
Module: [13 Guardrails 101](../../../13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 07 Big stats 1
Speaker notes: The notebook builds a ladder rather than searching for one universal detector. Constrained decoding can make illegal structured output unreachable, but it needs logit or grammar control and does not decide whether a legitimate action is authorized. Regex rules are fast and predictable for exact patterns such as card numbers or credentials, but miss paraphrases. A small classifier catches learned language patterns but inherits its training coverage and can false-positive on ordinary support terms. An LLM judge can assess contextual properties, but adds model cost, latency, and its own uncertainty. These mechanisms are complementary, not monotonically better. For a VPN assistant, a card-number regex may redact input while a tool policy checks reset authorization. Ask learners to identify a failure that can be specified exactly. Stop at the cheapest rung that clears the required coverage and false-positive bar.
Check understanding: Which rung is best for an exact card-number pattern, and why?
Lab observation: Run the constrained-decoding demo and rules/classifier comparison; observe kept tokens, rule latency, and disagreements.
Sources: [JSONSchemaBench constrained-decoding study](https://arxiv.org/abs/2501.10868); [guardrail notebook](../../../13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Choose the cheapest sufficient rung · The practical check

- **Ask:** Which rung is best for an exact card-number pattern, and why?
- **Inspect:** Run the constrained-decoding demo and rules/classifier comparison; observe kept tokens, rule latency, and disagreements.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M13-C2B
Module: [13 Guardrails 101](../../../13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Which rung is best for an exact card-number pattern, and why?
Lab observation: Run the constrained-decoding demo and rules/classifier comparison; observe kept tokens, rule latency, and disagreements.
Sources: [JSONSchemaBench constrained-decoding study](https://arxiv.org/abs/2501.10868); [guardrail notebook](../../../13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Measure protection and friction

- Coverage without false positives is misleading
- Latency belongs in the release decision
- Test both harmful requests and legitimate requests that resemble them
- Real benign inputs are part of the test set

<!--
Slide ID: D3-M13-C3
Module: [13 Guardrails 101](../../../13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 05 Two column 3
Speaker notes: Measure both sides of the guardrail bargain. A detector that blocks every request has perfect attack coverage and zero usefulness. The notebook builds benign cases from real transcript first turns and adds planted attacks for instruction overrides, credentials, sensitive storage, and unauthorized approval. It reports attacks caught beside legitimate inputs wrongly blocked, plus latency. The classifier and rules can disagree because one catches learned phrasing and the other catches exact patterns. A judge can assess contextual support or tone, but a prompt that works as an evaluator may be too costly or too uncertain as a refusal gate. For the VPN example, a benign request should pass even if it contains technical words that overlap attack training data. Ask which false positive a support team would tolerate. Stop a rung from shipping when its false-positive rate exceeds the product’s explicit bar, regardless of its attack score.
Check understanding: Why must false positives appear beside attack coverage?
Lab observation: Compare the notebook’s rungs table; observe attacks caught, false positives, and mean milliseconds for each rung.
Sources: [NIST AI RMF GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf); [guardrail notebook](../../../13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Measure protection and friction · The practical check

- **Ask:** Why must false positives appear beside attack coverage?
- **Inspect:** Compare the notebook’s rungs table; observe attacks caught, false positives, and mean milliseconds for each rung.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M13-C3B
Module: [13 Guardrails 101](../../../13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: Why must false positives appear beside attack coverage?
Lab observation: Compare the notebook’s rungs table; observe attacks caught, false positives, and mean milliseconds for each rung.
Sources: [NIST AI RMF GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf); [guardrail notebook](../../../13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Stop safely and record why

- Cheapest first; stop at the first block
- Fail closed on guardrail errors
- Log the stage, reason, and owner for every blocked request
- Keep policy authorization outside text checks

<!--
Slide ID: D3-M13-C4
Module: [13 Guardrails 101](../../../13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes: Assemble the deployed order from measured evidence: cheapest first, stop at the first block, and fail closed when a rung raises. The notebook measures every rung separately, then shows the ladder’s early stopping behavior; the policy layer is intentionally separate because it acts on user and action authorization rather than text. For VPN support, rules might redact a credential, the classifier might block a prompt override, and a judge might inspect a contextual request—but none of those grants permission to reset an account. Add monitoring for false positives, latency, and newly observed attacks. A stopping rule is explicit: ship only the rungs that clear the coverage bar within the latency budget; document what remains unprotected and route consequential uncertainty to a person. Ask which rung should never be allowed to silently fail open. Stop when the ladder’s order and thresholds are recorded with its results.
Check understanding: What happens when one rung raises an exception?
Lab observation: Run the full ladder; observe the stopped_at rung, ran list, false-positive summary, and saved ladder_results artifact.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [InjecAgent](https://arxiv.org/abs/2403.02691); [guardrail notebook](../../../13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Stop safely and record why · The practical check

- **Ask:** What happens when one rung raises an exception?
- **Inspect:** Run the full ladder; observe the stopped_at rung, ran list, false-positive summary, and saved ladder_results artifact.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D3-M13-C4B
Module: [13 Guardrails 101](../../../13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.
Check understanding: What happens when one rung raises an exception?
Lab observation: Run the full ladder; observe the stopped_at rung, ran list, false-positive summary, and saved ladder_results artifact.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [InjecAgent](https://arxiv.org/abs/2403.02691); [guardrail notebook](../../../13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Research: untrusted context can steer action

- Retrieved text is data, not authority
- Tool authorization must survive model mistakes
- Turn every incident into a regression case

<!--
Slide ID: D3-M13-R1
Module: [13 Guardrails 101](../../../13_Guardrails_101/README.md)
Instructor: Rohit
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes: Optional research: InjecAgent frames indirect prompt injection as malicious instructions embedded in external content that a tool-integrated agent processes. That threat is especially relevant to retrieval-backed support: a poisoned article or ticket can attempt to redirect the agent, disclose data, or invoke an unrelated tool. The paper is a benchmark and vulnerability study, not evidence that one detector solves prompt injection. The architectural response is defense in depth: treat retrieved content as untrusted, constrain tool authority, evaluate trajectories and external state, and require confirmation or policy approval for consequential actions. The notebook’s planted prompt-injection task and separate policy-layer note are useful beginnings, while its text ladder does not establish production security. Ask which control remains if a classifier misses a paraphrase. Stop research when the attack becomes a regression case with a clear owner and observable blocked action.
Check understanding: Which boundary can still protect the tool if the retrieved text fools the model?
Lab observation: Run the notebook’s planted injection through the ladder and inspect which rung catches it; do not infer security from one pass.
Sources: [InjecAgent](https://arxiv.org/abs/2403.02691); [NIST AI RMF GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf); [guardrail notebook](../../../13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
