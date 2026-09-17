# Slide Alignment Loop — Progress

## Resolved paths

| Name | Resolved value | Notes |
|---|---|---|
| `MODULE_REPO` | `/Users/soypete/code/misc/Aspire_Titanium_Engineer` | Same as working repo. Module folders (`NN_*`), `docs/CONCEPTS.md`, `docs/READING_GUIDE.md` are READ-ONLY. |
| `PREV_SLIDES_DIR` | `~/Downloads/Titanium*` | 5 usable sources: Day 1 `.pptx` (+`.txt`), Cohort3 Sessions 01–04 `.pdf`, Session 02 `.zip`/folder. |
| `CONCEPTS` | `docs/CONCEPTS.md` | |
| `READING_GUIDE` | `docs/READING_GUIDE.md` | |
| `OUR_DECKS` | `docs/slides/chicago-sept-24/` | User-confirmed: script's `heredocs/` is a typo for `docs/`. Decks are per-day (`day1.md`…`day5.md`), not per-module. |
| `LOOP_DIR` | `docs/slides/chicago-sept-24/_loop/` | |
| `ALIGN_DIR` | `docs/slides/chicago-sept-24/_loop/alignment/` | |
| `COMPANION_DIR` | `docs/slides/chicago-sept-24/companions/` | |

**Deck convention (user-confirmed):** revise the module's slides in place inside the
matching `dayN.md`. Do not create per-module deck files.

## Module status

| # | Module | Day | Time | Instructor | Status | Files touched | Principles | Open questions |
|---|---|---|---|---|---|---|---|---|
| 01 | Dev environment | 1 | 30m | Miriah (no code) | **done** | `day1.md` (slides `D1-M01-*`, 9→17 slides, 30 min exactly); `_loop/alignment/01-dev-environment.md`; `companions/01-dev-environment.md`; `_loop/prev-slides-text/` (cache); `_loop/build/day1.html` | 14 | 15 — see companion §10. Headlines: READING_GUIDE has no module-01 entry; 5 concepts missing from CONCEPTS.md (draft PR, `type: summary`, fetch-vs-merge, cleanup cell, `make preflight`); 3 terminology conflicts with the prior deck (workbench→workspace, saved results→artifact, invented `workbench_context.json` removed); Cohort-3 Session02 is PNG-only and cannot be text-extracted. |
| 02 |Prompt patterns | 1 | 30m | Eli | **deck: partial** | `day1.md` | — | agenda, structured-output pair, ReAct→reasoning-budget fix, key terms. **Still owed by the loop spec: alignment file + companion sheet + prior-slide mapping.** |
| 03 |Agents 101 | 1 | 35m | Beric | **deck: partial** | `day1.md` | — | evolution + loop + whole-system SVGs (earlier commit), key terms. **Still owed by the loop spec: alignment file + companion sheet + prior-slide mapping.** |
| 04 |Vibe checks and judges | 1 | 30m | Beric | **deck: partial** | `day1.md` | — | baseline-judge pair, key terms. **Still owed by the loop spec: alignment file + companion sheet + prior-slide mapping.** |
| 05 |RAG | 1 | 30m | Beric | **deck: partial** | `day1.md` | — | weak-first arc SVG, "chain" named, key terms. **Still owed by the loop spec: alignment file + companion sheet + prior-slide mapping.** |
| 06 |Advanced retrieval | 2 | 35m | Eli | **deck: partial** | `day2.md` | — | "filter before you rank" triple, 2 SVGs, key terms. **Still owed by the loop spec: alignment file + companion sheet + prior-slide mapping.** |
| 07 |Agentic retrieval | 2 | 30m | Eli | **deck: partial** | `day2.md` | — | "inspect the difference" triple, DCI/Agentic RAG/wiki named. **Still owed by the loop spec: alignment file + companion sheet + prior-slide mapping.** |
| 08 |SDG and RAGAS | 2 | 30m | Beric | **deck: partial** | `day2.md` | — | "curate the test set" triple, datasheet named. **Still owed by the loop spec: alignment file + companion sheet + prior-slide mapping.** |
| 09 |Agent evals | 3 | 35m | Eli | **deck: partial** | `day3.md` | — | day-3 agenda slide. **Still owed by the loop spec: alignment file + companion sheet + prior-slide mapping.** |
| 10 |Agent memory | 3 | 30m | Beric | **deck: partial** | `day3.md` | — | root set named, memory-taxonomy note. **Still owed by the loop spec: alignment file + companion sheet + prior-slide mapping.** |
| 11 |Agent architecture | 3 | 35m | Rohit | **deck: partial** | `day3.md` | — | MCP + UTCP pair. **Still owed by the loop spec: alignment file + companion sheet + prior-slide mapping.** |
| 13 |Guardrails 101 | 3 | 30m | Rohit | **deck: partial** | `day3.md` | — | five-rung SVG ladder, day-3 closer. **Still owed by the loop spec: alignment file + companion sheet + prior-slide mapping.** |
| 17 |Deep research | 4 | 35m | Eli | **deck: partial** | `day4.md` | — | day-4 agenda, compile/trace pair. **Still owed by the loop spec: alignment file + companion sheet + prior-slide mapping.** |
| 18 |Off-the-shelf guardrails | 4 | 30m | Beric | **deck: partial** | `day4.md` | — | PII-redaction pair, placement SVG, fail-closed named. **Still owed by the loop spec: alignment file + companion sheet + prior-slide mapping.** |

Not in scope: 12, 14, 15, 16, 19–23.

## Notes for later runs

- **Prior-slides cache** is in `_loop/prev-slides-text/`: `Day1.pptx.txt` (43 slides, Cohort 4
  St. Charles, with notes), `Session01_Intro_AgenticAI.txt`, `Session03_AgentsInPractice.txt`.
  **Reuse it; do not regenerate.** `pdftotext` is not installed on this machine — the PDFs were
  extracted with `uv run --with pypdf`, which takes ~90 s per deck.
  `Session04_AdvancedTechniques.pdf` is not yet extracted (needed for modules 17, 18).
- **Blocked source:** `~/Downloads/Titanium_Engineer_Cohort3_Session02_RAG+Agents{.zip,/}` is
  PNG page images with no text layer. It covers RAG and agents, so it will matter for modules
  05–07. Either find an original with text, or OCR it.
- **Deck convention:** decks are per-day (`day1.md`…`day5.md`), not per-module. Edit the
  module's slides in place; the slide-ID convention is `D1-M01-C1`, `-C1B` for its paired
  "practical check" slide, `-R1` for optional, plus `-C0` concepts, `-RD1` reading,
  `-RS1` resources, `-Q1` check-your-understanding.
- **Note schema** in each slide's `<!-- -->` block: `Slide ID`, `Module`, `Instructor`,
  `Type`, `Minutes`, `Layout`, `Speaker notes` (as `Say:` / `Ask:` / `Watch:` / `Then:`
  bullets), `Sources`. Sum `Minutes:` across a module's slides to check the time budget.
- **Known debt outside module 01:** the boilerplate note line "Inspect the named output and
  verify its provenance" still appears in `D1-M02-C7`, `D1-M02-C8`, `D1-M05-C1`, `D1-M05-C1B`.
  Replace it when those modules come up.
- **Validation commands that work here:** `marp --html --allow-local-files -o
  docs/slides/chicago-sept-24/_loop/build/dayN.html docs/slides/chicago-sept-24/dayN.md`
  (local `marp` is installed; `npx` was not needed). Dump notebook cells with
  `uv run --no-project python` + `json` to get the indices that `cell#N` pointers must match.
- **Path note:** the script's `heredocs/slides/chicago-sept-24/` does not exist; the user
  confirmed it means `docs/slides/chicago-sept-24/`. `MODULE_REPO` is this same repo, so
  "read-only" applies to the module folders, `docs/CONCEPTS.md`, and `docs/READING_GUIDE.md`.

## Blocking issue for publication

**13 slides in `day1.md` link to `https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/CONCEPTS.md`, which returns 404.** `docs/CONCEPTS.md` and
`docs/READING_GUIDE.md` are untracked locally (`git status` shows `??`), so they do not
exist on `main` yet. The slide links are correct in form and will work the moment those two
files are committed and pushed; until then every "Course concepts" source link is dead.

These files are READ-ONLY for this loop, so this run did not commit them. Someone with
ownership of the course docs needs to push them. Verified 2026-09-17 by resolving every
module-03 URL: all others return 200.

## Foundation pass — days 1–4 (2026-09-17)

Four herdr subagents (codex), one per day, run in parallel. Each edited only its own `dayN.md`;
all shared-file edits were made by the orchestrator. **All verification checks pass.**

| Day | Slides added | Highlights |
|---|---|---|
| 1 | 9 (`D1-F0`, `D1-M01-C0A/C0B`, `D1-M02-C4A/C4AB`, `D1-M04-C1C/C1CB`, `D1-M05-C2A`, `D1-Z1`) + 1 edited | **Structured output** — the project's worst gap — now a slide pair quoting the notebook's own prose with the real `ProductBrief(BaseModel)` and `response_format=`. ReAct removed from module 02 (it appeared 0 times in that notebook); `D1-M02-C6` now teaches the reasoning-budget task it should. "OpenAI-compatible" and "Learn/Create/Grow" added as `Minutes: 0` build slides so **M01 stays exactly 30**. |
| 2 | 11 (`D2-F0`, three `C5/C5B/C5A` triples, `D2-Z1`) + 2 edited | Coverage for the uncovered tasks in 06/07/08, respecting day 2's concept/question/answer triple convention. First visuals on day 2: dense-vs-sparse and the retrieval ladder. |
| 3 | 6 (`D3-F1`, `D3-M11-C5/C5B`, `D3-M13-C2A/C2AB`, `D3-Z1`) | **The five guardrail rungs are named for the first time**, as an SVG ladder with a cell pointer per rung. Module 11's MCP and UTCP added — its own "six ways" had omitted two. |
| 4 | 6 (`D4-F1`, `D4-M17-C5/C5B`, `D4-M18-C5/C5B`, `D4-Z1`) | Coverage for modules 17/18's uncovered tasks; module 17 grounded in Deskmate (its notebook has zero scenario vocabulary). Orchestrator added the guardrail-placement SVG to `D4-M18-C2`. |

Every day now opens with a real agenda slide (none existed before; days 3 and 4 opened cold on
module content) and closes with a production slide whose rows are **lifted verbatim** from that
module's own `## From prototype to production` table — spot-checked against the notebooks.

Verification: all 5 decks render (`marp --no-stdin`); 43 cell pointers in range and matching
their claimed tasks; no module over budget and M01 exactly 30; zero instructor names in
projected copy; zero duplicate titles; no mermaid fences. 34 of 35 links in the new lines
return 200 — the one 404 is the pre-existing `docs/CONCEPTS.md` issue below.

Visual coverage went from day1 5 SVG / day2 0 / day3 0 / day4 0 to **day1 8, day2 2, day3 2,
day4 1**, plus code slides on day 1.

### Open questions from this pass

- `docs/READING_GUIDE.md` has no entry for modules 17 or 18 (reported by the day-4 agent).
- Scope note: industry trends are deliberately **not** in these slides — Beric and Eli cover
  them live with the code, which also keeps the decks consistent with
  `cohort-outline/sources-and-coverage.md`, whose narrative section disclaims forecasting.

## README key-terms audit (2026-09-17)

Audited the "Plain English first" terms table in every module README against its slides.
**58 terms across 11 modules; now 58/58 appear in projected slide copy** (was 51/58).

Three of the 14 modules have no terms table at all — **01, 02, and 04** — so there was nothing
to audit for them. Worth raising with the authors: modules 02 and 04 are dense with vocabulary
(persona, few-shot, structured output; rubric, vibe check, judge, disagreement), and a table
there would give the slides the same anchor the other eleven have.

Fixes made (all minimal — every slide already taught the concept, it just used different
wording than the README):

| Module | Term | Fix |
|---|---|---|
| 05 | Chain | `D1-M05-C2A` now closes with the README's own definition: question → retriever → prompt → model → text, in one call |
| 07 | **Agentic RAG**, **DCI** | `D2-M07-C1`'s comparison table said "Retriever" and "Direct corpus". The module's whole identity is DCI vs Agentic RAG — it is the notebook's filename — so both are now named |
| 07 | Wiki | `D2-M07-C2` showed a page index without calling it the wiki |
| 08 | Datasheet | added to the curation slide `D2-M08-C5`, which is where the artifact is produced |
| 10 | **Root set** | genuinely absent from all five decks. `D3-M10-C3`'s first bullet already described it ("protect instructions and recent turns") and now names it |
| 18 | Input/Output guardrail, **Fail closed** | `D4-M18-C1` said "input checks"/"output checks" and never contrasted fail-closed with fail-open. Both fixed with the README's wording |

Method note: an early pass over-reported 16 gaps by matching whole phrases. Excluding SVG
internals (whose `aria-label` text created false hits) and matching each term's distinctive
head-word brought the real count to 7. Only **Root set** and **Fail closed** (on day 4) were
absent outright; the rest were present under different words.

## Memory taxonomy + schedule check (2026-09-17)

**"Periodic memory" is not a memory type**, and the repo already treats it correctly. The word
appears nowhere in module 10; what a scheduled consolidation policy does is what this module
calls **compaction** (17 mentions across its README and notebook).

The module teaches **three kinds** — episodic, semantic, working — per its notebook name
`Three_Kinds_of_Memory.ipynb`. **Procedural** is present in the code as the instructions tier
of the token budget (`cell#21`: `"procedural (instructions)"`, `"semantic (recalled)"`,
`"episodic (summary)"`, `"working (recent turns)"`), so `D3-M10-C2`'s four-row table is
accurate to the code.

Open authoring question for the module owners (not fixed — module is read-only): a cleaner
split is **episodic / semantic / procedural** by *content*, with **working memory** being a
*lifetime* (turn-local) rather than a content type — since working memory holds a mix of the
other three for one turn. The README treats working as a third peer type. Decision taken for
the slides: **follow the code**, and carry the distinction in `D3-M10-C2`'s speaker notes so an
instructor can address it if the room raises it.

**Schedule verified against the authoritative module list.** All 14 selected modules appear on
their scheduled day with the scheduled instructor, no unselected module (12, 14, 15, 16, 19–23)
appears in any deck, and every module is within its time budget:

M01 30/30 · M02 19/30 · M03 21/35 · M04 19/30 · M05 17/30 · M06 15/35 · M07 15/30 · M08 15/30 ·
M09 15/35 · M10 15/30 · M11 19/35 · M13 19/30 · M17 19/35 · M18 19/30

Note on themes: module 09 (Agent evals) is delivered on **day 3** but sits under the
"Retrieval and agent evals" theme that spans days 2–3, which is why day 2's deck title mentions
evals. Confirmed as correct; no slides moved.

## Honest status, corrected 2026-09-17

The table above previously showed 13 modules as `todo`, which understated the deck work but
overstated nothing else. The accurate position:

- **Module 01 is the only module with the full loop deliverables** — alignment file,
  companion sheet, prior-slide mapping, and a revised deck block.
- **The other 13 modules have had deck work only.** They have no
  `_loop/alignment/NN-*.md` and no `companions/NN-*.md`. Their decks were improved by the
  cross-cutting passes this session (foundation pass, repetition/instructor-name cleanup,
  README key-terms audit, agentic-system diagrams), but none has been through Steps 1–4 of
  the loop spec: full code inventory, CONCEPTS/READING_GUIDE extraction, prior-instructor
  slide mapping, or a study sheet for the instructor.
- So a future run picking up module 02 should **not** assume its deck is aligned; it should
  run the full spec and expect to find more than the cross-cutting passes caught.

What the cross-cutting passes did deliver for all 14 modules: zero instructor names in
projected copy, zero duplicate titles, zero boilerplate note lines, every README key term on
a slide (58/58), every module within its time budget, all cell pointers verified, and all
five decks rendering.

### Review-page generator fixed (2026-09-17)

The slide-copy-beside-notes review pages were showing raw `<svg ...>` markup as if it were
projected copy — the generator HTML-escaped every line, so diagrams appeared as walls of
source. Fixed: it now passes `<div>`/`<svg>` blocks through verbatim, renders fenced code as
styled `<pre>`, and converts markdown tables to real `<table>` elements.

**All 14 modules now have a review page** at `preview/dayN-moduleNN-review.html`, generated
from the decks, with zero escaped SVG: 13 live diagrams, 7 code blocks, 10 tables. The
generator lives in the scratchpad (not committed — it is a tool, and `preview/` is untracked
by the README's stated review scope).

## Speaker-note repair, all four days (2026-09-17)

Reviewed Day 1 slide-by-slide, found four note-quality problems, then fixed them across all
four decks. Every count is now **zero**, and projected copy is provably unchanged (slide,
title and minute totals identical to the pre-edit baseline: 87/62/42/24 slides,
122/68/72/42 minutes).

| Issue | Before | After |
|---|---|---|
| `Say:` merely restates the slide title | 69 | 0 |
| Filler `Then:` ("Use the answer to decide whether to clarify or continue") | 30 | 0 |
| `core` slides with no notebook cell pointer | 124 | 0 |
| Instructor names in note bodies ("Eli compares…", "In Beric's trace…") | 12 | 0 |

Each rewritten `Say:` now states why the point matters rather than rewording the title — e.g.
"The judge is not an authority. It is an instrument, and you calibrate it first." Each `Then:`
names the actual hand-off. Every pointer reads `Notebook:cell#N is Task N of M — <title>`,
with the task verified against the notebook; 10 initially landed on the wrong task (a
sequential-mapping artifact) and were corrected to match their slide's subject.

Day 2's `D2-F2`…`D2-F9A` are recaps of day-1 modules 04/01/05, so their pointers go into those
day-1 notebooks rather than day 2's.

**Worker note.** Four herdr workers ran this in parallel; only day 4 completed
(14 `Say:`, 4 `Then:`, 16 pointers). The other three each blocked on a self-inflicted
transcription slip — a missing `/Users` prefix, a mistyped scratchpad path, a patch string that
did not match — and the brief's no-retry rule made each fatal. The first attempt for all four
also blocked on `uv` being unable to write `~/.cache/uv` in their sandbox; the helper was
switched to plain `python3`. Days 1–3 were finished directly. For future runs: give workers a
pre-verified path list rather than asking them to compose paths, and allow one self-correction
before the BLOCKED stop.

### Review artifacts

`preview/index.html` is the entry point: a table of all 14 modules with slide count, minutes
against budget, visual count and cell-pointer coverage, linking to each module's
projected-copy-beside-notes page and to the five rendered decks.

Also fixed: the review generator had been HTML-escaping every line, so `<svg>` markup appeared
as literal text where the diagram should be. It now passes HTML/SVG through, renders fenced
code, and builds real tables. The stat tiles are derived from the deck instead of hardcoded.

## Day 1 review pass, with author changes (2026-09-17)

Reviewed Day 1 slide by slide with the author. Changes made, all verified:

- **`D1-F4` retitled** "A prototype tests your ability to answer a question" — the old
  "…tests one uncertainty" did not match its three question-bullets. Stale references in the
  facilitator script and a `Then:` hand-off were updated too.
- **"Concepts in this module" (`D1-M01-C0`) removed.** Its two `Minutes: 0` build slides
  (endpoint, three acts) were promoted to 1 minute each, so module 01 holds exactly 30.
- **Deskmate misuse fixed.** Deskmate is the worked-example *product* (an IT helpdesk agent in
  the seed), not the dev environment, so "Can Deskmate run against our own endpoint?" was
  wrong on a module-01 slide. Now: every notebook reads `OPENAI_BASE_URL`, so the same code
  runs against a cloud key, a self-hosted server, or a local model.
- **Five module transition cards added** (`D1-T01`–`T05`) at `Minutes: 0`. None existed before
  — each module simply began on a content slide. `D1-T01` sets up module 01's four pieces and
  states "No AI in this module. It is the floor the other four stand on."
- **`D1-M01-C1B` rewritten.** It had repeated the `--status` command its partner already showed
  *with real output*, then added an unrelated rule. It now names Deskmate as the seed.
- **"Paper finding:" prefix removed** from the Brown et al. slide; the citation is already on it.

### The Ask / Inspect / Decide scaffold is gone — all 40 slides

Confirmed with the author as an artifact of a misunderstood "practical check" convention
carried over from the earlier deck. Every one of the 40 slides (15 day 1, 16 day 3, 9 day 4)
now has a real title stating a takeaway plus **one concrete worked example**; the scaffold's
content moved into the Say/Ask/Watch/Then notes, where it is delivery guidance rather than
projected text. Day 1's code-bearing slides went from 12 to 27 as a result.

### Author coordination requirements — all met

1. Brown et al. (2020) stays on its own `evidence`-typed slide immediately after the few-shot
   bullet slide → `D1-M02-C2B`, verified in position.
2. Structured output now teaches the explicit chain **model output → schema validation →
   parsed arguments → function or MCP tool call** on `D1-M02-C4AB`, with a `risk_level` JSON
   example, `ProductBrief`, `response_format=ProductBrief`, `message.parsed`, and the closing
   caveat that a valid shape is not a true value.

Every code artifact on these slides was checked against the notebook rather than illustrated:
`search_charter` is a real module-03 tool, `{"name", "args"}` is the shape
`Agent_Harness:cell#18` records, and `result.choices[0].message.parsed` is the real line in
`Prompt_Patterns:cell#21`. No student artifacts or answers were fabricated.

Verification: 5 decks render, 168 cell pointers in range, no module over budget (M01 exactly
30, M02 20/30), zero instructor names in projected copy or notes, zero duplicate titles, zero
scaffold, zero filler note lines.

## Days 3 and 4 cut back for code (2026-09-17)

The author asked for days 3 and 4 to be mostly code. Every module there was carrying a
5-concept + 5-paired-example structure; the examples largely previewed what the notebook shows
live. **All 28 paired "B" slides were removed from days 3 and 4**, and each one's example was
folded into its parent concept slide's `Watch:` note so nothing was lost — an instructor can
still tell it, it just no longer occupies a slide.

| Module | Slides | Slide minutes | Minutes left for code |
|---|---|---|---|
| 09 Agent evals | 9 → 5 | 15 → 8 | 27 of 35 |
| 10 Agent memory | 9 → 5 | 15 → 8 | 22 of 30 |
| 11 Agent architecture | 11 → 6 | 19 → 10 | 25 of 35 |
| 13 Guardrails 101 | 11 → 6 | 19 → 10 | 20 of 30 |
| 17 Deep research | 11 → 6 | 19 → 10 | 25 of 35 |
| 18 Off-the-shelf guardrails | 11 → 6 | 19 → 10 | 20 of 30 |

All three SVG diagrams on those days survived the cut (the five-rung guardrail ladder, the six
capability mechanisms, and guardrail placement). 10 duplicated cell pointers created by the
merge were de-duplicated.

Also this pass:

- **Removed** "Today walks Deskmate from dev → prompt → agents → RAG once…" from `D1-F0` at
  the author's request.
- **Toolformer takeaway corrected.** The author's reading is the accurate one and mine was
  vague: the paper's contribution is a *self-supervised* pass that keeps only API calls which
  measurably help, so **format familiarity is a reliability property**. The slide now says so
  and draws the practical conclusion — `bash` is the tool every model can already call — with
  a pointer to `Six_Ways:cell#24`, module 11's code-mode task, where a model writes a program a
  runtime executes. Verified against the arXiv abstract for 2302.04761.
- **Six more `Say:` echoes found and fixed** (3 on day 2, 3 on day 4). My earlier check compared
  the `Say:` line to the full title and so missed slides whose titles carry a `NN · ` module
  prefix. The check is now prefix-aware; all decks are at zero.

The review index now shows a **"min for code"** column so the balance is visible at a glance.

### Rendering bug: indented SVG was being code-blocked (2026-09-17)

The author reported the `D1-M03-C0` evolution diagram rendering as a grey box with its own
markup spilling out as prose. The deck source was fine; the cause was **indentation**. Markdown
treats a line indented four or more spaces as a code block, so partway through each inline
`<svg>` Marp stopped passing HTML through and began escaping it into `<pre>`. The result: the
first few shapes drew, then the rest of the diagram appeared as visible source text.

This was **silently affecting every deck**, not just the reported slide — 231 indented SVG
lines across days 1–4. All are now de-indented, and the rendered output has **zero** escaped
`<rect>`/`<text>`/`<path>` fragments on any deck. The diagrams themselves are unchanged and
verified intact (the evolution diagram still has its 4 boxes, 17 labels, 4 arrows and marker
defs).

The structural verifier now includes check **2b**, which fails if any line inside an `<svg>`
carries leading whitespace, so this cannot regress.

Also this pass, at the author's request:

- `D1-M02-C6`: removed "Deskmate can spend more effort on Priya's VPN question—but measure the
  cost", which restated the blockquote above it. The blockquote now reads "**Reasoning is token
  spend.** More effort costs more tokens and more time," and the `Ask:` note no longer ties the
  point to one scenario.
- `D1-M02-R1`: the three paper bullets are now links — Brown et al. 2020, Wei et al. 2022,
  Madaan et al. 2023. All three verified 200.

### Author review round 2 (2026-09-17)

- **`D1-M03-C4B` "One question, one safe exit" removed.** Its parent `C4` already makes the
  point and the notebook's Task 3 runs those three routes live, so the code covers it. The
  Task 3 pointer was carried into the parent's `Watch:` line. Module 03 now leaves 15 of its
  35 minutes for code.
- **`D1-M04-C1CB` rewritten.** The author could not read it — "hand score → echo baseline →
  judge → oracle ceiling" over "floor / ? / 1.0" did not explain itself, and it is **not**
  about rubrics. Retitled **"Test the agreement metric, not the judge"** and rebuilt as a
  three-row table (echo = floor, oracle = exactly 1.0, real judge = between), closing on: if
  the oracle is not 1.0, the *metric* is broken, not the judge. The notes now open by saying
  what the slide is not about.
- **Scenario asides moved off slides into notes.** `D1-M04-C1C`'s "For Deskmate, Marcus needs
  an auditable log…" moved, with the author's framing that this is what the user experiences
  in their own environment. Seven more appended asides moved the same way on `D1-M01-C0B`,
  `D1-M02-C4A`, `D1-Z1`, `D3-F1`, `D3-M11-C5`, `D3-M13-C2A`, `D3-Z1`.
  Deskmate stays in projected copy only where it **is** the content: the seed slide
  (`D1-M01-C1B`) and day 2's worked question/answer triples.

### Day 2 stops re-teaching day 1 (2026-09-17)

The author flagged "Prepare once; retrieve for each question" as a day-1 RAG recap sitting in
day 2. An audit found the whole framing block was doing that: **11 of its 13 slides re-taught
day-1 modules** — four on module 04 (evals and judges), two on module 01 (the eval record),
five on module 05 (RAG basics and the three gates). All 11 removed, **18 minutes freed**.

Day 2 now opens on its agenda and one "yesterday → today" bridge, then goes straight into
module 06. Slide time per module: 06 leaves 20 of 35 min for code, 07 leaves 15 of 30, 08
leaves 15 of 30.

Two bugs surfaced while doing it:

- **`D2-F0` had no projected copy at all** — an empty slide since the foundation pass, which
  every verification run had missed because the checks looked for *duplicate* titles, never
  *missing* ones. It now carries the day-2 agenda. The structural verifier gains check **2c**,
  which fails on any slide with empty projected copy.
- `D2-F1`'s `Say:` repeated its title; rewritten.

Also this round: all 17 day-2 question slides now project only the question (the title had
said "… · Question: …" with a `**Question:**` bullet restating it), and `D2-F5A` became a
table of the six fields a reusable eval record needs, each with what you cannot do without it.

### PowerPoint export

`scripts/marp_to_pptx.py` builds a .pptx from a Chicago deck — 91 slides for day 1, each with
its speaker notes, at 16:9. Run `uv run --no-project python scripts/marp_to_pptx.py 1`.
Inline SVG diagrams are marked `[diagram — see the HTML deck]` rather than rasterised, since
that needs a browser render. The generated .pptx stays untracked, per this branch's README
scope ("HTML, PDF, PPTX … intentionally excluded").

## Day 3 and 4 review (2026-09-17)

Structure is sound after the earlier cut — modules leave 20–27 min for code, no duplicate
titles, no scaffold, every core slide cites a verified cell. Content review found three
patterns across 26 slides, all now fixed:

**1. `NN · ` title prefixes, 10 slides (day 4 only).** Every day-4 module title read
"17 · Make research inspectable". The module is already on the transition card and in the
note metadata, so the prefix was noise on screen. Day 3 never did this. Stripped.

**2. Label-style titles, 7 slides.** "Recap: …", "Research: …", "Optional research · …" name
a category instead of the takeaway — the same problem as the "Paper finding:" prefix removed
from day 1. Now e.g. "Optional: retrieved text is data, never authority" and
"The model proposes; the harness decides".

**3. Bullet walls where the content wanted a visual.** Three worst cases rewritten:

- `D3-M09-C3` was four abstract bullets about reliability. It now shows the notebook's own
  arithmetic as a table — pass rate 0.80, **pass^3 ≈ 0.5** — retitled "80% is not what 80%
  sounds like". Verified: `Trajectory_Evals:cell#24` states exactly this, and 0.8³ = 0.512.
- `D3-M13-C1` "Guardrails sit at choke points" had no choke points on it. It now carries an
  SVG showing the three — input, tool boundary, output — around the loop.
- `D3-M11-C3` enumerated tool/skill/MCP/sub-agent/code-mode/manifest in prose, then `C5`'s
  diagram showed the same six. C3 is now "Choose a mechanism by who owns it", a four-row
  table of the questions that decide it, so the pair is one idea told once.

Day 3 visual mix went from 2 SVG / 2 tables to **3 SVG / 5 tables**.
