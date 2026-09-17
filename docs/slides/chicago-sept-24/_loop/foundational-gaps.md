# Foundational gaps audit — days 1–4

Prompted by finding that "agentic system" was never explained despite students being asked
to draw one four times. Method: test each concept the repo itself calls foundational
(`docs/CONCEPTS.md` § "The three ideas the whole repo is built on" and § "Cross-cutting
concepts, by frequency") against whether any slide in `day1`–`day4` actually *explains* it —
being a slide title, not a passing mention. Then cross-check every module's notebook tasks
against its deck slides.

Audited 2026-09-17 against 185 slides and 13 module notebooks.

## Tier 1 — Same class of gap as the agentic-system one

These are concepts the repo names as foundational, that the code depends on repeatedly, and
that **no slide ever explains**.

### 1. Structured output — the worst one

`docs/CONCEPTS.md:141` names exactly two model capabilities as **not optional**: tool
calling and structured output, because "the agent and eval modules are built on them."

- **Used in 8 notebooks**: 02, 03, 06, 08, 09, 12, 17, 21.
- **Listed as cross-cutting** for Mon–Thu, modules 02/03/06/09/17/21 (`CONCEPTS.md:714`).
- **It is a real task students run**: `02_Prompt_Patterns/Prompt_Patterns.ipynb` Task 4 of 7,
  `cell#20`–`cell#21`, which defines a `ProductBrief(BaseModel)` with a `Literal` risk field
  and calls `client.chat.completions.parse(..., response_format=ProductBrief)`.
- **Slides: zero.** Never a title, never mentioned in any body text across all five decks.

Tool calling, its stated twin, gets slides in module 03. Structured output gets none, even
though it is what lets every later module's code parse a model's answer instead of regexing
prose.

### 2. Module 02's slide set does not match its notebook

The notebook has seven numbered tasks. `CONCEPTS.md:276` lists the same seven patterns. The
deck covers six of them, invents one, and drops two:

| Notebook task (`Prompt_Patterns.ipynb`) | Deck slide |
|---|---|
| Task 1 — Persona | `D1-M02-C4` (merged with format) |
| Task 2 — Few-shot | `D1-M02-C2` |
| Task 3 — Reasoning budget | **none** |
| Task 4 — Structured output | **none** |
| Task 5 — Pasted context | `D1-M02-C3` |
| Task 6 — Self-refine | `D1-M02-C7` (merged) |
| Task 7 — Meta-prompting | `D1-M02-C7` (merged) |
| — | `D1-M02-C5` chain of thought (agenda names it; = reasoning budget) |
| — | `D1-M02-C6` **ReAct** — *the string "ReAct" appears 0 times in the notebook* |

So module 02 has a slide for a pattern its notebook never teaches (ReAct, which properly
belongs to module 03) while omitting two it does. `CONCEPTS.md:290` already anticipates part
of this: "Agenda also names **chain of thought** and **output-format enforcement** (= #3 and
#4)" — i.e. chain-of-thought *is* the reasoning-budget task and output-format enforcement
*is* structured output. The deck took the first mapping and dropped the second.

### 3. "Everything is OpenAI-compatible"

`CONCEPTS.md:131` — idea **1 of 3** the whole repo is built on. One endpoint shape, so
notebooks never hard-code a provider; they read `OPENAI_API_KEY`, `OPENAI_BASE_URL`,
`LLM_MODEL`, and a self-hosted or local server works identically.

- **Slides: zero** across all five decks. Grepped for `OPENAI_BASE_URL`, "OpenAI-compatible",
  "base url", "provider": no hits in projected copy or notes.
- Consequence: students never learn why they can swap in a local model, or why
  `helpers/llm.py` retries without `reasoning_effort` when a self-hosted server rejects it.
  It also undercuts the enterprise story — "this runs against your own endpoint" is exactly
  what a consultant's client asks.

### 4. Learn / Create / Grow

`CONCEPTS.md:185` — idea **3 of 3**. Every notebook is three acts, and knowing which act you
are in tells you what to do when stuck: "Stuck in Learn? Run the weak version and read what
it got wrong." Critically, **Create is the act that writes to the workspace**, so it is the
act a group cannot skip without leaving a hole later modules fill from the seed.

- **Slides: one bullet**, on `D1-M01-C0` (the concepts slide added this week). Never explained.
- Every module README is structured by it, so students see the words in 13 notebooks with no
  slide ever saying what they mean.

## Tier 2 — Real but narrower

### 5. The five guardrail rungs are never named

Module 13's notebook builds Rung 0 constrained decoding, Rung 1 rules, Rung 2 a classifier,
Rung 3 an LLM judge, Rung 4 a policy layer. The deck teaches the *ladder concept* well
(cheapest sufficient rung, protection vs. friction, fail closed) but never lists the rungs.
Grepping day3 for the rung names: "classifier" appears 3×, the other four zero times.

This is a defensible choice — teach the principle, let the notebook supply the rungs — but
it means a student cannot answer "what are the options?" from the slides, and Friday's panel
question "what did you choose not to ship?" is a rung question.

### 6. Module 05's weak-first arc is not visible

The notebook's shape is deliberate: Task 2 "What it costs to paste everything" → Task 3 "RAG
from scratch" → Task 4 "The same pipeline in LangChain". That is the course's core teaching
move (build the weak version, read what it got wrong, then reach for the library). The deck's
four concept slides state retrieval principles but never show the from-scratch → framework
progression, so the reason for doing it twice is lost.

### 7. Module 11 omits two of its six mechanisms

The module is literally "six ways to give an agent a capability." The deck covers tool,
skill, sub-agent, and code mode; **MCP server** and **UTCP manifest** get no slide, though
MCP is on Wednesday's required reading list and is the mechanism most likely to come up in a
client conversation.

## Not gaps (checked, found covered)

- **Never fabricate an artifact** — `AGENTS.md:55` hard rule; covered by `D1-M01-C1B`'s
  Decide line and day5's notes.
- **Traces, budgets, LLM-as-judge, BM25, reranking, measure-before-you-adopt** — all get
  slide titles, several across multiple modules.
- **Module 13's ladder, module 09's trajectory scoring, module 10's memory kinds** — the
  crude task-vs-title keyword check flagged these, but reading the slides shows the concepts
  are taught in different words. False positives.
- **Chunking and embeddings** — thin (one title, `D1-M05-C3B`) but present, and module 06
  covers the retrieval mechanics properly.

## Recommendation, in order

1. **A structured-output slide in module 02**, with the `ProductBrief` Pydantic model and the
   `response_format=` call beside it. Highest value: it is a real task, it is one of two
   non-optional capabilities, and 8 notebooks depend on it. Module 02 currently has 9 slides
   for a 30-minute slot, so there is room.
2. **Fix module 02's ReAct/reasoning-budget mismatch** — either retitle `D1-M02-C6` to the
   reasoning-budget task the notebook actually runs, or move ReAct to module 03 where the
   citation already lives (`D1-M03-C2` cites it).
3. **An "everything is OpenAI-compatible" slide**, early on day 1. Cheap, and it is the
   answer to a question every enterprise student will ask.
4. **Name the five rungs** on a module 13 slide, or in `D3-M13-C2`'s speaker notes at minimum.
5. **Learn / Create / Grow** as a real slide on day 1, stressing that Create writes the
   workspace. Pairs naturally with the module-01 workspace slide.
6. Module 11's MCP and UTCP mechanisms; module 05's weak-first arc.

## Cross-cutting note

All 13 of these modules' decks are **bullets-only** except modules 01 and 03, which now have
diagrams. Several Tier-1 fixes are naturally visual: structured output wants the schema and
the parsed object side by side; OpenAI-compatible wants one endpoint with three clients
pointing at it; Learn/Create/Grow wants three labelled acts with "writes to workspace" on the
middle one.
