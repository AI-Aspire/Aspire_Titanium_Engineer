---
marp: true
theme: default
paginate: true
size: 16:9
---
# Today: making the agent behave, not just answer

09 Agent evals 35m · 10 Agent memory 30m · 11 Agent architecture 35m · 13 Guardrails 101 30m

Day 2 made answers grounded; nothing yet proves that the path was sound, that it remembers, or that it refuses.

<!--
Slide ID: D3-F1
Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
Instructor: Eli
Type: agenda
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: Today we move from a grounded answer to behavior we can inspect, remember, and constrain.
- Ask: Which part of Priya’s VPN journey would you trust least if you only saw the final answer?
- Watch: Notebook:cell#9 (Trajectory_Evals) — the first task builds the agent under test; keep that path in view as the day moves through memory, architecture, and guardrails.
- Then: Start with the trajectory, then add state, capability boundaries, and policy. Priya’s VPN path, Marcus’s audit log, and every consequential action need evidence around the loop.
Sources: [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb); [Six Ways notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/Six_Ways.ipynb); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)
-->
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
# 80% is not what 80% sounds like

An agent that passes 80% of the time, run three times on the same task:

| Metric | Value |
|---|---|
| pass rate | 0.80 |
| **pass^3** — all three attempts succeed | **≈ 0.5** |

One run is a sample of one. Plant a regression and check the number actually moves.

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
- Then: Hand into “Run it again, then plant a regression”.
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
- Say: Forgetting on purpose is a feature: stale facts and leaked context are both memory bugs.
- Ask: What test detects a memory store that leaks one user’s ticket into another user’s session?
- Watch: Run the supersede-on-subject check and the leakage test; observe stale facts being rejected and user stores kept separate. Three_Kinds_of_Memory:cell#20 is Task 4 of 7 — Assemble working memory under a budget. In the notebook: Remember less, govern better; compaction should preserve recovery evidence.
- Then: Carry the observation into the next exercise.
Sources: [MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# Optional: memory needs retention, scope, and an owner

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
- Say: Optional: memory is a managed store with retention and scope, not a transcript.
- Ask: What does virtual context management move, and what remains fixed?
- Watch: Compare the notebook’s raw archive plus summary with the paper’s tiered-context idea.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [MemGPT paper](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)
-->
---
# The model proposes; the harness decides

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
- Say: Same boundary as Monday, now with the question of who owns each capability.
- Ask: Which component actually executes search_kb?
- Watch: Compare this boundary with the Six Ways capability catalogue and the search_kb call and trace shown in module 09. Six_Ways:cell#9 is Task 1 of 7 — A tool. In the notebook: Recap: the model is inside a harness that owns capability execution.
- Then: Carry the observation into the next exercise.
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
- Say: Without explicit state, a restarted run cannot tell you what actually completed.
- Ask: Where should authorization live if the model asks to reset a password?
- Watch: Put the named artifact on screen and trace where its values came from. Six_Ways:cell#12 is Task 2 of 7 — A skill. In the notebook: State makes recovery explicit; a skill also exposes a command boundary the harness can audit.
- Then: Hand into “What a restarted run knows”.
Sources: [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [ReAct](https://arxiv.org/abs/2210.03629); [module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
-->
---
# Choose a mechanism by who owns it

The six options come next. The choice is not about novelty:

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
- Say: Publish the budget and the stopping evidence together, or neither is checkable.
- Ask: Which of the six boxes would be invisible in a final-answer-only test?
- Watch: Module 11 notebook cue: read the six-row `tools_catalog` output and compare the two mechanisms selected for the group's lookup. Six_Ways:cell#20 is Task 4 of 7 — A sub-agent. In the notebook: Budget and evidence define the stop; the catalogue makes capability choices inspectable.
- Then: Hand into “Read the six-row catalogue”.
Sources: [Module 11 README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md); [Six Ways notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/Six_Ways.ipynb); [Module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
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
- Say: The ladder names five different jobs; only the last one answers who may perform an action.
- Ask: Where would you place Marcus’s request to reset Priya’s entitlement, and what evidence would that rung need?
- Watch: Notebook:cell#12 (Guardrail_Ladder) is Rung 0, constrained decoding; Notebook:cell#16 is Rung 1, rules; Notebook:cell#19 is Rung 2, a classifier; Notebook:cell#23 is Rung 3, an LLM judge; Notebook:cell#26 is Rung 4, a policy layer. In the notebook: A higher rung is not automatically better; it is a different control with a different failure surface.
- Then: Keep the ladder visible while comparing cost, coverage, and authority. Deskmate’s “never reset an entitlement without confirmation” is a policy question, not a regex.
Sources: [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb); [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
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
- Say: Coverage without a false-positive number is half a measurement.
- Ask: Why must false positives appear beside attack coverage?
- Watch: Compare the notebook’s rungs table; observe attacks caught, false positives, and mean milliseconds for each rung. Guardrail_Ladder:cell#16 is Task 3 of 7 — Rung 1, rules. In the notebook: Measure protection and friction together; a rule can catch an attack and still block legitimate traffic.
- Then: Hand into “Caught attacks against false positives”.
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
- Say: Fail closed, and log which rung stopped it — a block nobody can explain gets switched off.
- Ask: What happens when one rung raises an exception?
- Watch: Run the full ladder; observe the stopped_at rung, ran list, false-positive summary, and saved ladder_results artifact. Guardrail_Ladder:cell#19 is Task 4 of 7 — Rung 2, a classifier. In the notebook: Stop safely and record why; the ladder returns the first blocking rung and the stages it ran.
- Then: Carry the observation into the next exercise.
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
