# Alignment — Module 01 · Dev environment

Day 1 · 30 minutes · Miriah (no-code orientation) · Deck: `day1.md`, slides `D1-M01-*`

## Step 1 — Module inventory

Source read in full: `01_Dev_Environment/README.md`, `01_Dev_Environment/Dev_Environment.ipynb`
(44 cells), plus the prerequisites in `00_Setup/{README,keys,mac,windows}.md`.
`Dev_Environment.py` is the generated marimo mirror and was not treated as separate content.

### Learning objectives (stated and structural)

From the README's Learn/Create/Grow block and the notebook's eight numbered tasks:

1. Explain how a change becomes a reviewed pull request: two remotes, a branch, a diff
   you read, a commit message a reviewer can scan.
2. Run that loop end to end against real GitHub, on your own fork.
3. Initialise the group workspace and read which artifacts currently come from the seed.
4. Update an open pull request with a second commit, the way you answer a reviewer.
5. Name what production enforces automatically that was done by hand today.

### Principles, with evidence

| # | Principle | Evidence |
|---|---|---|
| P1 | You do not push to the course repository. `origin` is your fork; `upstream` is the course repo, and Git tracks both. | `Dev_Environment.ipynb:cell#9` (statement), `cell#10` (adds `upstream` from `COHORT["cohort"]["repo"]`) |
| P2 | Start the day by fetching upstream so you are not building on stale code; fetching updates remote branches without touching your files. | `Dev_Environment.ipynb:cell#12`, `cell#13` (`git fetch`, `log --oneline -5`, prints the `--ff-only` command rather than running it) |
| P3 | The workspace is the spine of the week: every later notebook reads and writes it, and `status()` shows which artifacts still come from the seed. | `Dev_Environment.ipynb:cell#16`, `cell#17` (`ws.init()`, `ws.status()`); `helpers/workspace.py:338` (`init`), `:359` (`status`), `:184` (`source`) |
| P4 | Keep `main` clean; work on a branch whose prefixed name tells a reviewer what it is about. | `Dev_Environment.ipynb:cell#20`, `cell#21` (`feat/{USER}-daily-loop`, `git switch -c`) |
| P5 | Read your own diff before committing — especially when an AI editor did the typing. Stage, then inspect what will actually go in. | `Dev_Environment.ipynb:cell#26`, `cell#27` (`git add`, `git diff --staged`, then commit); reinforced by the question cell `cell#29` |
| P6 | Commit messages follow `type: summary` so history stays searchable. | `Dev_Environment.ipynb:cell#26` (stated), `cell#27` (`docs: add {USER} to members`), `cell#34` (`docs: note favourite step`) |
| P7 | `git push -u` links the local branch to the fork; `gh` opens a draft pull request without leaving the terminal. | `Dev_Environment.ipynb:cell#30`, `cell#31` (`push -u`, `gh pr list`, `gh pr create --draft`, then `gh pr view`) |
| P8 | A pull request keeps tracking its branch — a second commit updates the same PR. That is how you answer a reviewer. | `Dev_Environment.ipynb:cell#33`, `cell#34` (second commit, push, `rev-list --count`) |
| P9 | The loop can be rerun from a clean slate: the cells that would otherwise conflict guard themselves, and a cleanup cell closes the PR and deletes the branch. | Guards: `Dev_Environment.ipynb:cell#21` (branch exists?), `cell#24` (`if USER not in existing`), `cell#27` (anything staged?), `cell#31` (PR already open?). Cleanup: `cell#38`, `cell#39` (`gh pr close --delete-branch`, `members.unlink`). **Not** guarded: `cell#34` appends its line unconditionally, so a rerun without cleanup duplicates it and the `rev-list --count` grows past 2. |
| P10 | Production enforces by rule what was done by hand today: branch protection, required checks, `CODEOWNERS`. | `Dev_Environment.ipynb:cell#41` (comparison table), `cell#42` (responsible controls), `cell#43` (grow further) |
| P11 | `uv sync` and `uv run --group` are *exact*: they remove groups you do not name. Use the make targets. | `00_Setup/README.md` ("One trap worth knowing"); `docs/CONCEPTS.md` ("Two setup traps that cost the most time") |
| P12 | Verify the environment before the room: `make preflight` classifies each host open / intercepted / blocked. | `00_Setup/README.md` ("Before you arrive: check the network"); `Makefile:33` (`preflight`) |
| P13 | Notebook state is shared and long-range, so cells run in order; a stale kernel is the single most common cause of "it broke". | Verified cross-cell dependencies: `USER` defined `cell#6` → used `cell#21`, `24`, `27`, `31`; `BRANCH` defined `cell#21` → used `cell#31`, `34`, `37`, `39`; `on_the_fork` defined `cell#10` → used `cell#13`; `ORIGIN_SLUG` defined `cell#10` → used `cell#31`, `39`. Floor row in `docs/CONCEPTS.md:83` ("half of all 'it broke' is stale kernel state \| all"). |
| P14 | Every command runs through one helper that prints what it ran, so a student can always separate a git error from a notebook bug. | `Dev_Environment.ipynb:cell#6` (`sh()` wraps `subprocess.run`, prints `$ cmd` plus stdout+stderr, raises on non-zero unless `check=False`); every later code cell calls it. Also the first hard stop: `cell#6` raises when `gh auth status` fails. |

### Libraries, models, services

No LLM call and no API key in this module — the only module on Day 1 that needs neither.
Uses `git`, GitHub CLI (`gh`), `uv`, Jupyter; Python stdlib `re`, `subprocess`, `pathlib`;
repo-local `helpers.config` (`COHORT`, `ROOT`) and `helpers.workspace`. No versions pinned
in the notebook. `gh` commands used: `auth status`, `api user`, `pr list`, `pr create`,
`pr view`, `pr close`.

### External references found in the module

| Link | Where it appears |
|---|---|
| https://docs.github.com/en/get-started/using-github/github-flow | `01_Dev_Environment/README.md`, "Before you arrive" |
| https://git-scm.com/downloads | `00_Setup/README.md` tools table |
| https://cli.github.com | `00_Setup/README.md` tools table |
| https://docs.astral.sh/uv/getting-started/installation/ | `00_Setup/README.md` tools table |
| https://code.visualstudio.com | `00_Setup/README.md` tools table |

### Hands-on activities (what students actually type)

`make setup`; `uv run jupyter lab`; then run cells 6–39 in order, which execute
`git remote add upstream`, `git fetch`, `git switch -c`, `git add`, `git diff --staged`,
`git commit`, `git push -u origin`, `gh pr create --draft`, a second commit and push, and
the cleanup. Students also edit `project/members.md` implicitly (the cell writes it) and,
in **Your turn** (`cell#36`, `cell#37`), fill in one section of `project/CHARTER.md`
themselves and push it. Per `AGENTS.md`, the charter and the two `❓ Question` cells
(`cell#19`, `cell#29`) belong to the student.

### Prerequisites carried in

All from `00_Setup`, done before the first morning: `gh auth login`; a fork cloned with
`gh repo fork AI-Aspire/Aspire_Titanium_Engineer --clone`; `.env` copied from
`.env.template`; `make setup`; and `uv run python scripts/check_workspace.py --status`
reading `seed` on every row. This is the first module of the week, so nothing carries over
from an earlier module.

### Where students will get stuck

- `gh auth status` not logged in — `cell#6` raises. The notebook prose says to fix it in a
  terminal and rerun (`cell#7`).
- `upstream` URL wrong → `git fetch` permission error (`cell#14` calls this out).
- `git switch` refuses because of uncommitted changes (`cell#22`).
- Push rejected because the fork's `main` needs the Task 2 fast-forward first (`cell#32`).
- Corporate proxy blocking hosts — found by `make preflight`, not by this notebook.
- `ModuleNotFoundError` from a bare `uv sync` having removed an optional group (P11).
- Windows: needs Git Bash or WSL 2, and long paths enabled (`00_Setup/windows.md`).
- Intel Mac: pinned older wheels, may need `uv sync --group dev --reinstall` (`00_Setup/mac.md`).
- Conceptual: `check-day` failing on everything is *normal* before the group saves work
  (`docs/CONCEPTS.md`, "One expectation to set now").

## Step 1b — Concepts and readings

### CONCEPTS.md entries for this module

Definitions quoted as worded in `docs/CONCEPTS.md`.

| Concept | Definition in CONCEPTS.md | Where in the code |
|---|---|---|
| Two remotes | "`origin` = your fork, `upstream` = the course repo." (§01 · Dev environment) | `cell#10` |
| The daily loop | "Branch → change → read the diff → commit → push → draft PR → second commit on the same PR." (§01) | `cell#20`–`cell#34` |
| `gh` CLI | "`gh` CLI for fork and PR from the terminal." (§01) | `cell#6`, `cell#31` |
| Workspace initialisation | "Workspace initialisation, and reading which artifacts come from the seed." (§01) | `cell#17` |
| Artifact | "one named, schema-validated output (`prompts`, `transcripts`, `eval_cases`, …)" (§2 The workspace) | `helpers/workspace.py` `SCHEMA` |
| Workspace root | "`workspace/`, untracked, your group's own data" (§2) | `cell#17` |
| Seed root | "`data/seed/`, tracked, the Deskmate worked example" (§2) | `cell#17` output |
| Fallback | "`load()` returns the seed when yours is missing or invalid — **and prints a line saying so**" (§2) | `helpers/workspace.py:194` |
| Manifest | "`manifest.json` — which module wrote what, when" (§2) | README "Writes: manifest, charter" |
| Learn / Create / Grow | "Every notebook is three acts… Learn — the idea from scratch, weak version first. Create — … **This is the act that writes to the workspace**… Grow — what production would need; discussed, not built." (§3) | `cell#8`, `cell#15`, `cell#40` |
| `uv` groups are exact | "`uv sync` and `uv run --group dev` install exactly the groups you name and **remove** every group you do not." (§Two setup traps) | `00_Setup/README.md` |
| *Grow* controls | "branch protection, required checks, code owners." (§01) | `cell#41`, `cell#42` |

Also relevant, from §Laptop setup — the floor: the row "Git: branch, diff, commit, push,
two remotes | Monday's dev-environment demo is this loop | 01" names module 01 explicitly.

### Missing from CONCEPTS

In the code but not defined in CONCEPTS.md for this module:

- **Draft pull request.** `cell#31` uses `--draft` and checks `isDraft` in the output;
  CONCEPTS.md says "draft PR" in the loop line but never says what draft status means or
  why the demo uses it.
- **`type: summary` commit convention.** Taught in `cell#26` and used in `cell#27`/`cell#34`;
  CONCEPTS.md mentions "commit hygiene as graded" but not the convention itself.
- **`git fetch` versus fast-forward merge.** `cell#13` deliberately fetches but only *prints*
  the merge command. CONCEPTS.md's loop line skips the sync step entirely.
- **Idempotent/rerunnable notebook and the cleanup cell.** `cell#39` is a real teaching point
  (and how the room reruns the demo); not in CONCEPTS.md.
- **`make preflight` and the open/intercepted/blocked verdicts.** In `00_Setup/README.md` and
  `Makefile:33`; CONCEPTS.md's setup section names `make setup` and `check_workspace.py` but
  not `preflight`, though it is the one command that finds a corporate-proxy problem early.

### Unused concepts

In CONCEPTS.md's module-01 orbit but never exercised by this notebook:

- `Fallback` only. The notebook never calls `load()` or `save()`, so students never see the
  seed-fallback line that `load()` prints; first real use is module 02.
  **`Manifest` and `Schema` are exercised**, though the notebook prose never names them:
  `ws.init()` (`cell#17`) writes `manifest.json` via `SCHEMA["manifest"].path` and calls
  `_record("charter", "01", …)` when the charter is no longer a template
  (`helpers/workspace.py:338`–`355`), and `ws.status()` iterates the `SCHEMA` registry to
  print each artifact's source (`helpers/workspace.py:359`–`364`, `SCHEMA` at `:44`). So the
  mechanic runs in front of the students under a different name — worth saying aloud rather
  than deferring.
- `make check-day D=N` and the "9 problems on D=1 is normal" expectation: important for
  Monday's wrap, not part of this notebook.
- The five-environments table (graph, optim, SDG, voice venvs): pre-work reading, nothing in
  module 01 touches it.

### READING_GUIDE entries

**`docs/READING_GUIDE.md` has no entry for module 01.** Its Monday table covers prompting
and product framing (Chain-of-thought, Self-Refine, The LLM Application Stack, Concrete Idea
Worksheet) — modules 02 and the framing block, not the dev environment. The guide's own
header also demotes itself: "This earlier reading guide remains background; its daily
grouping is not current schedule authority."

So this module's reading list comes from the module itself:

| Reading | Link | Required? | Principle supported |
|---|---|---|---|
| GitHub flow | https://docs.github.com/en/get-started/using-github/github-flow | Required — named under "Before you arrive" in `01_Dev_Environment/README.md` | P1, P4, P7 |
| Before-you-arrive exercise (not a URL) | — | Required | P6 — "Read the last five commit messages on a repository you work in and mark which ones a reviewer could scan; bring the list." |
| `00_Setup/README.md` | repo | Required (pre-work) | P11, P12 |
| GitHub protected branches | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches | Optional — **deck-added, not from the module.** It appears only in our own `D1-M01-R1` source note (predating this pass); the module README says "Reads: nothing" and names only GitHub flow. Kept because it is official docs and matches `cell#41`/`cell#42`. | P10 |

### Terms introduced here, referenced later

Module 01 is the first module, so it introduces rather than references. Terms it introduces
that later decks should point back to instead of re-teaching: **workspace**, **seed**,
**artifact**, **manifest**, **Learn/Create/Grow**, and the **two remotes / daily loop**.
The workspace mechanic in particular is re-taught in almost every later module; from module
02 on, decks should say "the workspace you initialised in module 01."

## Step 2 — Prior slides → module mapping

### Sources searched

| Source | Extracted to | Module 01 content? |
|---|---|---|
| `Titanium AI Engineer Program- Day 1.pptx` (43 slides, Cohort 4 St. Charles) | `_loop/prev-slides-text/Day1.pptx.txt` | **Yes** — slides 13–17 |
| `Titanium_Engineer_Cohort3_Session01_Intro_AgenticAI.pdf` (~100 slides) | `_loop/prev-slides-text/Session01_Intro_AgenticAI.txt` | **No teaching slides.** Slide 46 is a title card, "Dev Env Check & GitHub Walkthrough / Mr Chris"; slide 47 is a 30-minute group activity (product leader, problem statement) whose footnote reads "we are coming around to check on your dev environment setup during this time as well!" Setup was handled as floor-walking during an unrelated activity. See `Session01_Intro_AgenticAI.txt:220-236`. |
| `Titanium_Engineer_Cohort3_Session03_AgentsInPractice.pdf` | `_loop/prev-slides-text/Session03_AgentsInPractice.txt` | No |
| `Titanium_Engineer_Cohort3_Session04_AdvancedTechniques.pdf` | not extracted this run | Not expected (Day 4 material) |
| `Titanium_Engineer_Cohort3_Session02_RAG+Agents{.zip,/}` | — | **Blocked:** PNG page images only, no text layer. Irrelevant to module 01 (RAG/agents). |
| `Titanium AI Engineer Program- Day 1.txt` | — | Plain-text companion to the pptx; same content. |

Note for later runs: `pdftotext` is not installed on this machine. The PDFs were extracted
with `uv run --with pypdf`, which is slow (~90 s per deck) — the cache in
`_loop/prev-slides-text/` should be reused rather than regenerated.

### Mapping table

| Prior slide | Principle illustrated | Module evidence | Match |
|---|---|---|---|
| Day1.pptx #13 "Simple Prototyping / Dev Environment (Miriah)" — section divider, body text is the placeholder "text,,," | — | — | none (divider) |
| Day1.pptx #14 "Your Environment is a Shared Workbench": source files / dependencies & settings / saved results, plus a `workbench_context.json` mock and "with AI skills, agent files, docs… shared context are crucial" | Environment as source + settings + results; adjacent to P3 | `cell#17` (`ws.status()` shows results and their source) | partial — right instinct, but the fictional `workbench_context.json` matches nothing in the repo, and the module's real mechanic is `workspace/` vs `data/seed/` |
| Day1.pptx #15 "The Repo Keeps a History of the Work" (title only in the extract) | P5, P6 | `cell#26`, `cell#27` | partial |
| Day1.pptx #16 "A Small Change Should Have a Clear History" (title only) | P4, P5, P6 | `cell#20`–`cell#27` | partial |
| Day1.pptx #17 "Review the Change, Not Just the Successful Run": intended files and shared destinations / credentials out of history / preserve context to repeat, with a `pipeline.py` diff showing a hard-coded `sk-prod-…` key replaced by `os.getenv` | P5, and the AI-editor review point | `cell#26`, `cell#27`, question `cell#29`; secrets rule in `00_Setup/keys.md` ("Never commit `.env`… `make scrub`… CI fails if one gets through") | **exact** on the principle; the leaked-key diff is a better illustration than anything in the notebook |
| Session01 #46 "Dev Env Check & GitHub Walkthrough — Mr Chris" (plus #47, a 30-minute group activity whose footnote reads "we are coming around to check on your dev environment setup during this time as well!") | all of P1–P9, delivered live | whole notebook | none — #46 is a title card and #47 is an activity slide; neither teaches the loop. The content was live and unrecorded. |

### Prior-slide principles absent from the code

- **"AI skills, agent files, docs… shared context are crucial"** (#14). Useful context, not
  in module 01. The repo does have `AGENTS.md`/`CLAUDE.md` and `docs/skills/`, so this is a
  legitimate aside — but it belongs nearer module 11 (skills vs. tools vs. MCP) than here.
- **The `workbench_context.json` schema** (#14). Invented for the slide; no such file exists.
  Outdated/misleading — do not carry it forward.
- **"Smaller models often forget best practices when completing complex tasks"** (#17 notes).
  A claim with no evidence in the repo and no citation on the slide. Keep the reviewable
  point (read the diff your AI editor wrote) and drop the unsourced model claim.

### Code principles with no prior slide — coverage gaps

P1 (two remotes), P2 (sync upstream), P7 (push `-u` and open a draft PR from the terminal),
P8 (second commit updates the same PR), P9 (idempotent cells and cleanup), P10 (branch
protection / required checks / `CODEOWNERS`), P11 (`uv` groups are exact), P12 (`make
preflight`). Eight of twelve principles had no prior slide — consistent with the walkthrough
having been delivered live from a title card.

### Reference materials the prior instructor used

Day 1 pptx module-01 slides cite **no sources at all** (unlike its prompt-patterns slides,
which cite Wei et al. 2022, Yao et al. 2022, Brown et al. 2020). The deck's other slides cite
Concrete Idea Worksheet, Machine Learning Yearning, The LLM Application Stack, The
product-market fit framework, and Building effective agents — none apply to module 01, and
none of those five appear in READING_GUIDE with a URL except The LLM Application Stack and
the product-market fit framework.

### Terminology conflicts

| Term | Prior slides | CONCEPTS.md | Resolution |
|---|---|---|---|
| "Shared workbench" (#14) | A metaphor covering source, settings, and results together | No such term. The repo's term is **workspace**, with a precise meaning: `workspace/` (yours, untracked) vs `data/seed/` (tracked worked example) | Use **workspace**. The metaphor may stay as a spoken aside, but the slide must name the repo's term, or students will not connect it to `ws.init()`. |
| "Saved Results" (#14) | Generic | **Artifact** — "one named, schema-validated output" | Use **artifact**. |
| "Dependencies & Settings" (#14) | Generic | `.env` / `uv` groups — and the trap is that groups are *exact* | Name `.env` and `uv` groups; the generic phrasing hides the week's most expensive trap. |

## Step 3 — Deck changelog

Edited `day1.md`, the `D1-M01-*` block (was lines 312–521). The day-file structure and the
`Slide ID` / `Module` / `Instructor` / `Type` / `Minutes` / `Layout` / `Speaker notes` /
`Sources` note schema, the Marp front-matter, and the `· The practical check` paired-slide
convention are all preserved.

**Before:** 10 slides (5 concept + 5 practical-check pairs), ~17 minutes of a 30-minute
slot, covering only the workbench metaphor, repo history, clear history, and review. Four
of twelve principles touched. Speaker-note "Watch:" lines were identical boilerplate across
slides ("Inspect the named output and verify its provenance"). No concepts slide, no reading
slide, no resources slide, no check-your-understanding slide, and no pointer to a single
notebook cell.

**After:** 16 slides, ~29 minutes. Changes:

| Change | Detail |
|---|---|
| Added `D1-M01-C0` | "Concepts in this module" — terms worded from CONCEPTS.md §01 and §2. Required by the loop spec; was missing. |
| Rewrote `D1-M01-C1`/`C1B` | Retitled to name the repo's term: workspace and seed, not "shared workbench". Points at `cell#17`. Dropped the invented `workbench_context.json`. |
| Kept `D1-M01-C2`/`C2B` | "The repo keeps a history of the work" — kept, with the `spec → prompts → …` chain retained, now pointing at `ws.init()`/`ws.status()` and `manifest.json`. |
| Added `D1-M01-C3` | **New:** two remotes (P1) and sync (P2) — the module's opening idea, previously absent. Points at `cell#9`–`cell#13`. |
| Rewrote `D1-M01-C4`/`C4B` (was C3/C3B) | "A small change should have a clear history" now names the branch prefix and the `type: summary` convention, pointing at `cell#20`–`cell#27`. |
| Kept and sourced `D1-M01-C5`/`C5B` (was C4/C4B) | "Review the change, not just the successful run" — the one exact match with the prior deck. Carried forward the leaked-key example from Day1.pptx #17, now tied to `00_Setup/keys.md` and `make scrub`. Dropped the unsourced "smaller models forget best practices" claim. |
| Added `D1-M01-C6` | **New:** push `-u`, draft PR from the terminal, and a second commit updating the same PR (P7, P8). Points at `cell#30`–`cell#34`. |
| Added `D1-M01-C7` | **New:** setup traps — `uv` groups are exact, `make preflight` verdicts, and "`check-day` failing before you save work is normal" (P11, P12). This is the no-code slot's highest-value content and was entirely missing. |
| Added `D1-M01-C8` | **New, from the coverage audit:** "How to survive a notebook" — the `sh()` helper prints `$ cmd` + output, cells run in order because state is shared, read the last line and rerun that cell, and `gh auth status` is the first hard stop. Closes the three real gaps the audit found (P13, P14). `C1B` and `C2B` each gave up a minute to hold the 30-minute budget. |
| Kept `D1-M01-R1` | Optional "make review a system property" (P10), unchanged apart from a cell pointer. |
| Added `D1-M01-RD1` | "Before and after class reading" — required/optional, built from the module README's "Before you arrive" and `00_Setup`, with a note that READING_GUIDE has no module-01 entry. |
| Added `D1-M01-RS1` | "Resources" slide — verified links only. |
| Added `D1-M01-Q1` | "Check your understanding" — 5 questions. |
| Removed | The "shared workbench" framing as a *title*, and the `workbench_context.json` mock (invented, matches no repo file). Both recorded here rather than deleted silently. |

Reinforcement questions were added to every core slide's note block as an `Ask:` line, and
each slide's `Watch:` line was rewritten to say something specific to that slide instead of
the repeated boilerplate.

All links used are either in the module (`00_Setup/README.md` tools table, README's GitHub
flow link), already present and verified in our deck (protected branches), or GitHub blob
links into this repo following the existing convention. No new URLs were invented.

## Step 5 — Validation

- `marp --html` rendered `day1.md` to `_loop/build/day1.html`, exit 0, no warnings. 64 slides
  in the full day deck; the `D1-M01-*` block sums to exactly 30 `Minutes:`.
- Every `cell#N` pointer written above and in the deck was checked against a numbered dump of
  `01_Dev_Environment/Dev_Environment.ipynb` (44 cells, indices 0–43).

### Coverage audit (second pass)

Every shell command, Python construct, and Grow-section topic in the notebook was extracted
mechanically and matched against the deck's module-01 block: **34 of 34 items covered.**

Three real gaps were found and closed by adding `D1-M01-C8`:

| Gap | Why it mattered | Fix |
|---|---|---|
| Jupyter run order / stale kernel | `docs/CONCEPTS.md:83` calls it "half of all *it broke*" for **all** modules; this is the week's first notebook and nothing in Day 1 covered it. State is genuinely long-range — `BRANCH` is set in `cell#21` and still used in `cell#39`. | `C8` bullet 2 + `Ask:` note |
| `gh auth status` as the first hard stop | `cell#6` raises without it; was in the companion sheet but on no slide | `C8` bullet 4 + `Watch:` note |
| The `sh()` helper | Every command in the notebook goes through it; unexplained, students cannot tell a git error from a notebook bug | `C8` bullet 1 + `Watch:` note |

Two were judged not worth slide space and folded into existing speaker notes instead:
`git log --oneline -5` and `git status -sb` (outputs students read rather than skills they
need) now appear in `C3`'s `Watch:` line. `git rev-parse --show-toplevel` is plumbing inside
`cell#6` and is left out deliberately.

### Prerequisite audit

Of the 11 rows in `docs/CONCEPTS.md` § "Laptop setup — the floor", **five are exercised by
this notebook** (git, Jupyter kernels, `uv`, `pathlib.Path`, env vars/`.env`) and six are
not (type hints, `dataclass`, JSON/JSONL authoring, `async`/`await`, HTTP/REST/streaming) —
those arrive from module 02 on. Note that `pathlib.Path` is listed in the floor table against
modules 05/10/13 but is **first used here** (`cell#24`, `cell#34`, `cell#39`). The full
table, plus the one genuine Python hurdle (`cell#10`'s remote-slug regex, verified against
SSH, HTTPS, and `.git` forms, and its silent fallback when no match) is in the companion
sheet §1b.

### Independent review

This file and the deck edit were cross-checked by two external reviewers run in parallel
(Codex and OpenCode, read-only, against the same brief). Findings applied:

| Finding | Change |
|---|---|
| P9's "every cell is idempotent" was **false** — `cell#34` appends unconditionally | P9 rewritten to name which cells guard themselves and which does not; the duplicate-line consequence documented in the companion sheet and in slide `D1-M01-C6`'s notes |
| "Unused concepts" wrongly listed `Manifest` and `Schema` | Corrected: `ws.init()` writes `manifest.json` and `ws.status()` walks `SCHEMA`, so both run in `cell#17`; only `Fallback` is genuinely unexercised |
| Protected-branches link described as coming "from the module" | Relabelled deck-added, with the reason it was kept |
| "Title card only" over-compressed the Cohort-3 evidence | Both slide 46 (title card) and slide 47 (activity + setup-check footnote) now described, with a line reference |
| `D1-M01-R1` claimed a cell pointer it lacked | `cell#41` added to that slide's source note |

Reviewers found **no incorrect or off-by-one `cell#N` pointers** across the file, and
confirmed independently that `docs/READING_GUIDE.md` has no module-01 entry.

One reviewer finding was **not** applied: that boilerplate `Watch:` lines survive in the
deck. Those four lines (`day1.md` slides `D1-M02-C7`, `D1-M02-C8`, `D1-M05-C1`,
`D1-M05-C1B`) belong to modules 02 and 05 and are out of scope for this run — they are left
for those modules' runs. The `D1-M01-*` block contains none.
- `cohort.toml` `[cohort] repo` confirmed present, as read by `cell#10`.
- `helpers/workspace.py` `init` (line 338), `status` (359), `source` (184), `load` (194)
  confirmed present. `Makefile` targets `preflight` (33), `setup` (36), `check-day` (85)
  confirmed present.

## Open questions

Carried into the companion sheet, §10.
