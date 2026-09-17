---
marp: true
theme: default
paginate: true
size: 16:9
---
# Today: making the agent behave, not just answer

- 09 Agent evals — 35m
- 10 Agent memory — 30m
- 11 Agent architecture — 35m
- 13 Guardrails 101 — 30m

<!--
Slide ID: D3-F1
Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
Instructor: Eli
Type: agenda
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: Day 2 made answers grounded. Nothing yet proves the path was sound, that it remembers, or that it refuses.
- Ask: Which part of Priya’s VPN journey would you trust least if you only saw the final answer?
- Watch: Notebook:cell#9 (Trajectory_Evals) — the first task builds the agent under test; keep that path in view as the day moves through memory, architecture, and guardrails.
- Then: Start with the trajectory, then add state, capability boundaries, and policy. Priya’s VPN path, Marcus’s audit log, and every consequential action need evidence around the loop.
Sources: [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb); [Six Ways notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/Six_Ways.ipynb); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# 09 · Agent evals

**Did it behave, or did it just answer?** · 35 min

- Day 2 made answers grounded. Nothing yet proves the path was sound.

<!--
Slide ID: D3-T09
Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
Instructor: Eli
Type: transition
Minutes: 0
Layout: 01 Title
Speaker notes:
- Say: Day 2 made answers grounded. Nothing yet proves the path was sound. That is what this module is for.
- Ask: Hold for a beat — this is the hand-off, not content.
- Watch: Name the module and who is running it, then move. One breath.
- Then: Straight into the first content slide.
Sources: [Module 09 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md).
-->
---
# A useful answer is not enough

`goal → user turns → tool calls → observations → final state`

- An AI answer can sound right and still take the wrong path
- Evaluate the complete trajectory, not only the final sentence

<!--
Slide ID: D3-M09-C1
Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: A right answer reached by a wrong path will fail the next question you ask.
- Ask: What evidence would a final answer hide that the trajectory exposes?
- Watch: Run the notebook’s first agent-under-test cell; observe the section count, search_kb call, and answer naming a section. Trajectory_Evals:cell#9 is Task 1 of 8 — Build the agent under test. In the notebook: A useful answer is not enough; the trajectory exposes whether the agent searched and what it found.
- Then: Carry the observation into the next exercise.
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
- Say: A test needs a hidden success condition; if the agent can see the answer, you measured nothing.
- Ask: Which requirement should be deterministic for the VPN task, and which needs judgment?
- Watch: Inspect one generated task row; observe its category, opening, facts, and hidden success condition. Trajectory_Evals:cell#12 is Task 2 of 8 — Compose tasks from your eval cases. In the notebook: Turn a prompt into a testable task by hiding what success means from the agent.
- Then: Hand into “Deterministic check or judged criterion”.
Sources: [OpenAI evals build guide](https://github.com/openai/evals/blob/main/docs/build-eval.md); [OpenAI graders reference](https://platform.openai.com/docs/api-reference/graders); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)
-->
---
# The compounding error problem

An agent that passes 80% of the time, run three times on the same task:

| Metric | Value |
|---|---|
| pass rate | 0.80 |
| **pass^3** — all three attempts succeed | **≈ 0.5** |

Each step multiplies. A multi-step agent at 80% per step is a coin flip end to end — and one run tells you nothing about which.

<!--
Slide ID: D3-M09-C3
Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: One green run is a coin flip you won. Reliability only shows up across repeats.
- Ask: Why can pass^k be much lower than pass rate without either metric being wrong?
- Watch: Run repeated tasks and the planted regression; compare lookup-category movement with out-of-scope and injection categories. Trajectory_Evals:cell#16 is Task 3 of 8 — Simulate the user. In the notebook: Reliability lives across repeated trajectories, not one green run.
- Then: So run each task k times. The regression-planting check comes next, and it depends on this.
Sources: [$\tau$-bench](https://arxiv.org/abs/2406.12045); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)
-->
---
# Stop on evidence, not confidence

- Keep the worst trace beside the score
- Gate changes to prompts, tools, and retrieval
- A score without the trace can hide the first incorrect step
- Stop when coverage and known-failure bars are met

<!--
Slide ID: D3-M09-C4
Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
Instructor: Eli
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes:
- Say: Ship on a number you measured, and on a harness you proved catches a planted break.
- Ask: What must be reproducible before you call an agent change ready to ship?
- Watch: Read the printed capability report and locate the worst failure and planted-regression result. Trajectory_Evals:cell#19 is Task 4 of 8 — Score the trajectory, not the answer. In the notebook: Stop on evidence, not confidence; the report must show what failed and whether the harness caught the planted break.
- Then: Hand into “Read the capability report”.
Sources: [OpenAI evals](https://evals.openai.com/); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)
-->
---
# Optional: a trace is evidence; state is what resumes

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
- Say: Optional: a trace is evidence; state is what lets a run resume from it.
- Ask: What does tau-bench add beyond checking the agent’s final sentence?
- Watch: Compare the notebook’s current text/fact checks with its Grow suggestion to assert external state.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [ReAct](https://arxiv.org/abs/2210.03629); [$\tau$-bench](https://arxiv.org/abs/2406.12045); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)
-->
---
# 10 · Agent memory

**What should survive the session — and what should not?** · 30 min

- An agent that forgets everything repeats itself. One that remembers everything leaks.

<!--
Slide ID: D3-T10
Module: [10 Agent memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
Instructor: Beric
Type: transition
Minutes: 0
Layout: 01 Title
Speaker notes:
- Say: An agent that forgets everything repeats itself. One that remembers everything leaks. That is what this module is for.
- Ask: Hold for a beat — this is the hand-off, not content.
- Watch: Name the module and who is running it, then move. One breath.
- Then: Straight into the first content slide.
Sources: [Module 10 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md).
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
- Say: The model remembers nothing. Memory is state you write, govern, and choose to restore.
- Ask: Where does the remembered Mac fact live between the two model calls?
- Watch: Run the naive memory demonstration; observe the same-session answer versus the fresh-session “I do not know.”. Three_Kinds_of_Memory:cell#9 is Task 1 of 7 — See the gap. In the notebook: Memory is restored context, not a faculty that survives a model call.
- Then: The harness must choose what to persist and what to place back into the next prompt.
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
- Say: Give each memory a job. An undifferentiated store recalls the wrong thing.
- Ask: Which memory type should preserve the tool call that actually ran? (Episodic — it is what happened, not what is true.)
- Watch: These four are the token-budget tiers the notebook assembles in cell#21. The notebook is named for three *kinds* — episodic, semantic, working — because procedural here is the instructions tier, not a store the group writes to. In the notebook: Give each memory a job; an episode records what the trace says happened.
- Then: Worth saying if it comes up: the cleaner split is episodic / semantic / procedural by *content*, with working memory being a lifetime — the per-turn view assembled from the other three. "Periodic memory" is not a fourth type; scheduled consolidation is what this module calls compaction.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Budget memory deliberately

- The **root set** — instructions and recent turns — is never trimmed
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
- Say: Context is a budget. Decide what gets trimmed first, before the window forces the choice.
- Ask: Which tier does the notebook drop first, and which two tiers does it protect?
- Watch: Compare the 6,000- and 120-token breakdowns, then observe compacted=True and raw retrieval of ticket 48213. Three_Kinds_of_Memory:cell#16 is Task 3 of 7 — A long-term store you can read. In the notebook: Budget memory deliberately; the assembler makes the trade-off observable.
- Then: Carry the observation into the next exercise.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Your context window is not your effective context window

- **Capacity is not architecture.** A 1M-token window is what the model can *accept*, not what it can reliably *use*
- **Position and difficulty degrade it.** Relevant facts buried mid-context get missed; on NoLiMa, 11 of 13 models fell below half their short-context score by 32K
- **So memory is a retrieval problem.** Select what this step needs — rank, filter, scope — instead of appending until the window fills

> [Lost in the Middle](https://arxiv.org/abs/2307.03172) · [RULER](https://arxiv.org/abs/2404.06654) · [NoLiMa](https://arxiv.org/abs/2502.05167)

<!--
Slide ID: D3-M10-C4X
Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 05 Two column
Speaker notes:
- Say: Every context problem has an escape hatch: wait for a bigger window. The research says that does not fix the part that is actually hard.
- Ask: Audience — if an agent hits a 250K-token limit, what is the first question? Not "how do we compact better" but "why did this task need 250K tokens?"
- Watch: Three separate questions hide inside "long context" — how much can it accept, how efficiently can it process, and how reliably can it pick what matters. The industry solved the first two. Three_Kinds_of_Memory:cell#20 is Task 4 of 7 — Assemble working memory under a budget.
- Then: Conversation history is not relevant because it happened. A tool result is not relevant because the agent produced it. Context needs a lifecycle.
Sources: [Lost in the Middle](https://arxiv.org/abs/2307.03172), [RULER](https://arxiv.org/abs/2404.06654), [NoLiMa](https://arxiv.org/abs/2502.05167), [MemGPT](https://arxiv.org/abs/2310.08560)
-->
---
# Remember less, govern better

**Not all context is equally important.** More memory is not better memory.

- Retrieve *into* memory the way you retrieve into a prompt — rank, filter, take the top few
- Supersede stale facts, and delete when required
- Scope by user or tenant, then test for truthfulness, staleness, and leakage

A memory store is a corpus you own. Everything from the last two days applies to it.

<!--
Slide ID: D3-M10-C4
Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
Instructor: Beric
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: More memory is not better memory. This is a retrieval problem wearing a different name.
- Ask: What test detects a memory store that leaks one user’s ticket into another user’s session?
- Watch: Run the supersede-on-subject check and the leakage test; observe stale facts being rejected and user stores kept separate. Three_Kinds_of_Memory:cell#20 is Task 4 of 7 — Assemble working memory under a budget. In the notebook: Remember less, govern better; compaction should preserve recovery evidence.
- Then: Same moves as days 1 and 2 — rank, filter, scope — now applied to what the agent carries forward.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# 11 · Agent architecture

**One capability, six ways to give it to an agent.** · 35 min

- A tool, a skill folder, an MCP server, a sub-agent, a code-mode runtime, a manifest-described API
- What reaches the model in each — and what breaks first

<!--
Slide ID: D3-T11
Module: [11 Agent architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
Instructor: Rohit
Type: transition
Minutes: 0
Layout: 01 Title
Speaker notes:
- Say: One capability, six mechanisms. The module is a comparison, not a tour.
- Ask: Hold for a beat — this is the hand-off, not content.
- Watch: This is the README's own framing: what reaches the model in each case, and what breaks first. The deliverable is a catalogue saying when to use which.
- Then: Straight into the first content slide.
Sources: [Module 11 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md).
-->
---
# The model proposes; the harness decides

`user → harness → model → proposed tool call → authorization → tool → observation → harness`

- The model — whatever `LLM_MODEL` is set to — only *generates* a request
- Your harness authorizes it, runs it, and records what happened

**Every one of the six mechanisms sits on the far side of that boundary.** What changes is who owns the thing being called.

<!--
Slide ID: D3-M11-C1
Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: Same boundary as Monday. What changes today is who owns the capability on the far side of it.
- Ask: Which component actually executes the tool? Not the model — it only ever emits a request.
- Watch: Task 1 wires a `lookup` function as a tool: a Python function, a JSON schema handed to the model, and your loop running it. The model is provider-agnostic — it is whatever `LLM_MODEL` names, defaulting to `gpt-4.1-mini`. Six_Ways:cell#9 is Task 1 of 7 — A tool.
- Then: So the six mechanisms are not six technologies. They are six answers to: who owns this capability?
Sources: [Module 11 README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md); [Six Ways notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/Six_Ways.ipynb); [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture)
-->
---
# Six ways to give an agent a capability

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 760 245" width="900" role="img" aria-label="Six capability mechanisms: tool, skill, MCP server, sub-agent, code mode, and API manifest">
<rect x="28" y="34" width="210" height="62" rx="9" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.5"/><text x="133" y="61" font-size="16" font-weight="700" text-anchor="middle" fill="#5b21b6">tool</text><text x="133" y="82" font-size="12.5" text-anchor="middle" fill="#6d28d9">your process</text>
<rect x="275" y="34" width="210" height="62" rx="9" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/><text x="380" y="61" font-size="16" font-weight="700" text-anchor="middle" fill="#92400e">skill</text><text x="380" y="82" font-size="12.5" text-anchor="middle" fill="#b45309">versioned capability</text>
<rect x="522" y="34" width="210" height="62" rx="9" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/><text x="627" y="61" font-size="16" font-weight="700" text-anchor="middle" fill="#075985">MCP server</text><text x="627" y="82" font-size="12.5" text-anchor="middle" fill="#0369a1">separate service</text>
<rect x="28" y="139" width="210" height="62" rx="9" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/><text x="133" y="166" font-size="16" font-weight="700" text-anchor="middle" fill="#075985">sub-agent</text><text x="133" y="187" font-size="12.5" text-anchor="middle" fill="#0369a1">delegated role</text>
<rect x="275" y="139" width="210" height="62" rx="9" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/><text x="380" y="166" font-size="16" font-weight="700" text-anchor="middle" fill="#92400e">code mode</text><text x="380" y="187" font-size="12.5" text-anchor="middle" fill="#b45309">capability logic</text>
<rect x="522" y="139" width="210" height="62" rx="9" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.5"/><text x="627" y="166" font-size="16" font-weight="700" text-anchor="middle" fill="#5b21b6">API manifest</text><text x="627" y="187" font-size="12.5" text-anchor="middle" fill="#6d28d9">described endpoint</text>
<path d="M380 214 V232" stroke="#94a3b8" stroke-width="2" marker-end="url(#m11a)"/><text x="380" y="243" font-size="12.5" text-anchor="middle" fill="#475569">choose by ownership, auth, context, and failure behavior</text>
<defs><marker id="m11a" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#94a3b8"/></marker></defs>
</svg>
</div>

<!--
Slide ID: D3-M11-C5
Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: These are six capability boundaries, not six brands or six permissions.
- Ask: Who owns Deskmate’s ticket system, and what would you need to audit before connecting to it?
- Watch: Notebook:cell#17 (Six_Ways) — an MCP server is a separate process discovered over the Model Context Protocol; compare it with the in-process tool. In the notebook: MCP adds a service boundary; UTCP describes an existing API boundary.
- Then: Treat the ticket system as an external boundary and inspect its auth, health, version, and trace behavior. Deskmate’s ticket system is somebody else’s service; MCP is one way to reach it without owning it.
Sources: [Six Ways notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/Six_Ways.ipynb); [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture)
-->
---
# The same capability, six places to put it

One `lookup` function. Six boundaries you could put it behind:

| | The capability lives | You own |
|---|---|---|
| Tool | in your process | everything |
| Skill | in a folder the harness shells out to | the script |
| MCP server | in a separate process | the protocol contract |
| Sub-agent | in another agent's loop | its budget and prompt |
| Code mode | in a runtime that executes model-written code | the sandbox |
| Manifest | in an API you already run | nothing new |

The model's request looks the same in every case. **What changes is who is responsible when it breaks.**

<!--
Slide ID: D3-M11-C2
Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes:
- Say: Six mechanisms, one capability. The choice is an ownership question, not a technology preference.
- Ask: Audience — your team already runs an internal API. Which row is that, and what do you gain by not rebuilding it?
- Watch: The notebook implements all six against the same `lookup`, which is what makes them comparable. Six_Ways:cell#12 is Task 2 of 7 — A skill.
- Then: Note what is NOT here: state graphs and durable execution are module 12, which is not on this cohort's schedule.
Sources: [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture), [local Six Ways notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/Six_Ways.ipynb)
-->
---
# Choose a mechanism by who owns it

Given the six, the choice is an ownership question — not a novelty contest:

| Ask | Because |
|---|---|
| Who owns the schema? | you cannot version someone else's contract |
| What enters the context? | every mechanism costs tokens differently |
| How does it authenticate? | a service boundary needs a credential |
| What breaks first? | failure mode decides your fallback |

No mechanism grants permission. Scope every capability regardless of how it is exposed.

<!--
Slide ID: D3-M11-C3
Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 04 Icon cards 2
Speaker notes:
- Say: Pick by ownership, auth, and what enters context — not by which is newest.
- Ask: Which job belongs to a tool, an MCP connection, and a skill?
- Watch: Put the named artifact on screen and trace where its values came from. Six_Ways:cell#17 is Task 3 of 7 — An MCP server. In the notebook: Tools, MCP, and skills have different jobs; MCP adds a separate process boundary.
- Then: Hand into “Tool, skill, MCP, or sub-agent”.
Sources: [ReAct](https://arxiv.org/abs/2210.03629); [$\tau$-bench](https://arxiv.org/abs/2406.12045); [module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
-->
---
# Optional: long work needs checkpoints, not a longer context

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
- Say: Optional: long work needs checkpoints and safe retries, not a longer context window.
- Ask: What does the benchmark evaluate that a model-only architecture cannot represent?
- Watch: Put the named artifact on screen and trace where its values came from.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [LangGraph: Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph); [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents); [module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
-->
---
# 13 · Guardrails 101

**What stops it when the model is wrong?** · 30 min

- Instructions influence. Only a control at a choke point constrains.

<!--
Slide ID: D3-T13
Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
Instructor: Rohit
Type: transition
Minutes: 0
Layout: 01 Title
Speaker notes:
- Say: Instructions influence. Only a control at a choke point constrains. That is what this module is for.
- Ask: Hold for a beat — this is the hand-off, not content.
- Watch: Name the module and who is running it, then move. One breath.
- Then: Straight into the first content slide.
Sources: [Module 13 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md).
-->
---
# Guardrails sit at choke points

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 720 150" width="880" role="img" aria-label="Three choke points around the agent loop: input before the model, the tool boundary, and output before the user">
<rect x="246" y="44" width="150" height="62" rx="9" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.5"/>
<text x="321" y="70" font-size="15" font-weight="700" text-anchor="middle" fill="#5b21b6">the loop</text>
<text x="321" y="90" font-size="12" text-anchor="middle" fill="#6d28d9">model + your code</text>
<rect x="18" y="44" width="150" height="62" rx="9" fill="#fee2e2" stroke="#dc2626" stroke-width="2.5"/>
<text x="93" y="68" font-size="13.5" font-weight="700" text-anchor="middle" fill="#7f1d1d">input</text>
<text x="93" y="88" font-size="11.5" text-anchor="middle" fill="#b91c1c">scope · injection</text>
<rect x="474" y="44" width="150" height="62" rx="9" fill="#fee2e2" stroke="#dc2626" stroke-width="2.5"/>
<text x="549" y="68" font-size="13.5" font-weight="700" text-anchor="middle" fill="#7f1d1d">output</text>
<text x="549" y="88" font-size="11.5" text-anchor="middle" fill="#b91c1c">unsupported claims</text>
<rect x="246" y="118" width="150" height="28" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="3"/>
<text x="321" y="137" font-size="12.5" font-weight="700" text-anchor="middle" fill="#92400e">tool boundary · authorization</text>
<path d="M170 75 H242" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#ck)"/>
<path d="M398 75 H470" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#ck)"/>
<path d="M321 108 V114" stroke="#d97706" stroke-width="2.5"/>
<text x="660" y="79" font-size="12" text-anchor="middle" fill="#475569" font-style="italic">user</text>
<defs><marker id="ck" markerWidth="10" markerHeight="10" refX="8.5" refY="3" orient="auto"><path d="M0 0 L8.5 3 L0 6 z" fill="#94a3b8"/></marker></defs>
</svg>
</div>

Instructions *influence*. Only a control at one of these three points can *constrain* — and none of them grants permission.

<!--
Slide ID: D3-M13-C1
Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: Instructions influence the model. Only code at a choke point constrains it.
- Ask: Why is a prompt instruction not enough to authorize a password reset?
- Watch: Run case-set creation; observe benign transcript inputs alongside planted attacks and expected allow/block labels. Guardrail_Ladder:cell#9 is Task 1 of 7 — Build the case set from your transcripts. In the notebook: Guardrails sit at choke points, where the request and intended action can be checked independently.
- Then: Hand into “Benign cases beside planted attacks”.
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
- Say: Each rung buys coverage and costs latency or false positives. Cheapest that clears the bar.
- Ask: Which rung is best for an exact card-number pattern, and why?
- Watch: Run the constrained-decoding demo and rules/classifier comparison; observe kept tokens, rule latency, and disagreements. Guardrail_Ladder:cell#12 is Task 2 of 7 — Rung 0, constrained decoding. In the notebook: Choose the cheapest sufficient rung; constrained decoding makes an invalid output unreachable.
- Then: Hand into “Compare the rungs you can afford”.
Sources: [JSONSchemaBench constrained-decoding study](https://arxiv.org/abs/2501.10868); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Name the five guardrail rungs

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 760 280" width="900" role="img" aria-label="A five-rung guardrail ladder from constrained decoding through rules, a classifier, an LLM judge, and a policy layer">
<text x="380" y="22" font-size="14" text-anchor="middle" fill="#475569">cheapest and most mechanical</text>
<path d="M112 52 V238" stroke="#94a3b8" stroke-width="4"/><path d="M648 52 V238" stroke="#94a3b8" stroke-width="4"/>
<rect x="112" y="48" width="536" height="34" rx="7" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/><text x="380" y="70" font-size="15" font-weight="700" text-anchor="middle" fill="#5b21b6">Rung 0 · constrained decoding</text>
<rect x="112" y="86" width="536" height="34" rx="7" fill="#fef3c7" stroke="#d97706" stroke-width="2"/><text x="380" y="108" font-size="15" font-weight="700" text-anchor="middle" fill="#92400e">Rung 1 · rules</text>
<rect x="112" y="124" width="536" height="34" rx="7" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/><text x="380" y="146" font-size="15" font-weight="700" text-anchor="middle" fill="#075985">Rung 2 · a classifier</text>
<rect x="112" y="162" width="536" height="34" rx="7" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/><text x="380" y="184" font-size="15" font-weight="700" text-anchor="middle" fill="#5b21b6">Rung 3 · an LLM judge</text>
<rect x="112" y="200" width="536" height="34" rx="7" fill="#fef3c7" stroke="#d97706" stroke-width="2"/><text x="380" y="222" font-size="15" font-weight="700" text-anchor="middle" fill="#92400e">Rung 4 · a policy layer</text>
<text x="380" y="265" font-size="14" text-anchor="middle" fill="#475569">more context and authority</text>
</svg>
</div>

<!--
Slide ID: D3-M13-C2A
Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: Rungs 0 and 1 give a verdict. Rung 2 and up give a score you have to threshold — which is a different kind of control.
- Ask: Audience — which of these five can only answer yes or no? Constrained decoding and rules. Everything above returns a number.
- Watch: Notebook:cell#12 (Guardrail_Ladder) is Rung 0, constrained decoding; Notebook:cell#16 is Rung 1, rules; Notebook:cell#19 is Rung 2, a classifier; Notebook:cell#23 is Rung 3, an LLM judge; Notebook:cell#26 is Rung 4, a policy layer. In the notebook: A higher rung is not automatically better; it is a different control with a different failure surface.
- Then: Worth saying out loud, and it is a point the industry glosses over: once a check returns a score rather than a verdict — the Rung 2 classifier, the Rung 3 LLM judge, any follow-up model detecting content — it is not really a guardrail, it is a validation layer. A guardrail lets an action through or it does not. A validation layer hands you a probability you must threshold, so it has a false-positive rate and can be argued with. The classifier is deterministic at inference, but you still choose the cutoff. Industry calls all five guardrails, which blurs a real engineering difference: only Rungs 0 and 1 and the Rung 4 policy layer reliably block. A policy question like "never reset an entitlement without confirmation" is not a regex, and it is not a threshold either.
Sources: [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb); [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
-->
---
# Every rung gets three numbers

Run all five rungs against the same case set. Per rung:

| Measure | The question it answers |
|---|---|
| attacks caught | does it protect? |
| false positives | does it block legitimate traffic? |
| mean latency (ms) | can you afford it on every request? |

Coverage alone is not a result. A rule that catches every attack **and** blocks real users has failed.
<!--
Slide ID: D3-M13-C3
Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 05 Two column 3
Speaker notes:
- Say: Three numbers per rung, and you need all three. Protection without friction is an unfinished measurement.
- Ask: Audience — a rung catches 100% of attacks. What do you still need to know before shipping it?
- Watch: The case set holds planted attacks and real benign inputs that resemble them, which is what makes the false-positive column meaningful. Guardrail_Ladder:cell#31 is Task 7 of 7 — Measure them all, then assemble the ladder.
- Then: Those numbers are what the release decision is made from — not a sense that the guardrails feel strict enough.
Sources: [NIST AI RMF GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Your harness handles the block, not the model

The ladder runs inside your loop, so the loop owns what happens on a block:

- Run cheapest first, and **stop at the first block**
- **Fail closed:** a rung that throws counts as a block — otherwise it switches itself off during an outage while the logs stay quiet
- Log the stage, the reason, and the owner for every blocked request
- Keep policy authorization outside the text checks entirely

A block nobody can explain gets switched off by the first person it inconveniences.
<!--
Slide ID: D3-M13-C4
Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
Instructor: Rohit
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes:
- Say: This is harness work, not model work. The model never sees any of it.
- Ask: Audience — what happens if your classifier service times out? If the answer is "the request goes through", the guardrail is decorative.
- Watch: Each rung is wrapped so an exception counts as a block, for exactly that reason. Guardrail_Ladder:cell#31 is Task 7 of 7 — Measure them all, then assemble the ladder.
- Then: Fail closed, log which rung stopped it and why, and keep authorization in policy rather than in a text check.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [InjecAgent](https://arxiv.org/abs/2403.02691); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# Optional: retrieved text is data, never authority

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
- Say: Optional: retrieved text is data, never authority. Tool authorization must survive a mistake.
- Ask: Which boundary can still protect the tool if the retrieved text fools the model?
- Watch: Run the notebook’s planted injection through the ladder and inspect which rung catches it; do not infer security from one pass.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [InjecAgent](https://arxiv.org/abs/2403.02691); [NIST AI RMF GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
---
# What production adds around the loop

| What we built | Production equivalent |
|---|---|
| One store per user in a folder | Per-tenant isolation, tested for leakage in the eval harness |
| A stdio MCP server | Authenticated deployment, health checks, protocol version tests |
| A ladder in a for loop, failing closed | A ladder with latency budgets, fail-closed alerts, and false-positive tracking |

<!--
Slide ID: D3-Z1
Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
Instructor: Rohit
Type: close
Minutes: 2
Layout: 05 Two column 3
Speaker notes:
- Say: Production adds controls around the same loop: scoped memory, authenticated capability boundaries, and measured guardrails.
- Ask: Which production equivalent would catch the most dangerous Deskmate failure first: leakage, an untrusted service, or silent guardrail drift?
- Watch: Notebook:cell#39 (Three_Kinds_of_Memory) supplies the per-user isolation row; Notebook:cell#38 (Six_Ways) supplies the MCP row; Notebook:cell#38 (Guardrail_Ladder) supplies the ladder row.
- Then: Carry the chosen boundary into Friday’s release decision and name what remains unmeasured. Marcus gets an auditable boundary; Priya’s context stays scoped as the loop grows.
Sources: [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb); [Six Ways notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/Six_Ways.ipynb); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
