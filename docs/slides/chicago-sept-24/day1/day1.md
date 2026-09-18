---
marp: true
theme: default
paginate: true
size: 16:9
class: invert
title: Day 1 — Prototype and retrieve
# ⚠️ GOOGLE SLIDES IS AUTHORITATIVE FOR DAY 1.
#
# The day-1 deck has been revised by hand in Google Slides — slide variety,
# wording, and ordering were corrected there, and those changes are not
# reflected in this file. Review and edit day 1 in Google Slides.
#
# This markdown and the day1.html beside it are a historical record of the
# pre-revision deck, kept for the speaker notes, the cell# anchors, and the
# source links, which are all still accurate. Do not port edits from here into
# Google Slides: you would reintroduce the repetition that was removed, most of
# all in the opening framing slides.
#
# Days 2 through 5 are still authored in markdown, and edits to those belong
# here as usual.
---
# Today: from a repo to a retrieving agent

<div style="display:flex;justify-content:center;margin-top:.3em">
<svg viewBox="0 0 860 200" width="1080" role="img" aria-label="The five modules of the day, drawn to their length in minutes, ending in pitches">
<text x="10" y="34" font-size="14" fill="#94a3b8">Five demos, 155 minutes of them, one question carried through all five</text>
<rect x="10" y="60" width="157" height="74" rx="9" fill="#1e293b" stroke="#94a3b8" stroke-width="2.5"/><text x="20" y="86" font-size="15" font-weight="700" fill="#cbd5e1">01</text><text x="20" y="108" font-size="13" fill="#f1f5f9">Dev environment</text><text x="20" y="126" font-size="12" fill="#94a3b8">30 min</text><rect x="173" y="60" width="157" height="74" rx="9" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/><text x="183" y="86" font-size="15" font-weight="700" fill="#7dd3fc">02</text><text x="183" y="108" font-size="13" fill="#f1f5f9">Prompt patterns</text><text x="183" y="126" font-size="12" fill="#94a3b8">30 min</text><rect x="335" y="60" width="184" height="74" rx="9" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2.5"/><text x="345" y="86" font-size="15" font-weight="700" fill="#c4b5fd">03</text><text x="345" y="108" font-size="13" fill="#f1f5f9">Agents 101</text><text x="345" y="126" font-size="12" fill="#94a3b8">35 min</text><rect x="525" y="60" width="157" height="74" rx="9" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/><text x="535" y="86" font-size="15" font-weight="700" fill="#fcd34d">04</text><text x="535" y="108" font-size="13" fill="#f1f5f9">Vibe checks and judges</text><text x="535" y="126" font-size="12" fill="#94a3b8">30 min</text><rect x="687" y="60" width="157" height="74" rx="9" fill="#0f3320" stroke="#4ade80" stroke-width="2.5"/><text x="697" y="86" font-size="15" font-weight="700" fill="#86efac">05</text><text x="697" y="108" font-size="13" fill="#f1f5f9">RAG</text><text x="697" y="126" font-size="12" fill="#94a3b8">30 min</text>
<path d="M10 160 H850" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 4"/>
<text x="10" y="186" font-size="13" fill="#94a3b8">charter first</text>
<text x="850" y="186" font-size="13" fill="#fcd34d" text-anchor="end">then pitches, four minutes per group</text>
</svg>
</div>

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

<div style="display:flex;gap:1.2em;align-items:stretch;margin-top:.2em">
<div style="flex:1.3;background:#0b2b40;border-left:6px solid #38bdf8;border-radius:10px;padding:.7em 1em;display:flex;flex-direction:column;justify-content:center">
<div style="font-size:.55em;letter-spacing:.12em;text-transform:uppercase;color:#7dd3fc">One person, one recurring question</div>
<div style="font-size:1.25em;line-height:1.25;color:#f1f5f9;margin-top:.3em">“How do I restore access to my work account?”</div>
<div style="font-size:.6em;color:#94a3b8;margin-top:.5em">An illustrative shape only. Your group names its own person and question.</div>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:.55em;font-size:.68em">
<div style="background:#1e293b;border-radius:8px;padding:.5em .8em"><b style="color:#7dd3fc">Who</b><br>a named person, not “users”</div>
<div style="background:#1e293b;border-radius:8px;padding:.5em .8em"><b style="color:#fcd34d">Recurring</b><br>asked often enough to be worth a system</div>
<div style="background:#1e293b;border-radius:8px;padding:.5em .8em"><b style="color:#c4b5fd">Decision</b><br>what becomes easier once it is answered</div>
<div style="color:#94a3b8;padding:.2em .8em">The technology stays open until the question is fixed.</div>
</div>
</div>

> Source: [Concrete Idea Worksheet](https://corporate.aiaspire.ai/accenture/titanium/NA/agenda/cohort_2/Concrete_Idea_Worksheet.pdf)

<!--
Slide ID: D1-F1
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 01 Title
Speaker notes:
- Say: Teams that start from a technology build something impressive that nobody asked for.
- Ask: What decision would become easier if this question were answered well?
- Watch: In the later charter exercise, write one user and one recurring question; do not fill in the group's choice here.
- Then: Hand into “Define what a useful answer must contain”.
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
- Say: If you cannot say what a correct answer contains, you cannot tell a good demo from a lucky one.
- Ask: Which part of the answer would let you detect that the procedure is stale?
- Watch: During charter work, have the group write what a correct answer must contain for three questions.
- Then: Carry the observation into the next exercise.
Sources: [Concrete Idea Worksheet](https://corporate.aiaspire.ai/accenture/titanium/NA/agenda/cohort_2/Concrete_Idea_Worksheet.pdf); [Charter template](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/project/CHARTER.md).
-->

---
# Separate the task, the evidence, and the decision

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 860 300" width="900" role="img" aria-label="Task at the top, evidence bottom left, decision bottom right; the evidence changes when policy changes, the decision has an owner">
<defs><marker id="tri-a" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#94a3b8"/></marker></defs>
<path d="M430 96 L190 214" stroke="#94a3b8" stroke-width="2" marker-end="url(#tri-a)"/>
<path d="M430 96 L670 214" stroke="#94a3b8" stroke-width="2" marker-end="url(#tri-a)"/>
<path d="M270 244 H590" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5 5"/>
<g text-anchor="middle">
<rect x="320" y="22" width="220" height="64" rx="10" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/>
<text x="430" y="49" font-size="17" font-weight="700" fill="#7dd3fc">Task</text>
<text x="430" y="70" font-size="13" fill="#f1f5f9">what question must be answered</text>
<rect x="60" y="214" width="220" height="64" rx="10" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/>
<text x="170" y="241" font-size="17" font-weight="700" fill="#fcd34d">Evidence</text>
<text x="170" y="262" font-size="13" fill="#f1f5f9">the facts that can change</text>
<rect x="580" y="214" width="220" height="64" rx="10" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2.5"/>
<text x="690" y="241" font-size="17" font-weight="700" fill="#c4b5fd">Decision</text>
<text x="690" y="262" font-size="13" fill="#f1f5f9">who acts, what needs approval</text>
<text x="430" y="236" font-size="12" fill="#94a3b8">a policy update moves this edge</text>
<text x="260" y="150" font-size="12" fill="#94a3b8" transform="rotate(-26 260 150)">is answered from</text>
<text x="600" y="150" font-size="12" fill="#94a3b8" transform="rotate(26 600 150)">is owned by</text>
</g>
<text x="430" y="296" font-size="13" fill="#94a3b8" text-anchor="middle">A prompt that says “you are an administrator” moves none of the three.</text>
</svg>
</div>

> Source: [Semantic contracts research notes](https://github.com/soypete/ctx-eng-book/blob/main/research/semantic-contracts.md)

<!--
Slide ID: D1-F3
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 05 Two column
Speaker notes:
- Say: Most bad AI features blur these three, then cannot explain which part failed.
- Ask: Which of the three changes when a policy is updated: the task, the evidence, or the decision owner?
- Watch: Ask groups to put one changing fact and one accountable decision owner on their napkin sketch.
- Then: Hand into “A prototype tests your ability to answer a question”.
Sources: [Author's semantic-contract notes](https://github.com/soypete/ctx-eng-book/blob/main/research/semantic-contracts.md); [Course authoring principles](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/AUTHORING.md).
-->

---
# A prototype tests your ability to answer a question

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 860 240" width="1040" role="img" aria-label="Five candidate questions on the left narrow through a funnel to one uncertainty in the middle, which produces one observable failure and a stopping rule on the right">
<text x="24" y="34" font-size="12" fill="#94a3b8" letter-spacing="1.5">CANDIDATE UNCERTAINTIES</text>
<text x="24" y="62" font-size="13" fill="#94a3b8" font-weight="400">Will it find the right procedure?</text><text x="24" y="92" font-size="13" fill="#f1f5f9" font-weight="700">Will it keep the evidence?</text><text x="24" y="122" font-size="13" fill="#94a3b8" font-weight="400">Will it know when it lacks enough?</text><text x="24" y="152" font-size="13" fill="#94a3b8" font-weight="400">Will it answer fast enough?</text><text x="24" y="182" font-size="13" fill="#94a3b8" font-weight="400">Will it refuse the wrong things?</text>
<path d="M300 44 L420 96 L420 156 L300 210 Z" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
<path d="M300 44 H290 M300 210 H290" stroke="#94a3b8" stroke-width="1.5"/>
<rect x="436" y="88" width="180" height="76" rx="10" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/>
<text x="526" y="118" font-size="13" fill="#fcd34d" text-anchor="middle" letter-spacing="1.5">ONE UNCERTAINTY</text>
<text x="526" y="142" font-size="14" fill="#f1f5f9" text-anchor="middle">tested by this prototype</text>
<path d="M616 126 H636" stroke="#94a3b8" stroke-width="2"/>
<rect x="640" y="52" width="210" height="70" rx="10" fill="#3f1212" stroke="#f87171" stroke-width="2"/>
<text x="745" y="76" font-size="13" fill="#fca5a5" text-anchor="middle" font-weight="700">the failure that changes</text>
<text x="745" y="92" font-size="13" fill="#fca5a5" text-anchor="middle" font-weight="700">the design</text>
<text x="745" y="112" font-size="12" fill="#f1f5f9" text-anchor="middle">written down before the run</text>
<rect x="640" y="134" width="210" height="70" rx="10" fill="#0f3320" stroke="#4ade80" stroke-width="2"/>
<text x="745" y="158" font-size="13" fill="#86efac" text-anchor="middle" font-weight="700">the evidence that is</text>
<text x="745" y="174" font-size="13" fill="#86efac" text-anchor="middle" font-weight="700">enough to stop</text>
<text x="745" y="194" font-size="12" fill="#f1f5f9" text-anchor="middle">a number, not a feeling</text>
</svg>
</div>

> Source: [Machine Learning Yearning](https://github.com/ajaymache/machine-learning-yearning/blob/master/full%20book/machine-learning-yearning.pdf)

<!--
Slide ID: D1-F4
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 06 Process steps
Speaker notes:
- Say: A prototype that tests four things at once tells you nothing about any of them.
- Ask: What result would make you abandon the current approach rather than add another feature?
- Watch: In the charter, write two likely failures and how the group would notice each one.
- Then: Hand into “PoC: prove the mechanism manually”.
Sources: [Machine Learning Yearning](https://github.com/ajaymache/machine-learning-yearning/blob/master/full%20book/machine-learning-yearning.pdf); [Charter template](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/project/CHARTER.md).
-->

---
# PoC: prove the mechanism manually

<div style="display:flex;justify-content:center;margin-top:.3em">
<svg viewBox="0 0 860 200" width="1060" role="img" aria-label="Three chevrons: ask the question, paste the facts by hand, check the answer against the source">
<polygon points="14,40 260,40 282,94 260,148 14,148 14,94" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/><text x="54" y="80" font-size="22" font-weight="700" fill="#7dd3fc">Ask</text><text x="54" y="106" font-size="13" fill="#f1f5f9">the question, in a chat</text><text x="54" y="130" font-size="12" fill="#94a3b8">nothing automated yet</text><polygon points="290,40 536,40 558,94 536,148 290,148 312,94" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/><text x="330" y="80" font-size="22" font-weight="700" fill="#fcd34d">Paste</text><text x="330" y="106" font-size="13" fill="#f1f5f9">the relevant facts, by hand</text><text x="330" y="130" font-size="12" fill="#94a3b8">you are the retriever</text><polygon points="566,40 812,40 834,94 812,148 566,148 588,94" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2.5"/><text x="606" y="80" font-size="22" font-weight="700" fill="#c4b5fd">Check</text><text x="606" y="106" font-size="13" fill="#f1f5f9">the answer against source and criteria</text><text x="606" y="130" font-size="12" fill="#94a3b8">you are the judge</text>
<text x="430" y="186" font-size="13" fill="#94a3b8" text-anchor="middle">Each of these becomes a component later. Automate the one you can already measure.</text>
</svg>
</div>

> Source: [The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/)

<!--
Slide ID: D1-F5
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 09 Lab and code
Speaker notes:
- Say: Do it by hand first. If a person cannot do it with the data available, neither can a model.
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
- Say: The exit criterion is a recorded comparison, not a room that liked the demo.
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
- Say: One person, one flow, end to end. Breadth is what you add after that works.
- Ask: What is the smallest end-to-end flow your user could complete without a team member explaining the demo?
- Watch: Groups should keep their first product boundary narrow enough to demonstrate in the pitch.
- Then: Carry the observation into the next exercise.
Sources: [The product-market fit framework](https://pmarchive.com/guide_to_startups_part4.html); [Concrete startup idea handout](https://corporate.aiaspire.ai/accenture/titanium/NA/agenda/cohort_2/What_We_Mean_by_a_Concrete_Startup_Idea.pdf).
-->

---
# The MVP is one designed experience

<div style="font-size:.72em;margin-top:.2em">

| A car prepared for a test drive | Your MVP |
|---|---|
| One route the salesperson has driven | One user task, start to finish |
| Controls that work without explanation | A flow the user completes without a teammate narrating |
| The brakes are tested before the customer sits down | The failure response is designed, not discovered live |
| Not every option on the price list | Not every feature the roadmap imagines |

</div>

<div style="font-size:.7em;color:#94a3b8;margin-top:.4em">Mark the one flow you will show, and the options it deliberately leaves out.</div>

> Source: [The product-market fit framework](https://pmarchive.com/guide_to_startups_part4.html)

<!--
Slide ID: D1-F8
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 05 Two column 3
Speaker notes:
- Say: An MVP is a coherent experience, not a feature list with the rough edges left in.
- Ask: What would count as a test drive for your proposed AI product?
- Watch: In the napkin sketch, mark the one flow the group will show and the future options it will leave out.
- Then: Hand into “Production is repeatable operation”.
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
- Say: Production is not a bigger prototype; it is the same task surviving variation you did not pick.
- Ask: Which production responsibility would be missing if the demo only showed a successful answer?
- Watch: Groups should name one quality risk and one person who would own the consequence of failure.
- Then: Hand into “Production is the infrastructure around the car”.
Sources: [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents); [Module 01 production discussion](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).
-->

---
# Production is the infrastructure around the car

<div style="display:flex;justify-content:center;margin-top:0">
<svg viewBox="0 0 860 300" width="960" role="img" aria-label="The model sits at the centre of four rings: context, workflows, evals and observability, infrastructure">
<circle cx="300" cy="150" r="150.0" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/><circle cx="300" cy="150" r="116.0" fill="#0f3320" stroke="#4ade80" stroke-width="2"/><circle cx="300" cy="150" r="82.0" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2"/><circle cx="300" cy="150" r="50.0" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2"/>
<circle cx="300" cy="150" r="30" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/>
<text x="300" y="155" font-size="13" font-weight="700" fill="#7dd3fc" text-anchor="middle">model</text>
<text x="620" y="54" font-size="15" font-weight="700" fill="#cbd5e1">infrastructure</text><text x="620" y="72" font-size="12" fill="#f1f5f9">hosting, secrets, identity, cost</text><path d="M444.0 150 Q 490.0 46 612 48" stroke="#94a3b8" stroke-width="1.5" fill="none" stroke-dasharray="3 4"/><text x="620" y="106" font-size="15" font-weight="700" fill="#86efac">evals and observability</text><text x="620" y="124" font-size="12" fill="#f1f5f9">decide whether a change ships</text><path d="M410.0 150 Q 456.0 98 612 100" stroke="#4ade80" stroke-width="1.5" fill="none" stroke-dasharray="3 4"/><text x="620" y="158" font-size="15" font-weight="700" fill="#c4b5fd">workflows</text><text x="620" y="176" font-size="12" fill="#f1f5f9">permissions and recovery</text><path d="M376.0 150 Q 422.0 150 612 152" stroke="#a78bfa" stroke-width="1.5" fill="none" stroke-dasharray="3 4"/><text x="620" y="210" font-size="15" font-weight="700" fill="#fcd34d">context</text><text x="620" y="228" font-size="12" fill="#f1f5f9">prepared, refreshed, scoped</text><path d="M344.0 150 Q 390.0 202 612 204" stroke="#fbbf24" stroke-width="1.5" fill="none" stroke-dasharray="3 4"/>
<text x="300" y="292" font-size="13" fill="#94a3b8" text-anchor="middle">The car is the smallest part of the road trip.</text>
</svg>
</div>

> Source: [The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/)

<!--
Slide ID: D1-F10
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 06 Process steps 1
Speaker notes:
- Say: The model is the engine. Almost everything that makes it shippable is the car around it.
- Ask: Which control would you need before allowing the assistant to change data rather than only suggest a next step?
- Watch: Ask groups to circle one production concern their current PoC intentionally leaves unresolved.
- Then: Hand into “The same build ladder applies to AI”.
Sources: [The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/); [Author's context-assembly notes](https://github.com/soypete/ctx-eng-book/blob/main/research/context-assembly-pipeline-patterns.md).
-->

---
# The same build ladder applies to AI

<div style="display:flex;justify-content:center;margin-top:.2em">
<svg viewBox="0 0 860 250" width="1060" role="img" aria-label="Three risers from proof of concept to minimum viable product to production, each naming what it adds and the question it answers">
<rect x="20" y="150" width="268" height="90" rx="8" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/><text x="36" y="182" font-size="20" font-weight="700" fill="#7dd3fc">PoC</text><text x="36" y="206" font-size="12" fill="#f1f5f9">prompt, manual context, manual checks</text><text x="36" y="228" font-size="12" fill="#94a3b8">asks: does the mechanism work at all</text><text x="296" y="134" font-size="12" fill="#94a3b8">evidence, not a component, moves you up →</text><rect x="300" y="95" width="268" height="145" rx="8" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/><text x="316" y="127" font-size="20" font-weight="700" fill="#fcd34d">MVP</text><text x="316" y="151" font-size="12" fill="#f1f5f9">one usable path: skills, code, or MCP</text><text x="316" y="173" font-size="12" fill="#94a3b8">asks: can one person complete one flow</text><text x="576" y="79" font-size="12" fill="#94a3b8">evidence, not a component, moves you up →</text><rect x="580" y="40" width="268" height="200" rx="8" fill="#0f3320" stroke="#4ade80" stroke-width="2.5"/><text x="596" y="72" font-size="20" font-weight="700" fill="#86efac">Production</text><text x="596" y="96" font-size="12" fill="#f1f5f9">workflows, context, evals, infrastructure</text><text x="596" y="118" font-size="12" fill="#94a3b8">asks: does it hold under expected variation</text>
</svg>
</div>

> Source: [The LLM application stack](https://a16z.com/emerging-architectures-for-llm-applications/)

<!--
Slide ID: D1-F11
Module: Framing, before the selected modules
Instructor: Miriah
Type: framing
Minutes: 1
Layout: 04 Icon cards
Speaker notes:
- Say: AI does not get its own ladder. The rungs are the same; only the failure modes are new.
- Ask: Which new evidence—not which new component—would move your system to the next level?
- Watch: Groups should label their proposed system as a PoC, MVP, or production target and state what evidence is still missing.
- Then: Hand into “Day 1: answer one question, then earn complexity”.
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
- Say: One question, answered well, beats four half-built capabilities at the Friday panel.
- Ask: What is the first question your group will answer, and what evidence will tell you whether the prototype helped?
- Watch: Carry the question, answer contract, and first failure hypothesis into the group charter.
- Then: Carry the observation into the next exercise.
Sources: [Day 1 schedule](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/schedule/day1.md); [Day 1 cohort outline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/slides/chicago-sept-24/README.md); [Concrete Idea Worksheet](https://corporate.aiaspire.ai/accenture/titanium/NA/agenda/cohort_2/Concrete_Idea_Worksheet.pdf).
-->

---
# 01 · Dev environment

**Dev** — the machinery every later notebook assumes · 30 min

- Where the model comes from: one endpoint, any provider
- How a notebook is shaped: Learn, then **Create**, then Grow
- Where your work lives: `workspace/`, and the seed until it exists
- How a change gets reviewed: branch, diff, commit, pull request

No AI in this module. It is the floor the other four stand on.

<!--
Slide ID: D1-T01
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: transition
Minutes: 0
Layout: 01 Title
Speaker notes:
- Say: No AI in this module. It is the four pieces of machinery every later notebook assumes, so an hour lost here is an hour lost on Thursday.
- Ask: Ask who has already run `make setup` — it tells you how much of the slot is teaching and how much is triage.
- Watch: These four bullets are the module in order: the endpoint, the notebook's three acts, the workspace, then the git loop. The last two are what Friday's panel actually inspects.
- Then: Straight into the endpoint slide; it is the one that explains why any provider works.
Sources: [Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md).
-->
---

# One endpoint shape, whatever is behind it

<div style="display:flex;justify-content:center;margin-top:.35em">
<svg viewBox="0 0 860 200" width="980" role="img" aria-label="OpenAI, vLLM, Ollama, and the AIP gateway all speak the same OpenAI-compatible chat completions endpoint; the AIP gateway is the one this cohort uses">
<g text-anchor="middle">
<rect x="330" y="14" width="200" height="58" rx="9" fill="#172554" stroke="#38bdf8" stroke-width="2.5"/>
<text x="430" y="39" font-size="15" font-weight="700" fill="#7dd3fc">POST /v1/chat/completions</text>
<text x="430" y="58" font-size="12" fill="#38bdf8">one client shape</text>
<rect x="14" y="120" width="180" height="56" rx="9" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
<text x="104" y="154" font-size="15" font-weight="700" fill="#cbd5e1">OpenAI</text>
<rect x="212" y="120" width="180" height="56" rx="9" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
<text x="302" y="154" font-size="15" font-weight="700" fill="#cbd5e1">vLLM</text>
<rect x="410" y="120" width="180" height="56" rx="9" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
<text x="500" y="154" font-size="15" font-weight="700" fill="#cbd5e1">Ollama</text>
<rect x="622" y="116" width="224" height="64" rx="9" fill="#3a2a0a" stroke="#fbbf24" stroke-width="3"/>
<text x="734" y="142" font-size="15" font-weight="700" fill="#fcd34d">AIP gateway</text>
<text x="734" y="164" font-size="12" fill="#fcd34d">this week — via VPN</text>
</g>
<path d="M104 116 L370 76" stroke="#94a3b8" stroke-width="2" marker-end="url(#compat-arrow)"/>
<path d="M302 116 L400 76" stroke="#94a3b8" stroke-width="2" marker-end="url(#compat-arrow)"/>
<path d="M500 116 L460 76" stroke="#94a3b8" stroke-width="2" marker-end="url(#compat-arrow)"/>
<path d="M734 112 L495 74" stroke="#fbbf24" stroke-width="3" marker-end="url(#compat-arrow-hi)"/>
<defs>
<marker id="compat-arrow" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#94a3b8"/></marker>
<marker id="compat-arrow-hi" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#fbbf24"/></marker>
</defs>
</svg>
</div>

Same code, either way. Only `.env` changes: `OPENAI_BASE_URL`, `OPENAI_API_KEY`, `APIM_KEY`, `LLM_MODEL`.

Every notebook reads `OPENAI_BASE_URL`, so **the same code runs against a cloud key, a self-hosted server, or a local model.**

<!--
Slide ID: D1-M01-C0A
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 1
Layout: 02 Agenda 1
Speaker notes:
- Say: The client shape stays stable while the endpoint can be OpenAI, vLLM, Ollama — or a corporate API gateway. Nothing in the notebooks changes when the endpoint does.
- Ask: What would you change in the notebook if the endpoint moved from a hosted service to your own server?
- Watch: Keep the answer operational: `OPENAI_BASE_URL` selects the compatible endpoint; the notebook also reads the model and key from environment variables. The answer to the Ask is "nothing in the notebook" — only `.env`.
- Watch: Say plainly that this is exactly what they are doing this week. On the AIP environment the calls go through an Accenture API gateway rather than straight to a provider, so `OPENAI_BASE_URL` points at that gateway and a personal subscription key goes in `.env` as `APIM_KEY` alongside `OPENAI_API_KEY`. One key covers the models, the embeddings, and the reranker. Values come from the AIP setup guide and the provisioning tracker on SharePoint, not from a slide — and never from a chat message.
- Then: Two consequences worth naming now, because they cost the most time later. The VPN has to be connected before any API call, or every call returns 401 and it looks like a bad key. And the models behind the gateway are not the defaults in this repo's docs, so the model names in `.env` come from the guide too.
- Then: Notebook:cell#9 — Task 1 introduces the provider-independent setup before the rest of the repo loop.
Sources: [Course concepts](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md); [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).
-->

---

# Every notebook has three acts

<div style="display:flex;justify-content:center;margin-top:.65em">
<svg viewBox="0 0 720 170" width="900" role="img" aria-label="Learn, Create, Grow: learn builds the weak version, create writes to workspace, grow discusses production">
<g text-anchor="middle">
<rect x="20" y="35" width="200" height="78" rx="9" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2.5"/>
<text x="120" y="68" font-size="19" font-weight="700" fill="#c4b5fd">Learn</text>
<text x="120" y="91" font-size="12.5" fill="#a78bfa">weak version first</text>
<rect x="260" y="35" width="200" height="78" rx="9" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/>
<text x="360" y="68" font-size="19" font-weight="700" fill="#fcd34d">Create</text>
<text x="360" y="91" font-size="12.5" fill="#fbbf24">writes to workspace</text>
<rect x="500" y="35" width="200" height="78" rx="9" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/>
<text x="600" y="68" font-size="19" font-weight="700" fill="#7dd3fc">Grow</text>
<text x="600" y="91" font-size="12.5" fill="#38bdf8">what production needs</text>
</g>
<path d="M225 74 H255" stroke="#94a3b8" stroke-width="2" marker-end="url(#acts-arrow)"/>
<path d="M465 74 H495" stroke="#94a3b8" stroke-width="2" marker-end="url(#acts-arrow)"/>
<defs><marker id="acts-arrow" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#94a3b8"/></marker></defs>
</svg>
</div>

<!--
Slide ID: D1-M01-C0B
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 1
Layout: 06 Process steps
Speaker notes:
- Say: Learn makes the idea visible, Create makes it yours, and Grow names what production would require.
- Ask: Which artifact would prove that your group has moved past the seed example?
- Watch: The middle act is the handoff: it writes group artifacts to `workspace/`; without it, later notebooks can run while still reading Deskmate's seed.
- Then: Notebook:cell#16 — Task 3 runs `ws.init()` and `ws.status()` so students can see the workspace boundary. Skip Create and Thursday reads Deskmate's seed instead of your group's Priya transcripts.
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

# The seed is Deskmate, not your group

Every `seed` row above is the instructors' worked example: **Deskmate**, an IT helpdesk agent.

- Notebooks run on it from day one, so nothing is ever blocked
- Each one you produce replaces a row — and until then the seed answers for you
- **Never hand-write a file in `workspace/`.** Run the notebook that writes it

A number you did not measure is not yours to defend on Friday.

<!--
Slide ID: D1-M01-C1B
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 1
Layout: 04 Icon cards
Speaker notes:
- Say: Every seed row is somebody else's product. That is fine today and a problem on Friday.
- Ask: Ask what happens to a group that skips a module — the notebook still runs, which is exactly the trap.
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
- Watch: The module README's header names what this notebook reads and writes: reads nothing, writes the manifest and the charter. Dev_Environment:cell#16 is Task 3 of 8 — Initialise your workspace.
- Then: Point out that an SME reviewer in Phase 3 can read the manifest and see the same thing.
Sources: [Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Artifact integrity rules](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/AGENTS.md).
-->

---

# The manifest makes a result traceable

```json
{"artifact":"judge_scores", "module":"04", "count":24}
{"artifact":"baseline_runs", "module":"05", "count":3}
```

Takeaway: follow the artifact and its writer before trusting the number.

<!--
Slide ID: D1-M01-C2B
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 1
Layout: 05 Two column 2
Speaker notes:
- Say: A result is useful when its path and writer are visible.
- Ask: Which row would you inspect first if a judge score changed?
- Watch: Compare the two manifest rows: Module 04 wrote 24 judge scores; Module 05 wrote 3 baseline runs. Dev_Environment:cell#16 is Task 3 of 8 — Initialise your workspace.
- Then: Follow the artifact and its writer before trusting the number.
Sources: [Module 01 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md); [Charter template](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/project/CHARTER.md).
-->

---

# You work on a fork, not the course repo

<div style="display:flex;justify-content:center;margin-top:.4em">
<svg viewBox="0 0 620 170" width="880" role="img" aria-label="origin is your fork, which you push to; upstream is the course repository, which you fetch from">
<rect x="10" y="46" width="176" height="74" rx="9" fill="#172554" stroke="#60a5fa" stroke-width="2.5"/>
<text x="98" y="76" font-size="17" font-weight="700" text-anchor="middle" fill="#93c5fd">your fork</text>
<text x="98" y="99" font-size="14" font-family="monospace" text-anchor="middle" fill="#cbd5e1">origin</text>
<rect x="434" y="46" width="176" height="74" rx="9" fill="#1e293b" stroke="#94a3b8" stroke-width="2.5"/>
<text x="522" y="76" font-size="17" font-weight="700" text-anchor="middle" fill="#f1f5f9">course repo</text>
<text x="522" y="99" font-size="14" font-family="monospace" text-anchor="middle" fill="#cbd5e1">upstream</text>
<path d="M188 68 H430" stroke="#60a5fa" stroke-width="2.5" marker-end="url(#ar1)"/>
<text x="309" y="58" font-size="14" text-anchor="middle" fill="#60a5fa">push, then pull request</text>
<path d="M430 100 H192" stroke="#94a3b8" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#ar2)"/>
<text x="309" y="122" font-size="14" text-anchor="middle" fill="#cbd5e1">git fetch upstream</text>
<text x="309" y="152" font-size="13" text-anchor="middle" fill="#94a3b8" font-style="italic">you have write access on the left, not the right</text>
<defs>
<marker id="ar1" markerWidth="10" markerHeight="10" refX="8.5" refY="3" orient="auto"><path d="M0 0 L8.5 3 L0 6 z" fill="#60a5fa"/></marker>
<marker id="ar2" markerWidth="10" markerHeight="10" refX="8.5" refY="3" orient="auto"><path d="M0 0 L8.5 3 L0 6 z" fill="#94a3b8"/></marker>
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
- Say: Two remotes, two jobs. You push to the one you have write access to, and send changes back as pull requests.
- Ask: You fetched upstream and your files did not change. Is something wrong?
- Watch: Task 1 (cell#10) adds `upstream` if it is missing, reading the slug from `cohort.toml`. Task 2 (cell#13) fetches, shows the last five upstream commits with `git log --oneline -5` and the branch's position with `git status -sb`, then only *prints* the fast-forward command, so students run the merge deliberately.
- Then: Note that fetching updates your copy of the remote branches without touching your working files.
- Then: The shape is the same on the AIP environment, with different names. There the curriculum repo lives in Azure DevOps and is read-only — that is the box on the right — and each team has its own repo with write access, which is the box on the left. So "fork" and "upstream" become "your team repo" and "the shared labs repo", and the two-remote habit is unchanged. The clone is from a specific branch, not the default one, so anyone whose repo looks empty or wrong has probably cloned the default branch; the guide has the exact command.
Sources: [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow); [Module 01 notebook, Tasks 1-2](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb).
-->

---

# A small change should have a clear history

<div style="display:flex;justify-content:center;margin-top:.3em">
<svg viewBox="0 0 660 130" width="900" role="img" aria-label="branch, then change, then read the diff, then commit">
<g font-size="14" text-anchor="middle">
<rect x="6" y="34" width="140" height="58" rx="8" fill="#172554" stroke="#60a5fa" stroke-width="2"/>
<text x="76" y="52" font-size="12" fill="#60a5fa">STEP 1</text>
<text x="76" y="72" font-weight="700" fill="#93c5fd">branch</text>
<rect x="176" y="34" width="140" height="58" rx="8" fill="#172554" stroke="#60a5fa" stroke-width="2"/>
<text x="246" y="52" font-size="12" fill="#60a5fa">STEP 2</text>
<text x="246" y="72" font-weight="700" fill="#93c5fd">change</text>
<rect x="346" y="34" width="140" height="58" rx="8" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/>
<text x="416" y="52" font-size="12" fill="#fbbf24">STEP 3</text>
<text x="416" y="72" font-weight="700" fill="#fcd34d">read the diff</text>
<rect x="516" y="34" width="140" height="58" rx="8" fill="#172554" stroke="#60a5fa" stroke-width="2"/>
<text x="586" y="52" font-size="12" fill="#60a5fa">STEP 4</text>
<text x="586" y="72" font-weight="700" fill="#93c5fd">commit</text>
</g>
<path d="M148 63 H172" stroke="#94a3b8" stroke-width="2" marker-end="url(#s1)"/>
<path d="M318 63 H342" stroke="#94a3b8" stroke-width="2" marker-end="url(#s1)"/>
<path d="M488 63 H512" stroke="#94a3b8" stroke-width="2" marker-end="url(#s1)"/>
<text x="416" y="112" font-size="13" text-anchor="middle" fill="#fbbf24" font-style="italic">the step your AI editor cannot do for you</text>
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

# A commit records; a pull request reviews

```text
branch: feat/<login>-daily-loop
commit: docs: add <login> to members
review: pull request
```

Takeaway: committing records the change; review happens in the pull request.

<!--
Slide ID: D1-M01-C4B
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: This small history shows the distinction between recording work and reviewing it.
- Ask: Where in this sequence does another person inspect the change?
- Watch: Compare the branch and commit from the notebook with the separate pull-request review step. Dev_Environment:cell#20 is Task 4 of 8 — Branch for today's work.
- Then: Committing records the change; review happens in the pull request.
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

# A reviewable change explains its why

```diff
- api_key = "sk-prod-8f921a99b01c"
+ api_key = os.getenv("SECRET_API_KEY")
```

Takeaway: explain the changed line and the evidence before requesting review.

<!--
Slide ID: D1-M01-C5B
Module: [01 Dev environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md)
Instructor: Miriah, no-code orientation
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes:
- Say: The changed line tells a reviewer what happened; the explanation tells them why.
- Ask: What would you say about this line before asking for review?
- Watch: Compare the old hard-coded key with the environment lookup, then read the staged diff. Dev_Environment:cell#26 is Task 6 of 8 — Review the diff, then commit.
- Then: Explain the changed line and the evidence before requesting review.
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
- Two modules need an extra group: **`make setup-optim`** (15, DSPy) and **`make setup-graph`** (16)
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
- Say: These lines prevent most of the time the room would otherwise lose.
- Ask: A notebook that worked an hour ago now fails with `ModuleNotFoundError`. What changed?
- Watch: The answer is almost always that a bare `uv sync` or `uv run --group dev` removed an optional group. Fix: `make setup`, which keeps the groups already installed. Dev_Environment:cell#33 is Task 8 of 8 — Update the open pull request.
- Watch: This is not hypothetical — it came back from device testing as "No module named 'dspy'", because a setup guide's install command left out the optional group that carries it. If anyone hits it on a module, the fix is the matching make target, not a bare uv sync.
- Then: For an intercepted host, the terminal works because the machine trusts the private CA, but a container will not — keep the CA file to hand.
- Then: On the AIP environment the install command differs by platform: Mac and ALCS run `make setup`, and Windows is told to spell the groups out in full rather than use a bare `uv sync`. Either way the rule on this slide is the same one. A wrong Jupyter kernel produces the same symptom, so if a package is definitely installed, check the kernel before reinstalling anything.
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
- Say: Branch protection is how you stop relying on everyone remembering to be careful.
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
# 02 · Prompt patterns

**Prompt** — one call, and everything it needs in it

- A prompt has no memory, no facts of its own, and cannot act.
- 30 min

<!--
Slide ID: D1-T02
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli
Type: transition
Minutes: 0
Layout: 01 Title
Speaker notes:
- Say: A prompt has no memory, no facts of its own, and cannot act. That is what this module is for.
- Ask: Hold the room for a beat here — this is the hand-off, not content.
- Watch: Name the module, its stage on the journey, and who is running it. Keep it to one breath.
- Then: Straight into the first content slide.
Sources: [Module 02 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md).
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
- Say: Everything the model knows about this request has to be in the request.
- Ask: What important fact would the model be forced to guess if it is not in the prompt?
- Watch: Begin with one question and keep it fixed; each pattern changes only the request around it. Prompt_Patterns:cell#9 is Task 1.
- Then: Hand into “Few-shot: show the behavior you want”.
Sources: [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb).
-->

---

# Few-shot: show the behavior you want

- Give two or three examples of good inputs and outputs
- Demonstrate conventions the model cannot infer
- Change the examples when the behavior changes

<!--
Slide ID: D1-M02-C2
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli, code walkthrough
Type: core
Minutes: 2
Layout: 08 Quote
Speaker notes:
- Say: Two labelled examples teach a convention that no amount of description will.
- Ask: What behavior would you demonstrate with an example rather than describe in another paragraph?
- Watch: Compare no-examples against two labelled examples, holding the question and evidence fixed — Prompt_Patterns:cell#13, Task 2.
- Then: Hand into “Context supplies the facts the model cannot know”.
Sources: [Few-shot learners, Brown et al., 2020](https://arxiv.org/abs/2005.14165); [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb).
-->

---

# Scale makes few-shot learning stronger

> “Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches.”

— Brown et al. (2020)

<!--
Slide ID: D1-M02-C2B
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli
Type: evidence
Minutes: 1
Layout: 08 Quote
Speaker notes:
- Say: The paper's claim is about scale and task-agnostic few-shot performance; it is not a promise that examples replace evaluation.
- Ask: What would you measure before assuming a larger model is better for your task?
- Watch: Keep the claim attached to Brown et al. (2020); do not turn it into a universal claim about every model or corpus.
- Then: Return to the notebook and show the two labelled examples.
Sources: [Few-shot learners, Brown et al., 2020](https://arxiv.org/abs/2005.14165).
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
- Say: The model has never read your charter. Whatever it needs, you supply.
- Ask: What fact would the model otherwise have to guess?
- Watch: Same prompt with and without the pasted policy excerpt — Prompt_Patterns:cell#23, Task 5. This is the manual ancestor of RAG.
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
- Say: Voice and shape are separable from truth — a well-formatted answer can still be wrong.
- Ask: Which part of the prompt changes the reader, and which part changes the shape of the answer?
- Watch: Compare persona and structured-output variants; check factual content separately from voice — Prompt_Patterns:cell#9 (persona), cell#20 (schema).
- Then: Carry the observation into the next exercise.
Sources: [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb); [Author's semantic-contract notes](https://github.com/soypete/ctx-eng-book/blob/main/research/semantic-contracts.md).
-->

---

# A schema makes the shape a contract

Asking politely for JSON works most of the time. **Most of the time is not good enough for code that calls `json.loads`.**

A schema turns the shape into a contract — so the next step can be *code*, not a human reading prose.

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
- Then: Notebook:cell#20 — Task 4 introduces the structured-output contract in the notebook's own prose. Marcus can sort a queue by `risk_level`. He cannot sort a paragraph.
Sources: [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb); [Course concepts](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md).
-->

---

# Structured output is how a model calls a function

model output → **schema validation** → parsed arguments → function or MCP tool call

<div style="display:flex;gap:1em;align-items:flex-start;font-size:.72em">
<div style="flex:1">

```python
class ProductBrief(BaseModel):
    risk_level: Literal["low","medium","high"]

r = client.chat.completions.parse(
    ..., response_format=ProductBrief)
brief = r.choices[0].message.parsed
```

</div>
<div style="flex:1">

```json
{"risk_level": "high"}
```
```json
{"name": "search_charter",
 "args": {"query": "refund policy"}}
```

</div>
</div>

Toolformer trained a model to decide **which** API to call and **what arguments to pass**, keeping only the calls that measurably helped. The lesson for us: the more familiar the format, the more reliably a model emits it — which is why `bash` is the tool every model can already call.

A valid shape is still not a true value.

<!--
Slide ID: D1-M02-C4AB
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli, code walkthrough
Type: core
Minutes: 2
Layout: 09 Lab and code
Speaker notes:
- Say: This is the hinge of the week — a schema is what turns model output into something code can dispatch.
- Ask: Where would you validate a field whose value is shaped correctly but factually wrong?
- Watch: Prompt_Patterns:cell#20 is Task 4 of 7 — Structured output. Agent_Harness:cell#18 records every call as {"name", "args"}; Six_Ways:cell#24 is Task 5 of 7 — Code mode, where the model writes a program a runtime executes.
- Then: Worth saying if the room is technical: a familiar format is a reliability property, not a style choice — that is the argument for bash and for code mode in module 11.
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
- Say: Making the steps visible is what lets you check the work instead of trusting it.
- Ask: Which step could you verify independently?
- Watch: Compare a direct answer with one that exposes checkable steps — Prompt_Patterns:cell#17, the reasoning-budget task.
- Then: Hand into “Spend a reasoning budget deliberately”.
Sources: [Chain-of-thought prompting, Wei et al., 2022](https://arxiv.org/abs/2201.11903); [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb).
-->

---

# Spend a reasoning budget deliberately

- Compare no explicit reasoning against a high budget
- Read the token counts and the time cost
- Keep the trap question and evidence fixed

> Reasoning is token spend. More effort costs more tokens and more time.

<!--
Slide ID: D1-M02-C6
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli, code walkthrough
Type: core
Minutes: 2
Layout: 06 Process steps 1
Speaker notes:
- Say: A reasoning budget is a model setting with a measurable cost.
- Ask: What result would justify paying for more reasoning on this question?
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
- Say: One loop improves the answer; the other improves the instructions. Different tools.
- Ask: Did the revision improve the answer, the prompt, or both—and what evidence shows that?
- Watch: Put the named artifact on screen and trace where its values came from. Prompt_Patterns:cell#31 is Task 7 of 7 — Meta-prompting.
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
- Say: Hold the question fixed and change one thing, or you are collecting anecdotes.
- Ask: If prompt B wins one case but loses another, what would you inspect before choosing it?
- Watch: Put the named artifact on screen and trace where its values came from. Prompt_Patterns:cell#31 is Task 7 of 7 — Meta-prompting.
- Then: If the next step depends on an observation or tool result, investigate an agent.
Sources: [Prompt patterns Create/Grow](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb); [Simple workflows versus agents](https://www.anthropic.com/engineering/building-effective-agents).
-->

---

# Optional: from examples to measured refinement

- [Brown et al., 2020](https://arxiv.org/abs/2005.14165): examples supplied at inference time
- [Wei et al., 2022](https://arxiv.org/abs/2201.11903): reasoning demonstrations on tested tasks
- [Madaan et al., 2023](https://arxiv.org/abs/2303.17651): feedback and revision loops

<!--
Slide ID: D1-M02-R1
Module: [02 Prompt patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md)
Instructor: Eli
Type: optional
Minutes: 0
Layout: 08 Quote
Speaker notes:
- Say: Optional: this is where hand-tuned prompts give way to measured optimisation.
- Ask: Which of these mechanisms would address your observed error, and which would not?
- Watch: Optional reading, not an extra optimization module.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [Brown et al., 2020](https://arxiv.org/abs/2005.14165); [Wei et al., 2022](https://arxiv.org/abs/2201.11903); [Madaan et al., 2023](https://arxiv.org/abs/2303.17651).
-->

---
# 03 · Agents 101

**Agents** — a loop your code owns

- Reasoning alone cannot look anything up, or do anything.
- 35 min

<!--
Slide ID: D1-T03
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric
Type: transition
Minutes: 0
Layout: 01 Title
Speaker notes:
- Say: Reasoning alone cannot look anything up, or do anything. That is what this module is for.
- Ask: Hold the room for a beat here — this is the hand-off, not content.
- Watch: Name the module, its stage on the journey, and who is running it. Keep it to one breath.
- Then: Straight into the first content slide.
Sources: [Module 03 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md).
-->
---
# From prompt to agent: why the loop exists

<div style="display:flex;justify-content:center;margin-top:.15em">
<svg viewBox="0 0 760 210" width="920" role="img" aria-label="Four stages: a direct prompt, chain-of-thought which improves reasoning, Toolformer which shows models can call tools, and the harness where your code owns the tools">
<g text-anchor="middle">
<rect x="6" y="40" width="170" height="82" rx="9" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
<text x="91" y="62" font-size="11.5" fill="#94a3b8">ASK</text>
<text x="91" y="83" font-size="14.5" font-weight="700" fill="#f1f5f9">direct prompt</text>
<text x="91" y="104" font-size="11.5" fill="#cbd5e1">one call, one answer</text>

<rect x="196" y="40" width="170" height="82" rx="9" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/>
<text x="281" y="62" font-size="11.5" fill="#38bdf8">THINK</text>
<text x="281" y="83" font-size="14.5" font-weight="700" fill="#7dd3fc">chain of thought</text>
<text x="281" y="104" font-size="11.5" fill="#38bdf8">steps, still no facts</text>

<rect x="386" y="40" width="170" height="82" rx="9" fill="#0f3320" stroke="#4ade80" stroke-width="2"/>
<text x="471" y="62" font-size="11.5" fill="#4ade80">ACT</text>
<text x="471" y="83" font-size="14.5" font-weight="700" fill="#86efac">tool use</text>
<text x="471" y="104" font-size="11.5" fill="#4ade80">reach outside the model</text>

<rect x="576" y="40" width="178" height="82" rx="9" fill="#3a2a0a" stroke="#fbbf24" stroke-width="3"/>
<text x="665" y="62" font-size="11.5" fill="#fbbf24">GOVERN</text>
<text x="665" y="83" font-size="14.5" font-weight="700" fill="#fcd34d">the harness</text>
<text x="665" y="104" font-size="11.5" fill="#fbbf24">your code authorizes</text>
</g>
<path d="M178 81 H192" stroke="#94a3b8" stroke-width="2" marker-end="url(#e1)"/>
<path d="M368 81 H382" stroke="#94a3b8" stroke-width="2" marker-end="url(#e1)"/>
<path d="M558 81 H572" stroke="#94a3b8" stroke-width="2" marker-end="url(#e1)"/>
<g font-size="11" text-anchor="middle" fill="#94a3b8">
<text x="281" y="140">Wei et al. 2022</text>
<text x="471" y="140">Toolformer, Schick et al. 2023</text>
<text x="665" y="140">where this course lives</text>
</g>
<text x="380" y="176" font-size="13" text-anchor="middle" fill="#f1f5f9">Reasoning alone cannot look anything up. Tool use can — but something must decide if it is allowed.</text>
<text x="380" y="198" font-size="12.5" text-anchor="middle" fill="#fcd34d" font-style="italic">Toolformer taught the model to call tools. We keep the tools in code we own.</text>
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
- Watch: Chain of thought made the model's reasoning explicit and measurably better on hard tasks, but a reasoning step cannot retrieve a fact the model was never given. Toolformer showed models can learn to call an API mid-generation — that is the "why agents" moment. The difference here: Toolformer trained tool calls into the weights; we keep tools in code, so the harness can authorize, budget, and log every call. Agent_Harness:cell#9 is Task 1 of 6 — Give the agent something to look up.
- Then: Hand into the loop diagram — the amber GOVERN box is the next slide, drawn in detail.
Sources: [Chain-of-thought prompting, Wei et al., 2022](https://arxiv.org/abs/2201.11903); [Toolformer, Schick et al., 2023](https://arxiv.org/abs/2302.04761); [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
-->
---

# A model answers; an agent can choose a next step

<div style="display:flex;justify-content:center;margin-top:.2em">
<svg viewBox="0 0 700 250" width="900" role="img" aria-label="An agent loop: the model requests a tool, your code authorizes and runs it, the observation returns to the model, and the loop exits with an answer, a clarification, a refusal, or an exhausted budget">
<rect x="2" y="2" width="696" height="196" rx="12" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="7 5"/>
<text x="14" y="22" font-size="13" fill="#94a3b8" font-style="italic">the harness — yours, not the model's</text>

<rect x="36" y="74" width="152" height="66" rx="9" fill="#2a1d5a" stroke="#a78bfa" stroke-width="2.5"/>
<text x="112" y="101" font-size="16" font-weight="700" text-anchor="middle" fill="#c4b5fd">model</text>
<text x="112" y="122" font-size="12.5" text-anchor="middle" fill="#a78bfa">picks a next step</text>

<rect x="274" y="74" width="152" height="66" rx="9" fill="#3a2a0a" stroke="#fbbf24" stroke-width="3"/>
<text x="350" y="99" font-size="15.5" font-weight="700" text-anchor="middle" fill="#fcd34d">your code</text>
<text x="350" y="120" font-size="12.5" text-anchor="middle" fill="#fbbf24">authorizes + runs</text>

<rect x="512" y="74" width="152" height="66" rx="9" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/>
<text x="588" y="101" font-size="16" font-weight="700" text-anchor="middle" fill="#7dd3fc">tool</text>
<text x="588" y="122" font-size="12.5" text-anchor="middle" fill="#38bdf8">does the work</text>

<path d="M190 96 H270" stroke="#a78bfa" stroke-width="2.5" marker-end="url(#g1)"/>
<text x="230" y="87" font-size="11.5" text-anchor="middle" fill="#a78bfa">tool call</text>
<path d="M428 96 H508" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#g2)"/>
<path d="M508 126 H432" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#g3)"/>
<text x="470" y="146" font-size="11.5" text-anchor="middle" fill="#38bdf8">result</text>
<path d="M274 130 H194" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#g3)"/>
<text x="234" y="150" font-size="11.5" text-anchor="middle" fill="#38bdf8">observation</text>

<path d="M112 146 V176 H350" stroke="#94a3b8" stroke-width="2" fill="none" marker-end="url(#g4)"/>
<text x="240" y="192" font-size="12" text-anchor="middle" fill="#cbd5e1">loop again, or exit</text>

<text x="350" y="228" font-size="13.5" text-anchor="middle" fill="#f1f5f9" font-weight="600">exit: answer · clarify · decline · budget exhausted</text>
<defs>
<marker id="g1" markerWidth="10" markerHeight="10" refX="8.5" refY="3" orient="auto"><path d="M0 0 L8.5 3 L0 6 z" fill="#a78bfa"/></marker>
<marker id="g2" markerWidth="10" markerHeight="10" refX="8.5" refY="3" orient="auto"><path d="M0 0 L8.5 3 L0 6 z" fill="#fbbf24"/></marker>
<marker id="g3" markerWidth="10" markerHeight="10" refX="8.5" refY="3" orient="auto"><path d="M0 0 L8.5 3 L0 6 z" fill="#38bdf8"/></marker>
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
- Say: The loop is yours. The model only proposes; your code decides.
- Ask: Which box actually runs a tool, and which box decides whether it is allowed?
- Watch: In the streamed trace, locate the model message requesting a tool, the tool result, and the model's response to it — Agent_Harness:cell#21, Task 4.
- Then: Carry the observation into the next exercise.
Sources: [Agent harness notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Workflow and agent definitions](https://www.anthropic.com/engineering/building-effective-agents).
-->

---

# The trace proves the agent took a tool step

```text
for node, update in chunk.items():
    print(f"--- {node}")
    print("tool result:", textwrap.shorten(str(m.content), 300))
    print("tool call:", [(c["name"], c["args"]) for c in m.tool_calls])
```

Takeaway: the tool request and result are the evidence of an agent loop.

<!--
Slide ID: D1-M03-C1B
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: The trace makes the agent's next step visible.
- Ask: Which line proves the system used a tool?
- Watch: Locate the model request, tool result, and second model response in order. Agent_Harness:cell#21 is Task 4 of 6 — Watch the loop, step by step.
- Then: The tool request and result are the evidence of an agent loop.
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
- Say: A tool is a contract you publish, and the model sees nothing but that contract.
- Ask: If a retrieved page says “ignore your rules,” does that change the tool's permissions?
- Watch: Inspect how precise tool descriptions affect tool selection; do not equate making a tool call with making the correct call. Agent_Harness:cell#16 is Task 3 of 6 — Ask questions your users would ask.
- Then: Carry the observation into the next exercise.
Sources: [ReAct, Yao et al., 2022](https://arxiv.org/abs/2210.03629); [Agent harness tools](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb).
-->

---

# A tool contract is a permission boundary

```text
search_charter(query: str)
→ returns matching charter section text
```

Takeaway: tighten the contract before tuning the prompt.

<!--
Slide ID: D1-M03-C2B
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes:
- Say: The model can select only from the name, description, and input schema it sees.
- Ask: What does this contract permit the model to request?
- Watch: Compare the declared query input with the returned charter section; the contract does not grant access beyond that action. Agent_Harness:cell#9 is Task 1 of 6 — Give the agent something to look up.
- Then: Tighten the contract before tuning the prompt.
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
- Say: Limits, budgets, and exits belong to the harness — the model cannot enforce its own.
- Ask: What should the user receive when the budget ends before the task is complete?
- Watch: Watch middleware messages and the enforced limit; inspect the saved transcript rather than only the final answer. Agent_Harness:cell#21 is Task 4 of 6 — Watch the loop, step by step.
- Then: Carry the observation into the next exercise.
Sources: [Agent harness limits and trace](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
-->

---

# The trace records a control, not just an answer

```text
[middleware] model call with 1 message(s)
[middleware] model call with 3 message(s)
limit: 4 model calls
```

Takeaway: a budget is real only when the trace makes its effect visible.

<!--
Slide ID: D1-M03-C3B
Module: [03 Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: The trace shows work that a polished final answer can hide.
- Ask: What control would you point to if the run stopped early?
- Watch: Compare the middleware lines and the enforced budget; inspect the transcript, not only the final answer. Agent_Harness:cell#24 is Task 5 of 6 — Add middleware.
- Then: A budget is real only when the trace makes its effect visible.
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
- Say: Autonomy without a stopping rule is just an unbounded bill and an unread trace.
- Ask: What observation would change the next step in your proposed loop?
- Watch: Compare in-scope, human-needed, and out-of-scope questions — Agent_Harness:cell#16 is Task 3 of 6 — Ask questions your users would ask, where those three routes run live. Check tool behaviour matches the scope before praising fluency; the limit itself is cell#24, Task 5 of 6 — Add middleware.
- Then: A diagnosis needing an initial symptom, a search, and a follow-up question may benefit from adaptation.
Sources: [Agent harness Create/Grow](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/Agent_Harness.ipynb); [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
-->

---
# An agentic system is the loop plus everything around it

<div style="display:flex;justify-content:center;margin-top:.1em">
<svg viewBox="0 0 760 290" width="920" role="img" aria-label="The agent loop at the centre, surrounded by retrieval, memory, guardrails, and evaluation, each labelled with the module that covers it">
<rect x="196" y="96" width="368" height="96" rx="11" fill="#2a1d5a" stroke="#a78bfa" stroke-width="3"/>
<text x="380" y="124" font-size="16" font-weight="700" text-anchor="middle" fill="#c4b5fd">the agent loop</text>
<text x="380" y="147" font-size="13" text-anchor="middle" fill="#a78bfa">model → tool call → your code → observation</text>
<text x="380" y="173" font-size="12" text-anchor="middle" fill="#a78bfa" font-style="italic">module 03 · today</text>

<rect x="12" y="20" width="164" height="62" rx="9" fill="#0b2b40" stroke="#38bdf8" stroke-width="2"/>
<text x="94" y="45" font-size="14.5" font-weight="700" text-anchor="middle" fill="#7dd3fc">retrieval</text>
<text x="94" y="65" font-size="11.5" text-anchor="middle" fill="#38bdf8">modules 05 · 06 · 07</text>

<rect x="584" y="20" width="164" height="62" rx="9" fill="#0f3320" stroke="#4ade80" stroke-width="2"/>
<text x="666" y="45" font-size="14.5" font-weight="700" text-anchor="middle" fill="#86efac">memory</text>
<text x="666" y="65" font-size="11.5" text-anchor="middle" fill="#4ade80">module 10</text>

<rect x="12" y="206" width="164" height="62" rx="9" fill="#3f1212" stroke="#f87171" stroke-width="2"/>
<text x="94" y="231" font-size="14.5" font-weight="700" text-anchor="middle" fill="#fecaca">guardrails</text>
<text x="94" y="251" font-size="11.5" text-anchor="middle" fill="#fca5a5">modules 13 · 18</text>

<rect x="584" y="206" width="164" height="62" rx="9" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2"/>
<text x="666" y="231" font-size="14.5" font-weight="700" text-anchor="middle" fill="#fcd34d">evaluation</text>
<text x="666" y="251" font-size="11.5" text-anchor="middle" fill="#fbbf24">modules 04 · 09</text>

<path d="M176 58 C 240 58, 214 96, 258 96" stroke="#38bdf8" stroke-width="2" fill="none" marker-end="url(#a1)"/>
<path d="M584 58 C 520 58, 546 96, 502 96" stroke="#4ade80" stroke-width="2" fill="none" marker-end="url(#a2)"/>
<path d="M176 230 C 240 230, 214 192, 258 192" stroke="#f87171" stroke-width="2" fill="none" marker-end="url(#a3)"/>
<path d="M584 230 C 520 230, 546 192, 502 192" stroke="#fbbf24" stroke-width="2" fill="none" marker-end="url(#a4)"/>

<text x="380" y="214" font-size="11.5" text-anchor="middle" fill="#94a3b8">every step recorded in a trace — the thing you debug and evaluate</text>
<text x="380" y="286" font-size="13" text-anchor="middle" fill="#f1f5f9" font-weight="600">This is the diagram you will redraw all week, and bring to Friday's panel.</text>
<defs>
<marker id="a1" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#38bdf8"/></marker>
<marker id="a2" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#4ade80"/></marker>
<marker id="a3" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#f87171"/></marker>
<marker id="a4" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 z" fill="#fbbf24"/></marker>
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
- Watch: Name the module under each box so the week has a shape. Today builds only the purple box; by Friday a defensible system has all five, or a stated reason one is missing. Agent_Harness:cell#28 is Task 6 of 6 — Save the transcripts.
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
- Say: Optional: fluent reasoning is not the same as reliable action over many steps.
- Ask: After an interruption, which evidence would make a retry safe?
- Watch: Optional research only; the first harness does not implement full production recovery.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [ReAct](https://arxiv.org/abs/2210.03629); [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
-->

---
# 04 · Vibe checks and judges

**Measure** — before you trust any of it

- “Looks good” is a hypothesis, not a result.
- 30 min

<!--
Slide ID: D1-T04
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric
Type: transition
Minutes: 0
Layout: 01 Title
Speaker notes:
- Say: “Looks good” is a hypothesis, not a result. That is what this module is for.
- Ask: Hold the room for a beat here — this is the hand-off, not content.
- Watch: Name the module, its stage on the journey, and who is running it. Keep it to one breath.
- Then: Straight into the first content slide.
Sources: [Module 04 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md).
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
- Say: “Looks good” is a hypothesis. Everything after this slide is how you test it.
- Ask: Could two reviewers reasonably disagree about the word “helpful” in your rubric?
- Watch: Start from rubric definitions and hand-scored transcripts, before any automated judge — Vibe_Checks_LLM_Judge:cell#9 (rubric), cell#16 (judge by hand first).
- Then: For the support question, “clear answer” and “correct permitted next step” are different requirements.
Sources: [Vibe checks and judges notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM judge study, Zheng et al., 2023](https://arxiv.org/abs/2306.05685).
-->

---

# A rubric turns “good” into a test

```json
{"aspect":"actionable",
 "pass":"names the exact next step, menu path, or entitlement"}
```

Takeaway: write the pass definition before asking a judge to score.

<!--
Slide ID: D1-M04-C1B
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: A pass definition gives reviewers the same target.
- Ask: Could two reviewers apply this actionability rule the same way?
- Watch: Read the aspect and its pass condition before reviewing any transcript. Vibe_Checks_LLM_Judge:cell#9 is Task 1 of 9 — Write the rubric.
- Then: Write the pass definition before asking a judge to score.
Sources: [Vibe checks and judges notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM judge study, Zheng et al., 2023](https://arxiv.org/abs/2306.05685).
-->

---

# Establish the floor before trusting a judge

- **Echo:** give every transcript the middle score
- **Oracle:** copy the hand score exactly
- A real judge should clear the floor and approach the ceiling

<!--
Slide ID: D1-M04-C1C
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: Baselines tell us whether the agreement number contains signal before a judge enters the room.
- Ask: What would it mean if the oracle did not score 1.0 against the hand labels?
- Watch: Echo is the floor; oracle is the ceiling. A broken measure can make a bad judge look useful.
- Then: For Deskmate, Marcus needs an auditable log — that is what the user actually experiences in their environment, so the agreement measure has to work before a model is allowed to score anything. Vibe_Checks_LLM_Judge:cell#20 is Task 4 of 9 — Two dumb baselines before any judge.
Sources: [Vibe checks and judges notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM judge study, Zheng et al., 2023](https://arxiv.org/abs/2306.05685).
-->

---

# Test the agreement metric, not the judge

Score the same transcripts three ways and compare agreement with your hand scores:

| Scorer | What it does | Agreement should be |
|---|---|---|
| Echo | gives every transcript the middle score | **low** — this is the floor |
| Oracle | copies your hand score | **exactly 1.0** — the ceiling |
| A real judge | actually reads the transcript | between the two |

If the oracle is not 1.0, the **metric** is broken — not the judge.

<!--
Slide ID: D1-M04-C1CB
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 06 Process steps
Speaker notes:
- Say: This is not about rubrics. It asks a narrower question: can the agreement number tell a good scorer from a useless one at all?
- Ask: Echo scores everything the same and still gets some agreement by luck. What does that number tell you about any judge you compare to it?
- Watch: Two scorers that cannot judge — echo and oracle — run through the same agreement calculation. The oracle copies the hand scores, so it must read exactly 1.0; anything else means the calculation is wrong.
- Then: Only once the floor and ceiling look right is a real judge's score worth reading. Vibe_Checks_LLM_Judge:cell#20 is Task 4 of 9 — Two dumb baselines before any judge.
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
- Say: The judge is not an authority. It is an instrument, and you calibrate it first.
- Ask: What is the difference between a valid score and a justified score?
- Watch: Inspect the strict judge's error handling and compare its rationale with a hand verdict on the same transcript. Vibe_Checks_LLM_Judge:cell#25 is Task 5 of 9 — Build a strict judge.
- Then: Hand into “Read the judge's reasoning, not its number”.
Sources: [Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685); [Strict judge implementation](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb).
-->

---

# A score needs a reason you can inspect

```json
{"judge":"human","score":5,
 "rationale":"Answered without checking a source."}
```

Takeaway: the rationale explains whether the score is justified.

<!--
Slide ID: D1-M04-C2B
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes:
- Say: A number without a rationale gives you nothing to investigate.
- Ask: What evidence justifies the score of 5?
- Watch: Compare the score with the one-line rationale and inspect the strict judge's validated response. Vibe_Checks_LLM_Judge:cell#25 is Task 5 of 9 — Build a strict judge.
- Then: The rationale explains whether the score is justified.
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
- Say: Fluency and correctness are independent. Score them apart or you conflate them.
- Ask: Can an answer faithfully repeat an outdated procedure and still fail the user's task?
- Watch: Inspect the separate judge columns and their rationales; identify which dimension explains a disagreement. Vibe_Checks_LLM_Judge:cell#28 is Task 6 of 9 — Three judges that measure different things.
- Then: Carry the observation into the next exercise.
Sources: [Three judge dimensions](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [Ragas faithfulness definition](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/).
-->

---

# One answer can pass one dimension and fail another

```text
groundedness: 6   actionable: 10   clarity: 10
human:         5
```

Takeaway: separate scores show whether the problem is evidence, action, or expression.

<!--
Slide ID: D1-M04-C3B
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: Separate dimensions keep a fluent error from looking like a complete pass.
- Ask: Which dimension is the weak one in this row?
- Watch: Compare the three judge columns and their rationales; each measures one property. Vibe_Checks_LLM_Judge:cell#28 is Task 6 of 9 — Three judges that measure different things.
- Then: Separate scores show whether the problem is evidence, action, or expression.
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
- Say: Where graders disagree is where your rubric is ambiguous, not where the model is bad.
- Ask: What would make you distrust the judge rather than change the answer?
- Watch: Read the highest-disagreement row in the heatmap and explain the evidence. Do not replace an observed failure with a guessed score. Vibe_Checks_LLM_Judge:cell#35 is Task 8 of 9 — Find disagreement, not a winner.
- Then: Hand into “Follow the disagreement”.
Sources: [Disagreement analysis and responsible controls](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb); [LLM judge limitations](https://arxiv.org/abs/2306.05685).
-->

---

# The widest spread is the next case to read

```text
groundedness 10 | actionable 5 | clarity 10
spread         5
```

Takeaway: investigate the row with the widest spread before changing the system.

<!--
Slide ID: D1-M04-C4B
Module: [04 Vibe checks and judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes:
- Say: A spread is a reading list, not a winner.
- Ask: Which row would you open first, and why?
- Watch: Read the highest-spread row with its rationales; do not replace an observed failure with a guessed score. Vibe_Checks_LLM_Judge:cell#35 is Task 8 of 9 — Find disagreement, not a winner.
- Then: Investigate the row with the widest spread before changing the system.
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
- Say: Optional: before you trust the measurement, measure the measurement.
- Ask: How would you detect a bias that both model judges share?
- Watch: Optional reading; no new evaluation-framework lab is required.
- Then: Skip if time is short; offer as optional stretch or research.
Sources: [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685); [Notebook calibration discussion](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/Vibe_Checks_LLM_Judge.ipynb).
-->

---
# 05 · RAG

**RAG** — give the loop something true to say

- An agent with tools still has no grounded evidence.
- 30 min

<!--
Slide ID: D1-T05
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric
Type: transition
Minutes: 0
Layout: 01 Title
Speaker notes:
- Say: An agent with tools still has no grounded evidence. That is what this module is for.
- Ask: Hold the room for a beat here — this is the hand-off, not content.
- Watch: Name the module, its stage on the journey, and who is running it. Keep it to one breath.
- Then: Straight into the first content slide.
Sources: [Module 05 overview](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md).
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
- Say: Retrieval is not a feature. It is what you reach for when the model lacks the facts.
- Ask: If the source is wrong, what can retrieval actually improve?
- Watch: Put the named artifact on screen and trace where its values came from. RAG_with_LangChain:cell#9 is Task 1 of 7 — See the gap.
- Then: Today's notebook uses a practical retrieve-then-prompt pipeline, not a reproduction of the paper's training method.
Sources: [RAG, Lewis et al., 2020](https://arxiv.org/abs/2005.11401); [RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb).
-->

---

# Retrieval grounds the answer, or the model invents one

**Ask two questions against the same KB page:**

```text
"VPN is green but staging times out"
  → grounded: Settings → Routing → "Route private ranges", then restart

"What does a yellow VPN shield mean?"
  → the page documents only a green shield. There is no answer to ground.
```

Takeaway: retrieval lets the model cite the page — and lets you catch the question it should refuse.

<!--
Slide ID: D1-M05-C1B
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards
Speaker notes:
- Say: Retrieval is a hallucination control. Grounded, the model quotes the page; ungrounded, it produces something plausible anyway.
- Ask: Ask the room what a model with no KB access says to the yellow-shield question. Someone will guess "degraded connection" — which is exactly the invented answer.
- Watch: `data/seed/corpus/kb/vpn.md` documents a green shield and the split-tunnel fix; it says nothing about yellow. The first question has evidence to cite, the second does not. RAG_with_LangChain:cell#9 is Task 1 of 7 — See the gap.
- Then: A grounded system answers the first and declines the second. That refusal is a feature, and it is what module 04's judge scores.
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
- Say: Indexing happens once; searching happens per question. Confusing them costs money.
- Ask: Which step changes the stored index, and which step happens for every question?
- Watch: Locate chunk creation, ranking, and context assembly before the library version; explain what each library component replaces. RAG_with_LangChain:cell#17 is Task 3 of 7 — RAG from scratch.
- Then: Carry the observation into the next exercise.
Sources: [RAG from scratch and library pipeline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [Author's context-assembly notes](https://github.com/soypete/ctx-eng-book/blob/main/research/context-assembly-pipeline-patterns.md).
-->

---

# Retrieval earns its shortcut

<div style="display:flex;justify-content:center;margin-top:.2em">
<svg viewBox="0 0 780 190" width="920" role="img" aria-label="RAG learning arc: paste everything, build retrieval from scratch, then use LangChain">
<g text-anchor="middle">
<rect x="12" y="38" width="220" height="76" rx="9" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
<text x="122" y="67" font-size="15" font-weight="700" fill="#cbd5e1">paste everything</text>
<text x="122" y="91" font-size="12" fill="#94a3b8">measure token cost</text>
<rect x="280" y="38" width="220" height="76" rx="9" fill="#3a2a0a" stroke="#fbbf24" stroke-width="2.5"/>
<text x="390" y="67" font-size="15" font-weight="700" fill="#fcd34d">from scratch</text>
<text x="390" y="91" font-size="12" fill="#fbbf24">embed · rank · paste</text>
<rect x="548" y="38" width="220" height="76" rx="9" fill="#0b2b40" stroke="#38bdf8" stroke-width="2.5"/>
<text x="658" y="67" font-size="15" font-weight="700" fill="#7dd3fc">LangChain</text>
<text x="658" y="91" font-size="12" fill="#38bdf8">library replaces pieces</text>
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

# The chain assembles evidence before generation

```text
question → retriever → format_docs → prompt → model → text
```

Takeaway: inspect the assembled context before blaming the model.

<!--
Slide ID: D1-M05-C2B
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 05 Two column 2
Speaker notes:
- Say: The chain makes the evidence handoff explicit.
- Ask: Which arrow happens for every question?
- Watch: Trace the question through the retriever, document formatter, prompt, model, and parser. RAG_with_LangChain:cell#20 is Task 4 of 7 — The same pipeline in LangChain.
- Then: Inspect the assembled context before blaming the model.
Sources: [RAG from scratch and library pipeline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [Author's context-assembly notes](https://github.com/soypete/ctx-eng-book/blob/main/research/context-assembly-pipeline-patterns.md).
-->

---

# What to look for when a RAG answer is wrong

Three gates, in order. Only one of them is the model's fault:

- **Source** — did the corpus contain the fact at all?
- **Retrieval** — did it reach the model's context?
- **Generation** — did the answer use the passage, and keep its limits?

<!--
Slide ID: D1-M05-C3
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 04 Icon cards 2
Speaker notes:
- Say: Check them in order. Two of the three gates fail before the model ever sees the evidence.
- Ask: Which component should change if the answer-bearing passage never reaches the prompt?
- Watch: Compare two k settings on the same question and inspect actual chunks. Keep baseline contexts with each answer. RAG_with_LangChain:cell#28 is Task 6 of 7 — Retrieval quality is a dial.
- Then: Same three gates on day 2 when the ladder gets measured, so use these words. The lab stores questions, answers and contexts together so a later check can name which gate failed.
Sources: [RAG setup, top-k comparison, saved baseline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [RAG artifact contract](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md).
-->

---

# More chunks can recover the missing setting

```text
k = 1  → answer-bearing VPN passage absent
k = 4  → vpn.md reaches the prompt
```

Takeaway: change retrieval when the needed passage never arrives.

<!--
Slide ID: D1-M05-C3B
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 2
Layout: 07 Big stats
Speaker notes:
- Say: The first repair is to get the answer-bearing passage into context.
- Ask: What changed between the two retrieval settings?
- Watch: Compare the chunks and saved contexts for the same question at two k values. RAG_with_LangChain:cell#28 is Task 6 of 7 — Retrieval quality is a dial.
- Then: Change retrieval when the needed passage never arrives.
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
- Say: Letting the agent choose how to search is a different design, with different failures.
- Ask: What evidence would justify a second search instead of a final answer or clarification?
- Watch: Establish the fixed baseline first. Save its failures so later retrieval approaches have a fair comparison. RAG_with_LangChain:cell#20 is Task 4 of 7 — The same pipeline in LangChain.
- Then: Hand into “Save the baseline's failures”.
Sources: [RAG baseline](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb); [Agentic retrieval comparison](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/DCI_vs_Agentic_RAG.ipynb); [RAG versus long-context study](https://arxiv.org/abs/2407.16833).
-->

---

# A baseline failure is a comparison point

```text
Question: analytics warehouse access
Expected: entitlement, approver, wait
Baseline: “analytics_warehouse”; manager; one day
```

Takeaway: save the fixed baseline before asking a second search to beat it.

<!--
Slide ID: D1-M05-C4B
Module: [05 RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md)
Instructor: Beric, code walkthrough
Type: core
Minutes: 1
Layout: 09 Lab and code 2
Speaker notes:
- Say: A baseline gives the next retrieval strategy something concrete to improve.
- Ask: What would a second search have to improve in this answer?
- Watch: Keep the question, expected content, answer, and contexts together in the saved run. RAG_with_LangChain:cell#32 is Task 7 of 7 — Answer every vibe check and save.
- Then: Save the fixed baseline before asking a second search to beat it.
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
- Say: Optional: retrieval is a set of trade-offs you measure, not a box you tick.
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
- Then: Notebook:cell#41, Notebook:cell#40, Notebook:cell#38 — close by naming the three module tables behind these rows. For Deskmate, that means Priya's answer and Marcus's queue need repeatable review, shape, and retrieval.
Sources: [Module 01 notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/Dev_Environment.ipynb); [Prompt patterns notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/Prompt_Patterns.ipynb); [RAG notebook](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/RAG_with_LangChain.ipynb).
-->
