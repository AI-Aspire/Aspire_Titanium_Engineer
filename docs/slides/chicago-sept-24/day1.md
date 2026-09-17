---
marp: true
theme: default
paginate: true
size: 16:9
title: Day 1 — Prototype and retrieve
---

# Today: from a repo to a retrieving agent

- 01 Dev environment — 30m · 02 Prompt patterns — 30m
- 03 Agents 101 — 35m · 04 Vibe checks and judges — 30m
- 05 RAG — 30m

Today walks Deskmate from dev → prompt → agents → RAG once; the rest of the week deepens each stage.

<!--
Slide ID: D1-F0
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 2
Layout: 02 Agenda
Speaker notes:
- Say: Today walks one connected path from a repo to a retrieving agent.
- Ask: Which stage would you want evidence from before you let the next stage depend on it?
- Watch: Keep the five module times visible; the agenda is a map, not a promise that each stage is production-ready today.
- Then: Notebook:cell#9 — start with the first development task, then return to the journey after the five modules.
Sources: [Day 1 schedule](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/schedule/day1.md); [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).
-->

---

# Start with a question, not a technology

- Name one person and one difficult recurring question
- Identify the decision that follows the answer
- Leave the technology choice open

> Source: [Concrete Idea Worksheet](https://corporate.aiaspire.ai/accenture/titanium/NA/agenda/cohort_2/Concrete_Idea_Worksheet.pdf)

<!--
Slide ID: D1-F1
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 01 Title
Speaker notes:
- Say: Start with a question, not a technology
- Ask: What decision would become easier if this question were answered well?
- Watch: In the later charter exercise, write one user and one recurring question; do not fill in the group's choice here.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [Concrete Idea Worksheet](https://corporate.aiaspire.ai/accenture/titanium/NA/agenda/cohort_2/Concrete_Idea_Worksheet.pdf); [Charter template](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/project/CHARTER.md).
-->

---

# Define what a useful answer must contain

- The answer: the next step or decision
- The evidence: the fact or procedure supporting it
- The boundary: when to ask a person or say “not enough evidence”

> Source: [Concrete Idea Worksheet](https://corporate.aiaspire.ai/accenture/titanium/NA/agenda/cohort_2/Concrete_Idea_Worksheet.pdf)

<!--
-->

<!--
Slide ID: D1-F2
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 02 Agenda 1
Speaker notes:
- Say: Define what a useful answer must contain
- Ask: Which part of the answer would let you detect that the procedure is stale?
- Watch: During charter work, have the group write what a correct answer must contain for three questions.
- Then: Carry the observation into the next exercise.
Sources: [Concrete Idea Worksheet](https://corporate.aiaspire.ai/accenture/titanium/NA/agenda/cohort_2/Concrete_Idea_Worksheet.pdf); [Charter template](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/project/CHARTER.md).
-->

---

# Separate the task, the evidence, and the decision

- Task: what question must be answered?
- Evidence: what facts can change?
- Decision: who acts, and what requires approval?

> Source: [Semantic contracts research notes](https://github.com/soypete/ctx-eng-book/blob/main/research/semantic-contracts.md)

<!--
Slide ID: D1-F3
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 05 Two column
Speaker notes:
- Say: Separate the task, the evidence, and the decision
- Ask: Which of the three changes when a policy is updated: the task, the evidence, or the decision owner?
- Watch: Ask groups to put one changing fact and one accountable decision owner on their napkin sketch.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [Author's semantic-contract notes](https://github.com/soypete/ctx-eng-book/blob/main/research/semantic-contracts.md); [Course authoring principles](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/AUTHORING.md).
-->

---

# A prototype tests one uncertainty

- Can the approach answer the question at all?
- What failure would change the design?
- What evidence is enough to stop?

> Source: [Machine Learning Yearning](https://github.com/ajaymache/machine-learning-yearning/blob/master/full%20book/machine-learning-yearning.pdf)

<!--
Slide ID: D1-F4
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 06 Process steps
Speaker notes:
- Say: A prototype tests one uncertainty
- Ask: What result would make you abandon the current approach rather than add another feature?
- Watch: In the charter, write two likely failures and how the group would notice each one.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [Machine Learning Yearning](https://github.com/ajaymache/machine-learning-yearning/blob/master/full%20book/machine-learning-yearning.pdf); [Charter template](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/project/CHARTER.md).
-->

---

# PoC: prove the mechanism manually

- Ask the question in a chat
- Copy in the relevant facts by hand
- Check the answer against the source and criteria

> Source: [The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/)

<!--
Slide ID: D1-F5
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 09 Lab and code
Speaker notes:
- Say: PoC: prove the mechanism manually
- Ask: Which manual step would you automate first, and what evidence would show that automation is safe?
- Watch: Groups later build two prompt-only prototypes; keep the copied context and answer criteria visible for comparison.
- Then: Carry the observation into the next exercise.
Sources: [The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/); [Course authoring principles](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/AUTHORING.md).
-->

---

# A PoC exits with evidence, not enthusiasm

- Compare the attempt with explicit criteria
- Record the failure and the next change
- Stop if the question or evidence is still unclear

> Source: [Machine Learning Yearning](https://github.com/ajaymache/machine-learning-yearning/blob/master/full%20book/machine-learning-yearning.pdf)

<!--
Slide ID: D1-F6
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 05 Two column 1
Speaker notes:
- Say: A PoC exits with evidence, not enthusiasm
- Ask: What would make a prompt-only PoC a useful failure?
- Watch: Groups should carry one comparison question and two likely failures into the prompt-pattern exercise.
- Then: Compare the revision against the same criteria.
Sources: [Machine Learning Yearning](https://github.com/ajaymache/machine-learning-yearning/blob/master/full%20book/machine-learning-yearning.pdf); [Prompt patterns module](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md).
-->

---

# MVP: one person completes one useful flow

- A repeatable input and output
- A narrow boundary around one user task
- Enough usability to complete the decision

> Source: [The product-market fit framework](https://pmarchive.com/guide_to_startups_part4.html)

<!--
Slide ID: D1-F7
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 05 Two column 2
Speaker notes:
- Say: MVP: one person completes one useful flow
- Ask: What is the smallest end-to-end flow your user could complete without a team member explaining the demo?
- Watch: Groups should keep their first product boundary narrow enough to demonstrate in the pitch.
- Then: Carry the observation into the next exercise.
Sources: [The product-market fit framework](https://pmarchive.com/guide_to_startups_part4.html); [Concrete startup idea handout](https://corporate.aiaspire.ai/accenture/titanium/NA/agenda/cohort_2/What_We_Mean_by_a_Concrete_Startup_Idea.pdf).
-->

---

# The MVP is one designed experience

- Like a car prepared for a test drive
- One coherent design, not every possible feature
- Test the route, controls, and failure response

> Source: [The product-market fit framework](https://pmarchive.com/guide_to_startups_part4.html)

<!--
Slide ID: D1-F8
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 05 Two column 3
Speaker notes:
- Say: The MVP is one designed experience
- Ask: What would count as a test drive for your proposed AI product?
- Watch: In the napkin sketch, mark the one flow the group will show and the future options it will leave out.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [The product-market fit framework](https://pmarchive.com/guide_to_startups_part4.html); [The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/).
-->

---

# Production is repeatable operation

- The same useful task works across expected variation
- Quality, permissions, recovery, and ownership are explicit
- Changes are tested before users depend on them

> Source: [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)

<!--
Slide ID: D1-F9
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 07 Big stats
Speaker notes:
- Say: Production is repeatable operation
- Ask: Which production responsibility would be missing if the demo only showed a successful answer?
- Watch: Groups should name one quality risk and one person who would own the consequence of failure.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents); [Module 01 production discussion](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).
-->

---

# Production is the infrastructure around the car

- Context is prepared, refreshed, and scoped
- Workflows execute with permissions and recovery
- Evals and observability decide whether changes ship

> Source: [The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/)

<!--
Slide ID: D1-F10
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 06 Process steps 1
Speaker notes:
- Say: Production is the infrastructure around the car
- Ask: Which control would you need before allowing the assistant to change data rather than only suggest a next step?
- Watch: Ask groups to circle one production concern their current PoC intentionally leaves unresolved.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/); [Author's context-assembly notes](https://github.com/soypete/ctx-eng-book/blob/main/research/context-assembly-pipeline-patterns.md).
-->

---

# The same build ladder applies to AI

- PoC: prompt plus manual context and checks
- MVP: one usable path with skills, code, or MCP
- Production: workflows, context, evals, and infrastructure

> Source: [The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/)

<!--
Slide ID: D1-F11
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 04 Icon cards
Speaker notes:
- Say: The same build ladder applies to AI
- Ask: Which new evidence—not which new component—would move your system to the next level?
- Watch: Groups should label their proposed system as a PoC, MVP, or production target and state what evidence is still missing.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/); [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
-->

---

# Day 1: answer one question, then earn complexity

- Define the question and answer contract
- Build a prompt, an agent, and a RAG baseline
- Check what improved before adding more machinery

> Source: [Day 1 schedule](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/schedule/day1.md)

<!--
Slide ID: D1-F12
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 02 Agenda
Speaker notes:
- Say: Day 1: answer one question, then earn complexity
- Ask: What is the first question your group will answer, and what evidence will tell you whether the prototype helped?
- Watch: Carry the question, answer contract, and first failure hypothesis into the group charter.
- Then: Carry the observation into the next exercise.
Sources: [Day 1 schedule](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/schedule/day1.md); [Day 1 cohort outline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/slides/chicago-sept-24/README.md); [Concrete Idea Worksheet](https://corporate.aiaspire.ai/accenture/titanium/NA/agenda/cohort_2/Concrete_Idea_Worksheet.pdf).
-->

---

# Concepts in this module

- **Two remotes:** `origin` is your fork, `upstream` is the course repo
- **The daily loop:** branch → change → read the diff → commit → push → draft PR → second commit
- **Workspace / seed / artifact:** where your group's work lives, and what stands in until it exists
- **Learn / Create / Grow:** the three acts of every notebook this week

<!--
Slide ID: D1-M01-C0
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 2
Layout: 02 Agenda 1
Speaker notes:
- Say: Four terms you will hear all week; this module is where three of them start.
- Ask: Which of these four do you already use daily, and which is new?
- Watch: Definitions are quoted from the course concept list; keep the same words in later modules rather than re-defining them.
- Then: Move into the workspace slide; the loop slides follow.
Sources: [Course concepts](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md); [Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md).
-->

---

# One endpoint, three compatible clients

<div style="display:flex;justify-content:center;margin-top:.35em">
<svg viewBox="0 0 720 190" width="900" role="img" aria-label="OpenAI, vLLM, and Ollama clients point to one OpenAI-compatible chat completions endpoint">
  <g text-anchor="middle">
    <rect x="260" y="18" width="200" height="58" rx="9" fill="#e8f0fe" stroke="#0284c7" stroke-width="2.5"/>
    <text x="360" y="43" font-size="15" font-weight="700" fill="#075985">POST /v1/chat/completions</text>
    <text x="360" y="62" font-size="12" fill="#0369a1">your endpoint</text>
    <rect x="24" y="118" width="170" height="54" rx="9" fill="#f1f5f9" stroke="#94a3b8" stroke-width="2"/>
    <text x="109" y="151" font-size="15" font-weight="700" fill="#334155">OpenAI</text>
    <rect x="275" y="118" width="170" height="54" rx="9" fill="#f1f5f9" stroke="#94a3b8" stroke-width="2"/>
    <text x="360" y="151" font-size="15" font-weight="700" fill="#334155">vLLM</text>
    <rect x="526" y="118" width="170" height="54" rx="9" fill="#f1f5f9" stroke="#94a3b8" stroke-width="2"/>
    <text x="611" y="151" font-size="15" font-weight="700" fill="#334155">Ollama</text>
  </g>
  <path d="M109 114 L300 79" stroke="#94a3b8" stroke-width="2" marker-end="url(#compat-arrow)"/>
  <path d="M360 114 V80" stroke="#94a3b8" stroke-width="2" marker-end="url(#compat-arrow)"/>
  <path d="M611 114 L420 79" stroke="#94a3b8" stroke-width="2" marker-end="url(#compat-arrow)"/>
  <defs><marker id="compat-arrow" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#94a3b8"/></marker></defs>
</svg>
</div>

Can Deskmate run against our own endpoint? **Yes — set `OPENAI_BASE_URL`.**

<!--
Slide ID: D1-M01-C0A
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: build
Minutes: 0
Layout: 02 Agenda 1
Speaker notes:
- Say: The client shape stays stable while the endpoint can be OpenAI, vLLM, or Ollama.
- Ask: What would you change for Priya's VPN question if the endpoint moved from a hosted service to your own server?
- Watch: Keep the answer operational: `OPENAI_BASE_URL` selects the compatible endpoint; the notebook also reads the model and key from environment variables.
- Then: Notebook:cell#9 — Task 1 introduces the provider-independent setup before the rest of the repo loop.
Sources: [Course concepts](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md); [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).
-->

---

# Every notebook has three acts

<div style="display:flex;justify-content:center;margin-top:.65em">
<svg viewBox="0 0 720 170" width="900" role="img" aria-label="Learn, Create, Grow: learn builds the weak version, create writes to workspace, grow discusses production">
  <g text-anchor="middle">
    <rect x="20" y="35" width="200" height="78" rx="9" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.5"/>
    <text x="120" y="68" font-size="19" font-weight="700" fill="#5b21b6">Learn</text>
    <text x="120" y="91" font-size="12.5" fill="#6d28d9">weak version first</text>
    <rect x="260" y="35" width="200" height="78" rx="9" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/>
    <text x="360" y="68" font-size="19" font-weight="700" fill="#92400e">Create</text>
    <text x="360" y="91" font-size="12.5" fill="#b45309">writes to workspace</text>
    <rect x="500" y="35" width="200" height="78" rx="9" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/>
    <text x="600" y="68" font-size="19" font-weight="700" fill="#075985">Grow</text>
    <text x="600" y="91" font-size="12.5" fill="#0369a1">what production needs</text>
  </g>
  <path d="M225 74 H255" stroke="#94a3b8" stroke-width="2" marker-end="url(#acts-arrow)"/>
  <path d="M465 74 H495" stroke="#94a3b8" stroke-width="2" marker-end="url(#acts-arrow)"/>
  <defs><marker id="acts-arrow" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#94a3b8"/></marker></defs>
</svg>
</div>

Skip Create and Thursday reads Deskmate's seed instead of your group's Priya transcripts.

<!--
Slide ID: D1-M01-C0B
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: build
Minutes: 0
Layout: 06 Process steps
Speaker notes:
- Say: Learn makes the idea visible, Create makes it yours, and Grow names what production would require.
- Ask: Which artifact would prove that your group has moved past the seed example?
- Watch: The middle act is the handoff: it writes group artifacts to `workspace/`; without it, later notebooks can run while still reading Deskmate's seed.
- Then: Notebook:cell#16 — Task 3 runs `ws.init()` and `ws.status()` so students can see the workspace boundary.
Sources: [Course concepts](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md); [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).
-->

---

# The workspace holds what your group produces

<div style="display:flex;gap:1.1em;align-items:flex-start">
<div style="flex:1">

- `workspace/` is yours, untracked

</div>
<div style="flex:1;font-size:.6em">

```text
$ uv run python scripts/check_workspace.py --status
manifest       seed   manifest.json
charter        seed   pitch/charter.md
prompts        seed   prompts/prompts.jsonl
transcripts    seed   transcripts/transcripts.jsonl
judge_scores   seed   evals/judge_scores.jsonl
```

</div>
</div>

Every row says `seed` on a fresh clone. That is correct, not broken.

<!--
Slide ID: D1-M01-C1-B1
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: build
Minutes: 0
Layout: 05 Two column
Speaker notes:
- Say: Build step 1 of 3 — reveal this point, then advance.
Sources: [Module 01 notebook, Task 3](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Workspace concepts](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md).

-->

---

# The workspace holds what your group produces

<div style="display:flex;gap:1.1em;align-items:flex-start">
<div style="flex:1">

- `workspace/` is yours, untracked
- `data/seed/` is the tracked worked example

</div>
<div style="flex:1;font-size:.6em">

```text
$ uv run python scripts/check_workspace.py --status
manifest       seed   manifest.json
charter        seed   pitch/charter.md
prompts        seed   prompts/prompts.jsonl
transcripts    seed   transcripts/transcripts.jsonl
judge_scores   seed   evals/judge_scores.jsonl
```

</div>
</div>

Every row says `seed` on a fresh clone. That is correct, not broken.

<!--
Slide ID: D1-M01-C1-B2
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: build
Minutes: 0
Layout: 05 Two column
Speaker notes:
- Say: Build step 2 of 3 — reveal this point, then advance.
Sources: [Module 01 notebook, Task 3](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Workspace concepts](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md).

-->

---

# The workspace holds what your group produces

<div style="display:flex;gap:1.1em;align-items:flex-start">
<div style="flex:1">

- `workspace/` is yours, untracked
- `data/seed/` is the tracked worked example
- An **artifact** is one named, schema-validated output

</div>
<div style="flex:1;font-size:.6em">

```text
$ uv run python scripts/check_workspace.py --status
manifest       seed   manifest.json
charter        seed   pitch/charter.md
prompts        seed   prompts/prompts.jsonl
transcripts    seed   transcripts/transcripts.jsonl
judge_scores   seed   evals/judge_scores.jsonl
```

</div>
</div>

Every row says `seed` on a fresh clone. That is correct, not broken.

<!--
Slide ID: D1-M01-C1
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 2
Layout: 05 Two column
Speaker notes:
- Say: The workspace holds what your group produces; the seed stands in until it does.
- Ask: If a notebook shows you data you do not recognise, what happened?
- Watch: Task 3 of 8 runs `ws.init()` then `ws.status()` (notebook cell#17) and prints a table whose rows read `seed` on a fresh clone.
- Then: Set the expectation that every row saying `seed` on Monday morning is correct, not broken.
Sources: [Module 01 notebook, Task 3](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Workspace concepts](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md).
-->

---

# Tell your work from the worked example

- **Ask:** If a notebook shows you data you do not recognise, what happened?
- **Inspect:** `uv run python scripts/check_workspace.py --status` — one row per artifact, each marked as yours or from the seed
- **Decide:** never hand-write a file in `workspace/`; run the notebook that writes it, or let the seed carry it

<!--
Slide ID: D1-M01-C1B
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 1
Layout: 04 Icon cards
Speaker notes:
- Say: The fallback is loud on purpose — `load()` prints a line when it falls back to the seed.
- Ask: Take the question on the slide as a show of hands, then let someone read the answer off their own `--status` output.
- Watch: Run `--status` live if the room is ready; otherwise show the table from notebook cell#17.
- Then: Name the rule that governs the rest of the week: a number you did not measure is not yours to defend.
Sources: [Module 01 notebook, Task 3](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Artifact integrity rules](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/AGENTS.md).
-->

---

# The repo keeps a history of the work

`spec → prompts → prompt history → checks + rubrics → results → docs`

- The spec says what needs to be built

> Source: [Module 01](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)

<!--
Slide ID: D1-M01-C2-B1
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: build
Minutes: 0
Layout: 06 Process steps
Speaker notes:
- Say: Build step 1 of 3 — reveal this point, then advance.
Sources: [Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Artifact integrity rules](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/AGENTS.md).

-->

---

# The repo keeps a history of the work

`spec → prompts → prompt history → checks + rubrics → results → docs`

- The spec says what needs to be built
- Prompts, checks, and rubrics make the work repeatable

> Source: [Module 01](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)

<!--
Slide ID: D1-M01-C2-B2
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: build
Minutes: 0
Layout: 06 Process steps
Speaker notes:
- Say: Build step 2 of 3 — reveal this point, then advance.
Sources: [Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Artifact integrity rules](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/AGENTS.md).

-->

---

# The repo keeps a history of the work

`spec → prompts → prompt history → checks + rubrics → results → docs`

- The spec says what needs to be built
- Prompts, checks, and rubrics make the work repeatable
- Results and docs give people and AI tools something to inspect and use

> Source: [Module 01](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)

<!--
Slide ID: D1-M01-C2
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: The repo keeps a history of the work, and `manifest.json` records which module wrote what, when.
- Ask: If an answer changes, which part of the history would you inspect first?
- Watch: The module README's header names what this notebook reads and writes: reads nothing, writes the manifest and the charter.
- Then: Point out that an SME reviewer in Phase 3 can read the manifest and see the same thing.
Sources: [Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Artifact integrity rules](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/AGENTS.md).
-->

---

# Where the project keeps its evidence

- **Ask:** If an answer changes, which part of the history would you inspect first?
- **Inspect:** the spec, the prompts, the saved results, and the reference docs each live in a known place
- **Decide:** `manifest.json` records which module wrote what and when — read it before you trust a number

<!--
Slide ID: D1-M01-C2B
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 1
Layout: 05 Two column 2
Speaker notes:
- Say: Your GitHub repo is itself a certification deliverable, so this history is graded.
- Ask: Push past the first answer — most people say the results; the spec and the prompts are usually where the change actually is.
- Watch: Show `project/CHARTER.md` and note that notebooks use the seed until its template marker is removed.
- Then: Leave the manifest on screen going into the fork slide — it is the evidence a reviewer reads.
Sources: [Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Charter template](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/project/CHARTER.md).
-->

---

# You work on a fork, not the course repo

<div style="display:flex;justify-content:center;margin-top:.4em">
<svg viewBox="0 0 620 170" width="880" role="img" aria-label="origin is your fork, which you push to; upstream is the course repository, which you fetch from">
  <rect x="10" y="46" width="176" height="74" rx="9" fill="#e8f0fe" stroke="#2563eb" stroke-width="2.5"/>
  <text x="98" y="76" font-size="17" font-weight="700" text-anchor="middle" fill="#1e3a8a">your fork</text>
  <text x="98" y="99" font-size="14" font-family="monospace" text-anchor="middle" fill="#334155">origin</text>
  <rect x="434" y="46" width="176" height="74" rx="9" fill="#f1f5f9" stroke="#64748b" stroke-width="2.5"/>
  <text x="522" y="76" font-size="17" font-weight="700" text-anchor="middle" fill="#0f172a">course repo</text>
  <text x="522" y="99" font-size="14" font-family="monospace" text-anchor="middle" fill="#334155">upstream</text>
  <path d="M188 68 H430" stroke="#2563eb" stroke-width="2.5" marker-end="url(#ar1)"/>
  <text x="309" y="58" font-size="14" text-anchor="middle" fill="#2563eb">push, then pull request</text>
  <path d="M430 100 H192" stroke="#64748b" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#ar2)"/>
  <text x="309" y="122" font-size="14" text-anchor="middle" fill="#475569">git fetch upstream</text>
  <text x="309" y="152" font-size="13" text-anchor="middle" fill="#64748b" font-style="italic">you have write access on the left, not the right</text>
  <defs>
    <marker id="ar1" markerWidth="10" markerHeight="10" refX="8.5" refY="3" orient="auto"><path d="M0 0 L8.5 3 L0 6 z" fill="#2563eb"/></marker>
    <marker id="ar2" markerWidth="10" markerHeight="10" refX="8.5" refY="3" orient="auto"><path d="M0 0 L8.5 3 L0 6 z" fill="#64748b"/></marker>
  </defs>
</svg>
</div>

<!--
Slide ID: D1-M01-C3
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 2
Layout: 05 Two column 1
Speaker notes:
- Say: Two remotes, two jobs. You push to your fork and send changes back as pull requests.
- Ask: You fetched upstream and your files did not change. Is something wrong?
- Watch: Task 1 (cell#10) adds `upstream` if it is missing, reading the slug from `cohort.toml`. Task 2 (cell#13) fetches, shows the last five upstream commits with `git log --oneline -5` and the branch's position with `git status -sb`, then only *prints* the fast-forward command, so students run the merge deliberately.
- Then: Note that fetching updates your copy of the remote branches without touching your working files.
Sources: [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow); [Module 01 notebook, Tasks 1-2](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).
-->

---

# A small change should have a clear history

<div style="display:flex;justify-content:center;margin-top:.3em">
<svg viewBox="0 0 660 130" width="900" role="img" aria-label="branch, then change, then read the diff, then commit">
  <g font-size="14" text-anchor="middle">
    <rect x="6" y="34" width="140" height="58" rx="8" fill="#e8f0fe" stroke="#2563eb" stroke-width="2"/>
    <text x="76" y="52" font-size="12" fill="#2563eb">STEP 1</text>
    <text x="76" y="72" font-weight="700" fill="#1e3a8a">branch</text>
    <rect x="176" y="34" width="140" height="58" rx="8" fill="#e8f0fe" stroke="#2563eb" stroke-width="2"/>
    <text x="246" y="52" font-size="12" fill="#2563eb">STEP 2</text>
    <text x="246" y="72" font-weight="700" fill="#1e3a8a">change</text>
    <rect x="346" y="34" width="140" height="58" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/>
    <text x="416" y="52" font-size="12" fill="#b45309">STEP 3</text>
    <text x="416" y="72" font-weight="700" fill="#92400e">read the diff</text>
    <rect x="516" y="34" width="140" height="58" rx="8" fill="#e8f0fe" stroke="#2563eb" stroke-width="2"/>
    <text x="586" y="52" font-size="12" fill="#2563eb">STEP 4</text>
    <text x="586" y="72" font-weight="700" fill="#1e3a8a">commit</text>
  </g>
  <path d="M148 63 H172" stroke="#94a3b8" stroke-width="2" marker-end="url(#s1)"/>
  <path d="M318 63 H342" stroke="#94a3b8" stroke-width="2" marker-end="url(#s1)"/>
  <path d="M488 63 H512" stroke="#94a3b8" stroke-width="2" marker-end="url(#s1)"/>
  <text x="416" y="112" font-size="13" text-anchor="middle" fill="#b45309" font-style="italic">the step your AI editor cannot do for you</text>
  <defs><marker id="s1" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#94a3b8"/></marker></defs>
</svg>
</div>

Branch name a reviewer can scan · commit as `type: summary`

<!--
Slide ID: D1-M01-C4
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes:
- Say: Keep `main` clean and do the work on a branch.
- Ask: Does committing a change mean that someone else has reviewed it?
- Watch: Task 4 (cell#21) creates `feat/<login>-daily-loop`; Task 6 (cell#27) stages, shows `git diff --staged`, then commits `docs: add <login> to members`.
- Then: The answer to the ask is no — committing records, reviewing is the pull request, which comes next.
Sources: [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow); [Module 01 notebook, Tasks 4-6](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).
-->

---

# Four things to check before you share

- **Ask:** Does committing a change mean that someone else has reviewed it?
- **Inspect:** where you are, which branch, what the diff says, and where it is going
- **Decide:** stop if the diff holds files you did not mean to touch, or the remote is unfamiliar

<!--
Slide ID: D1-M01-C4B
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: The branch name and the commit message are the two things a reviewer reads first.
- Ask: Expect a split on the slide's question. The answer is no: committing records, reviewing is the pull request.
- Watch: Before class, students were asked to read the last five commit messages on a repo they work in and mark which a reviewer could scan. Ask for one example.
- Then: That split is the hand-off — the next slide is the pull request, where review actually happens.
Sources: [Module 01 before-you-arrive](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).
-->

---

# Review the change, not just the successful run

<div style="display:flex;gap:1.1em;align-items:flex-start">
<div style="flex:1">

- Check intended files and destinations

</div>
<div style="flex:1.25;font-size:.62em">

```diff
  def deploy_agent():
      destination = "/shared/exports/v1"
-     api_key = "sk-prod-8f921a99b01c"
+     api_key = os.getenv("SECRET_API_KEY")
      validate_schema(destination)
```

</div>
</div>

> The green run and the safe run are not the same run.

<!--
Slide ID: D1-M01-C5-B1
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: build
Minutes: 0
Layout: 05 Two column 1
Speaker notes:
- Say: Build step 1 of 3 — reveal this point, then advance.
Sources: [Module 01 notebook, Task 6](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Keys and endpoints](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/00_Setup/keys.md).

-->

---

# Review the change, not just the successful run

<div style="display:flex;gap:1.1em;align-items:flex-start">
<div style="flex:1">

- Check intended files and destinations
- Keep credentials out of history

</div>
<div style="flex:1.25;font-size:.62em">

```diff
  def deploy_agent():
      destination = "/shared/exports/v1"
-     api_key = "sk-prod-8f921a99b01c"
+     api_key = os.getenv("SECRET_API_KEY")
      validate_schema(destination)
```

</div>
</div>

> The green run and the safe run are not the same run.

<!--
Slide ID: D1-M01-C5-B2
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: build
Minutes: 0
Layout: 05 Two column 1
Speaker notes:
- Say: Build step 2 of 3 — reveal this point, then advance.
Sources: [Module 01 notebook, Task 6](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Keys and endpoints](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/00_Setup/keys.md).

-->

---

# Review the change, not just the successful run

<div style="display:flex;gap:1.1em;align-items:flex-start">
<div style="flex:1">

- Check intended files and destinations
- Keep credentials out of history
- Preserve enough context to repeat it

</div>
<div style="flex:1.25;font-size:.62em">

```diff
  def deploy_agent():
      destination = "/shared/exports/v1"
-     api_key = "sk-prod-8f921a99b01c"
+     api_key = os.getenv("SECRET_API_KEY")
      validate_schema(destination)
```

</div>
</div>

> The green run and the safe run are not the same run.

<!--
Slide ID: D1-M01-C5
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 2
Layout: 05 Two column 1
Speaker notes:
- Say: This is the step where your AI editor does most of the typing, which is exactly why you read the diff.
- Ask: What would a reviewer need beyond a screenshot of the answer?
- Watch: The prior cohort's illustration is worth reusing: a diff replacing a hard-coded `sk-prod-...` key with `os.getenv`. The repo's own rule is that `.env` is never committed, `make scrub` strips keys from notebook outputs, and CI fails if one gets through.
- Then: The notebook asks this as a question cell (cell#29) and the answer belongs to the student.
Sources: [Module 01 notebook, Task 6](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Keys and endpoints](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/00_Setup/keys.md).
-->

---

# Explain the change to someone who was not there

- **Ask:** What would a reviewer need beyond a screenshot of the answer?
- **Inspect:** walk a teammate through the edit and the evidence you saved for it
- **Decide:** if you cannot explain why a line changed, do not ask anyone to review it yet

<!--
Slide ID: D1-M01-C5B
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes:
- Say: A reviewer needs the diff, the destination, and enough context to rerun the comparison.
- Ask: Have one pair actually try it out loud for thirty seconds; the gaps surface fast.
- Watch: Point at the diff, not the output. A green run with an unreviewed diff is the failure mode.
- Then: Keep the rule for the notebook: the AI editor types, you still read the diff before Task 6 commits it.
Sources: [Module 01 notebook, Task 6](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Keys and endpoints](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/00_Setup/keys.md).
-->

---

# The pull request is the unit of review

```bash
git push -u origin feat/<you>-daily-loop   # -u links branch to your fork
gh pr create --base main --head feat/<you>-daily-loop --draft
```

- Then commit again and push: the **same** pull request picks it up

> One pull request, two commits.

<!--
Slide ID: D1-M01-C6-B1
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: build
Minutes: 0
Layout: 06 Process steps 1
Speaker notes:
- Say: Build step 1 of 2 — reveal this point, then advance.
Sources: [Module 01 notebook, Tasks 7-8](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).

-->

---

# The pull request is the unit of review

```bash
git push -u origin feat/<you>-daily-loop   # -u links branch to your fork
gh pr create --base main --head feat/<you>-daily-loop --draft
```

- Then commit again and push: the **same** pull request picks it up
- That is how you answer a reviewer — not by opening a second PR

> One pull request, two commits.

<!--
Slide ID: D1-M01-C6
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 3
Layout: 06 Process steps 1
Speaker notes:
- Say: The pull request keeps tracking its branch, so it picks up whatever you push next.
- Ask: Predict what Task 8 prints. The notebook makes a second commit and pushes it — how many pull requests exist afterwards?
- Watch: Task 7 (cell#31) pushes and opens a draft PR against the student's own fork; Task 8 (cell#34) commits again and prints a commit count of 2. One pull request, two commits.
- Then: The demo targets their own fork, so it is safe to rerun; the cleanup cell (cell#39) closes the PR and deletes the branch. If someone's count reads 3 or more, they reran Task 8 without cleanup — cell#34 appends its line unconditionally.
Sources: [Module 01 notebook, Tasks 7-8](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).
-->

---

# Two setup traps that cost the most time

```bash
make setup       # keeps optional groups. a bare `uv sync` REMOVES them
make preflight   # each host: open | intercepted | blocked
make check-day   # fails on everything before you save work — expected
```

- `uv sync` and `uv run --group` are **exact**: they remove every group you do not name

<!--
Slide ID: D1-M01-C7-B1
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: build
Minutes: 0
Layout: 04 Icon cards
Speaker notes:
- Say: Build step 1 of 2 — reveal this point, then advance.
Sources: [Setup and troubleshooting](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/00_Setup/README.md); [Course concepts, setup traps](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md).

-->

---

# Two setup traps that cost the most time

```bash
make setup       # keeps optional groups. a bare `uv sync` REMOVES them
make preflight   # each host: open | intercepted | blocked
make check-day   # fails on everything before you save work — expected
```

- `uv sync` and `uv run --group` are **exact**: they remove every group you do not name
- `intercepted` means a proxy signs the certs — your terminal trusts it, a container will not

<!--
 keep the ordering: the first line is the one that prevents the most lost time -->

<!--
Slide ID: D1-M01-C7
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 3
Layout: 04 Icon cards
Speaker notes:
- Say: These three lines prevent most of the time the room would otherwise lose.
- Ask: A notebook that worked an hour ago now fails with `ModuleNotFoundError`. What changed?
- Watch: The answer is almost always that a bare `uv sync` or `uv run --group dev` removed an optional group. Fix: `make setup`, which keeps the groups already installed.
- Then: For an intercepted host, the terminal works because the machine trusts the private CA, but a container will not — keep the CA file to hand.
Sources: [Setup and troubleshooting](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/00_Setup/README.md); [Course concepts, setup traps](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md).
-->

---

# How to survive a notebook

- Every cell prints the command it ran, as `$ git …`, then that command's output

<!--
Slide ID: D1-M01-C8-B1
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: build
Minutes: 0
Layout: 04 Icon cards
Speaker notes:
- Say: Build step 1 of 4 — reveal this point, then advance.
Sources: [Course concepts, laptop setup floor](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md); [Module 01 notebook, Setup cell](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).

-->

---

# How to survive a notebook

- Every cell prints the command it ran, as `$ git …`, then that command's output
- **Run cells in order, top to bottom.** Half of all "it broke" is stale kernel state

<!--
Slide ID: D1-M01-C8-B2
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: build
Minutes: 0
Layout: 04 Icon cards
Speaker notes:
- Say: Build step 2 of 4 — reveal this point, then advance.
Sources: [Course concepts, laptop setup floor](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md); [Module 01 notebook, Setup cell](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).

-->

---

# How to survive a notebook

- Every cell prints the command it ran, as `$ git …`, then that command's output
- **Run cells in order, top to bottom.** Half of all "it broke" is stale kernel state
- If a cell fails: read the last line, fix it, rerun *that* cell — not the whole notebook

<!--
Slide ID: D1-M01-C8-B3
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: build
Minutes: 0
Layout: 04 Icon cards
Speaker notes:
- Say: Build step 3 of 4 — reveal this point, then advance.
Sources: [Course concepts, laptop setup floor](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md); [Module 01 notebook, Setup cell](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).

-->

---

# How to survive a notebook

- Every cell prints the command it ran, as `$ git …`, then that command's output
- **Run cells in order, top to bottom.** Half of all "it broke" is stale kernel state
- If a cell fails: read the last line, fix it, rerun *that* cell — not the whole notebook
- `gh auth status` failing is the first hard stop: fix it in a terminal, then rerun

<!--
Slide ID: D1-M01-C8
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: This is the first notebook of the week, so these habits are worth thirty seconds now rather than an hour later.
- Ask: A cell you have already run succeeds, you edit a cell above it, rerun only the lower one — is the state what you think it is?
- Watch: The `sh()` helper in cell#6 wraps `subprocess.run` and prints `$ <command>` plus stdout and stderr, so students can always see exactly what ran. Cell#6 also captures their GitHub login and the repo root, and raises if `gh auth status` says they are not logged in.
- Then: Every task cell in this notebook ends with a line telling you what you should have seen; if you did not see it, stop there rather than running on.
Sources: [Course concepts, laptop setup floor](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md); [Module 01 notebook, Setup cell](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).
-->

---

# Optional: make review a system property

- Required checks can block known failures
- Named reviewers keep ownership visible
- Version evidence alongside the change

<!--
Slide ID: D1-M01-R1
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah
Type: optional
Minutes: 0
Layout: 04 Icon cards
Speaker notes:
- Say: Optional: make review a system property
- Ask: Which failure would your current checks miss even if every check passed?
- Watch: The notebook's Grow section (cell#41) pairs each thing done by hand today with what production does automatically: branch protection, required checks, `CODEOWNERS`, a bot that syncs forks.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches); [Module 01 Grow section, cell#41](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).
-->

---

# Before and after class reading

**Before (required)**
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow) — the loop this module runs
- [Setup guide](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/00_Setup/README.md) — tools, keys, `make setup`, `make preflight`
- Bring a list: the last five commit messages from a repo you work in, marked for whether a reviewer could scan them

**After (optional)**
- [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)

<!--
Slide ID: D1-M01-RD1
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah
Type: reading
Minutes: 1
Layout: 02 Agenda 1
Speaker notes:
- Say: One required link, one required setup document, one exercise you were asked to bring.
- Ask: Who brought the five commit messages? Take one example and read it aloud.
- Watch: The course reading guide has no entry for this module; these come from the module README's "Before you arrive" and from the setup guide.
- Then: Hold the protected-branches link for anyone who finishes the notebook early.
Sources: [Module 01 before-you-arrive](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Setup guide](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/00_Setup/README.md).
-->

---

# Resources

- [Module 01 README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md) and [notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb)
- [Setup](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/00_Setup/README.md) · [keys](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/00_Setup/keys.md) · [mac](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/00_Setup/mac.md) · [windows](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/00_Setup/windows.md)
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow) · [GitHub CLI](https://cli.github.com) · [uv install](https://docs.astral.sh/uv/getting-started/installation/) · [git downloads](https://git-scm.com/downloads)
- [Course concepts](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md)

<!--
Slide ID: D1-M01-RS1
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah
Type: resources
Minutes: 1
Layout: 02 Agenda 1
Speaker notes:
- Say: Everything on this slide is in the repo or is official documentation.
- Ask: Anyone still blocked on setup? Now is the moment, not tomorrow morning.
- Watch: The mac and windows pages are the ones people skip and then need: Intel wheel pins, Git Bash or WSL, long paths.
- Then: Point at office hours after wrap for anything unresolved.
Sources: [Setup guide](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/00_Setup/README.md); [Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md).
-->

---

# Check your understanding

1. Which remote do you push to, and which do you pull course updates from?
2. You run `--status` and every row says `seed`. Is that a problem?
3. You make a second commit on the branch and push. How many pull requests are open?
4. A notebook that worked yesterday now fails with `ModuleNotFoundError`. What is the first thing you check?
5. Name one thing you did by hand today that production would enforce automatically.

<!--
Slide ID: D1-M01-Q1
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah
Type: check
Minutes: 3
Layout: 02 Agenda 1
Speaker notes:
- Say: Five questions; answer them out loud at your table before the notebook.
- Ask: Take question 3 as a show of hands first, then explain.
- Watch: Answers — (1) push to `origin`, your fork; pull from `upstream`, the course repo. (2) No: on a fresh clone every artifact resolves to the seed, which is how notebooks run standalone. (3) One; a pull request tracks its branch. (4) Whether a bare `uv sync` or `--group` removed an optional group, then `make setup`. (5) Branch protection, required checks, or `CODEOWNERS`.
- Then: Hand over to the notebook; the eight tasks run the loop end to end.
Sources: [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Course concepts](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md).
-->

---

# A prompt is the brief for one request

- State the task and intended audience
- Supply the facts the model cannot know directly
- Define the answer you need back

<!--
Slide ID: D1-M02-C1
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: A prompt is the brief for one request
- Ask: What important fact would the model be forced to guess if it is not in the prompt?
- Watch: Eli begins with the same question and shows how each prompt pattern changes the request.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb).
-->

---

# Few-shot: show the behavior you want

- Give two or three examples of good inputs and outputs
- Demonstrate conventions the model cannot infer
- Change the examples when the behavior changes

> **Paper finding:** “Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches.” — Brown et al. (2020)

<!--
Slide ID: D1-M02-C2
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli, code walkthrough
Type: core
Minutes: 2
Layout: 08 Quote
Speaker notes:
- Say: Few-shot: show the behavior you want
- Ask: What behavior would you demonstrate with an example rather than describe in another paragraph?
- Watch: Eli compares a prompt with no examples against one with examples while holding the question and evidence constant.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [Few-shot learners, Brown et al., 2020](https://arxiv.org/abs/2005.14165); [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb).
-->

---

# Context supplies the facts the model cannot know

- Add the relevant policy, record, or project detail
- Give the model enough context for this question
- Remove irrelevant or unauthorized information

<!--
Slide ID: D1-M02-C3
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli, code walkthrough
Type: core
Minutes: 2
Layout: 05 Two column
Speaker notes:
- Say: Context supplies the facts the model cannot know
- Ask: What fact would the model otherwise have to guess?
- Watch: Eli compares the same prompt with and without a supplied policy excerpt.
- Then: Carry the observation into the next exercise.
Sources: [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb); [The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/).
-->

---

# Persona and format shape the answer

- Persona: set the viewpoint and audience
- Format: define the fields a person or program needs
- Remember: a good shape can still contain a wrong value

<!--
Slide ID: D1-M02-C4
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli, code walkthrough
Type: core
Minutes: 2
Layout: 05 Two column 1
Speaker notes:
- Say: Persona and format shape the answer
- Ask: Which part of the prompt changes the reader, and which part changes the shape of the answer?
- Watch: Eli compares persona and structured-output variants and checks factual content separately from voice and formatting.
- Then: Carry the observation into the next exercise.
Sources: [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb); [Author's semantic-contract notes](https://github.com/soypete/ctx-eng-book/blob/main/research/semantic-contracts.md).
-->

---

# A schema makes the shape a contract

Asking politely for JSON works most of the time. Most of the time is not good enough for code that calls `json.loads`. A schema makes the shape a contract.

Marcus needs a field he can sort a queue by: `risk_level` is sortable; prose is not.

<!--
Slide ID: D1-M02-C4A
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli, code walkthrough
Type: core
Minutes: 2
Layout: 08 Quote
Speaker notes:
- Say: Structured output is a boundary between a model response and code that has to use it.
- Ask: Which part of Marcus's queue would become unreliable if risk arrived as free text?
- Watch: Keep the distinction sharp: a schema guarantees shape and allowed values, not factual correctness.
- Then: Notebook:cell#20 — Task 4 introduces the structured-output contract in the notebook's own prose.
Sources: [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb); [Course concepts](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md).
-->

---

# Put the contract in code

```python
class ProductBrief(BaseModel):
    product_name: str
    problem: str
    users: List[str]
    must_do: List[str]
    must_not_do: List[str]
    risk_level: Literal["low", "medium", "high"]
```

```python
result = client.chat.completions.parse(
    model=MODEL,
    messages=[...],
    response_format=ProductBrief,
)
```

<!--
Slide ID: D1-M02-C4AB
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli, code walkthrough
Type: core
Minutes: 2
Layout: 09 Lab and code
Speaker notes:
- Say: The typed object gives the caller a stable shape and makes `risk_level` one of three values.
- Ask: Where would you validate a field whose value is shaped correctly but factually wrong?
- Watch: Point to `response_format=ProductBrief`; the parser is part of the call contract, not a prompt suggestion.
- Then: Notebook:cell#21 — run the model's typed `ProductBrief` parse before comparing patterns.
Sources: [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb); [Course concepts](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md).
-->

---

# Chain of thought makes difficult work explicit

- Break the task into smaller, checkable steps
- Ask for assumptions, calculations, and evidence
- Check the result outside the model

> Source: [Chain-of-thought prompting](https://arxiv.org/abs/2201.11903)

<!--
Slide ID: D1-M02-C5
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli, code walkthrough
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: Chain of thought makes difficult work explicit
- Ask: Which step could you verify independently?
- Watch: Eli compares a direct answer with a structured answer that exposes checkable work.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [Chain-of-thought prompting, Wei et al., 2022](https://arxiv.org/abs/2201.11903); [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb).
-->

---

# Spend a reasoning budget deliberately

- Compare no explicit reasoning against a high budget
- Read the token counts and the time cost
- Keep the trap question and evidence fixed

> More effort costs more tokens and more time.

Deskmate can spend more effort on Priya's VPN question—but measure the cost.

<!--
Slide ID: D1-M02-C6
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli, code walkthrough
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes:
- Say: A reasoning budget is a model setting with a measurable cost.
- Ask: What evidence would justify spending more tokens on Priya's VPN question?
- Watch: Hold the question and model constant; compare the token counts and latency before deciding whether more effort helped.
- Then: Notebook:cell#17 — Task 3 is the reasoning-budget comparison, not a tool-use loop.
Sources: [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb); [Course concepts](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md).
-->

---

# Self-refine changes the answer; meta-prompting changes the brief

- **Self-refine:** draft → critique → revise the answer
- **Meta-prompting:** inspect the task → improve the prompt
- Re-run the same cases; stop when the criterion is met

> Source: [Self-Refine](https://arxiv.org/abs/2303.17651)

<!--
Slide ID: D1-M02-C7
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli, code walkthrough
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes:
- Say: Self-refine changes the answer; meta-prompting changes the brief
- Ask: Did the revision improve the answer, the prompt, or both—and what evidence shows that?
- Watch: Put the named artifact on screen and trace where its values came from.
- Then: Compare the revision against the same criteria.
Sources: [Self-Refine, Madaan et al., 2023](https://arxiv.org/abs/2303.17651); [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb).
-->

---

# Compare patterns like an experiment

- Hold the question, evidence, model, and criteria constant
- Change one pattern at a time: examples, context, format, or reasoning
- Record quality, consistency, time, and cost before choosing

> Source: [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb)

<!--
Slide ID: D1-M02-C8
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli, code walkthrough
Type: core
Minutes: 1
Layout: 09 Lab and code
Speaker notes:
- Say: Compare patterns like an experiment
- Ask: If prompt B wins one case but loses another, what would you inspect before choosing it?
- Watch: Put the named artifact on screen and trace where its values came from.
- Then: If the next step depends on an observation or tool result, investigate an agent.
Sources: [Prompt patterns Create/Grow](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb); [Simple workflows versus agents](https://www.anthropic.com/engineering/building-effective-agents).
-->

---

# Optional: from examples to measured refinement

- Brown et al.: examples supplied at inference time
- Wei et al.: reasoning demonstrations on tested tasks
- Madaan et al.: feedback and revision loops

<!--
Slide ID: D1-M02-R1
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes:
- Say: Optional: from examples to measured refinement
- Ask: Which of these mechanisms would address your observed error, and which would not?
- Watch: Optional reading, not an extra optimization module.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [Brown et al., 2020](https://arxiv.org/abs/2005.14165); [Wei et al., 2022](https://arxiv.org/abs/2201.11903); [Madaan et al., 2023](https://arxiv.org/abs/2303.17651).
-->

---
# From prompt to agent: why the loop exists

<div style="display:flex;justify-content:center;margin-top:.15em">
<svg viewBox="0 0 760 210" width="920" role="img" aria-label="Four stages: a direct prompt, chain-of-thought which improves reasoning, Toolformer which shows models can call tools, and the harness where your code owns the tools">
  <g text-anchor="middle">
    <rect x="6" y="40" width="170" height="82" rx="9" fill="#f1f5f9" stroke="#94a3b8" stroke-width="2"/>
    <text x="91" y="62" font-size="11.5" fill="#64748b">ASK</text>
    <text x="91" y="83" font-size="14.5" font-weight="700" fill="#0f172a">direct prompt</text>
    <text x="91" y="104" font-size="11.5" fill="#475569">one call, one answer</text>

    <rect x="196" y="40" width="170" height="82" rx="9" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
    <text x="281" y="62" font-size="11.5" fill="#0369a1">THINK</text>
    <text x="281" y="83" font-size="14.5" font-weight="700" fill="#075985">chain of thought</text>
    <text x="281" y="104" font-size="11.5" fill="#0369a1">steps, still no facts</text>

    <rect x="386" y="40" width="170" height="82" rx="9" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
    <text x="471" y="62" font-size="11.5" fill="#15803d">ACT</text>
    <text x="471" y="83" font-size="14.5" font-weight="700" fill="#14532d">tool use</text>
    <text x="471" y="104" font-size="11.5" fill="#15803d">reach outside the model</text>

    <rect x="576" y="40" width="178" height="82" rx="9" fill="#fef3c7" stroke="#d97706" stroke-width="3"/>
    <text x="665" y="62" font-size="11.5" fill="#b45309">GOVERN</text>
    <text x="665" y="83" font-size="14.5" font-weight="700" fill="#92400e">the harness</text>
    <text x="665" y="104" font-size="11.5" fill="#b45309">your code authorizes</text>
  </g>
  <path d="M178 81 H192" stroke="#94a3b8" stroke-width="2" marker-end="url(#e1)"/>
  <path d="M368 81 H382" stroke="#94a3b8" stroke-width="2" marker-end="url(#e1)"/>
  <path d="M558 81 H572" stroke="#94a3b8" stroke-width="2" marker-end="url(#e1)"/>
  <g font-size="11" text-anchor="middle" fill="#64748b">
    <text x="281" y="140">Wei et al. 2022</text>
    <text x="471" y="140">Toolformer, Schick et al. 2023</text>
    <text x="665" y="140">where this course lives</text>
  </g>
  <text x="380" y="176" font-size="13" text-anchor="middle" fill="#0f172a">Reasoning alone cannot look anything up. Tool use can — but something must decide if it is allowed.</text>
  <text x="380" y="198" font-size="12.5" text-anchor="middle" fill="#92400e" font-style="italic">Toolformer taught the model to call tools. We keep the tools in code we own.</text>
  <defs><marker id="e1" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#94a3b8"/></marker></defs>
</svg>
</div>

<!--
Slide ID: D1-M03-C0
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric
Type: core
Minutes: 3
Layout: 06 Process steps
Speaker notes:
- Say: You just spent thirty minutes on prompting. This is what prompting cannot do, and why the next thing is a loop.
- Ask: Module 02's best prompt still cannot answer "what does our charter say about refunds". What is missing — better reasoning, or access?
- Watch: Chain of thought made the model's reasoning explicit and measurably better on hard tasks, but a reasoning step cannot retrieve a fact the model was never given. Toolformer showed models can learn to call an API mid-generation — that is the "why agents" moment. The difference here: Toolformer trained tool calls into the weights; we keep tools in code, so the harness can authorize, budget, and log every call.
- Then: Hand into the loop diagram — the amber GOVERN box is the next slide, drawn in detail.
Sources: [Chain-of-thought prompting, Wei et al., 2022](https://arxiv.org/abs/2201.11903); [Toolformer, Schick et al., 2023](https://arxiv.org/abs/2302.04761); [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
-->
---

# A model answers; an agent can choose a next step

<div style="display:flex;justify-content:center;margin-top:.2em">
<svg viewBox="0 0 700 250" width="900" role="img" aria-label="An agent loop: the model requests a tool, your code authorizes and runs it, the observation returns to the model, and the loop exits with an answer, a clarification, a refusal, or an exhausted budget">
  <rect x="2" y="2" width="696" height="196" rx="12" fill="none" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="7 5"/>
  <text x="14" y="22" font-size="13" fill="#64748b" font-style="italic">the harness — yours, not the model's</text>

  <rect x="36" y="74" width="152" height="66" rx="9" fill="#ede9fe" stroke="#7c3aed" stroke-width="2.5"/>
  <text x="112" y="101" font-size="16" font-weight="700" text-anchor="middle" fill="#5b21b6">model</text>
  <text x="112" y="122" font-size="12.5" text-anchor="middle" fill="#6d28d9">picks a next step</text>

  <rect x="274" y="74" width="152" height="66" rx="9" fill="#fef3c7" stroke="#d97706" stroke-width="3"/>
  <text x="350" y="99" font-size="15.5" font-weight="700" text-anchor="middle" fill="#92400e">your code</text>
  <text x="350" y="120" font-size="12.5" text-anchor="middle" fill="#b45309">authorizes + runs</text>

  <rect x="512" y="74" width="152" height="66" rx="9" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/>
  <text x="588" y="101" font-size="16" font-weight="700" text-anchor="middle" fill="#075985">tool</text>
  <text x="588" y="122" font-size="12.5" text-anchor="middle" fill="#0369a1">does the work</text>

  <path d="M190 96 H270" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#g1)"/>
  <text x="230" y="87" font-size="11.5" text-anchor="middle" fill="#7c3aed">tool call</text>
  <path d="M428 96 H508" stroke="#d97706" stroke-width="2.5" marker-end="url(#g2)"/>
  <path d="M508 126 H432" stroke="#0284c7" stroke-width="2.5" marker-end="url(#g3)"/>
  <text x="470" y="146" font-size="11.5" text-anchor="middle" fill="#0369a1">result</text>
  <path d="M274 130 H194" stroke="#0284c7" stroke-width="2.5" marker-end="url(#g3)"/>
  <text x="234" y="150" font-size="11.5" text-anchor="middle" fill="#0369a1">observation</text>

  <path d="M112 146 V176 H350" stroke="#94a3b8" stroke-width="2" fill="none" marker-end="url(#g4)"/>
  <text x="240" y="192" font-size="12" text-anchor="middle" fill="#475569">loop again, or exit</text>

  <text x="350" y="228" font-size="13.5" text-anchor="middle" fill="#0f172a" font-weight="600">exit: answer · clarify · decline · budget exhausted</text>
  <defs>
    <marker id="g1" markerWidth="10" markerHeight="10" refX="8.5" refY="3" orient="auto"><path d="M0 0 L8.5 3 L0 6 z" fill="#7c3aed"/></marker>
    <marker id="g2" markerWidth="10" markerHeight="10" refX="8.5" refY="3" orient="auto"><path d="M0 0 L8.5 3 L0 6 z" fill="#d97706"/></marker>
    <marker id="g3" markerWidth="10" markerHeight="10" refX="8.5" refY="3" orient="auto"><path d="M0 0 L8.5 3 L0 6 z" fill="#0284c7"/></marker>
    <marker id="g4" markerWidth="10" markerHeight="10" refX="8.5" refY="3" orient="auto"><path d="M0 0 L8.5 3 L0 6 z" fill="#94a3b8"/></marker>
  </defs>
</svg>
</div>

A tool call is a **request**. The amber box decides whether it happens.

<!--
Slide ID: D1-M03-C1
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: A model answers; an agent can choose a next step
- Ask: Which box actually runs a tool, and which box decides whether it is allowed?
- Watch: In Beric's trace, locate the model message requesting a tool, the tool result, and the subsequent model response.
- Then: Carry the observation into the next exercise.
Sources: [Agent harness notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Workflow and agent definitions](https://www.anthropic.com/engineering/building-effective-agents).
-->

---

# Find the tool call in the trace
- **Ask:** Which box actually runs a tool, and which box decides whether it is allowed?
- **Inspect:** In the trace, locate the model message requesting a tool, the tool result, and the model's response to it — the purple, blue, and purple boxes from the previous slide, in that order.
- **Decide:** If you cannot point at the tool request in the trace, you have a model, not an agent.

<!--
Slide ID: D1-M03-C1B
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: A model answers; an agent can choose a next step
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: In Beric's trace, locate the model message requesting a tool, the tool result, and the subsequent model response.
- Then: If you cannot point at the tool request in the trace, you have a model, not an agent.
Sources: [Agent harness notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Workflow and agent definitions](https://www.anthropic.com/engineering/building-effective-agents).
-->

---

# Tools give the loop controlled capabilities

- A tool contract names an action and its inputs
- Observations give the next step new evidence
- A tool call is a request; it is not proof that the action succeeded
- Read access and write permission are different

<!--
Slide ID: D1-M03-C2
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: Tools give the loop controlled capabilities
- Ask: If a retrieved page says “ignore your rules,” does that change the tool's permissions?
- Watch: Inspect how precise tool descriptions affect tool selection; do not equate making a tool call with making the correct call.
- Then: Carry the observation into the next exercise.
Sources: [ReAct, Yao et al., 2022](https://arxiv.org/abs/2210.03629); [Agent harness tools](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb).
-->

---

# The description is all the model sees
- **Ask:** If a retrieved page says “ignore your rules,” does that change the tool's permissions?
- **Inspect:** Inspect how precise tool descriptions affect tool selection; do not equate making a tool call with making the correct call.
- **Decide:** Fix the tool contract before you touch the prompt — the description is all the model sees.

<!--
Slide ID: D1-M03-C2B
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes:
- Say: Tools give the loop controlled capabilities
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Inspect how precise tool descriptions affect tool selection; do not equate making a tool call with making the correct call.
- Then: Fix the tool contract before you touch the prompt — the description is all the model sees.
Sources: [ReAct, Yao et al., 2022](https://arxiv.org/abs/2210.03629); [Agent harness tools](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb).
-->

---

# The harness owns the loop's boundaries

- Instructions define the job and permitted scope
- Budgets and approvals constrain execution
- Exits include answer, clarify, decline, or budget exhausted
- A trace records requests, results, and exits

<!--
Slide ID: D1-M03-C3
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes:
- Say: The harness owns the loop's boundaries
- Ask: What should the user receive when the budget ends before the task is complete?
- Watch: Watch middleware messages and the enforced limit; inspect the saved transcript rather than only the final answer.
- Then: Carry the observation into the next exercise.
Sources: [Agent harness limits and trace](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
-->

---

# Watch a limit actually fire
- **Ask:** What should the user receive when the budget ends before the task is complete?
- **Inspect:** Watch middleware messages and the enforced limit; inspect the saved transcript rather than only the final answer.
- **Decide:** A limit only counts if the transcript shows it firing. Untested limits are decoration.

<!--
Slide ID: D1-M03-C3B
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: The harness owns the loop's boundaries
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Watch middleware messages and the enforced limit; inspect the saved transcript rather than only the final answer.
- Then: A limit only counts if the transcript shows it firing. Untested limits are decoration.
Sources: [Agent harness limits and trace](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
-->

---

# Autonomy needs a reason and a stopping rule

- Use a loop when observations change the plan
- Stop for missing evidence, permission, or budget
- Keep a simpler workflow when the path is already known
- Judge the outcome and the route taken

<!--
Slide ID: D1-M03-C4
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 05 Two column 3
Speaker notes:
- Say: Autonomy needs a reason and a stopping rule
- Ask: What observation would change the next step in your proposed loop?
- Watch: Compare in-scope, human-needed, and out-of-scope questions. Check whether tool behavior matches the scope before praising fluency.
- Then: A diagnosis needing an initial symptom, a search, and a follow-up question may benefit from adaptation.
Sources: [Agent harness Create/Grow](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
-->

---

# In scope, needs a human, or out of scope
- **Ask:** What observation would change the next step in your proposed loop?
- **Inspect:** Compare in-scope, human-needed, and out-of-scope questions. Check whether tool behavior matches the scope before praising fluency.
- **Decide:** Give the loop a stopping rule before you give it autonomy.

<!--
Slide ID: D1-M03-C4B
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes:
- Say: Autonomy needs a reason and a stopping rule
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Compare in-scope, human-needed, and out-of-scope questions. Check whether tool behavior matches the scope before praising fluency.
- Then: Give the loop a stopping rule before you give it autonomy.
Sources: [Agent harness Create/Grow](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
-->

---
# An agentic system is the loop plus everything around it

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 760 290" width="920" role="img" aria-label="The agent loop at the centre, surrounded by retrieval, memory, guardrails, and evaluation, each labelled with the module that covers it">
  <rect x="196" y="96" width="368" height="96" rx="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="3"/>
  <text x="380" y="124" font-size="16" font-weight="700" text-anchor="middle" fill="#5b21b6">the agent loop</text>
  <text x="380" y="147" font-size="13" text-anchor="middle" fill="#6d28d9">model → tool call → your code → observation</text>
  <text x="380" y="173" font-size="12" text-anchor="middle" fill="#7c3aed" font-style="italic">module 03 · today</text>

  <rect x="12" y="20" width="164" height="62" rx="9" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <text x="94" y="45" font-size="14.5" font-weight="700" text-anchor="middle" fill="#075985">retrieval</text>
  <text x="94" y="65" font-size="11.5" text-anchor="middle" fill="#0369a1">modules 05 · 06 · 07</text>

  <rect x="584" y="20" width="164" height="62" rx="9" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="666" y="45" font-size="14.5" font-weight="700" text-anchor="middle" fill="#14532d">memory</text>
  <text x="666" y="65" font-size="11.5" text-anchor="middle" fill="#15803d">module 10</text>

  <rect x="12" y="206" width="164" height="62" rx="9" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="94" y="231" font-size="14.5" font-weight="700" text-anchor="middle" fill="#7f1d1d">guardrails</text>
  <text x="94" y="251" font-size="11.5" text-anchor="middle" fill="#b91c1c">modules 13 · 18</text>

  <rect x="584" y="206" width="164" height="62" rx="9" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="666" y="231" font-size="14.5" font-weight="700" text-anchor="middle" fill="#92400e">evaluation</text>
  <text x="666" y="251" font-size="11.5" text-anchor="middle" fill="#b45309">modules 04 · 09</text>

  <path d="M176 58 C 240 58, 214 96, 258 96" stroke="#0284c7" stroke-width="2" fill="none" marker-end="url(#a1)"/>
  <path d="M584 58 C 520 58, 546 96, 502 96" stroke="#16a34a" stroke-width="2" fill="none" marker-end="url(#a2)"/>
  <path d="M176 230 C 240 230, 214 192, 258 192" stroke="#dc2626" stroke-width="2" fill="none" marker-end="url(#a3)"/>
  <path d="M584 230 C 520 230, 546 192, 502 192" stroke="#d97706" stroke-width="2" fill="none" marker-end="url(#a4)"/>

  <text x="380" y="214" font-size="11.5" text-anchor="middle" fill="#64748b">every step recorded in a trace — the thing you debug and evaluate</text>
  <text x="380" y="286" font-size="13" text-anchor="middle" fill="#0f172a" font-weight="600">This is the diagram you will redraw all week, and bring to Friday's panel.</text>
  <defs>
    <marker id="a1" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#0284c7"/></marker>
    <marker id="a2" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#16a34a"/></marker>
    <marker id="a3" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#dc2626"/></marker>
    <marker id="a4" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#d97706"/></marker>
  </defs>
</svg>
</div>

<!--
Slide ID: D1-M03-C5
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric
Type: core
Minutes: 3
Layout: 06 Process steps
Speaker notes:
- Say: "Agent" is the loop in the middle. "Agentic system" is the loop plus the four things around it — and the rest of the week is those four boxes.
- Ask: Which box does your prototype not have yet, and what breaks first without it?
- Watch: Name the module under each box so the week has a shape. Today builds only the purple box; by Friday a defensible system has all five, or a stated reason one is missing.
- Then: The group block asks you to draw your own version of this. Use this as the frame, not the answer — your boxes will differ.
Sources: [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents); [Module 03 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md); [Course concepts](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md).
-->
---

# Optional: action loops need more than fluent reasoning

- ReAct links actions with returned observations
- Harness studies examine longer task continuity
- Recovery needs checkpoints and side-effect awareness
- Investigate recovery before adding autonomy

<!--
Slide ID: D1-M03-R1
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes:
- Say: Optional: action loops need more than fluent reasoning
- Ask: After an interruption, which evidence would make a retry safe?
- Watch: Optional research only; the first harness does not implement full production recovery.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [ReAct](https://arxiv.org/abs/2210.03629); [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
-->

---

# “Looks good” is the start of a test, not the result

- A test case is an input and an expected property
- A rubric explains what counts as acceptable
- A score needs a case, criterion, and reason
- Human review exposes unclear criteria first

<!--
Slide ID: D1-M04-C1
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: “Looks good” is the start of a test, not the result
- Ask: Could two reviewers reasonably disagree about the word “helpful” in your rubric?
- Watch: Beric starts with rubric definitions and hand-scored transcripts before introducing the automated judge.
- Then: For the support question, “clear answer” and “correct permitted next step” are different requirements.
Sources: [Vibe checks and judges notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM judge study, Zheng et al., 2023](https://arxiv.org/abs/2306.05685).
-->

---

# Hand-score before you automate
- **Ask:** Could two reviewers reasonably disagree about the word “helpful” in your rubric?
- **Inspect:** Start from rubric definitions and hand-scored transcripts, before any automated judge runs.
- **Decide:** Write the rubric before the judge. Hand-score first, or you cannot tell if the judge is wrong.

<!--
Slide ID: D1-M04-C1B
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: “Looks good” is the start of a test, not the result
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Beric starts with rubric definitions and hand-scored transcripts before introducing the automated judge.
- Then: Write the rubric before the judge. Hand-score first, or you cannot tell if the judge is wrong.
Sources: [Vibe checks and judges notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM judge study, Zheng et al., 2023](https://arxiv.org/abs/2306.05685).
-->

---

# Establish the floor before trusting a judge

- **Echo:** give every transcript the middle score
- **Oracle:** copy Marcus's hand score exactly
- A real judge should clear the floor and approach the ceiling

For Deskmate, Marcus needs an auditable log, so the agreement measure must work before a model is allowed to score it.

<!--
Slide ID: D1-M04-C1C
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: Baselines tell us whether the agreement number contains signal before a judge enters the room.
- Ask: What would it mean if the oracle did not score 1.0 on Marcus's hand labels?
- Watch: Echo is the floor; oracle is the ceiling. A broken measure can make a bad judge look useful.
- Then: Notebook:cell#20 — Task 4 runs both dumb baselines before any judge call.
Sources: [Vibe checks and judges notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM judge study, Zheng et al., 2023](https://arxiv.org/abs/2306.05685).
-->

---

# Measure the measure before the model

```text
hand score  →  echo baseline  →  judge  →  oracle ceiling
                  floor           ?          1.0
```

No model call here. First make sure the yardstick can see the difference.

<!--
Slide ID: D1-M04-C1CB
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: The baseline exercise isolates the agreement calculation from model quality.
- Ask: Which result would make you stop and repair the metric before reading another transcript?
- Watch: The oracle must be exactly 1.0; if it is not, the measure is broken rather than the judge being surprising.
- Then: Notebook:cell#20 — inspect the floor and ceiling output before the strict judge in Task 5.
Sources: [Vibe checks and judges notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM judge study, Zheng et al., 2023](https://arxiv.org/abs/2306.05685).
-->

---

# A judge is another model with a narrow job

- Give it the case, evidence, answer, and criterion
- Validate its score and explanation
- A format-valid judgment can still be substantively wrong
- Compare its verdict with human review

<!--
Slide ID: D1-M04-C2
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 05 Two column
Speaker notes:
- Say: A judge is another model with a narrow job
- Ask: What is the difference between a valid score and a justified score?
- Watch: Inspect the strict judge's error handling and compare its rationale with a hand verdict on the same transcript.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685); [Strict judge implementation](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb).
-->

---

# Read the judge's reasoning, not its number
- **Ask:** What is the difference between a valid score and a justified score?
- **Inspect:** Inspect the strict judge's error handling and compare its rationale with a hand verdict on the same transcript.
- **Decide:** Pin the judge's temperature and read its rationale, not just its number.

<!--
Slide ID: D1-M04-C2B
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes:
- Say: A judge is another model with a narrow job
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Inspect the strict judge's error handling and compare its rationale with a hand verdict on the same transcript.
- Then: Pin the judge's temperature and read its rationale, not just its number.
Sources: [Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685); [Strict judge implementation](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb).
-->

---

# An answer can be clear, useful, and wrong

- Groundedness: supported by the supplied evidence
- Actionability: helps the user take a next step
- These are separate dimensions; one should not hide another
- Clarity: understandable to the intended reader

<!--
Slide ID: D1-M04-C3
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards 1
Speaker notes:
- Say: An answer can be clear, useful, and wrong
- Ask: Can an answer faithfully repeat an outdated procedure and still fail the user's task?
- Watch: Inspect the separate judge columns and their rationales; identify which dimension explains a disagreement.
- Then: Carry the observation into the next exercise.
Sources: [Three judge dimensions](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [Ragas faithfulness definition](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/).
-->

---

# Score the dimensions separately
- **Ask:** Can an answer faithfully repeat an outdated procedure and still fail the user's task?
- **Inspect:** Inspect the separate judge columns and their rationales; identify which dimension explains a disagreement.
- **Decide:** Score the dimensions separately, or a fluent wrong answer scores as a right one.

<!--
Slide ID: D1-M04-C3B
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: An answer can be clear, useful, and wrong
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Inspect the separate judge columns and their rationales; identify which dimension explains a disagreement.
- Then: Score the dimensions separately, or a fluent wrong answer scores as a right one.
Sources: [Three judge dimensions](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [Ragas faithfulness definition](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/).
-->

---

# Disagreement tells you where to investigate

- Read disputed cases before changing the system
- Separate rubric defects from answer defects
- Treat disagreement as an investigation signal
- Keep failures and version the measurement

<!--
Slide ID: D1-M04-C4
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: Disagreement tells you where to investigate
- Ask: What would make you distrust the judge rather than change the answer?
- Watch: Read the highest-disagreement row in the heatmap and explain the evidence. Do not replace an observed failure with a guessed score.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [Disagreement analysis and responsible controls](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM judge limitations](https://arxiv.org/abs/2306.05685).
-->

---

# Follow the disagreement
- **Ask:** What would make you distrust the judge rather than change the answer?
- **Inspect:** Read the highest-disagreement row in the heatmap and explain the evidence. Do not replace an observed failure with a guessed score.
- **Decide:** Investigate where graders disagree; that row is where the rubric is unclear.

<!--
Slide ID: D1-M04-C4B
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes:
- Say: Disagreement tells you where to investigate
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Read the highest-disagreement row in the heatmap and explain the evidence. Do not replace an observed failure with a guessed score.
- Then: Investigate where graders disagree; that row is where the rubric is unclear.
Sources: [Disagreement analysis and responsible controls](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM judge limitations](https://arxiv.org/abs/2306.05685).
-->

---

# Optional: calibrate the measuring instrument

- Judge studies test agreement and systematic bias
- Shared errors can survive agreement between models
- Agreement is not calibration against the real business decision
- Preserve human-reviewed cases for future changes

<!--
Slide ID: D1-M04-R1
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes:
- Say: Optional: calibrate the measuring instrument
- Ask: How would you detect a bias that both model judges share?
- Watch: Optional reading; no new evaluation-framework lab is required.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685); [Notebook calibration discussion](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb).
-->

---

# A direct question needs accessible evidence

- The model may not know your current procedure
- Retrieval finds material relevant to the question
- RAG grounds an answer in selected context, not truth itself
- Generation uses that material to draft an answer

<!--
Slide ID: D1-M05-C1
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 05 Two column
Speaker notes:
- Say: A direct question needs accessible evidence
- Ask: If the source is wrong, what can retrieval actually improve?
- Watch: Put the named artifact on screen and trace where its values came from.
- Then: Today's notebook uses a practical retrieve-then-prompt pipeline, not a reproduction of the paper's training method.
Sources: [RAG, Lewis et al., 2020](https://arxiv.org/abs/2005.11401); [RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb).
-->

---

# Same question, with and without evidence
- **Ask:** If the source is wrong, what can retrieval actually improve?
- **Inspect:** Ask the same question with and without retrieved context; read the evidence rather than assuming the second answer is better.
- **Decide:** Retrieval earns its place only when the evidence changes the answer.

<!--
Slide ID: D1-M05-C1B
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: A direct question needs accessible evidence
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Ask the same question with and without retrieved context; read the evidence rather than assuming the second answer is better.
- Then: Retrieval earns its place only when the evidence changes the answer.
Sources: [RAG, Lewis et al., 2020](https://arxiv.org/abs/2005.11401); [RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb).
-->

---

# Prepare the library, then search it for each question

- Split source pages into retrievable passages
- Embeddings represent text for similarity search
- Retrieval supplies question-specific evidence directly to the request; it does not change model weights
- Select passages and assemble the model's context

<!--
Slide ID: D1-M05-C2
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: Prepare the library, then search it for each question
- Ask: Which step changes the stored index, and which step happens for every question?
- Watch: Locate chunk creation, ranking, and context assembly before the library version; explain what each library component replaces.
- Then: Carry the observation into the next exercise.
Sources: [RAG from scratch and library pipeline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [Author's context-assembly notes](https://github.com/soypete/ctx-eng-book/blob/main/research/context-assembly-pipeline-patterns.md).
-->

---

# Retrieval earns its shortcut

<div style="display:flex;justify-content:center;margin-top:.2em">
<svg viewBox="0 0 780 190" width="920" role="img" aria-label="RAG learning arc: paste everything, build retrieval from scratch, then use LangChain">
  <g text-anchor="middle">
    <rect x="12" y="38" width="220" height="76" rx="9" fill="#f1f5f9" stroke="#94a3b8" stroke-width="2"/>
    <text x="122" y="67" font-size="15" font-weight="700" fill="#334155">paste everything</text>
    <text x="122" y="91" font-size="12" fill="#64748b">measure token cost</text>
    <rect x="280" y="38" width="220" height="76" rx="9" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/>
    <text x="390" y="67" font-size="15" font-weight="700" fill="#92400e">from scratch</text>
    <text x="390" y="91" font-size="12" fill="#b45309">embed · rank · paste</text>
    <rect x="548" y="38" width="220" height="76" rx="9" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/>
    <text x="658" y="67" font-size="15" font-weight="700" fill="#075985">LangChain</text>
    <text x="658" y="91" font-size="12" fill="#0369a1">library replaces pieces</text>
  </g>
  <path d="M240 76 H272" stroke="#94a3b8" stroke-width="2" marker-end="url(#rag-arc-arrow)"/>
  <path d="M508 76 H540" stroke="#94a3b8" stroke-width="2" marker-end="url(#rag-arc-arrow)"/>
  <defs><marker id="rag-arc-arrow" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#94a3b8"/></marker></defs>
</svg>
</div>

For Deskmate and Priya's VPN question: paste all twelve KB pages, read the cost, then retrieve three chunks instead.

The third step wires it into a **chain**: question → retriever → prompt → model → text, in one call.

<!--
Slide ID: D1-M05-C2A
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: The library step is last because the from-scratch version makes every hidden operation visible.
- Ask: What would you measure before replacing the twelve-page prompt with three retrieved chunks?
- Watch: Tie the arc to Priya's question: paste everything establishes the cost, from scratch exposes chunking and ranking, and LangChain packages those pieces.
- Then: Notebook:cell#12, Notebook:cell#17, Notebook:cell#20 — run the three stages in order.
Sources: [RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [RAG, Lewis et al., 2020](https://arxiv.org/abs/2005.11401).
-->

---

# Read the context you assembled
- **Ask:** Which step changes the stored index, and which step happens for every question?
- **Inspect:** Locate chunk creation, ranking, and context assembly before the library version; explain what each library component replaces.
- **Decide:** Read the assembled context before blaming the model for the answer.

<!--
Slide ID: D1-M05-C2B
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes:
- Say: Prepare the library, then search it for each question
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Locate chunk creation, ranking, and context assembly before the library version; explain what each library component replaces.
- Then: Read the assembled context before blaming the model for the answer.
Sources: [RAG from scratch and library pipeline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [Author's context-assembly notes](https://github.com/soypete/ctx-eng-book/blob/main/research/context-assembly-pipeline-patterns.md).
-->

---

# Diagnose the missing evidence before the answer

- Did the source contain the needed fact?
- Did retrieval put it into the model’s context?
- Did the final answer preserve the meaning and limits of the source?
- Did the answer use it correctly?

<!--
Slide ID: D1-M05-C3
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards 2
Speaker notes:
- Say: Diagnose the missing evidence before the answer
- Ask: Which component should change if the answer-bearing passage never reaches the prompt?
- Watch: Compare two k settings on the same question and inspect actual chunks. Keep baseline contexts with each answer.
- Then: The lab stores questions, answers, and contexts together so later checks can identify the failure stage.
Sources: [RAG setup, top-k comparison, saved baseline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [RAG artifact contract](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md).
-->

---

# Change k, inspect the chunks
- **Ask:** Which component should change if the answer-bearing passage never reaches the prompt?
- **Inspect:** Compare two k settings on the same question and inspect actual chunks. Keep baseline contexts with each answer.
- **Decide:** Repair retrieval before you rewrite the prompt.

<!--
Slide ID: D1-M05-C3B
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: Diagnose the missing evidence before the answer
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Compare two k settings on the same question and inspect actual chunks. Keep baseline contexts with each answer.
- Then: Repair retrieval before you rewrite the prompt.
Sources: [RAG setup, top-k comparison, saved baseline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [RAG artifact contract](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md).
-->

---

# Agentic retrieval changes the search strategy

- A fixed pipeline retrieves before answering
- An agent can search again when evidence is missing
- The agent still needs a permission boundary and a stopping rule
- Both still need relevant, permitted sources

<!--
Slide ID: D1-M05-C4
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes:
- Say: Agentic retrieval changes the search strategy
- Ask: What evidence would justify a second search instead of a final answer or clarification?
- Watch: Establish the fixed baseline first. Save its failures so later retrieval approaches have a fair comparison.
- Then: Use the answer to decide whether to clarify or continue.
Sources: [RAG baseline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [Agentic retrieval comparison](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb); [RAG versus long-context study](https://arxiv.org/abs/2407.16833).
-->

---

# Save the baseline's failures
- **Ask:** What evidence would justify a second search instead of a final answer or clarification?
- **Inspect:** Establish the fixed baseline first. Save its failures so later retrieval approaches have a fair comparison.
- **Decide:** Save the baseline's failures now; they are what later retrieval has to beat.

<!--
Slide ID: D1-M05-C4B
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes:
- Say: Agentic retrieval changes the search strategy
- Ask: Put the slide's question to the room first and wait; the answer below is the one to land, not to read out.
- Watch: Establish the fixed baseline first. Save its failures so later retrieval approaches have a fair comparison.
- Then: Save the baseline's failures now; they are what later retrieval has to beat.
Sources: [RAG baseline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [Agentic retrieval comparison](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb); [RAG versus long-context study](https://arxiv.org/abs/2407.16833).
-->

---

# Optional: retrieval is a design space, not a slogan

- Lewis et al.: combine generation with retrieved knowledge
- Long-context studies compare another evidence route
- No retrieval strategy wins every question or corpus
- Test coverage, answer quality, cost, and source control

<!--
Slide ID: D1-M05-R1
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric
Type: optional
Minutes: 0
Layout: 05 Two column 3
Speaker notes:
- Say: Optional: retrieval is a design space, not a slogan
- Ask: Which assumptions would you need to match before applying a paper's result to your system?
- Watch: Optional research; the required exercise remains the fixed RAG baseline.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [Retrieval-augmented generation](https://arxiv.org/abs/2005.11401); [Retrieval Augmented Generation or Long-Context LLMs?](https://arxiv.org/abs/2407.16833).
-->

---

# What today becomes in production

| What we built | Production equivalent |
|---|---|
| Opened a pull request by hand | Templates and a `CODEOWNERS` file that request the right reviewers |
| A Pydantic model as the output contract | Schema registries and validation middleware shared across teams |
| A single dense retriever | Hybrid search with a reranker on top |

For Deskmate, that means Priya's answer and Marcus's queue need repeatable review, shape, and retrieval.

<!--
Slide ID: D1-Z1
Module: Day 1 closing
Instructor: Miriah
Type: framing
Minutes: 2
Layout: 05 Two column
Speaker notes:
- Say: These are the production equivalents named by today's own notebooks, not a new checklist.
- Ask: Which row would expose stale-page confidence or cross-user ticket leakage first?
- Watch: Keep the table wording verbatim; connect Priya's evidence and Marcus's audit trail without promising that today's prototype solves either risk.
- Then: Notebook:cell#41, Notebook:cell#40, Notebook:cell#38 — close by naming the three module tables behind these rows.
Sources: [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb); [RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb).
-->
