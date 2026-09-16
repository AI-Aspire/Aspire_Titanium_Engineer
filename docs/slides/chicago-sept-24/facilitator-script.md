# Chicago · September 24 facilitator script

This is the detailed preparation layer for the [Chicago slide outlines](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/tree/main/docs/slides/chicago-sept-24). Do not read this document aloud or paste it into speaker notes. Use the short notes in the day files while presenting; use this script to prepare, answer questions, and rehearse the next beat.

## Delivery rhythm

- Miriah introduces the concept, recurring user question, and design boundaries.
- Eli and Beric introduce the code notebooks and lead the exercises.
- During breakout work, the instructional team circulates, listens, and helps groups go deeper or get unstuck.
- Ask a question, listen for the signal, and move to the next action. Protect hands-on time; skip optional material when the room needs to build.

## Slide-by-slide preparation


### D1-F1 · Start with a question, not a technology

- Module: Framing, before the selected modules
- Instructor: Miriah
- Type: framing
- Timing: 1 minute
- Layout: 01 Title

#### Detailed preparation

Open with the design discipline the day needs: begin with a real person and a recurring question, not “we need an agent” or “we should use RAG.” Use “How do I restore access to my work account?” only as an illustrative shape; groups must choose their own question. Name the user, the difficult part, and the decision that follows. The question is the thread we can carry through a manual prompt, an agent, retrieval, and evaluation. The Concrete Idea Worksheet is the product-framing source; it supports making the problem concrete, not a claim that this example is the cohort's project.

#### Ask

What decision would become easier if this question were answered well?

#### Watch in the exercise

In the later charter exercise, write one user and one recurring question; do not fill in the group's choice here.

#### Sources

[Concrete Idea Worksheet](https://corporate.aiaspire.ai/accenture/titanium/NA/agenda/cohort_2/Concrete_Idea_Worksheet.pdf); [Charter template](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/project/CHARTER.md).


### D1-F2 · Define what a useful answer must contain

- Module: Framing, before the selected modules
- Instructor: Miriah
- Type: framing
- Timing: 1 minute
- Layout: 02 Agenda 1

#### Detailed preparation

A useful answer is not merely a fluent paragraph. For the access question, it should give a permitted next step, identify the current procedure or evidence, and say when the system cannot safely decide. The group should define this contract before comparing prompts. The answer contract is also the future evaluation target: if the group cannot say what the answer must contain, it cannot tell whether a prototype improved. Keep the fields blank for the group; do not supply a completed charter.

#### Ask

Which part of the answer would let you detect that the procedure is stale?

#### Watch in the exercise

During charter work, have the group write what a correct answer must contain for three questions.

#### Sources

[Concrete Idea Worksheet](https://corporate.aiaspire.ai/accenture/titanium/NA/agenda/cohort_2/Concrete_Idea_Worksheet.pdf); [Charter template](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/project/CHARTER.md).


### D1-F3 · Separate the task, the evidence, and the decision

- Module: Framing, before the selected modules
- Instructor: Miriah
- Type: framing
- Timing: 1 minute
- Layout: 05 Two column

#### Detailed preparation

This separation keeps the prototype testable. “How do I restore access?” is the task. The current access procedure and account state are evidence. The employee, helpdesk, or approver owns the decision. A model can help summarize evidence, but it does not receive authority merely because the prompt says “you are an administrator.” This distinction will matter when the day adds prompts, tools, and retrieval. The local semantic-contract notes are an author synthesis: use them to explain why field names and ownership need explicit meaning, not as an independent empirical result.

#### Ask

Which of the three changes when a policy is updated: the task, the evidence, or the decision owner?

#### Watch in the exercise

Ask groups to put one changing fact and one accountable decision owner on their napkin sketch.

#### Sources

[Author's semantic-contract notes](https://github.com/soypete/ctx-eng-book/blob/main/research/semantic-contracts.md); [Course authoring principles](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/AUTHORING.md).


### D1-F4 · A prototype tests one uncertainty

- Module: Framing, before the selected modules
- Instructor: Miriah
- Type: framing
- Timing: 1 minute
- Layout: 06 Process steps

#### Detailed preparation

A proof of concept is a focused experiment. It should answer one uncertainty that matters: can the system identify the right procedure, preserve the required evidence, or recognize when it lacks enough information? Define the failure before running the test. Machine Learning Yearning is useful because it frames development around choosing an error target and an evaluation signal; do not present it as an AI-specific maturity standard. The group should choose a question and an observable success condition before adding components.

#### Ask

What result would make you abandon the current approach rather than add another feature?

#### Watch in the exercise

In the charter, write two likely failures and how the group would notice each one.

#### Sources

[Machine Learning Yearning](https://github.com/ajaymache/machine-learning-yearning/blob/master/full%20book/machine-learning-yearning.pdf); [Charter template](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/project/CHARTER.md).


### D1-F5 · PoC: prove the mechanism manually

- Module: Framing, before the selected modules
- Instructor: Miriah
- Type: framing
- Timing: 1 minute
- Layout: 09 Lab and code

#### Detailed preparation

The first AI PoC can be a chat window, copy-and-paste, and a human check. That exposes whether the question, evidence, and answer contract make sense before the team automates the path. For the access example, paste the current procedure, ask for the next step and source passage, then compare the result with the answer contract. Record the input and output. The a16z application-stack essay is a practitioner architecture overview; use it for the idea that an LLM application has surrounding components, not as proof that one stack is universally correct.

#### Ask

Which manual step would you automate first, and what evidence would show that automation is safe?

#### Watch in the exercise

Groups later build two prompt-only prototypes; keep the copied context and answer criteria visible for comparison.

#### Sources

[The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/); [Course authoring principles](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/AUTHORING.md).


### D1-F6 · A PoC exits with evidence, not enthusiasm

- Module: Framing, before the selected modules
- Instructor: Miriah
- Type: framing
- Timing: 1 minute
- Layout: 05 Two column 1

#### Detailed preparation

Do not ask whether the answer “feels better.” Ask which criteria it met, which evidence was missing, and what the next experiment is. A PoC is complete when the team has learned enough to choose a next step: revise the question, change the supplied evidence, change the prompt, or stop. A fluent response is not itself evidence. This is the bridge into prompt patterns: Eli's module will make the brief repeatable and compare variations on the same task.

#### Ask

What would make a prompt-only PoC a useful failure?

#### Watch in the exercise

Groups should carry one comparison question and two likely failures into the prompt-pattern exercise.

#### Sources

[Machine Learning Yearning](https://github.com/ajaymache/machine-learning-yearning/blob/master/full%20book/machine-learning-yearning.pdf); [Prompt patterns module](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md).


### D1-F7 · MVP: one person completes one useful flow

- Module: Framing, before the selected modules
- Instructor: Miriah
- Type: framing
- Timing: 1 minute
- Layout: 05 Two column 2

#### Detailed preparation

An MVP is one usable path for one important user task. For the access question, it might accept the request, gather the relevant procedure, present a proposed next step and source, and route uncertainty to a person. It does not need every system integration on day one. The product-market-fit reading is a product-development frame, not an AI engineering standard. The practical test is whether a person can complete the flow and whether the team can measure its quality.

#### Ask

What is the smallest end-to-end flow your user could complete without a team member explaining the demo?

#### Watch in the exercise

Groups should keep their first product boundary narrow enough to demonstrate in the pitch.

#### Sources

[The product-market fit framework](https://pmarchive.com/guide_to_startups_part4.html); [Concrete startup idea handout](https://corporate.aiaspire.ai/accenture/titanium/NA/agenda/cohort_2/What_We_Mean_by_a_Concrete_Startup_Idea.pdf).


### D1-F8 · The MVP is one designed experience

- Module: Framing, before the selected modules
- Instructor: Miriah
- Type: framing
- Timing: 1 minute
- Layout: 05 Two column 3

#### Detailed preparation

A showable car is a single coherent design that someone can operate on a defined route; it is not yet the factory, dealer network, maintenance system, or safety certification. For an AI MVP, a small interface, reusable skill, code path, or MCP-connected capability can make one flow repeatable. The important change is that a user can complete the task with less manual explanation. Ask what the equivalent “test drive” is for the group's product.

#### Ask

What would count as a test drive for your proposed AI product?

#### Watch in the exercise

In the napkin sketch, mark the one flow the group will show and the future options it will leave out.

#### Sources

[The product-market fit framework](https://pmarchive.com/guide_to_startups_part4.html); [The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/).


### D1-F9 · Production is repeatable operation

- Module: Framing, before the selected modules
- Instructor: Miriah
- Type: framing
- Timing: 1 minute
- Layout: 07 Big stats

#### Detailed preparation

Production is the infrastructure around the working design. For an AI system, that means current context, identity and permissions, repeatable evaluation, monitoring, recovery, release controls, and a person or team responsible for incidents. A prompt-only application can be production software if it has those controls; a complex agent can remain a PoC if it does not. Anthropic's article supports the simplicity-first distinction between workflows and agents; use it as engineering guidance, not a universal maturity rubric.

#### Ask

Which production responsibility would be missing if the demo only showed a successful answer?

#### Watch in the exercise

Groups should name one quality risk and one person who would own the consequence of failure.

#### Sources

[Building effective agents](https://www.anthropic.com/engineering/building-effective-agents); [Module 01 production discussion](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).


### D1-F10 · Production is the infrastructure around the car

- Module: Framing, before the selected modules
- Instructor: Miriah
- Type: framing
- Timing: 1 minute
- Layout: 06 Process steps 1

#### Detailed preparation

Translate the physical analogy into system responsibilities. The user-facing assistant is the car; context assembly is the map and fuel, workflows are the route, permissions are the brakes and access gates, evals are the test track, and observability is the service record. These are analogies, not literal component requirements. The course will introduce them in sequence: prompts, agents, retrieval, evals, memory, architecture, guardrails, research, and off-the-shelf controls. The production question is always “what evidence says this change is safe enough to operate?”

#### Ask

Which control would you need before allowing the assistant to change data rather than only suggest a next step?

#### Watch in the exercise

Ask groups to circle one production concern their current PoC intentionally leaves unresolved.

#### Sources

[The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/); [Author's context-assembly notes](https://github.com/soypete/ctx-eng-book/blob/main/research/context-assembly-pipeline-patterns.md).


### D1-F11 · The same build ladder applies to AI

- Module: Framing, before the selected modules
- Instructor: Miriah
- Type: framing
- Timing: 1 minute
- Layout: 04 Icon cards

#### Detailed preparation

Make the translation explicit. The PoC is a question answered through a prompt, perhaps with copy-and-pasted evidence and a human check. The MVP makes one path repeatable with reusable instructions, code, a tool, or an MCP connection. Production adds the surrounding operation: workflows, fresh and authorized context, evaluation gates, monitoring, recovery, and accountable ownership. Technology does not determine the maturity level. Use this mental model when deciding whether an agent, retrieval, memory, or guardrail earns its complexity.

#### Ask

Which new evidence—not which new component—would move your system to the next level?

#### Watch in the exercise

Groups should label their proposed system as a PoC, MVP, or production target and state what evidence is still missing.

#### Sources

[The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/); [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).


### D1-F12 · Day 1: answer one question, then earn complexity

- Module: Framing, before the selected modules
- Instructor: Miriah
- Type: framing
- Timing: 1 minute
- Layout: 02 Agenda

#### Detailed preparation

Close the opening with the day's working contract. Groups will choose a real question, define what a useful answer contains, compare two prompt-only attempts, build a first agent, and build a RAG baseline over their own artifacts. The goal is not to leave with a production system; it is to leave with a concrete problem, evidence about a first solution, and an honest next step. Miriah then orients the shared development environment. The later code instructors own their notebook mechanics and implementation details.

#### Ask

What is the first question your group will answer, and what evidence will tell you whether the prototype helped?

#### Watch in the exercise

Carry the question, answer contract, and first failure hypothesis into the group charter.

#### Sources

[Day 1 schedule](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/schedule/day1.md); [Day 1 cohort outline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/slides/chicago-sept-24/README.md); [Concrete Idea Worksheet](https://corporate.aiaspire.ai/accenture/titanium/NA/agenda/cohort_2/Concrete_Idea_Worksheet.pdf).


### D1-M01-C1 · Your environment is a shared workbench

- Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
- Instructor: Miriah, no-code orientation
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column

#### Detailed preparation

A development environment is the place and configuration in which we edit and run the application. It is not the model itself. Engineers have long needed to reproduce a teammate's result; AI adds changing prompts, models, and context to that familiar problem. Use an access-help answer as the example: identical visible wording in a prompt is not enough to reproduce it if the model, source documents, or settings changed. Explain a dependency as a library the code needs, and a setting as a value controlling a run. Miriah owns this no-code orientation. The purpose is to locate the work and recognize its inputs and outputs, not to teach shell syntax. Keep API keys and confidential documents out of commits and screenshots. A saved output shows one observed run, not a guarantee about every future run.

#### Ask

Which changed input could explain two different answers from the same source file?

#### Watch in the exercise

Find the notebook, environment settings, and saved artifact location; distinguish source from result without running code in the concept slot.

#### Sources

[Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).


### D1-M01-C1B · Your environment is a shared workbench · The practical check

- Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
- Instructor: Miriah, no-code orientation
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.

#### Ask

Which changed input could explain two different answers from the same source file?

#### Watch in the exercise

Find the notebook, environment settings, and saved artifact location; distinguish source from result without running code in the concept slot.

#### Sources

[Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).


### D1-M01-C2 · The repo keeps a history of the work

- Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
- Instructor: Miriah, no-code orientation
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps

#### Detailed preparation

This is the simple history we want to preserve. The spec says what needs to be built. Prompts are the instructions we try; prompt history records what we asked, what context we supplied, and what the system returned. Checks are the recurring questions we use to see whether the system is helping. Rubrics say what we will look for in an answer. Results are the saved outputs we can inspect and compare. Docs are the reference materials people and AI tools can find and update in the repo. Seeds are starter examples for demonstrating the workflow; they are not evidence about the group’s product.

#### Ask

If an answer changes, which part of the history would you inspect first?

#### Watch in the exercise

Miriah points out where the project keeps the spec, prompts, saved results, and reference docs. The code walkthroughs will use these materials later.

#### Sources

[Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Module 01 workspace initialization](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Artifact integrity rules](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/AGENTS.md).


### D1-M01-C2B · The repo keeps a history of the work · The practical check

- Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
- Instructor: Miriah, no-code orientation
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.

#### Ask

If an answer changes, which part of the history would you inspect first?

#### Watch in the exercise

Miriah points out where the project keeps the spec, prompts, saved results, and reference docs. The code walkthroughs will use these materials later.

#### Sources

[Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Module 01 workspace initialization](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Artifact integrity rules](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/AGENTS.md).


### D1-M01-C3 · A small change should have a clear history

- Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
- Instructor: Miriah, no-code orientation
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps 1

#### Detailed preparation

Use the familiar idea of tracked changes in a shared document. Version control preserves a history instead of relying on filenames such as final-final. A branch separates work in progress, a diff reveals the exact edit, and a commit records a checkpoint. Pushing shares commits; a pull request invites review; merging incorporates the change. These are different actions. In this course, origin normally points to the learner's fork and upstream to the course repository. Those names are conventions whose actual addresses must be checked, not proof of ownership. Fetching receives remote history without itself changing working files. Ask learners to read an AI-written change before accepting it. A readable history will matter when a changed prompt improves one case and breaks another.

#### Ask

Does committing a change mean that someone else has reviewed it?

#### Watch in the exercise

Miriah shows location, branch, diff, and destination. Stop before sharing if the diff contains unexpected files or the remote is unfamiliar.

#### Sources

[GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow); [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).


### D1-M01-C3B · A small change should have a clear history · The practical check

- Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
- Instructor: Miriah, no-code orientation
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.

#### Ask

Does committing a change mean that someone else has reviewed it?

#### Watch in the exercise

Miriah shows location, branch, diff, and destination. Stop before sharing if the diff contains unexpected files or the remote is unfamiliar.

#### Sources

[GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow); [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).


### D1-M01-C4 · Review the change, not just the successful run

- Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
- Instructor: Miriah, no-code orientation
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 1

#### Detailed preparation

A successful local run answers only whether that attempt completed. Review asks whether the change is appropriate to share. For example, a more helpful access answer is not a good change if its debug output exposes an employee identifier. Record which prompt and source version were used so a teammate can repeat the comparison, accepting that model outputs may vary. The module's later production discussion introduces required checks, branch protection, and designated reviewers; these automate parts of the manual discipline, not human accountability. Stop when the changed files or destination are not understood. Miriah's selected presentation remains a no-code orientation even though the repository contains a notebook that opens a real demonstration pull request. Do not imply the live class will perform all of those actions during this primer.

#### Ask

What would a reviewer need beyond a screenshot of the answer?

#### Watch in the exercise

Explain the proposed edit and its saved evidence to a teammate; troubleshooting belongs in the practical block.

#### Sources

[Module 01 Learn/Create/Grow](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).


### D1-M01-C4B · Review the change, not just the successful run · The practical check

- Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
- Instructor: Miriah, no-code orientation
- Type: core
- Timing: 1 minute
- Layout: 09 Lab and code 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.

#### Ask

What would a reviewer need beyond a screenshot of the answer?

#### Watch in the exercise

Explain the proposed edit and its saved evidence to a teammate; troubleshooting belongs in the practical block.

#### Sources

[Module 01 Learn/Create/Grow](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).


### D1-M01-R1 · Optional: make review a system property

- Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
- Instructor: Miriah
- Type: optional
- Timing: 0 minutes
- Layout: 04 Icon cards

#### Detailed preparation

This optional engineering reading extends the shared-workbench idea. GitHub's protected-branch documentation describes enforceable review and check requirements. Its contribution is practical: team rules can be applied by the platform rather than remembered before each merge. It does not establish that the tests represent real user risks. For an AI application, investigate whether changing a prompt, model configuration, or retrieval source triggers the same quality review as changing code. Do not require learners to configure branch rules here. The question for later work is which evidence should prevent a change from being shared, and who owns exceptions. Read the official documentation for the current repository plan and permissions before selecting a particular configuration.

#### Ask

Which failure would your current checks miss even if every check passed?

#### Watch in the exercise

Optional follow-up only; no additional code exercise or core minutes.

#### Sources

[GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches); [Module 01 production discussion](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).


### D1-M02-C1 · A prompt is the brief for one request

- Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
- Instructor: Eli, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

A prompt is the brief for one request. It gives the model the task, audience, facts, and desired answer shape. It does not change the model’s training. Use the internal support question as the example: the model may understand “access” but cannot infer the team’s rules directly without supplying them. The rest of this module is a menu of ways to make that brief more useful.

#### Ask

What important fact would the model be forced to guess if it is not in the prompt?

#### Watch in the exercise

Eli begins with the same question and shows how each prompt pattern changes the request.

#### Sources

[Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb).


### D1-M02-C2 · Few-shot: show the behavior you want

- Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
- Instructor: Eli, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 08 Quote

#### Detailed preparation

Brown et al. found that scaling language models improved task-agnostic few-shot performance and sometimes made it competitive with earlier fine-tuned systems. Their setup used demonstrations in the text interaction without gradient updates or fine-tuning. The result is historically important, but it is not a promise that a few examples will solve our business problem. Few-shot is useful when the model needs to follow a local convention: how a consultant writes a finding, how an issue is classified, or which fields belong in a response. Use small, representative examples and keep them consistent. The model can still copy a mistake from an example, so check the result against the task.

#### Ask

What behavior would you demonstrate with an example rather than describe in another paragraph?

#### Watch in the exercise

Eli compares a prompt with no examples against one with examples while holding the question and evidence constant.

#### Sources

[Few-shot learners, Brown et al., 2020](https://arxiv.org/abs/2005.14165); [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb).


### D1-M02-C3 · Context supplies the facts the model cannot know

- Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
- Instructor: Eli, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column

#### Detailed preparation

Context is the information the model needs for this request but cannot know directly: a current policy, account state, project file, or customer record. More context is not always better. Include relevant, authorized facts and leave out sensitive or distracting material. If the answer changes when the policy changes, the next engineering question is how to provide current context reliably; retrieval addresses that later.

#### Ask

What fact would the model otherwise have to guess?

#### Watch in the exercise

Eli compares the same prompt with and without a supplied policy excerpt.

#### Sources

[Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb); [The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/).


### D1-M02-C4 · Persona and format shape the answer

- Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
- Instructor: Eli, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 1

#### Detailed preparation

A persona sets viewpoint and audience, not credentials or new knowledge. An output format makes the response easier to read or pass to another program. For example, “write for a helpdesk analyst” changes vocabulary, while fields such as issue, source, owner, and next step make the result inspectable. JSON is only a shape; it does not make the values correct.

#### Ask

Which part of the prompt changes the reader, and which part changes the shape of the answer?

#### Watch in the exercise

Eli compares persona and structured-output variants and checks factual content separately from voice and formatting.

#### Sources

[Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb); [Author's semantic-contract notes](https://github.com/soypete/ctx-eng-book/blob/main/research/semantic-contracts.md).


### D1-M02-C5 · Chain of thought makes difficult work explicit

- Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
- Instructor: Eli, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps

#### Detailed preparation

Chain-of-thought research showed benefits from intermediate-step examples on selected reasoning tasks. Teach the practical version: make assumptions, calculations, evidence, and a concise justification checkable. Do not treat a generated rationale as a faithful record of internal computation or as proof of correctness. More steps can add time while preserving the same error.

#### Ask

Which step could you verify independently?

#### Watch in the exercise

Eli compares a direct answer with a structured answer that exposes checkable work.

#### Sources

[Chain-of-thought prompting, Wei et al., 2022](https://arxiv.org/abs/2201.11903); [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb).


### D1-M02-C6 · ReAct: reason, act, observe

- Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
- Instructor: Eli, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps 1

#### Detailed preparation

ReAct combines reasoning with actions and observations. In a simple example, the model decides that it needs a current account status, calls an approved lookup, reads the result, and then answers or stops. This is the bridge to Agents 101: when the action is a real tool call, the prompt becomes part of a larger loop. ReAct does not grant permission; the surrounding application decides which tools exist, what they can do, and when the loop must stop.

#### Ask

What observation would change the next action?

#### Watch in the exercise

Eli will show the prompt pattern first; Beric will later show the agent harness that owns the tool loop.

#### Sources

[ReAct, Yao et al., 2022](https://arxiv.org/abs/2210.03629); [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb).


### D1-M02-C7 · Self-refine changes the answer; meta-prompting changes the brief

- Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
- Instructor: Eli, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 2

#### Detailed preparation

Self-refine asks the system to improve a draft answer. Meta-prompting asks the system to act like an editor of the task itself: inspect the request, identify ambiguity or missing requirements, and propose a clearer prompt. A useful meta-prompt might say: “Review this task, prompt, and failed examples. Identify ambiguity, missing constraints, and an improved prompt. Do not solve the task.” The team then tests that proposed prompt on the same cases. Meta-prompting produces a candidate instruction; it does not establish that the instruction is correct. Both loops can preserve the same model error, so use an external criterion, save the versions, and set a small revision budget.

#### Ask

Did the revision improve the answer, the prompt, or both—and what evidence shows that?

#### Watch in the exercise

Eli compares a first prompt and a meta-prompt-generated revision, then runs both against the same cases and records the prompt versions.

#### Sources

[Self-Refine, Madaan et al., 2023](https://arxiv.org/abs/2303.17651); [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb).


### D1-M02-C8 · Compare patterns like an experiment

- Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
- Instructor: Eli, code walkthrough
- Type: core
- Timing: 1 minute
- Layout: 09 Lab and code

#### Detailed preparation

The comparison is an experiment, not a contest between two unrelated demos. Keep the user question, evidence, model, output criteria, and test cases constant. Change one thing—for example, add two few-shot examples, add a policy excerpt, require a structured format, or ask for checkable reasoning. Save both prompt versions and outputs. Compare the whole pattern of results, not only the best answer: which criteria passed, which cases failed, how consistent were the answers, and what did the change cost in time or tokens? If the change improves the same task without new actions, keep the simpler prompt. If the failure is missing source or current information, investigate retrieval. If the next step depends on an observation or tool result, investigate an agent. If a fixed sequence works, keep it as a function or workflow.

#### Ask

If prompt B wins one case but loses another, what would you inspect before choosing it?

#### Watch in the exercise

Groups choose one pattern, compare two prompt-only prototypes on the same cases, record the evidence, and carry the unresolved failure into the agent exercise.

#### Sources

[Prompt patterns Create/Grow](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb); [Simple workflows versus agents](https://www.anthropic.com/engineering/building-effective-agents).


### D1-M02-R1 · Optional: from examples to measured refinement

- Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
- Instructor: Eli
- Type: optional
- Timing: 0 minutes
- Layout: 08 Quote

#### Detailed preparation

Use these papers to distinguish mechanisms, not to create a universal ranking of prompt tricks. The few-shot study investigated task demonstrations without parameter updates. The chain-of-thought study investigated intermediate reasoning examples on particular tasks and models. Self-Refine investigated model-generated feedback followed by revision. Their reported task results do not establish a benefit for the group's support workflow or current endpoint. A useful follow-up experiment would keep representative cases separate from prompt development and compare usefulness with latency and call count. Record regressions as well as improvements. The research question is whether the additional mechanism fixes a specific error, not whether the response sounds more thoughtful. This optional slide is outside the 15-minute introduction.

#### Ask

Which of these mechanisms would address your observed error, and which would not?

#### Watch in the exercise

Optional reading, not an extra optimization module.

#### Sources

[Brown et al., 2020](https://arxiv.org/abs/2005.14165); [Wei et al., 2022](https://arxiv.org/abs/2201.11903); [Madaan et al., 2023](https://arxiv.org/abs/2303.17651).


### D1-M03-C1 · A model answers; an agent can choose a next step

- Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps

#### Detailed preparation

The distinction is the surrounding application behavior, not a magical new kind of model. A single model call can suggest an action, but the application decides whether and how to execute it. An agent repeatedly uses a model to select a next step from permitted options, receives the result, and continues or stops. For an access question it might search a procedure, discover that information is missing, and ask a clarifying question. A fixed workflow can also call tools; call something agentic here when the next step is selected dynamically. Terminology varies across products, so keep this operational definition visible. If every step is known beforehand, a fixed workflow is often easier to inspect. The lab's tool loop is deliberately small and does not imply autonomous administration of a real account.

#### Ask

Which box actually runs a tool, and which box decides whether it is allowed?

#### Watch in the exercise

In Beric's trace, locate the model message requesting a tool, the tool result, and the subsequent model response.

#### Sources

[Agent harness notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Workflow and agent definitions](https://www.anthropic.com/engineering/building-effective-agents).


### D1-M03-C1B · A model answers; an agent can choose a next step · The practical check

- Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.

#### Ask

Which box actually runs a tool, and which box decides whether it is allowed?

#### Watch in the exercise

In Beric's trace, locate the model message requesting a tool, the tool result, and the subsequent model response.

#### Sources

[Agent harness notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Workflow and agent definitions](https://www.anthropic.com/engineering/building-effective-agents).


### D1-M03-C2 · Tools give the loop controlled capabilities

- Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

A tool is a function the model may ask the application to run. Its contract explains the name, purpose, and allowed arguments; arguments are the values passed to the function. The system must still validate those values and enforce access. The notebook's three tools search the charter, search saved prompt outputs, and log a request. These are not a full enterprise service catalog. ReAct is a research milestone connecting reasoning with actions and observations, helping explain why a lookup can change the next step instead of merely decorating the final response. A tool can fail, return no result, or return untrusted text. None of those outcomes gives the model new authority. A suggestion to log or change something must remain within the application's permitted scope.

#### Ask

If a retrieved page says “ignore your rules,” does that change the tool's permissions?

#### Watch in the exercise

Inspect how precise tool descriptions affect tool selection; do not equate making a tool call with making the correct call.

#### Sources

[ReAct, Yao et al., 2022](https://arxiv.org/abs/2210.03629); [Agent harness tools](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb).


### D1-M03-C2B · Tools give the loop controlled capabilities · The practical check

- Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.

#### Ask

If a retrieved page says “ignore your rules,” does that change the tool's permissions?

#### Watch in the exercise

Inspect how precise tool descriptions affect tool selection; do not equate making a tool call with making the correct call.

#### Sources

[ReAct, Yao et al., 2022](https://arxiv.org/abs/2210.03629); [Agent harness tools](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb).


### D1-M03-C3 · The harness owns the loop's boundaries

- Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps 1

#### Detailed preparation

The harness is the application scaffolding that manages instructions, tool execution, state, limits, and records. Middleware is code around that loop that can inspect or constrain a step. The lab adds logging and a model-call limit; a model-call limit is not identical to a tool-call limit because one model turn may request multiple tools. Describe a failed lookup: retrying forever cannot create missing evidence. The system needs a bounded exit and an honest explanation. A trace records observable events; it is not a readout of the model's hidden reasoning. Later architecture work adds recovery and durable state, evaluation inspects outcomes and trajectories, and memory controls what persists. These are separate responsibilities around the model, not properties gained by merely naming the system an agent.

#### Ask

What should the user receive when the budget ends before the task is complete?

#### Watch in the exercise

Watch middleware messages and the enforced limit; inspect the saved transcript rather than only the final answer.

#### Sources

[Agent harness limits and trace](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).


### D1-M03-C3B · The harness owns the loop's boundaries · The practical check

- Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.

#### Ask

What should the user receive when the budget ends before the task is complete?

#### Watch in the exercise

Watch middleware messages and the enforced limit; inspect the saved transcript rather than only the final answer.

#### Sources

[Agent harness limits and trace](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).


### D1-M03-C4 · Autonomy needs a reason and a stopping rule

- Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 3

#### Detailed preparation

An agent is useful when the needed sequence cannot be fully determined before observing results. That flexibility creates additional failure paths. For the recurring support question, a known procedure can be a fixed lookup and answer. A diagnosis needing an initial symptom, a search, and a follow-up question may benefit from adaptation. The system should decline an out-of-scope request, ask when essential information is absent, and stop before an unapproved action. These are legitimate outcomes, not embarrassing failures to hide. The current engineering direction is making longer tasks inspectable and recoverable; that is a challenge, not a claim that every workflow should become autonomous. The group should retain a simpler design if it meets its quality and cost requirements.

#### Ask

What observation would change the next step in your proposed loop?

#### Watch in the exercise

Compare in-scope, human-needed, and out-of-scope questions. Check whether tool behavior matches the scope before praising fluency.

#### Sources

[Agent harness Create/Grow](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).


### D1-M03-C4B · Autonomy needs a reason and a stopping rule · The practical check

- Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 1 minute
- Layout: 09 Lab and code 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.

#### Ask

What observation would change the next step in your proposed loop?

#### Watch in the exercise

Compare in-scope, human-needed, and out-of-scope questions. Check whether tool behavior matches the scope before praising fluency.

#### Sources

[Agent harness Create/Grow](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).


### D1-M03-R1 · Optional: action loops need more than fluent reasoning

- Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
- Instructor: Beric
- Type: optional
- Timing: 0 minutes
- Layout: 08 Quote

#### Detailed preparation

ReAct provides a research reference for interleaving reasoning and action. Anthropic's long-running harness article is an engineering case study on sustaining progress across sessions, not a universal proof of reliability. Together they motivate a distinction between choosing a useful next action and managing an application over time. Ask whether a restarted run knows what really completed. An attempted tool call is not evidence of a completed side effect; blindly repeating a write could duplicate work. Later architecture concepts cover checkpoints and safe retries. No new multi-agent or deployment lab is added here. Read the sources to identify what was tested, which environment supplied feedback, and what would differ for an internal helpdesk tool.

#### Ask

After an interruption, which evidence would make a retry safe?

#### Watch in the exercise

Optional research only; the first harness does not implement full production recovery.

#### Sources

[ReAct](https://arxiv.org/abs/2210.03629); [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).


### D1-M04-C1 · “Looks good” is the start of a test, not the result

- Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

A vibe check is an informal inspection of whether an output seems useful. In this course it becomes deliberate: write the expected properties and record a human verdict with a reason. Evaluation carries forward a familiar software-testing idea, checking behavior against expectations, but free-form answers often need a rubric rather than one exact string. For the support question, “clear answer” and “correct permitted next step” are different requirements. Write what passing each one means before looking at scores. A test case is a particular question and situation; a rubric is the rule for judging it. A handful of examples can reveal defects but cannot establish representative reliability. The next step is not immediately to automate the judgment, but to check that two people can apply the rule consistently.

#### Ask

Could two reviewers reasonably disagree about the word “helpful” in your rubric?

#### Watch in the exercise

Beric starts with rubric definitions and hand-scored transcripts before introducing the automated judge.

#### Sources

[Vibe checks and judges notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM judge study, Zheng et al., 2023](https://arxiv.org/abs/2306.05685).


### D1-M04-C1B · “Looks good” is the start of a test, not the result · The practical check

- Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.

#### Ask

Could two reviewers reasonably disagree about the word “helpful” in your rubric?

#### Watch in the exercise

Beric starts with rubric definitions and hand-scored transcripts before introducing the automated judge.

#### Sources

[Vibe checks and judges notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM judge study, Zheng et al., 2023](https://arxiv.org/abs/2306.05685).


### D1-M04-C2 · A judge is another model with a narrow job

- Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column

#### Detailed preparation

LLM-as-a-judge means using a language-model call to assess an output against a defined criterion. It can help inspect many responses, but it does not become an objective authority by returning a number. The 2023 MT-Bench and Chatbot Arena study examined model judging and identified biases including position and verbosity effects. The notebook checks that the returned score is in range and the rationale is present, retries malformed output, and reports failure rather than manufacturing a neutral score. That validates the response's format, not the truth of its judgment. The answering model and judge may be the same model in this lab, which can correlate their errors. Human calibration means comparing judgments on shared cases and resolving why they differ.

#### Ask

What is the difference between a valid score and a justified score?

#### Watch in the exercise

Inspect the strict judge's error handling and compare its rationale with a hand verdict on the same transcript.

#### Sources

[Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685); [Strict judge implementation](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb).


### D1-M04-C2B · A judge is another model with a narrow job · The practical check

- Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.

#### Ask

What is the difference between a valid score and a justified score?

#### Watch in the exercise

Inspect the strict judge's error handling and compare its rationale with a hand verdict on the same transcript.

#### Sources

[Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685); [Strict judge implementation](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb).


### D1-M04-C3 · An answer can be clear, useful, and wrong

- Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards 1

#### Detailed preparation

Consider an access answer that gives a beautifully worded but nonexistent menu path. It may be clear and actionable in tone while unsupported. Conversely, copying a correct policy passage may be grounded but leave the employee unsure what to do. The lab separates these dimensions into three judges. Do not average them into a number that lets readability cancel an unsupported instruction without an explicit decision rule. Groundedness is support relative to available evidence; it does not prove the evidence is current or correct. Use direct checks for properties that are exact, such as an identifier or required field, and model judgments for properties needing interpretation. This separation prepares later RAG metrics and agent outcome checks, which answer different questions from general answer quality.

#### Ask

Can an answer faithfully repeat an outdated procedure and still fail the user's task?

#### Watch in the exercise

Inspect the separate judge columns and their rationales; identify which dimension explains a disagreement.

#### Sources

[Three judge dimensions](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [Ragas faithfulness definition](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/).


### D1-M04-C3B · An answer can be clear, useful, and wrong · The practical check

- Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.

#### Ask

Can an answer faithfully repeat an outdated procedure and still fail the user's task?

#### Watch in the exercise

Inspect the separate judge columns and their rationales; identify which dimension explains a disagreement.

#### Sources

[Three judge dimensions](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [Ragas faithfulness definition](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/).


### D1-M04-C4 · Disagreement tells you where to investigate

- Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps

#### Detailed preparation

The most informative row may be the one where a judge disagrees with a person, not the one with the highest score. Read the answer, the criterion, and the source before deciding which component failed. If the rubric is vague, clarify it and re-score consistently; if evidence is absent, investigate retrieval; if the judge rewards irrelevant verbosity, revise and recalibrate the judge. A confidence-like number is not a calibrated probability of correctness. Preserve cases that expose failures and record model and rubric versions. Stop relying on a judge when it cannot distinguish known good and bad examples; return to reviewed cases. The forward direction is a repeatable measurement process tied to real decisions, not progressively more elaborate scoring dashboards.

#### Ask

What would make you distrust the judge rather than change the answer?

#### Watch in the exercise

Read the highest-disagreement row in the heatmap and explain the evidence. Do not replace an observed failure with a guessed score.

#### Sources

[Disagreement analysis and responsible controls](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM judge limitations](https://arxiv.org/abs/2306.05685).


### D1-M04-C4B · Disagreement tells you where to investigate · The practical check

- Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 1 minute
- Layout: 09 Lab and code 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.

#### Ask

What would make you distrust the judge rather than change the answer?

#### Watch in the exercise

Read the highest-disagreement row in the heatmap and explain the evidence. Do not replace an observed failure with a guessed score.

#### Sources

[Disagreement analysis and responsible controls](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM judge limitations](https://arxiv.org/abs/2306.05685).


### D1-M04-R1 · Optional: calibrate the measuring instrument

- Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
- Instructor: Beric
- Type: optional
- Timing: 0 minutes
- Layout: 08 Quote

#### Detailed preparation

The MT-Bench study is a starting point for reading about model judges, not a guarantee of agreement on enterprise questions. Its benchmarks and preference judgments are not identical to checking a private procedure. Investigate how answer order, verbosity, and the choice of judge affect your use case. Agreement alone is insufficient when evaluators share blind spots or lack the relevant source. A useful follow-up is to retain a reviewed set containing acceptable, unacceptable, and borderline examples and recheck it when the rubric or model changes. Human judgments also need clear criteria and reconciliation. The research question is whether the instrument supports the decision you intend to make, not whether one evaluator is universally best.

#### Ask

How would you detect a bias that both model judges share?

#### Watch in the exercise

Optional reading; no new evaluation-framework lab is required.

#### Sources

[Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685); [Notebook calibration discussion](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb).


### D1-M05-C1 · A direct question needs accessible evidence

- Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column

#### Detailed preparation

Retrieval-augmented generation, or RAG, combines finding external material with generating an answer from it. It addresses a knowledge-access problem: a model's training is not a live copy of the organization's changing procedures. Lewis and colleagues' 2020 paper is a milestone combining learned model knowledge with retrieved passages; information retrieval itself is much older. Today's notebook uses a practical retrieve-then-prompt pipeline, not a reproduction of the paper's training method. For an internal access question, evidence must be both relevant and permitted for this user. RAG does not guarantee truth, current sources, or correct reasoning. A plausible generated transcript in the corpus is not automatically authoritative policy. Source quality and provenance remain application responsibilities.

#### Ask

If the source is wrong, what can retrieval actually improve?

#### Watch in the exercise

Beric asks the same question without source text and with retrieved context; inspect the evidence rather than assuming the second answer must be better.

#### Sources

[RAG, Lewis et al., 2020](https://arxiv.org/abs/2005.11401); [RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb).


### D1-M05-C1B · A direct question needs accessible evidence · The practical check

- Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.

#### Ask

If the source is wrong, what can retrieval actually improve?

#### Watch in the exercise

Beric asks the same question without source text and with retrieved context; inspect the evidence rather than assuming the second answer must be better.

#### Sources

[RAG, Lewis et al., 2020](https://arxiv.org/abs/2005.11401); [RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb).


### D1-M05-C2 · Prepare the library, then search it for each question

- Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps

#### Detailed preparation

A corpus is the collection of source material. A chunk is a passage selected as a retrievable unit. An embedding is a list of numbers used to compare text in a learned representation; closeness is a relevance signal, not a truth score. Preparation builds the searchable collection. At request time the question is represented, candidate chunks are ranked, and selected passages are supplied directly in the request. The model then uses those retrieved passages as evidence, which is why prompting and retrieval belong in the same story. The notebook makes these steps visible with simple chunking and cosine similarity, then uses LangChain and local Qdrant to package them. The author's context-assembly notes help explain the pipeline but are a working synthesis. Keep the retrieved chunks with each answer so it can be traced back to what the model actually saw; carrying source IDs as chunk metadata is the module's Grow step.

#### Ask

Which step changes the stored index, and which step happens for every question?

#### Watch in the exercise

Locate chunk creation, ranking, and context assembly before the library version; explain what each library component replaces.

#### Sources

[RAG from scratch and library pipeline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [Author's context-assembly notes](https://github.com/soypete/ctx-eng-book/blob/main/research/context-assembly-pipeline-patterns.md).


### D1-M05-C2B · Prepare the library, then search it for each question · The practical check

- Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.

#### Ask

Which step changes the stored index, and which step happens for every question?

#### Watch in the exercise

Locate chunk creation, ranking, and context assembly before the library version; explain what each library component replaces.

#### Sources

[RAG from scratch and library pipeline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [Author's context-assembly notes](https://github.com/soypete/ctx-eng-book/blob/main/research/context-assembly-pipeline-patterns.md).


### D1-M05-C3 · Diagnose the missing evidence before the answer

- Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards 2

#### Detailed preparation

These questions separate errors that need different fixes. If the procedure never entered the corpus, changing the prompt cannot retrieve it. If it exists but the wrong chunks were selected, adjust retrieval. If the correct passage reached the model and the response ignored it, inspect generation and instructions. The top-k setting is the number of selected chunks: too few can omit necessary evidence, while more increases context and may add irrelevant or conflicting material. More is not automatically better. The lab stores questions, answers, and contexts together so later checks can identify the failure stage. It excludes the vibe-check answer-key page from retrieval; otherwise a comparison could reward retrieving the test answers. Stop interpreting an improvement as general quality when the evidence is empty, leaked, or unrepresentative.

#### Ask

Which component should change if the answer-bearing passage never reaches the prompt?

#### Watch in the exercise

Compare two k settings on the same question and inspect actual chunks. Keep baseline contexts with each answer.

#### Sources

[RAG setup, top-k comparison, saved baseline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [RAG artifact contract](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md).


### D1-M05-C3B · Diagnose the missing evidence before the answer · The practical check

- Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.

#### Ask

Which component should change if the answer-bearing passage never reaches the prompt?

#### Watch in the exercise

Compare two k settings on the same question and inspect actual chunks. Keep baseline contexts with each answer.

#### Sources

[RAG setup, top-k comparison, saved baseline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [RAG artifact contract](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md).


### D1-M05-C4 · Agentic retrieval changes the search strategy

- Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps 1

#### Detailed preparation

“RAG is dead” often mixes a criticism of a fixed retrieval recipe with the broader need to supply evidence. Agentic retrieval changes when and how searching happens; it does not eliminate retrieval. Long context is another option when a relevant source set can be supplied directly, but it still needs selection, freshness, and permission decisions. The engineering choice is conditional: compare the simplest adequate approach against adaptive searching on representative cases, cost, and latency. Additional searches should stop when the question is supported, the budget is used, or a missing permission or source prevents progress. Day 2 examines retrieval alternatives rather than assuming one architecture replaces all others. This slide sets up that question without introducing a new lab now.

#### Ask

What evidence would justify a second search instead of a final answer or clarification?

#### Watch in the exercise

Establish the fixed baseline first. Save its failures so later retrieval approaches have a fair comparison.

#### Sources

[RAG baseline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [Agentic retrieval comparison](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb); [RAG versus long-context study](https://arxiv.org/abs/2407.16833).


### D1-M05-C4B · Agentic retrieval changes the search strategy · The practical check

- Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
- Instructor: Beric, code walkthrough
- Type: core
- Timing: 1 minute
- Layout: 09 Lab and code 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change. Ask the check aloud, point to the lab observation, and record an honest result or gap.

#### Ask

What evidence would justify a second search instead of a final answer or clarification?

#### Watch in the exercise

Establish the fixed baseline first. Save its failures so later retrieval approaches have a fair comparison.

#### Sources

[RAG baseline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [Agentic retrieval comparison](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb); [RAG versus long-context study](https://arxiv.org/abs/2407.16833).


### D1-M05-R1 · Optional: retrieval is a design space, not a slogan

- Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
- Instructor: Beric
- Type: optional
- Timing: 0 minutes
- Layout: 05 Two column 3

#### Detailed preparation

Read the 2020 RAG paper for the separation of parameterized knowledge and retrieved evidence. Read the 2024 long-context comparison for a concrete experimental comparison and its chosen models, tasks, and resource assumptions. Do not generalize its findings into “retrieval always wins” or “long context makes search obsolete.” Neither source establishes performance for this group's corpus or current models. Adaptive retrieval adds another policy for selecting evidence and introduces additional calls and stopping decisions. A worthwhile follow-up keeps the question set and source permissions fixed, then measures where each design fails. The durable lesson is to make the evidence route inspectable. The future direction here is an open design question, not a prediction of a winning framework.

#### Ask

Which assumptions would you need to match before applying a paper's result to your system?

#### Watch in the exercise

Optional research; the required exercise remains the fixed RAG baseline.

#### Sources

[Retrieval-augmented generation](https://arxiv.org/abs/2005.11401); [Retrieval Augmented Generation or Long-Context LLMs?](https://arxiv.org/abs/2407.16833).


### D2-M06-C1 · 06 · Exact terms and related meanings need different signals

- Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column

#### Detailed preparation

Start with an internal helpdesk question such as “What is the approval path for ERR-4017?” The exact code and the paraphrase “approval path” create different retrieval clues. Sparse search means matching words in the query and passages; BM25 is one widely used scoring formula that accounts for term frequency, rarity, and document length. Dense search means comparing learned vector representations, so related wording can meet even when tokens differ. Neither score is a relevance proof: both only produce candidates. A reranker is a later model that reads the question and candidate passage together to reorder a shortlist. The retrieval notebook compares dense and BM25 over the same chunks and questions, after page-level evidence labels are corrected. Explain the trajectory from one dense retriever to a measured ladder: preserve the questions and inspect where evidence first appears. The practical stop is the cheapest rung that clears the task bar.

#### Ask

Which part of the question would dense retrieval risk blurring, and which part would BM25 preserve?

#### Watch in the exercise

Retrieval_Ladder Task 2 prints dense and scratch/library BM25 orders for one question; compare the disagreement.

#### Sources

[Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/); [Lucene BM25Similarity](https://lucene.apache.org/core/9_12_1/core/org/apache/lucene/search/similarities/BM25Similarity.html); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)


### D2-M06-C1B · 06 · Exact terms and related meanings need different signals · The practical check

- Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Which part of the question would dense retrieval risk blurring, and which part would BM25 preserve?

#### Watch in the exercise

Retrieval_Ladder Task 2 prints dense and scratch/library BM25 orders for one question; compare the disagreement.

#### Sources

[Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/); [Lucene BM25Similarity](https://lucene.apache.org/core/9_12_1/core/org/apache/lucene/search/similarities/BM25Similarity.html); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)


### D2-M06-C2 · Fuse ranks, then spend judgment carefully

- Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps

#### Detailed preparation

Use the same helpdesk question and show that BM25 may find an error code while dense retrieval finds a policy paraphrase. Their raw scores are not safely comparable because each system has its own scale. Reciprocal rank fusion combines rank positions, using a contribution such as 1/(60 + rank) in this notebook, so an item appearing near the top in both lists rises without score calibration. A reranker is a later, more expensive judge of the question and each candidate together; it can reorder only what entered its candidate pool. The sequence matters: retrieve broadly enough, fuse complementary lists, then rerank a bounded shortlist. The 2009 RRF paper motivates rank-level fusion; it does not guarantee an improvement on this corpus. Treat any gain as a measured result.

#### Ask

If the correct passage never enters the fused shortlist, can reranking recover it?

#### Watch in the exercise

Retrieval_Ladder Task 3 prints the fused list and cross-encoder order; inspect how many candidates reach the reranker.

#### Sources

[Reciprocal rank fusion paper](https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)


### D2-M06-C2B · Fuse ranks, then spend judgment carefully · The practical check

- Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

If the correct passage never enters the fused shortlist, can reranking recover it?

#### Watch in the exercise

Retrieval_Ladder Task 3 prints the fused list and cross-encoder order; inspect how many candidates reach the reranker.

#### Sources

[Reciprocal rank fusion paper](https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)


### D2-M06-C3 · Ask the question more than once

- Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps 1

#### Detailed preparation

Multi-query retrieval is query expansion around the same intent. For “How do I regain access after a locked account?”, rewrites might use “unlock account,” “account lockout recovery,” and the exact internal procedure name. Different wording can expose different lexical or semantic matches, especially for sparse clues. But every rewrite can also drift, duplicate noise, or increase latency. The notebook makes this trade-off visible by generating three rewrites, retrieving for each, and fusing the results. Keep the user question as the anchor and record the rewrites, candidates, and final context. Do not present expansion as a universal upgrade. A useful stopping rule is: add rewrites only when a labelled failure class improves enough to justify extra calls and review burden.

#### Ask

What evidence would show that a rewrite changed coverage rather than merely added duplicates?

#### Watch in the exercise

Retrieval_Ladder Task 3 prints three rewrites and one list per retriever; compare per-case reciprocal ranks in Task 4.

#### Sources

[Iterative query generation for multi-hop QA](https://aclanthology.org/D19-1261/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)


### D2-M06-C3B · Ask the question more than once · The practical check

- Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

What evidence would show that a rewrite changed coverage rather than merely added duplicates?

#### Watch in the exercise

Retrieval_Ladder Task 3 prints three rewrites and one list per retriever; compare per-case reciprocal ranks in Task 4.

#### Sources

[Iterative query generation for multi-hop QA](https://aclanthology.org/D19-1261/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)


### D2-M06-C4 · Choose the cheapest rung that clears the bar

- Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Define the measurement before looking at averages. Hit rate asks whether any top-K chunk came from a labelled evidence page. MRR asks how early the first relevant chunk appears: rank one contributes 1 and rank four contributes 0.25. The notebook also records latency, because an expensive rung is not free. Read the per-case matrix, not only the aggregate table: one question may justify a reranker while the rest do not. The notebook’s production lesson is to ship the cheapest rung that clears a bar and document which question type needs the expensive one. Scores depend on evidence labels and cutoff K; they do not prove the generated answer is correct. Stop when the observed failure is resolved, not when the ladder looks impressive.

#### Ask

Which metric would move when the right passage rises from rank eight to rank two, even if it was already inside the cutoff?

#### Watch in the exercise

Retrieval_Ladder Task 4 prints hit rate, MRR, latency, and a per-case reciprocal-rank matrix; use the matrix to choose one rung.

#### Sources

[DPR retrieval formulation](https://aclanthology.org/2020.emnlp-main.550/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)


### D2-M06-C4B · Choose the cheapest rung that clears the bar · The practical check

- Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
- Instructor: Eli
- Type: core
- Timing: 1 minute
- Layout: 09 Lab and code 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Which metric would move when the right passage rises from rank eight to rank two, even if it was already inside the cutoff?

#### Watch in the exercise

Retrieval_Ladder Task 4 prints hit rate, MRR, latency, and a per-case reciprocal-rank matrix; use the matrix to choose one rung.

#### Sources

[DPR retrieval formulation](https://aclanthology.org/2020.emnlp-main.550/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)


### D2-M06-R1 · Research: retrieval is a two-stage design

- Module: [06 Advanced retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md)
- Instructor: Eli
- Type: optional
- Timing: 0 minutes
- Layout: 08 Quote

#### Detailed preparation

Use Karpukhin and colleagues’ 2020 Dense Passage Retrieval paper as the research anchor. Its contribution is a dual-encoder dense retriever trained from question-passage pairs, presented as a practical alternative to sparse retrieval for open-domain question answering. The important trajectory for this course is architectural: a retriever selects a small candidate context and a reader examines it more deeply. The paper’s benchmark findings are not a promise about an internal helpdesk corpus, its labels, or its embedding endpoint. Ask learners to identify which assumption transfers and which does not. Dense retrieval supplies a complementary signal; it does not eliminate exact identifiers, chunking problems, authorization, or evaluation. The current engineering question is interface and budget: which candidate-generation and inspection stages fit the task?

#### Ask

Which claim from the paper is about a benchmark setup rather than a guarantee for our corpus?

#### Watch in the exercise

Alignment pending for optional research discussion; use the notebook’s dense-versus-BM25 comparison as the local bridge.

#### Sources

[Dense Passage Retrieval for Open-Domain Question Answering](https://aclanthology.org/2020.emnlp-main.550/); [local Retrieval Ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)


### D2-M07-C1 · 07 · Retrieval becomes an interface choice

- Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps

#### Detailed preparation

Hold the model, loop, questions, and scorer constant. Change only the document interface. Agentic RAG gives the model a BM25-backed search_chunks tool that returns ranked sections; the agent can call it again with a new query. Direct corpus interaction, or DCI, gives file tools that list pages, search the wiki, and read a whole page; the agent can choose its next request there too. In both modes, the model proposes a tool call, while application code executes and authorizes it. The retriever’s ranking determines which candidates come back; it does not control the agent’s sequence. For an internal helpdesk question involving an exact policy code and a second page, the interface changes what can be recovered after the first miss. The broader interface also raises authorization, logging, and cost obligations.

#### Ask

What stays constant in the notebook comparison, and what is deliberately changed?

#### Watch in the exercise

DCI_vs_Agentic_RAG setup defines both modes and keeps model, loop, questions, and scoring the same.

#### Sources

[DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)


### D2-M07-C1B · 07 · Retrieval becomes an interface choice · The practical check

- Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

What stays constant in the notebook comparison, and what is deliberately changed?

#### Watch in the exercise

DCI_vs_Agentic_RAG setup defines both modes and keeps model, loop, questions, and scoring the same.

#### Sources

[DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)


### D2-M07-C2 · Let the agent navigate a persistent map

- Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps 1

#### Detailed preparation

A raw corpus is not automatically navigable, but DCI does not inherently require a wiki. This notebook provides one as a navigation aid: a Markdown index containing page names, a purpose line, and section headings. The model proposes the purpose from a digest and the learner corrects it. The wiki is a persistent navigation artifact, not a query-time answer and not a replacement for source pages. In a helpdesk example, the agent can use the map to find an access policy page, inspect a matching line, then read surrounding context. That trajectory can preserve local context better than a single top-k slice, but it also exposes more of the corpus if tools are not scoped. The useful direction is maintained navigation with ownership, freshness, and link checks; DCI can also operate with other corpus maps or search aids.

#### Ask

Why does DCI need a map before it receives a question?

#### Watch in the exercise

Task 1 renders a wiki table; inspect whether each page has a distinct purpose and useful headings.

#### Sources

[DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)


### D2-M07-C2B · Let the agent navigate a persistent map · The practical check

- Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Why does DCI need a map before it receives a question?

#### Watch in the exercise

Task 1 renders a wiki table; inspect whether each page has a distinct purpose and useful headings.

#### Sources

[DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)


### D2-M07-C3 · Compare traces, not just answers

- Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 1

#### Detailed preparation

A fluent final answer hides the route that produced it. The notebook records tool sequence, characters of evidence read, latency, and a short answer for each mode. Then its judge scores each answer against the eval-case reference and records whether the answer named a labelled evidence page. Use a divergence question: did the weaker mode retrieve the wrong evidence, or retrieve the right evidence and synthesize badly? That separates interface failure from generation failure. DCI may earn extra calls when evidence is split across pages or exact identifiers matter; agentic BM25 RAG may be sufficient for a question mapped to one or two sections. These are hypotheses to test locally, not universal winners. Keep caller identity and tool authorization outside the language model’s discretion.

#### Ask

What trace field distinguishes an evidence miss from a generation miss?

#### Watch in the exercise

Tasks 4–5 print answer scores, named-page evidence, calls, characters, latency, and both traces.

#### Sources

[DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)


### D2-M07-C3B · Compare traces, not just answers · The practical check

- Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

What trace field distinguishes an evidence miss from a generation miss?

#### Watch in the exercise

Tasks 4–5 print answer scores, named-page evidence, calls, characters, latency, and both traces.

#### Sources

[DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)


### D2-M07-C4 · Stop at the smallest safe interface

- Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 2

#### Detailed preparation

The notebook’s production lesson is a routing rule: keep the cheaper mode that passes the questions and document what triggers a switch. Add safety to that rule. A DCI tool must be read-only, scoped to an authorized corpus, and checked against caller identity before list, search, or read. A turn limit prevents repeated calls; evidence characters and latency make the cost visible. At runtime, the agent can stop when the available evidence supports an answer, when no progress is being made, when the budget is exhausted, or when permission is missing. A reference answer is an evaluation aid, not a runtime requirement. An agent that reads more pages can still answer incorrectly or leak another user’s transcript, so inspect the trace before widening access.

#### Ask

What must be checked before a DCI read_page call on a user transcript?

#### Watch in the exercise

Task 2’s notebook question explicitly asks which tool could leak a transcript and what to check on the caller.

#### Sources

[DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)


### D2-M07-C4B · Stop at the smallest safe interface · The practical check

- Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
- Instructor: Eli
- Type: core
- Timing: 1 minute
- Layout: 09 Lab and code 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

What must be checked before a DCI read_page call on a user transcript?

#### Watch in the exercise

Task 2’s notebook question explicitly asks which tool could leak a transcript and what to check on the caller.

#### Sources

[DCI research paper](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)


### D2-M07-R1 · Research: direct corpus interaction widens the search interface

- Module: [07 Agentic retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md)
- Instructor: Eli
- Type: optional
- Timing: 0 minutes
- Layout: 08 Quote

#### Detailed preparation

The DCI paper is the research hook for this module. It argues that a fixed similarity interface compresses corpus access into a top-k decision before reasoning, which can be a bottleneck for exact lexical constraints, sparse clue conjunctions, local context checks, and iterative hypotheses. Its proposed interface lets an agent use general terminal tools over the raw corpus without an embedding model, vector index, or retrieval API. Present this as a research claim with a scope: the paper studies benchmark and agentic-search settings, while our notebook compares two local interfaces on a small, labelled corpus. The engineering trade is not semantic retrieval versus intelligence. It is interface resolution versus efficiency, with authorization and observability becoming more important as access broadens.

#### Ask

What evidence would falsify the claim that DCI is worth its extra calls for our questions?

#### Watch in the exercise

Alignment is present through the notebook’s controlled two-mode comparison; no cohort score is assumed.

#### Sources

[Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction](https://arxiv.org/abs/2605.05242); [local DCI versus Agentic RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb)


### D2-M08-C1 · 08 · Synthetic data makes failures testable

- Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps

#### Detailed preparation

Synthetic data generation here means using source documents and a model to propose evaluation cases: questions, reference answers, evidence labels, and metadata. It does not mean stochastic gradient descent. The motivation is coverage: a few friendly questions will not expose exact-token, multi-page, terse, or ambiguous failures. Start from a failure hypothesis—“the code is buried,” “the answer needs two pages,” or “the user omits the product name”—then generate a case that can test it. A generated case is a candidate, not truth. Review its grounding, clarity, representative wording, and intended difficulty before using it to compare retrievers or agents. Preserve provenance so a reviewer can find the source passage and understand why the case exists.

#### Ask

Which source artifact would let a reviewer reject a synthetic question as unsupported?

#### Watch in the exercise

Module 08 notebook cue: build a small-k baseline, then generate candidate questions and references from the corpus. Inspect the generated rows before curation.

#### Sources

[Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)


### D2-M08-C1B · 08 · Synthetic data makes failures testable · The practical check

- Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Which source artifact would let a reviewer reject a synthetic question as unsupported?

#### Watch in the exercise

Module 08 notebook cue: build a small-k baseline, then generate candidate questions and references from the corpus. Inspect the generated rows before curation.

#### Sources

[Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)


### D2-M08-C2 · Metrics answer different diagnostic questions

- Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Keep four lenses distinct and name their inputs. Context recall uses reference-answer information and retrieved context to ask whether needed information was recovered. Context precision uses the retrieved context, with relevance judgments, to ask whether the list is focused. Faithfulness uses the answer and supplied context to ask whether claims are supported. Answer relevancy uses the question and answer to ask whether the response addresses the request. Correctness is not the same as relevance: a response can discuss the right topic while stating a wrong procedure, and correctness needs a trusted reference or reviewed evidence. A retrieval failure can lower recall while the model remains faithful to what it saw. RAGAS introduced a reference-free framework for several dimensions, but model-based metrics remain instruments: inspect examples, calibrate, and never treat one score as ground truth.

#### Ask

If the correct passage is missing but the model says “I don’t know,” which retrieval lens is still failing?

#### Watch in the exercise

Module 08 notebook cue: score faithfulness, answer relevancy, context precision, and context recall, then inspect the metric rows and values.

#### Sources

[RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)


### D2-M08-C2B · Metrics answer different diagnostic questions · The practical check

- Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

If the correct passage is missing but the model says “I don’t know,” which retrieval lens is still failing?

#### Watch in the exercise

Module 08 notebook cue: score faithfulness, answer relevancy, context precision, and context recall, then inspect the metric rows and values.

#### Sources

[RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)


### D2-M08-C3 · Review synthetic cases as measurement assets

- Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

Coverage is a design choice, not a random side effect of generation. Vary topic, persona, query style, and reasoning depth. Include single-hop cases where one passage contains the answer and multi-hop cases where several passages must be connected. For an internal helpdesk corpus, a compliance lead may ask which obligation applies, an engineer may ask what to implement, and a terse user may provide only an error code. Add noisy but plausible phrasing without inventing policy. Reviewers should check that the reference answer is supported, the evidence labels are sufficient, the question is clear, and the difficulty is intentional. Curate once, then compare two system versions on the same set. Otherwise the metric change may be a test-set change.

#### Ask

Which dimension would expose a system that succeeds on polished questions but fails on terse error-code queries?

#### Watch in the exercise

Module 08 notebook cue: inspect deduplication, schema validation, quoted-page checks, the datasheet, and the kept/removed counts.

#### Sources

[RAGAS paper](https://arxiv.org/abs/2309.15217); [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)


### D2-M08-C3B · Review synthetic cases as measurement assets · The practical check

- Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Which dimension would expose a system that succeeds on polished questions but fails on terse error-code queries?

#### Watch in the exercise

Module 08 notebook cue: inspect deduplication, schema validation, quoted-page checks, the datasheet, and the kept/removed counts.

#### Sources

[RAGAS paper](https://arxiv.org/abs/2309.15217); [Ragas testset generation](https://docs.ragas.io/en/stable/concepts/test_data_generation/rag/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)


### D2-M08-C4 · Stop when the diagnosis is actionable

- Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 3

#### Detailed preparation

A useful evaluation cycle ends with a decision, not a dashboard. Form a failure hypothesis, generate and review cases, run the same cases through the system, inspect metric patterns and traces, then choose one change to test. Stop when the evidence identifies the next action: change chunking, increase candidate depth, add a reranker, constrain a tool, or revise the answer instruction. Synthetic cases can contain source leakage, unsupported references, duplicated wording, or judge bias. RAGAS-style metrics can disagree because they measure different properties and may depend on model judgments. Module 08 now implements a weak small-k pipeline, candidate generation and curation, four metrics, and a k comparison with an interval on the faithfulness difference. Those outputs are still observations to inspect, not universal thresholds.

#### Ask

What would make you reject a high metric score before changing the system?

#### Watch in the exercise

Module 08 notebook cue: compare the saved baseline and improved rows, chart the delta, and read the interval before interpreting the change. Do not invent a cohort result.

#### Sources

[RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)


### D2-M08-C4B · Stop when the diagnosis is actionable · The practical check

- Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
- Instructor: Beric
- Type: core
- Timing: 1 minute
- Layout: 09 Lab and code 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

What would make you reject a high metric score before changing the system?

#### Watch in the exercise

Module 08 notebook cue: compare the saved baseline and improved rows, chart the delta, and read the interval before interpreting the change. Do not invent a cohort result.

#### Sources

[RAGAS paper](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/); [Module 08 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/Improving_RAG_with_RAGAS.ipynb)


### D2-M08-R1 · Research: RAG evaluation needs multiple lenses

- Module: [08 SDG/RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md)
- Instructor: Beric
- Type: optional
- Timing: 0 minutes
- Layout: 08 Quote

#### Detailed preparation

The RAGAS paper is the optional research anchor. Its contribution is a reference-free framework intended to assess several dimensions of retrieval-augmented generation rather than collapse the pipeline into one end-to-end score. Use it to explain the origin of the metric distinction, then state the limit clearly: reference-free does not mean assumption-free or human-free. The framework relies on model judgments and prompts, so evaluators still need examples, calibration, and disagreement review. The paper’s experiments do not establish a universal threshold for an internal helpdesk system. The course translation is practical: pair metric outputs with retrieved context, answer claims, source provenance, and known failure cases. If the metric cannot change what you inspect or test next, it is not yet a useful diagnostic.

#### Ask

Which part of the RAG pipeline would remain invisible if we reported only answer relevancy?

#### Watch in the exercise

Module 08 notebook cue: use the produced datasheet and scores as evidence, while checking the curation decisions that produced the test set.

#### Sources

[RAGAS: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217); [RAGAS metrics documentation](https://docs.ragas.io/en/stable/concepts/metrics/)


### D3-M09-C1 · A useful answer is not enough

- Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps

#### Detailed preparation

Start with the recurring question: “Why can’t I access the VPN?” A final answer can sound plausible while the agent searched the wrong article, skipped a needed clarification, or violated a support policy. An agent eval therefore treats the task as a goal plus a hidden success condition, then records the whole trajectory. The model, permitted search tool, observations, user follow-ups, and stop signal all matter. This is the shift from testing a single string to testing behavior in context. ReAct established the reason/action/observation pattern; trajectory evals apply that systems view to testing. Ask: where would you locate “searched the knowledge base” and “asked for the employee’s operating system”? The notebook cue is a section count, a search_kb call, and a short answer naming a section. The diagram’s end-state assertion is proposed, not implemented locally; this lab checks text facts and tool use, while state assertions appear in Grow. Stop when the trace is inspectable, not when the prose merely sounds good.

#### Ask

What evidence would a final answer hide that the trajectory exposes?

#### Watch in the exercise

Run the notebook’s first agent-under-test cell; observe the section count, search_kb call, and answer naming a section.

#### Sources

[ReAct paper](https://arxiv.org/abs/2210.03629); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)


### D3-M09-C1B · A useful answer is not enough · The practical check

- Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

What evidence would a final answer hide that the trajectory exposes?

#### Watch in the exercise

Run the notebook’s first agent-under-test cell; observe the section count, search_kb call, and answer naming a section.

#### Sources

[ReAct paper](https://arxiv.org/abs/2210.03629); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)


### D3-M09-C2 · Turn a prompt into a testable task

- Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

Define the eval harness as the infrastructure that assembles tasks, runs the agent and simulated user, captures tool calls, and scores the result. A task is richer than a prompt: it includes a goal, persona, opening message, details the user reveals only when asked, and a success condition the agent never sees. The simulator makes missing information consequential. For the VPN question, the agent should ask for the platform before giving platform-specific steps. Use two complementary scorers: deterministic checks for facts and required tool behavior, and a rubric-based judge for supported, useful, policy-aligned answers. Neither is magic. Keyword checks can reward parroting; a judge can forgive a missing exact fact. The notebook’s planted out-of-scope and prompt-injection tasks make those boundaries visible. Ask which assertion belongs in code rather than in a judge prompt. Stop when each critical behavior has an observable assertion.

#### Ask

Which requirement should be deterministic for the VPN task, and which needs judgment?

#### Watch in the exercise

Inspect one generated task row; observe its category, opening, facts, and hidden success condition.

#### Sources

[OpenAI evals build guide](https://github.com/openai/evals/blob/main/docs/build-eval.md); [OpenAI graders reference](https://platform.openai.com/docs/api-reference/graders); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)


### D3-M09-C2B · Turn a prompt into a testable task · The practical check

- Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Which requirement should be deterministic for the VPN task, and which needs judgment?

#### Watch in the exercise

Inspect one generated task row; observe its category, opening, facts, and hidden success condition.

#### Sources

[OpenAI evals build guide](https://github.com/openai/evals/blob/main/docs/build-eval.md); [OpenAI graders reference](https://platform.openai.com/docs/api-reference/graders); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)


### D3-M09-C3 · Reliability lives across runs

- Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

One run is a sample, especially when a model user rephrases the request or the agent chooses a different tool path. If a task succeeds with probability p, pass^k asks how often all k attempts succeed; it exposes inconsistency that an average pass rate can hide. In this notebook, three repeats use the same configured model, agent, simulated user, and judge, so they reveal sampling variability within this harness—not broad confidence, independence, or production reliability. The planted regression returns the same first section for every query. Lookup tasks should move; out-of-scope and injection tasks may hold. That differential is evidence this harness responds to one known behavior change, not proof that it measures all behavior. Ask what a zero delta would mean. Stop when a failure becomes a reproducible task.

#### Ask

Why can pass^k be much lower than pass rate without either metric being wrong?

#### Watch in the exercise

Run repeated tasks and the planted regression; compare lookup-category movement with out-of-scope and injection categories.

#### Sources

[$\tau$-bench](https://arxiv.org/abs/2406.12045); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)


### D3-M09-C3B · Reliability lives across runs · The practical check

- Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Why can pass^k be much lower than pass rate without either metric being wrong?

#### Watch in the exercise

Run repeated tasks and the planted regression; compare lookup-category movement with out-of-scope and injection categories.

#### Sources

[$\tau$-bench](https://arxiv.org/abs/2406.12045); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)


### D3-M09-C4 · Stop on evidence, not confidence

- Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps 1

#### Detailed preparation

Close on the artifact a release manager can act on: a capability report with model and agent identity, per-task pass rate and pass^k, the worst failure, the turn where it first went wrong, and the planted-regression result. The report should preserve disagreement between deterministic checks and judges instead of collapsing it into one reassuring number. A useful stopping rule is evidence-based: stop iterating when the task set covers the intended capability, the release bar is met, and known failures have regression cases. If the cost or permissions make an agent unnecessary, stop and use a simpler workflow. The notebook writes capability_report from actual runs; it does not claim production readiness. Ask learners to name the first observable assertion they would add for VPN support. Their answer belongs in the notebook’s Your turn section, not in this deck.

#### Ask

What must be reproducible before you call an agent change ready to ship?

#### Watch in the exercise

Read the printed capability report and locate the worst failure and planted-regression result.

#### Sources

[OpenAI evals](https://evals.openai.com/); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)


### D3-M09-C4B · Stop on evidence, not confidence · The practical check

- Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
- Instructor: Eli
- Type: core
- Timing: 1 minute
- Layout: 09 Lab and code 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

What must be reproducible before you call an agent change ready to ship?

#### Watch in the exercise

Read the printed capability report and locate the worst failure and planted-regression result.

#### Sources

[OpenAI evals](https://evals.openai.com/); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb); [Unit Testing Your Agents](https://soypetetech.substack.com/p/unit-testing-your-agents)


### D3-M09-R1 · Research: from traces to state

- Module: [09 Agent evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md)
- Instructor: Eli
- Type: optional
- Timing: 0 minutes
- Layout: 08 Quote

#### Detailed preparation

Optional research: compare ReAct and tau-bench without treating either as a universal recipe. ReAct’s contribution is the interleaving of reasoning traces and actions so external observations can update the plan. Tau-bench adds dynamic user interaction, domain tools, policy guidelines, end-state evaluation, and pass^k. Those are different scopes: a prompting pattern is not an end-to-end release harness, and a benchmark result is not a guarantee for an internal helpdesk. Invite investigation into state-based assertions: did the agent actually create or update the ticket, rather than merely say that it did? The notebook currently scores tool use and text-level facts, then asks learners to move toward state assertions in Grow. The research question is whether the simulator and oracle represent the real support workflow closely enough to make a release decision. Stop research when the comparison changes a concrete assertion or task.

#### Ask

What does tau-bench add beyond checking the agent’s final sentence?

#### Watch in the exercise

Compare the notebook’s current text/fact checks with its Grow suggestion to assert external state.

#### Sources

[ReAct](https://arxiv.org/abs/2210.03629); [$\tau$-bench](https://arxiv.org/abs/2406.12045); [trajectory-evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)


### D3-M10-C1 · Memory is restored context

- Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column

#### Detailed preparation

A model does not remember a previous call by itself. The harness must choose what to persist and what to place back into the next prompt. Use the recurring VPN question: in session one, the user says they are on a Mac and belong to Finance; in session two, “the VPN still fails” should not force needless repetition, but only if the memory is scoped to that user and current enough. Define persistence as state that outlives the process that created it. Then name the risk: bad memory is worse than no memory because it creates confident continuity around a stale or wrong fact. The notebook begins with a naive buffer and a fresh session to make the gap observable. Memory is an application design, not a hidden model faculty. Ask which fact is safe to remember and which is merely transient. Stop before storing anything whose future value is unclear.

#### Ask

Where does the remembered Mac fact live between the two model calls?

#### Watch in the exercise

Run the naive memory demonstration; observe the same-session answer versus the fresh-session “I do not know.”

#### Sources

[MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)


### D3-M10-C1B · Memory is restored context · The practical check

- Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Where does the remembered Mac fact live between the two model calls?

#### Watch in the exercise

Run the naive memory demonstration; observe the same-session answer versus the fresh-session “I do not know.”

#### Sources

[MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)


### D3-M10-C2 · Give each memory a job

- Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards 1

#### Detailed preparation

The local notebook teaches three kinds of memory: episodic, semantic, and working. Episodic memory records what happened in a run; semantic memory stores durable facts recalled when relevant; working memory is what the assembler places in the current prompt. The VPN example makes the distinction concrete: “we tried reset and search_kb” is episodic, “Finance uses split tunnel” may be semantic, and the current error belongs in working memory. Treat procedural instructions—identity, constraints, skills, and response policy—as a separate persistence dimension that can be implemented in a harness; it is not one of the notebook’s three memory kinds and is not universally always loaded. Retrieval can select a memory; it does not make the memory true. Ask learners to classify “the user prefers concise steps” and “the ticket number from last week.” Stop when ownership, scope, and retention are explicit.

#### Ask

Which memory type should preserve the tool call that actually ran?

#### Watch in the exercise

Read the notebook’s three-kind implementation and identify the procedural, semantic, episodic, and working layers in the assembled prompt.

#### Sources

[MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)


### D3-M10-C2B · Give each memory a job · The practical check

- Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Which memory type should preserve the tool call that actually ran?

#### Watch in the exercise

Read the notebook’s three-kind implementation and identify the procedural, semantic, episodic, and working layers in the assembled prompt.

#### Sources

[MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)


### D3-M10-C3 · Budget memory deliberately

- Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats 1

#### Detailed preparation

Working memory is a budgeted assembly problem. The notebook stacks procedural instructions, recalled semantic memories, an episodic summary, and recent turns. When the budget is small, it drops the least relevant recalled memory first and protects the root set and newest turns. When a conversation grows, compaction condenses older turns while archiving raw text so a ticket number can still be recovered. This is a design choice, not a law: another product may protect an approval record or a safety constraint ahead of recency. The failure to watch is silent loss—an instruction or identifier disappears and the answer remains fluent. Use the VPN ticket number as the invariant. Ask what must never be trimmed in a support product. Stop compaction when the summary no longer preserves the facts needed for the next decision; retrieve the raw turn instead.

#### Ask

Which tier does the notebook drop first, and which two tiers does it protect?

#### Watch in the exercise

Compare the 6,000- and 120-token breakdowns, then observe compacted=True and raw retrieval of ticket 48213.

#### Sources

[MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)


### D3-M10-C3B · Budget memory deliberately · The practical check

- Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Which tier does the notebook drop first, and which two tiers does it protect?

#### Watch in the exercise

Compare the 6,000- and 120-token breakdowns, then observe compacted=True and raw retrieval of ticket 48213.

#### Sources

[MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)


### D3-M10-C4 · Remember less, govern better

- Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps

#### Detailed preparation

Memory needs governance as much as retrieval. Capture only facts that can improve a future decision; review them for truth, ownership, and sensitivity; supersede or expire stale values; delete on request; and isolate stores by user or tenant. The notebook tests a changed team fact by retiring the old subject record, then asks learners to run a two-user leakage test with different ticket numbers. Those tests are more valuable than a polished “remembered you” demo. A production design should retain lineage for important decisions and make the write path observable. A stopping rule is intentional forgetfulness: if the fact is not durable, scoped, and useful, do not write it. Ask whether a ticket number, device model, or temporary outage symptom belongs in long-term memory. Their answers should be argued from product need and risk, not inferred here.

#### Ask

What test detects a memory store that leaks one user’s ticket into another user’s session?

#### Watch in the exercise

Run the supersede-on-subject check and the leakage test; observe stale facts being rejected and user stores kept separate.

#### Sources

[MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)


### D3-M10-C4B · Remember less, govern better · The practical check

- Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
- Instructor: Beric
- Type: core
- Timing: 1 minute
- Layout: 09 Lab and code 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

What test detects a memory store that leaks one user’s ticket into another user’s session?

#### Watch in the exercise

Run the supersede-on-subject check and the leakage test; observe stale facts being rejected and user stores kept separate.

#### Sources

[MemGPT](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)


### D3-M10-R1 · Research: memory as a managed resource

- Module: [10 Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md)
- Instructor: Beric
- Type: optional
- Timing: 0 minutes
- Layout: 08 Quote

#### Detailed preparation

Optional research: MemGPT describes virtual context management inspired by operating-system memory tiers. Define a token as the model’s text-processing unit used to count context and budget prompt space; token counts vary by tokenizer and are not characters. Define an oracle as the trusted reference for whether a task’s intended state or answer is correct. MemGPT’s contribution is architectural: move information between a constrained active context and slower memory under explicit control. That is a useful origin for the notebook’s budget and compaction ideas, not proof that every product should adopt the same design. Compare it with an internal helpdesk, where privacy, deletion, recency, and auditability may dominate recall breadth. Stop investigation when it cannot change a retention or leakage test.

#### Ask

What does virtual context management move, and what remains fixed?

#### Watch in the exercise

Compare the notebook’s raw archive plus summary with the paper’s tiered-context idea.

#### Sources

[MemGPT paper](https://arxiv.org/abs/2310.08560); [memory notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/Three_Kinds_of_Memory.ipynb)


### D3-M11-C1 · Recap: model inside a harness

- Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
- Instructor: Rohit
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps

#### Detailed preparation

Keep the recap concise: a model generates an output from supplied context; a harness surrounds it with tools, state, policy, and control flow. The Module 11 notebook compares six ways to expose one lookup capability: a tool, skill folder, MCP server, sub-agent, code-mode runtime, and manifest-described API. The model may propose a lookup, but the harness validates the interface, executes the permitted call, returns the observation, and controls the next transition. For “Why can’t I access the VPN?”, a read-only search may be automatic while a password reset must pause for identity and approval. Do not imply that one mechanism wins universally. Ask learners to point to the executor and the approval boundary. Stop the recap once those responsibilities are named; the architecture work is about state, capability interfaces, and recovery.

#### Ask

Which component actually executes search_kb?

#### Watch in the exercise

Compare this boundary with the Six Ways capability catalogue and the search_kb call and trace shown in module 09.

#### Sources

[Module 11 README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md); [Six Ways notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/Six_Ways.ipynb); [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture)


### D3-M11-C1B · Recap: model inside a harness · The practical check

- Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
- Instructor: Rohit
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Which component actually executes search_kb?

#### Watch in the exercise

Compare this boundary with the Six Ways capability catalogue and the search_kb call and trace shown in module 09.

#### Sources

[Module 11 README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md); [Six Ways notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/Six_Ways.ipynb); [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture)


### D3-M11-C2 · State makes recovery explicit

- Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
- Instructor: Rohit
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps 1

#### Detailed preparation

Move from the recap to stateful control flow. Represent the support run as explicit states such as clarify, search, propose, approval-required, execute, verify, and escalate. A checkpoint records enough durable state to resume without guessing what completed. A retry policy must distinguish a safe read from a write that may have succeeded; idempotency means repeating the same request does not create a second side effect, usually through a stable request key or operation check. Put human approval immediately before a consequential action, and make approval part of the state transition rather than a sentence the model can claim. The harness owns timeouts, retry counts, and trace events. Ask which transition follows a lost response from password-reset. Stop retrying when the operation is non-idempotent or evidence is ambiguous; verify or escalate.

#### Ask

Where should authorization live if the model asks to reset a password?

#### Watch in the exercise

Module 11 notebook cue: compare the tool, skill, MCP, sub-agent, code-mode, and manifest traces; inspect what enters context and the recorded call count/context size.

#### Sources

[OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [ReAct](https://arxiv.org/abs/2210.03629); [module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)


### D3-M11-C2B · State makes recovery explicit · The practical check

- Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
- Instructor: Rohit
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Where should authorization live if the model asks to reset a password?

#### Watch in the exercise

Module 11 notebook cue: compare the tool, skill, MCP, sub-agent, code-mode, and manifest traces; inspect what enters context and the recorded call count/context size.

#### Sources

[OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [ReAct](https://arxiv.org/abs/2210.03629); [module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)


### D3-M11-C3 · Tools, MCP, and skills have different jobs

- Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
- Instructor: Rohit
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards 2

#### Detailed preparation

Now separate capability interfaces from instructions. A tool is an executable capability with typed inputs and a result, such as read_ticket or search_kb. MCP is a protocol for an AI application to connect to servers that expose capabilities such as tools and resources; the protocol does not itself grant authorization. A skill packages repeatable know-how—instructions, examples, resources, and sometimes scripts—for how to perform a kind of work. A skill can tell an agent how to prepare a support brief; a tool can fetch the ticket; an MCP server can provide a standardized connection to that tool and resource. None of the three is automatically trusted. Review third-party code, scope permissions, and keep the policy gate in the harness. Ask which interface belongs to “look up VPN status” and which belongs to “write a weekly incident brief.” Stop when each job has a clear owner.

#### Ask

Which job belongs to a tool, an MCP connection, and a skill?

#### Watch in the exercise

Module 11 notebook cue: edit the capability catalogue and compare two mechanisms for one lookup; inspect ownership, auth, call count, and context size.

#### Sources

[ReAct](https://arxiv.org/abs/2210.03629); [$\tau$-bench](https://arxiv.org/abs/2406.12045); [module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)


### D3-M11-C3B · Tools, MCP, and skills have different jobs · The practical check

- Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
- Instructor: Rohit
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Which job belongs to a tool, an MCP connection, and a skill?

#### Watch in the exercise

Module 11 notebook cue: edit the capability catalogue and compare two mechanisms for one lookup; inspect ownership, auth, call count, and context size.

#### Sources

[ReAct](https://arxiv.org/abs/2210.03629); [$\tau$-bench](https://arxiv.org/abs/2406.12045); [module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)


### D3-M11-C4 · Budget and evidence define the stop

- Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
- Instructor: Rohit
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Finish with operational limits rather than another definition. Set budgets for model turns, tool calls, wall-clock time, tokens, and money. Every transition should emit evidence: the input, selected capability, validated arguments, observation, checkpoint, approval decision, and final status. Recovery must distinguish “not attempted,” “completed,” and “unknown because the response was lost.” The Module 11 catalogue adds a decision aid: choose a mechanism by ownership, authentication, what enters context, and failure behavior. The VPN assistant can stop after verified resolution, after a bounded number of failed attempts with escalation, or when permission is missing. A successful demo is not production evidence; release needs repeatable evals, current context, authorization, monitoring, and accountable ownership. Ask which evidence would make a retry safe. Stop the concept lesson when the team can name the capability owner, budget, approval, and escalation.

#### Ask

Which of the six boxes would be invisible in a final-answer-only test?

#### Watch in the exercise

Module 11 notebook cue: read the six-row `tools_catalog` output and compare the two mechanisms selected for the group's lookup.

#### Sources

[Module 11 README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md); [Six Ways notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/Six_Ways.ipynb); [Module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)


### D3-M11-C4B · Budget and evidence define the stop · The practical check

- Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
- Instructor: Rohit
- Type: core
- Timing: 1 minute
- Layout: 09 Lab and code 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Which of the six boxes would be invisible in a final-answer-only test?

#### Watch in the exercise

Module 11 notebook cue: read the six-row `tools_catalog` output and compare the two mechanisms selected for the group's lookup.

#### Sources

[Module 11 README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md); [Six Ways notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/Six_Ways.ipynb); [Module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)


### D3-M11-R1 · Research: durable state for long-running work

- Module: [11 Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)
- Instructor: Rohit
- Type: optional
- Timing: 0 minutes
- Layout: 08 Quote

#### Detailed preparation

Optional research: read LangGraph’s “Thinking in LangGraph” as a framework explanation of stateful graphs, checkpoints, and human-in-the-loop recovery, then compare Anthropic’s long-running-agent harness case study. Their contribution is practical architecture guidance: make progress durable, separate phases, and give a resumed run explicit state and tests. They are not controlled evidence that one framework or harness is best for every support workflow. The useful question is where a VPN run can pause safely: after clarification, after retrieval, before an approved write, or after verification. Bring the discussion back to idempotency, bounded retries, and evidence of completed side effects. The Module 11 notebook supplies a capability-comparison lab; these sources extend it into recovery and long-running work. Stop research when the case study changes one checkpoint or recovery assertion.

#### Ask

What does the benchmark evaluate that a model-only architecture cannot represent?

#### Watch in the exercise

Module 11 notebook cue: compare the six capability mechanisms first; use this optional reading to propose one recovery assertion for the chosen mechanism.

#### Sources

[LangGraph: Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph); [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents); [module alignment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md)


### D3-M13-C1 · Guardrails sit at choke points

- Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
- Instructor: Rohit
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps

#### Detailed preparation

A guardrail is an independently enforced, testable policy that inspects, transforms, blocks, pauses, or escalates. “Do not reset passwords without approval” in a system prompt is an instruction; the tool gate that checks identity and approval is a guardrail. Use the recurring VPN question to distinguish harmless help from a consequential reset. Input checks can reject out-of-scope requests or redact unnecessary PII. Tool checks validate arguments and authorization immediately before execution. Output checks can catch unsupported claims or sensitive content before release. A policy layer maps user identity and requested action to permission; it is not a prompt and should not be inferred from text. The notebook’s ladder starts from cases drawn from transcripts plus planted attacks. Ask where the reset approval check belongs. Stop a request at the first sufficient choke point and fail closed if the check raises.

#### Ask

Why is a prompt instruction not enough to authorize a password reset?

#### Watch in the exercise

Run case-set creation; observe benign transcript inputs alongside planted attacks and expected allow/block labels.

#### Sources

[NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework); [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)


### D3-M13-C1B · Guardrails sit at choke points · The practical check

- Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
- Instructor: Rohit
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Why is a prompt instruction not enough to authorize a password reset?

#### Watch in the exercise

Run case-set creation; observe benign transcript inputs alongside planted attacks and expected allow/block labels.

#### Sources

[NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework); [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)


### D3-M13-C2 · Choose the cheapest sufficient rung

- Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
- Instructor: Rohit
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats 1

#### Detailed preparation

The notebook builds a ladder rather than searching for one universal detector. Constrained decoding can make illegal structured output unreachable, but it needs logit or grammar control and does not decide whether a legitimate action is authorized. Regex rules are fast and predictable for exact patterns such as card numbers or credentials, but miss paraphrases. A small classifier catches learned language patterns but inherits its training coverage and can false-positive on ordinary support terms. An LLM judge can assess contextual properties, but adds model cost, latency, and its own uncertainty. These mechanisms are complementary, not monotonically better. For a VPN assistant, a card-number regex may redact input while a tool policy checks reset authorization. Ask learners to identify a failure that can be specified exactly. Stop at the cheapest rung that clears the required coverage and false-positive bar.

#### Ask

Which rung is best for an exact card-number pattern, and why?

#### Watch in the exercise

Run the constrained-decoding demo and rules/classifier comparison; observe kept tokens, rule latency, and disagreements.

#### Sources

[JSONSchemaBench constrained-decoding study](https://arxiv.org/abs/2501.10868); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)


### D3-M13-C2B · Choose the cheapest sufficient rung · The practical check

- Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
- Instructor: Rohit
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Which rung is best for an exact card-number pattern, and why?

#### Watch in the exercise

Run the constrained-decoding demo and rules/classifier comparison; observe kept tokens, rule latency, and disagreements.

#### Sources

[JSONSchemaBench constrained-decoding study](https://arxiv.org/abs/2501.10868); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)


### D3-M13-C3 · Measure protection and friction

- Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
- Instructor: Rohit
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 3

#### Detailed preparation

Measure both sides of the guardrail bargain. A detector that blocks every request has perfect attack coverage and zero usefulness. The notebook builds benign cases from real transcript first turns and adds planted attacks for instruction overrides, credentials, sensitive storage, and unauthorized approval. It reports attacks caught beside legitimate inputs wrongly blocked, plus latency. The classifier and rules can disagree because one catches learned phrasing and the other catches exact patterns. A judge can assess contextual support or tone, but a prompt that works as an evaluator may be too costly or too uncertain as a refusal gate. For the VPN example, a benign request should pass even if it contains technical words that overlap attack training data. Ask which false positive a support team would tolerate. Stop a rung from shipping when its false-positive rate exceeds the product’s explicit bar, regardless of its attack score.

#### Ask

Why must false positives appear beside attack coverage?

#### Watch in the exercise

Compare the notebook’s rungs table; observe attacks caught, false positives, and mean milliseconds for each rung.

#### Sources

[NIST AI RMF GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)


### D3-M13-C3B · Measure protection and friction · The practical check

- Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
- Instructor: Rohit
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Why must false positives appear beside attack coverage?

#### Watch in the exercise

Compare the notebook’s rungs table; observe attacks caught, false positives, and mean milliseconds for each rung.

#### Sources

[NIST AI RMF GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)


### D3-M13-C4 · Stop safely and record why

- Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
- Instructor: Rohit
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps 1

#### Detailed preparation

Assemble the deployed order from measured evidence: cheapest first, stop at the first block, and fail closed when a rung raises. The notebook measures every rung separately, then shows the ladder’s early stopping behavior; the policy layer is intentionally separate because it acts on user and action authorization rather than text. For VPN support, rules might redact a credential, the classifier might block a prompt override, and a judge might inspect a contextual request—but none of those grants permission to reset an account. Add monitoring for false positives, latency, and newly observed attacks. A stopping rule is explicit: ship only the rungs that clear the coverage bar within the latency budget; document what remains unprotected and route consequential uncertainty to a person. Ask which rung should never be allowed to silently fail open. Stop when the ladder’s order and thresholds are recorded with its results.

#### Ask

What happens when one rung raises an exception?

#### Watch in the exercise

Run the full ladder; observe the stopped_at rung, ran list, false-positive summary, and saved ladder_results artifact.

#### Sources

[OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [InjecAgent](https://arxiv.org/abs/2403.02691); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)


### D3-M13-C4B · Stop safely and record why · The practical check

- Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
- Instructor: Rohit
- Type: core
- Timing: 1 minute
- Layout: 09 Lab and code 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

What happens when one rung raises an exception?

#### Watch in the exercise

Run the full ladder; observe the stopped_at rung, ran list, false-positive summary, and saved ladder_results artifact.

#### Sources

[OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/); [InjecAgent](https://arxiv.org/abs/2403.02691); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)


### D3-M13-R1 · Research: untrusted context can steer action

- Module: [13 Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md)
- Instructor: Rohit
- Type: optional
- Timing: 0 minutes
- Layout: 08 Quote

#### Detailed preparation

Optional research: InjecAgent frames indirect prompt injection as malicious instructions embedded in external content that a tool-integrated agent processes. That threat is especially relevant to retrieval-backed support: a poisoned article or ticket can attempt to redirect the agent, disclose data, or invoke an unrelated tool. The paper is a benchmark and vulnerability study, not evidence that one detector solves prompt injection. The architectural response is defense in depth: treat retrieved content as untrusted, constrain tool authority, evaluate trajectories and external state, and require confirmation or policy approval for consequential actions. The notebook’s planted prompt-injection task and separate policy-layer note are useful beginnings, while its text ladder does not establish production security. Ask which control remains if a classifier misses a paraphrase. Stop research when the attack becomes a regression case with a clear owner and observable blocked action.

#### Ask

Which boundary can still protect the tool if the retrieved text fools the model?

#### Watch in the exercise

Run the notebook’s planted injection through the ladder and inspect which rung catches it; do not infer security from one pass.

#### Sources

[InjecAgent](https://arxiv.org/abs/2403.02691); [NIST AI RMF GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf); [guardrail notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/Guardrail_Ladder.ipynb)


### D4-M17-C1 · 17 · Make research inspectable

- Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps

#### Detailed preparation

Start with the recurring workplace question: “Why did our support agent fail this access request, and what should we change?” A single prompt can produce a polished answer, but it hides whether the question was understood, whether search was broad enough, and where a claim came from. The notebook unrolls that opaque call into six nodes. Clarify decides whether the question is specific enough; brief states success criteria; plan creates bounded research tasks; research isolates each task; compress reduces findings into an evidence packet; write produces the report. LangGraph supplies the state graph, but the teaching point is the contract between steps. This is an engineering response to context and auditability problems, not proof that more nodes create better research. Check: which boundary would you inspect first when the final answer is wrong? Lab observation: six node updates, one trace event per node, and a query line per research task.

#### Ask

Which boundary would you inspect first when the final answer is wrong?

#### Watch in the exercise

Notebook cue: six node updates in order and trace events with query, corpus hits, web hits, and gaps.

#### Sources

[LangGraph graph API](https://docs.langchain.com/oss/python/langgraph/graph-api), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)


### D4-M17-C1B · 17 · Make research inspectable · The practical check

- Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Which boundary would you inspect first when the final answer is wrong?

#### Watch in the exercise

Notebook cue: six node updates in order and trace events with query, corpus hits, web hits, and gaps.

#### Sources

[LangGraph graph API](https://docs.langchain.com/oss/python/langgraph/graph-api), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)


### D4-M17-C2 · 17 · Research is a bounded loop

- Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps 1

#### Detailed preparation

The practical change is not “use the web.” It is to give each research task a narrow query, a bounded number of results, and an explicit handoff. The notebook’s researchers search the rendered corpus and, when Tavily is configured, the web; they extract short source text, reflect on relevance, and retain sources plus gaps. The default path still works with corpus-only evidence. That matters for a workplace assistant whose policy pages and prior traces are often more relevant than the open web. The stopping rule is evidence-based: a task with no source becomes an admitted gap. Do not let a fluent compression step turn an empty result into a fact. Check: what should the report say when all search paths return zero hits? Lab observation: the notebook prints per-task query and corpus/web hit counts.

#### Ask

What should the report say when every search path returns zero hits?

#### Watch in the exercise

Notebook cue: empty sources are surfaced as gaps; query lines and hit counts appear under research.

#### Sources

[LangGraph workflows](https://docs.langchain.com/oss/python/langgraph/workflows-agents), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)


### D4-M17-C2B · 17 · Research is a bounded loop · The practical check

- Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

What should the report say when every search path returns zero hits?

#### Watch in the exercise

Notebook cue: empty sources are surfaced as gaps; query lines and hit counts appear under research.

#### Sources

[LangGraph workflows](https://docs.langchain.com/oss/python/langgraph/workflows-agents), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)


### D4-M17-C3 · 17 · Provenance is part of the answer

- Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column

#### Detailed preparation

Use a concrete example: “The agent should ask for the device identifier before changing access.” A defensible report should connect that recommendation to a finding, the finding to a source page or search result, and the trace to the query that found it. The notebook prompts the writer to include inline sources and an open-gaps section, then the checkpoint asks the learner to compare citations with the distinct-source list. That is a human inspection cue, not an executable validation assertion. It may reveal an invented citation, but it does not prove that a cited page supports the claim. Provenance answers “where did this come from?”; it does not answer “is the source authoritative or current?” Check: what extra test would you add for support rather than citation presence? Lab observation: inspect the rendered report, distinct sources, and gaps together.

#### Ask

What does a valid citation prove, and what does it still not prove?

#### Watch in the exercise

Notebook cue: stop if the report cites a source absent from the distinct-sources list.

#### Sources

[LangGraph workflows](https://docs.langchain.com/oss/python/langgraph/workflows-agents), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)


### D4-M17-C3B · 17 · Provenance is part of the answer · The practical check

- Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

What does a valid citation prove, and what does it still not prove?

#### Watch in the exercise

Notebook cue: stop if the report cites a source absent from the distinct-sources list.

#### Sources

[LangGraph workflows](https://docs.langchain.com/oss/python/langgraph/workflows-agents), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)


### D4-M17-C4 · 17 · The next step is evidence policy

- Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
- Instructor: Eli
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 1

#### Detailed preparation

Close by separating prototype maturity from technology choice. The notebook gives us a useful working prototype: typed state, bounded nodes, optional tools, source filtering, a report, and a trace. It is not production readiness. A production research workflow must decide which sources may be searched, whose data may be exposed, how tool failures and retries are handled, how stale evidence is detected, and which eval cases gate changes. The safe stopping rule is often simpler: use the internal corpus only when the question is about internal policy, and do not turn on web search merely because it is available. The bridge is to the capability report from module 09: choose a top failure, research it, then make the resulting risk testable. Check: what permission would you require before enabling web search? Lab observation: compare Tavily enabled with the documented web-off path and inspect open gaps.

#### Ask

What permission would you require before enabling web search?

#### Watch in the exercise

Notebook cue: compare `TavilySearch` enabled with the documented `web: off` path and inspect open gaps.

#### Sources

[LangGraph durable execution](https://docs.langchain.com/oss/python/langgraph/durable-execution), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)


### D4-M17-C4B · 17 · The next step is evidence policy · The practical check

- Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
- Instructor: Eli
- Type: core
- Timing: 1 minute
- Layout: 09 Lab and code 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

What permission would you require before enabling web search?

#### Watch in the exercise

Notebook cue: compare `TavilySearch` enabled with the documented `web: off` path and inspect open gaps.

#### Sources

[LangGraph durable execution](https://docs.langchain.com/oss/python/langgraph/durable-execution), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)


### D4-M18-C1 · 18 · A guardrail is a boundary with a policy

- Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 06 Process steps

#### Detailed preparation

Return to the workplace question: “Can this assistant safely answer an access request?” A guardrail is not a second vague system prompt. It is a check attached to a boundary with a policy and a defined failure behavior. The notebook first redacts email, phone, SSN, or employee ID without blocking a legitimate request. It then checks scope and prompt injection before the model, and unsupported claims and tone after generation. The OpenAI Agents SDK distinguishes input and output guardrails and exposes tripwire exceptions when a check blocks. Tool guardrails are a separate boundary when the risk is the tool call itself. Check: where would you put a check that prevents an unauthorized account change? Lab observation: `run_guarded` records processed input, stage, blocked state, and tripwire.

#### Ask

Where would you put a check that prevents an unauthorized account change?

#### Watch in the exercise

Notebook cue: read the stage and tripwire fields for each guarded case.

#### Sources

[OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)


### D4-M18-C1B · 18 · A guardrail is a boundary with a policy · The practical check

- Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 04 Icon cards

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Where would you put a check that prevents an unauthorized account change?

#### Watch in the exercise

Notebook cue: read the stage and tripwire fields for each guarded case.

#### Sources

[OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)


### D4-M18-C2 · 18 · Placement changes the failure

- Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 2

#### Detailed preparation

Placement is an architectural decision. Input guardrails are not unconditionally before model execution: the SDK can run them in parallel by default. A blocking input check is the mode that completes before the agent starts, which matters for cost and side effects. An output guardrail can stop a final answer, but the model has already spent tokens and may already have used tools. A tool input guardrail is closer to the side effect and can reject or halt the tool call. The notebook deliberately teaches input and output agent guardrails, while its lookup tool remains a simple capability. Do not claim that an output phrase check authorizes an action. Check: which boundary is the strongest place to enforce “the requester is the account holder”? Lab observation: compare input-stage and output-stage tripwires, including the forced unsafe demo agents.

#### Ask

Which boundary should enforce requester authorization, and why?

#### Watch in the exercise

Notebook cue: forced overclaim and casual agents end at the output stage; input attacks stop earlier.

#### Sources

[OpenAI guardrail execution modes](https://openai.github.io/openai-agents-python/guardrails/#execution-modes), [Tool guardrails](https://openai.github.io/openai-agents-python/ref/tool_guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)


### D4-M18-C2B · 18 · Placement changes the failure · The practical check

- Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Which boundary should enforce requester authorization, and why?

#### Watch in the exercise

Notebook cue: forced overclaim and casual agents end at the output stage; input attacks stop earlier.

#### Sources

[OpenAI guardrail execution modes](https://openai.github.io/openai-agents-python/guardrails/#execution-modes), [Tool guardrails](https://openai.github.io/openai-agents-python/ref/tool_guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)


### D4-M18-C3 · 18 · Cheap rules are useful and brittle

- Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Connect this module to module 13’s ladder. The off-the-shelf SDK gives lifecycle plumbing and typed outcomes; it does not make the policy detector accurate. The notebook’s scope and injection checks are regex and vocabulary rules, PII is regex redaction, and claims and tone are pattern checks. Those are excellent teaching mechanisms because the result is inspectable. They miss paraphrases, new attack forms, and legitimate wording outside the corpus vocabulary. A classifier or LLM judge may improve coverage, but it adds training or prompt drift, latency, and another failure mode. The stopping rule is empirical: run every case, read false positives first, and keep a guardrail hard-blocking only when the harm of a miss justifies the cost of a false positive. Check: which tone violation should be warn-only? Lab observation: read the matrix, not just the attack count.

#### Ask

Which policy would you make warn-only, and what evidence would change your mind?

#### Watch in the exercise

Notebook cue: the matrix records five guardrail rows per case and flags uncaught attacks as findings.

#### Sources

[OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)


### D4-M18-C3B · 18 · Cheap rules are useful and brittle · The practical check

- Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 07 Big stats

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

Which policy would you make warn-only, and what evidence would change your mind?

#### Watch in the exercise

Notebook cue: the matrix records five guardrail rows per case and flags uncaught attacks as findings.

#### Sources

[OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)


### D4-M18-C4 · 18 · The system still owns authorization

- Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
- Instructor: Beric
- Type: core
- Timing: 2 minutes
- Layout: 05 Two column 3

#### Detailed preparation

End with the boundary students most often blur: content safety is not authorization. A guardrail can detect “reset my password” or redact an identifier, but only the application can verify identity, tenant, role, approval, and whether the tool is allowed to mutate state. Module 13's ladder defines the policy layer as deterministic authorisation on the user and the action, never a prompt. This notebook's Grow section points the scope check toward a tenant-aware policy classifier, and its `run_guarded` record keeps the model boundary separate from execution authorization. A useful record includes the case, stage, policy version, reason, and whether the model or tool was reached. This creates a bridge back to evals: every real incident should become a regression case, and every hard block should be reviewed for false positives. Check: what must be true before a password-reset tool can execute? Lab observation: inspect `model_reached`, `stage`, `expected`, and uncaught attack rows.

#### Ask

What must be true before a password-reset tool can execute?

#### Watch in the exercise

Notebook cue: use the saved `ots_results` fields to separate model boundary from execution authorization.

#### Sources

[OpenAI Agents SDK tools](https://openai.github.io/openai-agents-python/tools/), [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)


### D4-M18-C4B · 18 · The system still owns authorization · The practical check

- Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
- Instructor: Beric
- Type: core
- Timing: 1 minute
- Layout: 09 Lab and code 2

#### Detailed preparation

Use this short companion to turn the preceding concept into an observable engineering question. Keep the user question and evidence stable, then inspect the named notebook output or artifact. The point is not to add machinery automatically; it is to decide whether the current mechanism is sufficient, what failed, and what evidence would justify the next change.

#### Ask

What must be true before a password-reset tool can execute?

#### Watch in the exercise

Notebook cue: use the saved `ots_results` fields to separate model boundary from execution authorization.

#### Sources

[OpenAI Agents SDK tools](https://openai.github.io/openai-agents-python/tools/), [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)


### D4-M17-R1 · Optional research · State graphs for research

- Module: [17 Unroll deep research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md)
- Instructor: Eli
- Type: optional
- Timing: 0 minutes
- Layout: 08 Quote

#### Detailed preparation

This optional slide uses Anthropic’s June 2025 engineering case study as a concrete multi-agent research example. Anthropic describes a lead agent delegating parallel research to subagents, then compressing findings; its claimed internal result is vendor-reported and should not be treated as a cohort benchmark. The contribution is an architecture for breadth-first, open-ended questions; the tradeoff is materially higher token use, coordination complexity, and weaker fit for tightly coupled work. Compare that case with this notebook’s six-node single-graph workflow: both expose stages and handoffs, but neither makes sources authoritative. Ask the room whether parallel subagents are justified for an internal access-policy question. Stop when the group names a workload property, cost constraint, and evaluation needed to test the choice.

#### Ask

Which state boundary should stop when sources are empty?

#### Watch in the exercise

Notebook cue: compare the six node updates with the research trace and open gaps.

#### Sources

[Anthropic multi-agent research case study](https://www.anthropic.com/engineering/multi-agent-research-system), [LangGraph graph API](https://docs.langchain.com/oss/python/langgraph/graph-api), [Unroll deep research notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/Unroll_Deep_Research.ipynb)


### D4-M18-R1 · Optional research · Guardrails at the tool boundary

- Module: [18 Off-the-shelf guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md)
- Instructor: Beric
- Type: optional
- Timing: 0 minutes
- Layout: 08 Quote

#### Detailed preparation

This optional slide extends the notebook’s distinction between an answer boundary and an execution boundary. The OpenAI Agents SDK documentation describes tool guardrails that run around function-tool invocation and can allow normal execution, reject content while continuing, or raise an exception to halt. That is a sharper research question than “should we add more moderation?” For an access assistant, a sentence such as “I reset the account” is an output risk, while an unauthorized reset request is a tool-input risk. Ask the room to design one case for each and decide which outcome is appropriate. The notebook does not implement a mutating tool or a real authorization service, so this is a documented extension, not a claimed lab result. Stop when the policy owner and test case are named.

#### Ask

What tool-call condition should halt execution rather than merely warn?

#### Watch in the exercise

Alignment pending for this extension; the notebook’s confirmed cue is stage-specific tripwire handling.

#### Sources

[OpenAI tool guardrails](https://openai.github.io/openai-agents-python/ref/tool_guardrails/), [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/), [OTS guardrails notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/OTS_Guardrails.ipynb)


### D5-E1 · Show one working application flow

- Module: Evidence preparation
- Instructor: Course team
- Type: evidence
- Timing: 0 minutes
- Layout: 09 Lab and code

#### Detailed preparation

This is a demonstration format, not a production hosting requirement. Choose one recurring internal question and show the user-visible journey from input to answer. Keep the scope narrow enough that the audience can follow the actual mechanism: prompt, retrieval or tool call, returned observation, final answer, and any guardrail or evaluation record. Use the group’s real workspace artifacts where they exist; do not substitute a polished screenshot for a run. If the system is not reliable, say so and show the failure path. The audience should leave knowing what is working today and what evidence supports that statement. Check: can a viewer identify the exact artifact that proves the answer was grounded or the task passed? Lab observation: report only artifacts the notebooks actually generated.

#### Ask

What artifact proves the demonstrated path worked?

#### Watch in the exercise

Use existing workspace artifacts; do not fabricate scores, traces, or conclusions.

#### Sources

[Titanium Engineer README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/README.md), [Workspace contract](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/WORKSPACE.md), [Trajectory evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)


### D5-E2 · Compare against the simplest baseline

- Module: Evidence preparation
- Instructor: Course team
- Type: evidence
- Timing: 0 minutes
- Layout: 05 Two column

#### Detailed preparation

A comparison makes the engineering decision visible. Use the simplest credible baseline available: no context versus pasted context, dense versus hybrid retrieval, DCI versus agentic RAG, one run versus repeated trajectory evaluation, or unguarded versus guarded output. Keep the question and success condition constant. Do not claim that the newer path wins everywhere; the notebook exercises explicitly ask learners to inspect per-case matrices, disagreement, latency, and false positives. The most valuable comparison may be a non-win that tells the team to stop paying for an extra rung. Check: which row would change your decision if it got worse in the next run? Lab observation: use measured workspace artifacts when present and label any missing comparison as an open gap.

#### Ask

Which comparison row is your stopping rule?

#### Watch in the exercise

Point to the relevant saved artifact or mark the comparison as unmeasured.

#### Sources

[Titanium Engineer README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/README.md), [Reading guide](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/READING_GUIDE.md), [Retrieval ladder notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/Retrieval_Ladder.ipynb)


### D5-E3 · Explain architecture and one failure

- Module: Evidence preparation
- Instructor: Course team
- Type: evidence
- Timing: 0 minutes
- Layout: 09 Lab and code 1

#### Detailed preparation

The audience needs an explanation they can challenge. Draw the system boundary plainly: the model proposes; the application executes permitted tools; state and memory determine what context returns; guardrails inspect defined boundaries; the trace records what happened. Then replay one failure from the first incorrect step. If retrieval returned the wrong page, that is different from a judge mis-scoring a good answer. If memory leaked between users, that is different from a missing retention policy. Call each one by its evidence status: reproduced, suspected, or not measured. This keeps a working prototype honest without turning the session into a code review. Check: where did the failure first become observable? Lab observation: use actual trace, ladder, trajectory, or guardrail rows; no invented root cause.

#### Ask

At which boundary did the failure first become observable?

#### Watch in the exercise

Trace the claim to a real notebook output or mark it as pending.

#### Sources

[OpenAI Agents SDK agents](https://openai.github.io/openai-agents-python/agents/), [LangGraph graph API](https://docs.langchain.com/oss/python/langgraph/graph-api), [Workspace contract](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/WORKSPACE.md), [Agents 101 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb)


### D5-E4 · Make the next decision explicit

- Module: Evidence preparation
- Instructor: Course team
- Type: evidence
- Timing: 0 minutes
- Layout: 07 Big stats

#### Detailed preparation

End with a decision, not a generic future-work list. “Continue” means the demonstrated path cleared a stated bar and has a next controlled change. “Measure” means the evidence is insufficient, so name the missing case, metric, or trace and who will collect it. “Stop” means the added complexity, risk, or cost is not justified by the current result. None of these decisions requires the prototype to be hosted in production. The outcome is a working evaluated application: it documents observed behavior on tested cases and makes remaining uncertainty visible. Include one residual risk even when continuing; an uncaught attack, stale memory, weak retrieval case, or judge disagreement is useful evidence. Check: what exact result would reverse your decision? Lab observation: tie the decision to existing artifacts and unresolved gaps.

#### Ask

What exact result would reverse your decision?

#### Watch in the exercise

Decision must cite measured evidence or clearly state that it remains pending.

#### Sources

[Titanium Engineer README](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/README.md), [Demo scorecard](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/project/DEMO_SCORECARD.md), [Trajectory evals notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/Trajectory_Evals.ipynb)


