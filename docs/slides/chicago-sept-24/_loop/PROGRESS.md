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
| 02 | Prompt patterns | 1 | 30m | Eli | todo | | | |
| 03 | Agents 101 | 1 | 35m | Beric | todo | | | |
| 04 | Vibe checks and judges | 1 | 30m | Beric | todo | | | |
| 05 | RAG | 1 | 30m | Beric | todo | | | |
| 06 | Advanced retrieval | 2 | 35m | Eli | todo | | | |
| 07 | Agentic retrieval | 2 | 30m | Eli | todo | | | |
| 08 | SDG and RAGAS | 2 | 30m | Beric | todo | | | |
| 09 | Agent evals | 3 | 35m | Eli | todo | | | |
| 10 | Agent memory | 3 | 30m | Beric | todo | | | |
| 11 | Agent architecture | 3 | 35m | Rohit | todo | | | |
| 13 | Guardrails 101 | 3 | 30m | Rohit | todo | | | |
| 17 | Deep research | 4 | 35m | Eli | todo | | | |
| 18 | Off-the-shelf guardrails | 4 | 30m | Beric | todo | | | |

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
