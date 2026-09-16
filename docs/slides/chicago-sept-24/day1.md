---
marp: true
theme: default
paginate: true
size: 16:9
title: Day 1 — Prototype and retrieve
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
Speaker notes: Open with the design discipline the day needs: begin with a real person and a recurring question, not “we need an agent” or “we should use RAG.” Use “How do I restore access to my work account?” only as an illustrative shape; groups must choose their own question. Name the user, the difficult part, and the decision that follows. The question is the thread we can carry through a manual prompt, an agent, retrieval, and evaluation. The Concrete Idea Worksheet is the product-framing source; it supports making the problem concrete, not a claim that this example is the cohort's project.
Check understanding: What decision would become easier if this question were answered well?
Lab observation: In the later charter exercise, write one user and one recurring question; do not fill in the group's choice here.
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
Speaker notes: A useful answer is not merely a fluent paragraph. For the access question, it should give a permitted next step, identify the current procedure or evidence, and say when the system cannot safely decide. The group should define this contract before comparing prompts. The answer contract is also the future evaluation target: if the group cannot say what the answer must contain, it cannot tell whether a prototype improved. Keep the fields blank for the group; do not supply a completed charter.
Check understanding: Which part of the answer would let you detect that the procedure is stale?
Lab observation: During charter work, have the group write what a correct answer must contain for three questions.
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
Speaker notes: This separation keeps the prototype testable. “How do I restore access?” is the task. The current access procedure and account state are evidence. The employee, helpdesk, or approver owns the decision. A model can help summarize evidence, but it does not receive authority merely because the prompt says “you are an administrator.” This distinction will matter when the day adds prompts, tools, and retrieval. The local semantic-contract notes are an author synthesis: use them to explain why field names and ownership need explicit meaning, not as an independent empirical result.
Check understanding: Which of the three changes when a policy is updated: the task, the evidence, or the decision owner?
Lab observation: Ask groups to put one changing fact and one accountable decision owner on their napkin sketch.
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
Speaker notes: A proof of concept is a focused experiment. It should answer one uncertainty that matters: can the system identify the right procedure, preserve the required evidence, or recognize when it lacks enough information? Define the failure before running the test. Machine Learning Yearning is useful because it frames development around choosing an error target and an evaluation signal; do not present it as an AI-specific maturity standard. The group should choose a question and an observable success condition before adding components.
Check understanding: What result would make you abandon the current approach rather than add another feature?
Lab observation: In the charter, write two likely failures and how the group would notice each one.
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
Speaker notes: The first AI PoC can be a chat window, copy-and-paste, and a human check. That exposes whether the question, evidence, and answer contract make sense before the team automates the path. For the access example, paste the current procedure, ask for the next step and source passage, then compare the result with the answer contract. Record the input and output. The a16z application-stack essay is a practitioner architecture overview; use it for the idea that an LLM application has surrounding components, not as proof that one stack is universally correct.
Check understanding: Which manual step would you automate first, and what evidence would show that automation is safe?
Lab observation: Groups later build two prompt-only prototypes; keep the copied context and answer criteria visible for comparison.
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
Speaker notes: Do not ask whether the answer “feels better.” Ask which criteria it met, which evidence was missing, and what the next experiment is. A PoC is complete when the team has learned enough to choose a next step: revise the question, change the supplied evidence, change the prompt, or stop. A fluent response is not itself evidence. This is the bridge into prompt patterns: Eli's module will make the brief repeatable and compare variations on the same task.
Check understanding: What would make a prompt-only PoC a useful failure?
Lab observation: Groups should carry one comparison question and two likely failures into the prompt-pattern exercise.
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
Speaker notes: An MVP is one usable path for one important user task. For the access question, it might accept the request, gather the relevant procedure, present a proposed next step and source, and route uncertainty to a person. It does not need every system integration on day one. The product-market-fit reading is a product-development frame, not an AI engineering standard. The practical test is whether a person can complete the flow and whether the team can measure its quality.
Check understanding: What is the smallest end-to-end flow your user could complete without a team member explaining the demo?
Lab observation: Groups should keep their first product boundary narrow enough to demonstrate in the pitch.
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
Speaker notes: A showable car is a single coherent design that someone can operate on a defined route; it is not yet the factory, dealer network, maintenance system, or safety certification. For an AI MVP, a small interface, reusable skill, code path, or MCP-connected capability can make one flow repeatable. The important change is that a user can complete the task with less manual explanation. Ask what the equivalent “test drive” is for the group's product.
Check understanding: What would count as a test drive for your proposed AI product?
Lab observation: In the napkin sketch, mark the one flow the group will show and the future options it will leave out.
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
Speaker notes: Production is the infrastructure around the working design. For an AI system, that means current context, identity and permissions, repeatable evaluation, monitoring, recovery, release controls, and a person or team responsible for incidents. A prompt-only application can be production software if it has those controls; a complex agent can remain a PoC if it does not. Anthropic's article supports the simplicity-first distinction between workflows and agents; use it as engineering guidance, not a universal maturity rubric.
Check understanding: Which production responsibility would be missing if the demo only showed a successful answer?
Lab observation: Groups should name one quality risk and one person who would own the consequence of failure.
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
Speaker notes: Translate the physical analogy into system responsibilities. The user-facing assistant is the car; context assembly is the map and fuel, workflows are the route, permissions are the brakes and access gates, evals are the test track, and observability is the service record. These are analogies, not literal component requirements. The course will introduce them in sequence: prompts, agents, retrieval, evals, memory, architecture, guardrails, research, and off-the-shelf controls. The production question is always “what evidence says this change is safe enough to operate?”
Check understanding: Which control would you need before allowing the assistant to change data rather than only suggest a next step?
Lab observation: Ask groups to circle one production concern their current PoC intentionally leaves unresolved.
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
Speaker notes: Make the translation explicit. The PoC is a question answered through a prompt, perhaps with copy-and-pasted evidence and a human check. The MVP makes one path repeatable with reusable instructions, code, a tool, or an MCP connection. Production adds the surrounding operation: workflows, fresh and authorized context, evaluation gates, monitoring, recovery, and accountable ownership. Technology does not determine the maturity level. Use this mental model when deciding whether an agent, retrieval, memory, or guardrail earns its complexity.
Check understanding: Which new evidence—not which new component—would move your system to the next level?
Lab observation: Groups should label their proposed system as a PoC, MVP, or production target and state what evidence is still missing.
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
Speaker notes: Close the opening with the day's working contract. Groups will choose a real question, define what a useful answer contains, compare two prompt-only attempts, build a first agent, and build a RAG baseline over their own artifacts. The goal is not to leave with a production system; it is to leave with a concrete problem, evidence about a first solution, and an honest next step. Miriah then orients the shared development environment. The later code instructors own their notebook mechanics and implementation details.
Check understanding: What is the first question your group will answer, and what evidence will tell you whether the prototype helped?
Lab observation: Carry the question, answer contract, and first failure hypothesis into the group charter.
Sources: [Day 1 schedule](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/schedule/day1.md); [Day 1 cohort outline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/slides/chicago-sept-24/README.md); [Concrete Idea Worksheet](https://corporate.aiaspire.ai/accenture/titanium/NA/agenda/cohort_2/Concrete_Idea_Worksheet.pdf).
-->

---

# Your environment is a shared workbench

- Source files describe what should run
- Dependencies and settings shape how it runs
- Saved results record what actually happened

<!--
Slide ID: D1-M01-C1
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 2
Layout: 05 Two column
Speaker notes: A development environment is the place and configuration in which we edit and run the application. It is not the model itself. Engineers have long needed to reproduce a teammate's result; AI adds changing prompts, models, and context to that familiar problem. Use an access-help answer as the example: identical visible wording in a prompt is not enough to reproduce it if the model, source documents, or settings changed. Explain a dependency as a library the code needs, and a setting as a value controlling a run. Miriah owns this no-code orientation. The purpose is to locate the work and recognize its inputs and outputs, not to teach shell syntax. Keep API keys and confidential documents out of commits and screenshots. A saved output shows one observed run, not a guarantee about every future run.
Check understanding: Which changed input could explain two different answers from the same source file?
Lab observation: Find the notebook, environment settings, and saved artifact location; distinguish source from result without running code in the concept slot.
Sources: [Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).
-->

---

# Your environment is a shared workbench · The practical check

- **Ask:** Which changed input could explain two different answers from the same source file?
- **Inspect:** Find the notebook, environment settings, and saved artifact location; distinguish source from result without running code in the concept slot.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D1-M01-C1B
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.
Check understanding: Which changed input could explain two different answers from the same source file?
Lab observation: Find the notebook, environment settings, and saved artifact location; distinguish source from result without running code in the concept slot.
Sources: [Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).
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
Speaker notes: This is the simple history we want to preserve. The spec says what needs to be built. Prompts are the instructions we try; prompt history records what we asked, what context we supplied, and what the system returned. Checks are the recurring questions we use to see whether the system is helping. Rubrics say what we will look for in an answer. Results are the saved outputs we can inspect and compare. Docs are the reference materials people and AI tools can find and update in the repo. Seeds are starter examples for demonstrating the workflow; they are not evidence about the group’s product.
Check understanding: If an answer changes, which part of the history would you inspect first?
Lab observation: Miriah points out where the project keeps the spec, prompts, saved results, and reference docs. The code walkthroughs will use these materials later.
Sources: [Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Module 01 workspace initialization](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Artifact integrity rules](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/AGENTS.md).
-->

---

# The repo keeps a history of the work · The practical check

- **Ask:** If an answer changes, which part of the history would you inspect first?
- **Inspect:** Miriah points out where the project keeps the spec, prompts, saved results, and reference docs. The code walkthroughs will use these materials later.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D1-M01-C2B
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.
Check understanding: If an answer changes, which part of the history would you inspect first?
Lab observation: Miriah points out where the project keeps the spec, prompts, saved results, and reference docs. The code walkthroughs will use these materials later.
Sources: [Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Module 01 workspace initialization](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Artifact integrity rules](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/AGENTS.md).
-->

---

# A small change should have a clear history

- Branch: separate a piece of work
- Diff: inspect exactly what changed
- Commit: record a named checkpoint

<!--
Slide ID: D1-M01-C3
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes: Use the familiar idea of tracked changes in a shared document. Version control preserves a history instead of relying on filenames such as final-final. A branch separates work in progress, a diff reveals the exact edit, and a commit records a checkpoint. Pushing shares commits; a pull request invites review; merging incorporates the change. These are different actions. In this course, origin normally points to the learner's fork and upstream to the course repository. Those names are conventions whose actual addresses must be checked, not proof of ownership. Fetching receives remote history without itself changing working files. Ask learners to read an AI-written change before accepting it. A readable history will matter when a changed prompt improves one case and breaks another.
Check understanding: Does committing a change mean that someone else has reviewed it?
Lab observation: Miriah shows location, branch, diff, and destination. Stop before sharing if the diff contains unexpected files or the remote is unfamiliar.
Sources: [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow); [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).
-->

---

# A small change should have a clear history · The practical check

- **Ask:** Does committing a change mean that someone else has reviewed it?
- **Inspect:** Miriah shows location, branch, diff, and destination. Stop before sharing if the diff contains unexpected files or the remote is unfamiliar.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D1-M01-C3B
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.
Check understanding: Does committing a change mean that someone else has reviewed it?
Lab observation: Miriah shows location, branch, diff, and destination. Stop before sharing if the diff contains unexpected files or the remote is unfamiliar.
Sources: [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow); [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).
-->

---

# Review the change, not just the successful run

- Check intended files and shared destinations
- Keep credentials and private data out of history
- Preserve enough context to repeat the comparison

<!--
Slide ID: D1-M01-C4
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 2
Layout: 05 Two column 1
Speaker notes: A successful local run answers only whether that attempt completed. Review asks whether the change is appropriate to share. For example, a more helpful access answer is not a good change if its debug output exposes an employee identifier. Record which prompt and source version were used so a teammate can repeat the comparison, accepting that model outputs may vary. The module's later production discussion introduces required checks, branch protection, and designated reviewers; these automate parts of the manual discipline, not human accountability. Stop when the changed files or destination are not understood. Miriah's selected presentation remains a no-code orientation even though the repository contains a notebook that opens a real demonstration pull request. Do not imply the live class will perform all of those actions during this primer.
Check understanding: What would a reviewer need beyond a screenshot of the answer?
Lab observation: Explain the proposed edit and its saved evidence to a teammate; troubleshooting belongs in the practical block.
Sources: [Module 01 Learn/Create/Grow](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).
-->

---

# Review the change, not just the successful run · The practical check

- **Ask:** What would a reviewer need beyond a screenshot of the answer?
- **Inspect:** Explain the proposed edit and its saved evidence to a teammate; troubleshooting belongs in the practical block.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D1-M01-C4B
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.
Check understanding: What would a reviewer need beyond a screenshot of the answer?
Lab observation: Explain the proposed edit and its saved evidence to a teammate; troubleshooting belongs in the practical block.
Sources: [Module 01 Learn/Create/Grow](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).
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
Speaker notes: This optional engineering reading extends the shared-workbench idea. GitHub's protected-branch documentation describes enforceable review and check requirements. Its contribution is practical: team rules can be applied by the platform rather than remembered before each merge. It does not establish that the tests represent real user risks. For an AI application, investigate whether changing a prompt, model configuration, or retrieval source triggers the same quality review as changing code. Do not require learners to configure branch rules here. The question for later work is which evidence should prevent a change from being shared, and who owns exceptions. Read the official documentation for the current repository plan and permissions before selecting a particular configuration.
Check understanding: Which failure would your current checks miss even if every check passed?
Lab observation: Optional follow-up only; no additional code exercise or core minutes.
Sources: [GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches); [Module 01 production discussion](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).
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
Speaker notes: A prompt is the brief for one request. It gives the model the task, audience, facts, and desired answer shape. It does not change the model’s training. Use the internal support question as the example: the model may understand “access” but cannot infer the team’s rules directly without supplying them. The rest of this module is a menu of ways to make that brief more useful.
Check understanding: What important fact would the model be forced to guess if it is not in the prompt?
Lab observation: Eli begins with the same question and shows how each prompt pattern changes the request.
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
Speaker notes: Brown et al. found that scaling language models improved task-agnostic few-shot performance and sometimes made it competitive with earlier fine-tuned systems. Their setup used demonstrations in the text interaction without gradient updates or fine-tuning. The result is historically important, but it is not a promise that a few examples will solve our business problem. Few-shot is useful when the model needs to follow a local convention: how a consultant writes a finding, how an issue is classified, or which fields belong in a response. Use small, representative examples and keep them consistent. The model can still copy a mistake from an example, so check the result against the task.
Check understanding: What behavior would you demonstrate with an example rather than describe in another paragraph?
Lab observation: Eli compares a prompt with no examples against one with examples while holding the question and evidence constant.
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
Speaker notes: Context is the information the model needs for this request but cannot know directly: a current policy, account state, project file, or customer record. More context is not always better. Include relevant, authorized facts and leave out sensitive or distracting material. If the answer changes when the policy changes, the next engineering question is how to provide current context reliably; retrieval addresses that later.
Check understanding: What fact would the model otherwise have to guess?
Lab observation: Eli compares the same prompt with and without a supplied policy excerpt.
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
Speaker notes: A persona sets viewpoint and audience, not credentials or new knowledge. An output format makes the response easier to read or pass to another program. For example, “write for a helpdesk analyst” changes vocabulary, while fields such as issue, source, owner, and next step make the result inspectable. JSON is only a shape; it does not make the values correct.
Check understanding: Which part of the prompt changes the reader, and which part changes the shape of the answer?
Lab observation: Eli compares persona and structured-output variants and checks factual content separately from voice and formatting.
Sources: [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb); [Author's semantic-contract notes](https://github.com/soypete/ctx-eng-book/blob/main/research/semantic-contracts.md).
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
Speaker notes: Chain-of-thought research showed benefits from intermediate-step examples on selected reasoning tasks. Teach the practical version: make assumptions, calculations, evidence, and a concise justification checkable. Do not treat a generated rationale as a faithful record of internal computation or as proof of correctness. More steps can add time while preserving the same error.
Check understanding: Which step could you verify independently?
Lab observation: Eli compares a direct answer with a structured answer that exposes checkable work.
Sources: [Chain-of-thought prompting, Wei et al., 2022](https://arxiv.org/abs/2201.11903); [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb).
-->

---

# ReAct: reason, act, observe

- Decide what action would reduce uncertainty
- Call a tool or perform the next step
- Use the observation to choose what happens next

> Source: [ReAct](https://arxiv.org/abs/2210.03629)

<!--
Slide ID: D1-M02-C6
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli, code walkthrough
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes: ReAct combines reasoning with actions and observations. In a simple example, the model decides that it needs a current account status, calls an approved lookup, reads the result, and then answers or stops. This is the bridge to Agents 101: when the action is a real tool call, the prompt becomes part of a larger loop. ReAct does not grant permission; the surrounding application decides which tools exist, what they can do, and when the loop must stop.
Check understanding: What observation would change the next action?
Lab observation: Eli will show the prompt pattern first; Beric will later show the agent harness that owns the tool loop.
Sources: [ReAct, Yao et al., 2022](https://arxiv.org/abs/2210.03629); [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb).
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
Speaker notes: Self-refine asks the system to improve a draft answer. Meta-prompting asks the system to act like an editor of the task itself: inspect the request, identify ambiguity or missing requirements, and propose a clearer prompt. A useful meta-prompt might say: “Review this task, prompt, and failed examples. Identify ambiguity, missing constraints, and an improved prompt. Do not solve the task.” The team then tests that proposed prompt on the same cases. Meta-prompting produces a candidate instruction; it does not establish that the instruction is correct. Both loops can preserve the same model error, so use an external criterion, save the versions, and set a small revision budget.
Check understanding: Did the revision improve the answer, the prompt, or both—and what evidence shows that?
Lab observation: Eli compares a first prompt and a meta-prompt-generated revision, then runs both against the same cases and records the prompt versions.
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
Speaker notes: The comparison is an experiment, not a contest between two unrelated demos. Keep the user question, evidence, model, output criteria, and test cases constant. Change one thing—for example, add two few-shot examples, add a policy excerpt, require a structured format, or ask for checkable reasoning. Save both prompt versions and outputs. Compare the whole pattern of results, not only the best answer: which criteria passed, which cases failed, how consistent were the answers, and what did the change cost in time or tokens? If the change improves the same task without new actions, keep the simpler prompt. If the failure is missing source or current information, investigate retrieval. If the next step depends on an observation or tool result, investigate an agent. If a fixed sequence works, keep it as a function or workflow.
Check understanding: If prompt B wins one case but loses another, what would you inspect before choosing it?
Lab observation: Groups choose one pattern, compare two prompt-only prototypes on the same cases, record the evidence, and carry the unresolved failure into the agent exercise.
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
Speaker notes: Use these papers to distinguish mechanisms, not to create a universal ranking of prompt tricks. The few-shot study investigated task demonstrations without parameter updates. The chain-of-thought study investigated intermediate reasoning examples on particular tasks and models. Self-Refine investigated model-generated feedback followed by revision. Their reported task results do not establish a benefit for the group's support workflow or current endpoint. A useful follow-up experiment would keep representative cases separate from prompt development and compare usefulness with latency and call count. Record regressions as well as improvements. The research question is whether the additional mechanism fixes a specific error, not whether the response sounds more thoughtful. This optional slide is outside the 15-minute introduction.
Check understanding: Which of these mechanisms would address your observed error, and which would not?
Lab observation: Optional reading, not an extra optimization module.
Sources: [Brown et al., 2020](https://arxiv.org/abs/2005.14165); [Wei et al., 2022](https://arxiv.org/abs/2201.11903); [Madaan et al., 2023](https://arxiv.org/abs/2303.17651).
-->

---

# A model answers; an agent can choose a next step

- A model call generates a response from supplied input
- An agent loop can request tools and read results
- Agent behavior depends on the surrounding loop, not a special model label
- Application code executes and authorizes actions

<!--
Slide ID: D1-M03-C1
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes: The distinction is the surrounding application behavior, not a magical new kind of model. A single model call can suggest an action, but the application decides whether and how to execute it. An agent repeatedly uses a model to select a next step from permitted options, receives the result, and continues or stops. For an access question it might search a procedure, discover that information is missing, and ask a clarifying question. A fixed workflow can also call tools; call something agentic here when the next step is selected dynamically. Terminology varies across products, so keep this operational definition visible. If every step is known beforehand, a fixed workflow is often easier to inspect. The lab's tool loop is deliberately small and does not imply autonomous administration of a real account.
Check understanding: Which box actually runs a tool, and which box decides whether it is allowed?
Lab observation: In Beric's trace, locate the model message requesting a tool, the tool result, and the subsequent model response.
Sources: [Agent harness notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Workflow and agent definitions](https://www.anthropic.com/engineering/building-effective-agents).
-->

---

# A model answers; an agent can choose a next step · The practical check

- **Ask:** Which box actually runs a tool, and which box decides whether it is allowed?
- **Inspect:** In Beric's trace, locate the model message requesting a tool, the tool result, and the subsequent model response.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D1-M03-C1B
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.
Check understanding: Which box actually runs a tool, and which box decides whether it is allowed?
Lab observation: In Beric's trace, locate the model message requesting a tool, the tool result, and the subsequent model response.
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
Speaker notes: A tool is a function the model may ask the application to run. Its contract explains the name, purpose, and allowed arguments; arguments are the values passed to the function. The system must still validate those values and enforce access. The notebook's three tools search the charter, search saved prompt outputs, and log a request. These are not a full enterprise service catalog. ReAct is a research milestone connecting reasoning with actions and observations, helping explain why a lookup can change the next step instead of merely decorating the final response. A tool can fail, return no result, or return untrusted text. None of those outcomes gives the model new authority. A suggestion to log or change something must remain within the application's permitted scope.
Check understanding: If a retrieved page says “ignore your rules,” does that change the tool's permissions?
Lab observation: Inspect how precise tool descriptions affect tool selection; do not equate making a tool call with making the correct call.
Sources: [ReAct, Yao et al., 2022](https://arxiv.org/abs/2210.03629); [Agent harness tools](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb).
-->

---

# Tools give the loop controlled capabilities · The practical check

- **Ask:** If a retrieved page says “ignore your rules,” does that change the tool's permissions?
- **Inspect:** Inspect how precise tool descriptions affect tool selection; do not equate making a tool call with making the correct call.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D1-M03-C2B
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.
Check understanding: If a retrieved page says “ignore your rules,” does that change the tool's permissions?
Lab observation: Inspect how precise tool descriptions affect tool selection; do not equate making a tool call with making the correct call.
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
Speaker notes: The harness is the application scaffolding that manages instructions, tool execution, state, limits, and records. Middleware is code around that loop that can inspect or constrain a step. The lab adds logging and a model-call limit; a model-call limit is not identical to a tool-call limit because one model turn may request multiple tools. Describe a failed lookup: retrying forever cannot create missing evidence. The system needs a bounded exit and an honest explanation. A trace records observable events; it is not a readout of the model's hidden reasoning. Later architecture work adds recovery and durable state, evaluation inspects outcomes and trajectories, and memory controls what persists. These are separate responsibilities around the model, not properties gained by merely naming the system an agent.
Check understanding: What should the user receive when the budget ends before the task is complete?
Lab observation: Watch middleware messages and the enforced limit; inspect the saved transcript rather than only the final answer.
Sources: [Agent harness limits and trace](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
-->

---

# The harness owns the loop's boundaries · The practical check

- **Ask:** What should the user receive when the budget ends before the task is complete?
- **Inspect:** Watch middleware messages and the enforced limit; inspect the saved transcript rather than only the final answer.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D1-M03-C3B
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.
Check understanding: What should the user receive when the budget ends before the task is complete?
Lab observation: Watch middleware messages and the enforced limit; inspect the saved transcript rather than only the final answer.
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
Speaker notes: An agent is useful when the needed sequence cannot be fully determined before observing results. That flexibility creates additional failure paths. For the recurring support question, a known procedure can be a fixed lookup and answer. A diagnosis needing an initial symptom, a search, and a follow-up question may benefit from adaptation. The system should decline an out-of-scope request, ask when essential information is absent, and stop before an unapproved action. These are legitimate outcomes, not embarrassing failures to hide. The current engineering direction is making longer tasks inspectable and recoverable; that is a challenge, not a claim that every workflow should become autonomous. The group should retain a simpler design if it meets its quality and cost requirements.
Check understanding: What observation would change the next step in your proposed loop?
Lab observation: Compare in-scope, human-needed, and out-of-scope questions. Check whether tool behavior matches the scope before praising fluency.
Sources: [Agent harness Create/Grow](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
-->

---

# Autonomy needs a reason and a stopping rule · The practical check

- **Ask:** What observation would change the next step in your proposed loop?
- **Inspect:** Compare in-scope, human-needed, and out-of-scope questions. Check whether tool behavior matches the scope before praising fluency.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D1-M03-C4B
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.
Check understanding: What observation would change the next step in your proposed loop?
Lab observation: Compare in-scope, human-needed, and out-of-scope questions. Check whether tool behavior matches the scope before praising fluency.
Sources: [Agent harness Create/Grow](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
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
Speaker notes: ReAct provides a research reference for interleaving reasoning and action. Anthropic's long-running harness article is an engineering case study on sustaining progress across sessions, not a universal proof of reliability. Together they motivate a distinction between choosing a useful next action and managing an application over time. Ask whether a restarted run knows what really completed. An attempted tool call is not evidence of a completed side effect; blindly repeating a write could duplicate work. Later architecture concepts cover checkpoints and safe retries. No new multi-agent or deployment lab is added here. Read the sources to identify what was tested, which environment supplied feedback, and what would differ for an internal helpdesk tool.
Check understanding: After an interruption, which evidence would make a retry safe?
Lab observation: Optional research only; the first harness does not implement full production recovery.
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
Speaker notes: A vibe check is an informal inspection of whether an output seems useful. In this course it becomes deliberate: write the expected properties and record a human verdict with a reason. Evaluation carries forward a familiar software-testing idea, checking behavior against expectations, but free-form answers often need a rubric rather than one exact string. For the support question, “clear answer” and “correct permitted next step” are different requirements. Write what passing each one means before looking at scores. A test case is a particular question and situation; a rubric is the rule for judging it. A handful of examples can reveal defects but cannot establish representative reliability. The next step is not immediately to automate the judgment, but to check that two people can apply the rule consistently.
Check understanding: Could two reviewers reasonably disagree about the word “helpful” in your rubric?
Lab observation: Beric starts with rubric definitions and hand-scored transcripts before introducing the automated judge.
Sources: [Vibe checks and judges notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM judge study, Zheng et al., 2023](https://arxiv.org/abs/2306.05685).
-->

---

# “Looks good” is the start of a test, not the result · The practical check

- **Ask:** Could two reviewers reasonably disagree about the word “helpful” in your rubric?
- **Inspect:** Beric starts with rubric definitions and hand-scored transcripts before introducing the automated judge.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D1-M04-C1B
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.
Check understanding: Could two reviewers reasonably disagree about the word “helpful” in your rubric?
Lab observation: Beric starts with rubric definitions and hand-scored transcripts before introducing the automated judge.
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
Speaker notes: LLM-as-a-judge means using a language-model call to assess an output against a defined criterion. It can help inspect many responses, but it does not become an objective authority by returning a number. The 2023 MT-Bench and Chatbot Arena study examined model judging and identified biases including position and verbosity effects. The notebook checks that the returned score is in range and the rationale is present, retries malformed output, and reports failure rather than manufacturing a neutral score. That validates the response's format, not the truth of its judgment. The answering model and judge may be the same model in this lab, which can correlate their errors. Human calibration means comparing judgments on shared cases and resolving why they differ.
Check understanding: What is the difference between a valid score and a justified score?
Lab observation: Inspect the strict judge's error handling and compare its rationale with a hand verdict on the same transcript.
Sources: [Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685); [Strict judge implementation](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb).
-->

---

# A judge is another model with a narrow job · The practical check

- **Ask:** What is the difference between a valid score and a justified score?
- **Inspect:** Inspect the strict judge's error handling and compare its rationale with a hand verdict on the same transcript.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D1-M04-C2B
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.
Check understanding: What is the difference between a valid score and a justified score?
Lab observation: Inspect the strict judge's error handling and compare its rationale with a hand verdict on the same transcript.
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
Speaker notes: Consider an access answer that gives a beautifully worded but nonexistent menu path. It may be clear and actionable in tone while unsupported. Conversely, copying a correct policy passage may be grounded but leave the employee unsure what to do. The lab separates these dimensions into three judges. Do not average them into a number that lets readability cancel an unsupported instruction without an explicit decision rule. Groundedness is support relative to available evidence; it does not prove the evidence is current or correct. Use direct checks for properties that are exact, such as an identifier or required field, and model judgments for properties needing interpretation. This separation prepares later RAG metrics and agent outcome checks, which answer different questions from general answer quality.
Check understanding: Can an answer faithfully repeat an outdated procedure and still fail the user's task?
Lab observation: Inspect the separate judge columns and their rationales; identify which dimension explains a disagreement.
Sources: [Three judge dimensions](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [Ragas faithfulness definition](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/).
-->

---

# An answer can be clear, useful, and wrong · The practical check

- **Ask:** Can an answer faithfully repeat an outdated procedure and still fail the user's task?
- **Inspect:** Inspect the separate judge columns and their rationales; identify which dimension explains a disagreement.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D1-M04-C3B
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.
Check understanding: Can an answer faithfully repeat an outdated procedure and still fail the user's task?
Lab observation: Inspect the separate judge columns and their rationales; identify which dimension explains a disagreement.
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
Speaker notes: The most informative row may be the one where a judge disagrees with a person, not the one with the highest score. Read the answer, the criterion, and the source before deciding which component failed. If the rubric is vague, clarify it and re-score consistently; if evidence is absent, investigate retrieval; if the judge rewards irrelevant verbosity, revise and recalibrate the judge. A confidence-like number is not a calibrated probability of correctness. Preserve cases that expose failures and record model and rubric versions. Stop relying on a judge when it cannot distinguish known good and bad examples; return to reviewed cases. The forward direction is a repeatable measurement process tied to real decisions, not progressively more elaborate scoring dashboards.
Check understanding: What would make you distrust the judge rather than change the answer?
Lab observation: Read the highest-disagreement row in the heatmap and explain the evidence. Do not replace an observed failure with a guessed score.
Sources: [Disagreement analysis and responsible controls](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM judge limitations](https://arxiv.org/abs/2306.05685).
-->

---

# Disagreement tells you where to investigate · The practical check

- **Ask:** What would make you distrust the judge rather than change the answer?
- **Inspect:** Read the highest-disagreement row in the heatmap and explain the evidence. Do not replace an observed failure with a guessed score.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D1-M04-C4B
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.
Check understanding: What would make you distrust the judge rather than change the answer?
Lab observation: Read the highest-disagreement row in the heatmap and explain the evidence. Do not replace an observed failure with a guessed score.
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
Speaker notes: The MT-Bench study is a starting point for reading about model judges, not a guarantee of agreement on enterprise questions. Its benchmarks and preference judgments are not identical to checking a private procedure. Investigate how answer order, verbosity, and the choice of judge affect your use case. Agreement alone is insufficient when evaluators share blind spots or lack the relevant source. A useful follow-up is to retain a reviewed set containing acceptable, unacceptable, and borderline examples and recheck it when the rubric or model changes. Human judgments also need clear criteria and reconciliation. The research question is whether the instrument supports the decision you intend to make, not whether one evaluator is universally best.
Check understanding: How would you detect a bias that both model judges share?
Lab observation: Optional reading; no new evaluation-framework lab is required.
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
Speaker notes: Retrieval-augmented generation, or RAG, combines finding external material with generating an answer from it. It addresses a knowledge-access problem: a model's training is not a live copy of the organization's changing procedures. Lewis and colleagues' 2020 paper is a milestone combining learned model knowledge with retrieved passages; information retrieval itself is much older. Today's notebook uses a practical retrieve-then-prompt pipeline, not a reproduction of the paper's training method. For an internal access question, evidence must be both relevant and permitted for this user. RAG does not guarantee truth, current sources, or correct reasoning. A plausible generated transcript in the corpus is not automatically authoritative policy. Source quality and provenance remain application responsibilities.
Check understanding: If the source is wrong, what can retrieval actually improve?
Lab observation: Beric asks the same question without source text and with retrieved context; inspect the evidence rather than assuming the second answer must be better.
Sources: [RAG, Lewis et al., 2020](https://arxiv.org/abs/2005.11401); [RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb).
-->

---

# A direct question needs accessible evidence · The practical check

- **Ask:** If the source is wrong, what can retrieval actually improve?
- **Inspect:** Beric asks the same question without source text and with retrieved context; inspect the evidence rather than assuming the second answer must be better.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D1-M05-C1B
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.
Check understanding: If the source is wrong, what can retrieval actually improve?
Lab observation: Beric asks the same question without source text and with retrieved context; inspect the evidence rather than assuming the second answer must be better.
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
Speaker notes: A corpus is the collection of source material. A chunk is a passage selected as a retrievable unit. An embedding is a list of numbers used to compare text in a learned representation; closeness is a relevance signal, not a truth score. Preparation builds the searchable collection. At request time the question is represented, candidate chunks are ranked, and selected passages are supplied directly in the request. The model then uses those retrieved passages as evidence, which is why prompting and retrieval belong in the same story. The notebook makes these steps visible with simple chunking and cosine similarity, then uses LangChain and local Qdrant to package them. The author's context-assembly notes help explain the pipeline but are a working synthesis. Keep the retrieved chunks with each answer so it can be traced back to what the model actually saw; carrying source IDs as chunk metadata is the module's Grow step.
Check understanding: Which step changes the stored index, and which step happens for every question?
Lab observation: Locate chunk creation, ranking, and context assembly before the library version; explain what each library component replaces.
Sources: [RAG from scratch and library pipeline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [Author's context-assembly notes](https://github.com/soypete/ctx-eng-book/blob/main/research/context-assembly-pipeline-patterns.md).
-->

---

# Prepare the library, then search it for each question · The practical check

- **Ask:** Which step changes the stored index, and which step happens for every question?
- **Inspect:** Locate chunk creation, ranking, and context assembly before the library version; explain what each library component replaces.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D1-M05-C2B
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.
Check understanding: Which step changes the stored index, and which step happens for every question?
Lab observation: Locate chunk creation, ranking, and context assembly before the library version; explain what each library component replaces.
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
Speaker notes: These questions separate errors that need different fixes. If the procedure never entered the corpus, changing the prompt cannot retrieve it. If it exists but the wrong chunks were selected, adjust retrieval. If the correct passage reached the model and the response ignored it, inspect generation and instructions. The top-k setting is the number of selected chunks: too few can omit necessary evidence, while more increases context and may add irrelevant or conflicting material. More is not automatically better. The lab stores questions, answers, and contexts together so later checks can identify the failure stage. It excludes the vibe-check answer-key page from retrieval; otherwise a comparison could reward retrieving the test answers. Stop interpreting an improvement as general quality when the evidence is empty, leaked, or unrepresentative.
Check understanding: Which component should change if the answer-bearing passage never reaches the prompt?
Lab observation: Compare two k settings on the same question and inspect actual chunks. Keep baseline contexts with each answer.
Sources: [RAG setup, top-k comparison, saved baseline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [RAG artifact contract](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md).
-->

---

# Diagnose the missing evidence before the answer · The practical check

- **Ask:** Which component should change if the answer-bearing passage never reaches the prompt?
- **Inspect:** Compare two k settings on the same question and inspect actual chunks. Keep baseline contexts with each answer.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D1-M05-C3B
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.
Check understanding: Which component should change if the answer-bearing passage never reaches the prompt?
Lab observation: Compare two k settings on the same question and inspect actual chunks. Keep baseline contexts with each answer.
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
Speaker notes: “RAG is dead” often mixes a criticism of a fixed retrieval recipe with the broader need to supply evidence. Agentic retrieval changes when and how searching happens; it does not eliminate retrieval. Long context is another option when a relevant source set can be supplied directly, but it still needs selection, freshness, and permission decisions. The engineering choice is conditional: compare the simplest adequate approach against adaptive searching on representative cases, cost, and latency. Additional searches should stop when the question is supported, the budget is used, or a missing permission or source prevents progress. Day 2 examines retrieval alternatives rather than assuming one architecture replaces all others. This slide sets up that question without introducing a new lab now.
Check understanding: What evidence would justify a second search instead of a final answer or clarification?
Lab observation: Establish the fixed baseline first. Save its failures so later retrieval approaches have a fair comparison.
Sources: [RAG baseline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [Agentic retrieval comparison](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb); [RAG versus long-context study](https://arxiv.org/abs/2407.16833).
-->

---

# Agentic retrieval changes the search strategy · The practical check

- **Ask:** What evidence would justify a second search instead of a final answer or clarification?
- **Inspect:** Establish the fixed baseline first. Save its failures so later retrieval approaches have a fair comparison.
- **Decide:** keep the simplest design that clears the check; record the gap when it does not.

<!--
Slide ID: D1-M05-C4B
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes: Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.
Check understanding: What evidence would justify a second search instead of a final answer or clarification?
Lab observation: Establish the fixed baseline first. Save its failures so later retrieval approaches have a fair comparison.
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
Speaker notes: Read the 2020 RAG paper for the separation of parameterized knowledge and retrieved evidence. Read the 2024 long-context comparison for a concrete experimental comparison and its chosen models, tasks, and resource assumptions. Do not generalize its findings into “retrieval always wins” or “long context makes search obsolete.” Neither source establishes performance for this group's corpus or current models. Adaptive retrieval adds another policy for selecting evidence and introduces additional calls and stopping decisions. A worthwhile follow-up keeps the question set and source permissions fixed, then measures where each design fails. The durable lesson is to make the evidence route inspectable. The future direction here is an open design question, not a prediction of a winning framework.
Check understanding: Which assumptions would you need to match before applying a paper's result to your system?
Lab observation: Optional research; the required exercise remains the fixed RAG baseline.
Sources: [Retrieval-augmented generation](https://arxiv.org/abs/2005.11401); [Retrieval Augmented Generation or Long-Context LLMs?](https://arxiv.org/abs/2407.16833).
-->
