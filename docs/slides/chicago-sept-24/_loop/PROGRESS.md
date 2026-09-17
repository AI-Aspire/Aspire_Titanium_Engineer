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
