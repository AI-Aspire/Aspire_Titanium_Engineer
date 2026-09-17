# Companion study sheet — Module 01 · Dev environment

## 1. At a glance

| | |
|---|---|
| **Module** | 01 · Dev environment (`01_Dev_Environment/`) |
| **Day** | 1 (Monday) |
| **Time** | 30 minutes |
| **Instructor** | Miriah — no-code orientation slot |
| **Deck** | `docs/slides/chicago-sept-24/day1.md`, slides `D1-M01-C0` … `D1-M01-Q1` (16 slides, ~29 min) |
| **Prerequisites** | All from `00_Setup`, done before the first morning: `gh auth login`; a fork cloned via `gh repo fork AI-Aspire/Aspire_Titanium_Engineer --clone`; `.env` copied from `.env.template`; `make setup`; `uv run python scripts/check_workspace.py --status` reading `seed` on every row. First module of the week — nothing carries over from an earlier module. |
| **Keys / cost** | **None.** This is the only Day 1 module that makes no model call and needs no API key. Zero spend. |

**Summary.** This module is not about AI. It teaches the change-delivery loop every later
notebook assumes: you work on your own fork, sync from the course repo, branch, make a
change, read your own diff, commit with a scannable message, push, open a draft pull
request from the terminal, and then push a second commit that updates the *same* pull
request. Alongside that, it initialises `workspace/` — the directory that carries the
group's artifacts through the rest of the week — and shows which artifacts currently come
from the tracked seed example. The Grow section names what production enforces by rule
instead of by hand: branch protection, required checks, `CODEOWNERS`.

You know this loop already. The teaching risk is the opposite of the usual one: not that
the material is hard, but that it is familiar enough to rush, and the two things students
will actually be hurt by later — the workspace/seed mechanic and the `uv` groups trap —
are the two least git-like parts of the slot.

## 2. What students will be able to do

1. Say which remote they push to and which they pull course updates from, and add a missing
   `upstream` themselves.
2. Fetch upstream and fast-forward `main` without clobbering local work.
3. Run the full branch → diff → commit → push → draft PR loop from the terminal with `git`
   and `gh`, on their own fork.
4. Update an open pull request with a second commit, the way they would answer a reviewer.
5. Initialise `workspace/` and read `--status` output to tell their own artifacts from
   seeded ones.
6. Diagnose the week's two most expensive environment failures: a removed `uv` group, and a
   proxy-intercepted host.

## 3. Principles

### P1 · Two remotes, two jobs
`origin` is your fork, where you push. `upstream` is the course repository, where you pull
updates from.

**Why it matters:** students have no write access to the course repo; without `upstream`
they also have no way to pick up fixes published mid-week. This is also what makes each
student's GitHub repo a Phase 3 certification deliverable — their fork is the graded object.

**Where:** `Dev_Environment.ipynb:cell#9` (the explanation), `cell#10` (the code).

**What's actually happening:** `cell#10` reads the course slug out of `cohort.toml`
(`COHORT["cohort"]["repo"]`, i.e. `AI-Aspire/Aspire_Titanium_Engineer`), regex-parses
`git remote get-url origin` to work out the student's own slug, and compares them. If
`origin` is *not* the course repo, the student is on a fork, so it adds `upstream` if
absent. If `origin` *is* the course repo — an instructor's clone, say — it prints a note and
adds nothing. The flag it sets, `on_the_fork`, is reused in `cell#13`. Go analogy: this is
the same idea as your fork's `origin` plus the canonical module path in `go.mod`.

### P2 · Sync before you build
Start the day by fetching the latest course history so you are not building on stale code.
Fetching updates your local copy of the remote branches without touching your files.

**Why it matters:** the distinction between fetch and merge is the single most common git
confusion in a room, and this cell is deliberately built around it.

**Where:** `cell#12` (explanation), `cell#13` (code).

**What's actually happening:** `cell#13` runs `git fetch <upstream|origin>`, shows the last
five commits on the course `main`, and prints `git status -sb`. It then **prints but does
not run** the fast-forward command (`git switch main && git merge --ff-only … && git push
origin main`). That is intentional: merging changes the student's working tree, so the
notebook leaves it to them. Expect a student to say "I fetched and nothing changed" — that
is the correct outcome, and it is check-your-understanding question 1's cousin.

### P3 · The workspace is the spine of the week
`workspace/` is the group's own, untracked; `data/seed/` is the tracked worked example
(Deskmate). Until the group produces an artifact, the seed carries it — and the tooling says
so out loud.

**Why it matters:** this is the mechanic most likely to bite on Thursday. Each notebook
reads what earlier ones wrote, so a skipped module leaves a hole that later notebooks
silently fill from the seed. The course's hardest rule follows from it: never hand-write a
file in `workspace/`. A plausible `judge_scores.jsonl` that no judge produced corrupts
everything downstream, and the group ends Friday defending numbers nobody measured.

**Where:** `cell#16` (explanation), `cell#17` (`ws.init()` then `ws.status()`);
`helpers/workspace.py:338` (`init`), `:359` (`status`), `:184` (`source`), `:194` (`load`).

**What's actually happening:** `ws.init()` creates the workspace tree and copies the
charter in if one exists. `ws.status()` prints one row per artifact naming where it resolves
from. On a fresh clone all 35 artifacts resolve to `seed`, with three optional ones showing
`—` (`multi_agent_report`, `voice_sessions`, `scorecard`). The fallback in `load()` is
deliberately noisy: it prints a line when it falls back, so a student who sees unfamiliar
data has a way to find out why. Infra analogy: the seed is a committed fixture set, and
`--status` is `terraform plan` for provenance.

### P4 · Branch, with a name a reviewer can scan
Keep `main` clean; do the work on a branch whose prefixed name says what it is about.

**Where:** `cell#20` (explanation), `cell#21` (code).

**What's actually happening:** `cell#21` builds `feat/{USER}-daily-loop` from the student's
GitHub login (fetched once in `cell#6` via `gh api user --jq .login`), then switches to it —
using `git switch` if the branch already exists and `git switch -c` if not. That existence
check is what makes the notebook rerunnable.

### P5 · Read your own diff — especially when an AI editor wrote it
Stage the change, then inspect exactly what will go into the commit.

**Why it matters:** this is the module's real point and the one principle the prior cohort's
deck also got right. The notebook says it plainly in `cell#23`: "This is the step where your
AI editor does most of the typing." A green run with an unreviewed diff is the failure mode.

**Where:** `cell#26` (explanation), `cell#27` (code), and the student-owned question
`cell#29` ("What would you look for in a diff before committing code an AI editor wrote for
you?").

**What's actually happening:** `cell#27` runs `git add`, then `git --no-pager diff --staged`
so the output lands in the notebook rather than a pager, then commits only if something is
actually staged — otherwise it prints that it was already committed on an earlier run.
The secrets rule lives in `00_Setup/keys.md`: `.env` is gitignored, `make scrub` strips keys
from notebook outputs, and CI fails if one gets through.

### P6 · `type: summary` commit messages
**Where:** `cell#26` (stated), `cell#27` (`docs: add {USER} to members`), `cell#34`
(`docs: note favourite step`). Pre-class exercise in `01_Dev_Environment/README.md` asks
students to bring five real commit messages marked for scannability — worth actually
collecting in the room.

### P7 · The pull request is the unit of review
`git push -u` links the local branch to the fork so later pushes know where to go;
`gh pr create --draft` opens the review without leaving the terminal.

**Where:** `cell#30` (explanation), `cell#31` (code).

**What's actually happening:** `cell#31` pushes with `-u`, then checks for an existing PR
with `gh pr list --head <branch> --json url --jq '.[0].url // empty'` before creating one —
so a rerun reuses the open PR instead of failing. It creates the PR as a **draft**, against
the student's **own fork** (`--repo {ORIGIN_SLUG} --base main`), which is why the demo is
safe to run repeatedly and safe to close. `gh pr view` then prints `"isDraft": true`.

### P8 · A second commit updates the same pull request
**Why it matters:** this is how you answer a reviewer, and it is the one non-obvious fact
about pull requests for people who have only ever opened them in a web UI.

**Where:** `cell#33` (explanation), `cell#34` (code). `cell#34` commits again, pushes, and
prints `git rev-list --count main..<branch>` — expect `2`. One pull request, two commits.

### P9 · The notebook is rerunnable, and cleans up after itself
**Where:** guards in `cell#21` (branch already exists → `switch` not `switch -c`), `cell#24`
(`if USER not in existing`), `cell#27` (commit only if something is staged), `cell#31` (reuse
an open PR rather than creating a second); cleanup in `cell#38` (explanation) and `cell#39`
(code: `git switch main`, `gh pr close --delete-branch`, `git branch -D`,
`git push origin --delete`, `members.unlink(missing_ok=True)`, all with `check=False` so
cleanup never raises).

**One cell is not guarded.** `cell#34` appends its "favourite step" line *unconditionally*:

```python
members.write_text(members.read_text(...) + "  favourite step: ...\n", ...)
```

So if a student reruns the Create section **without** running cleanup, the line is appended
again, and the `git rev-list --count main..<branch>` at the end of `cell#34` prints 3 or more
instead of 2. Harmless, but it makes check-your-understanding question 3 look wrong. If
someone's count is not 2, ask whether they reran without cleanup — that is the cause, and it
is worth knowing before it happens in front of the room.

**Teaching note:** say out loud that cleanup closes the demo PR, because a student who wants
to keep theirs open as evidence should skip that cell. On real work you would merge instead —
the notebook says so in `cell#38`.

### P10 · Production enforces by rule what you did by hand
**Where:** `cell#41` (the comparison table), `cell#42` (branch protection, required checks,
`CODEOWNERS`), `cell#43` (stretch: `gh pr review --approve`, `gh pr checks`,
`gh pr merge --squash --delete-branch`; and setting a protection rule then watching a direct
push to `main` get rejected).

### P11 · `uv` groups are exact
`uv sync` and `uv run --group dev` install exactly the groups you name and **remove** every
group you do not.

**Why it matters:** this is the highest-frequency support ticket of the week. A notebook that
worked an hour ago dies on `ModuleNotFoundError` because something ran a bare `uv sync`. The
fix is `make setup`, which detects and keeps optional groups already present.

**Where:** `00_Setup/README.md` ("One trap worth knowing"); `docs/CONCEPTS.md` ("Two setup
traps that cost the most time"); `Makefile:36` (`setup`).

### P12 · Verify the network before the room
`make preflight` checks each host the notebooks need and returns one of three verdicts.

**Where:** `00_Setup/README.md` ("Before you arrive: check the network"); `Makefile:33`.

| Verdict | Meaning |
|---|---|
| open | Host answers, public CA signed it. Nothing to do. |
| intercepted | Host answers but a private CA signed the cert — a proxy is inspecting traffic. The terminal works because the machine trusts that CA; **a container or fresh environment does not**, so keep the CA file to hand. |
| blocked | Name did not resolve or connection did not open. Get the host allowed, or bring wheels on a laptop that can reach it. |

The command exits with an error only when *every* host fails.

## 4. Code walkthrough

One notebook: `01_Dev_Environment/Dev_Environment.ipynb`, 44 cells (indices 0–43).
`Dev_Environment.py` beside it is a generated marimo mirror — never hand-edit it.
Structure: intro (0–4) → Setup (5–7) → **Learn** (8–14) → **Create** (15–37) →
Cleanup (38–39) → **Grow** (40–43).

### Setup · cells 5–7
`cell#6` is the only real machinery in the notebook. It defines `sh(cmd, check, quiet)`,
which wraps `subprocess.run(shell=True, capture_output=True)`, prints `$ cmd` followed by
stdout+stderr so students always see what ran, raises `RuntimeError` on a non-zero exit
unless `check=False`, and returns stripped stdout. Everything after this is `sh(...)` calls.
It then runs `git --version`, `gh --version | head -1`, `gh auth status`, and captures
`USER` (`gh api user --jq .login`) and `REPO_ROOT` (`git rev-parse --show-toplevel`).

**Expected output:** three version lines, an auth block, and `✅ logged in as <login>;
repository root <path>`.
**Failure mode:** not logged in → the cell raises. Fix in a terminal with `gh auth login`,
then rerun (`cell#7` says exactly this).

### Learn · Tasks 1–2 · cells 8–14
Task 1 (`cell#10`): the two-remotes logic described in P1. Prints `origin → <slug>`, adds
`upstream` if needed, then `git remote -v`. **Expected:** `origin` and, on a fork,
`upstream`, each twice (fetch and push).
Task 2 (`cell#13`): fetch, last five upstream commits, `git status -sb`, and the printed
fast-forward command. See P2.

### Create · Tasks 3–8 · cells 15–35
- **Task 3** (`cell#17`): `ws.init()`, `ws.status()`. Expected: a `✅` line naming the
  workspace path, then a table where every row says `seed` or `—`. Student-owned question
  follows at `cell#19`.
- **Task 4** (`cell#21`): switch to `feat/<login>-daily-loop`.
- **Task 5** (`cell#24`): the change itself — appends `- <login>` to `project/members.md`,
  creating the file with a `# Members` header if absent, and only if the login is not
  already present. Deliberately trivial; it is a stand-in for real work.
- **Task 6** (`cell#27`): stage, show the staged diff, commit. Student-owned question at
  `cell#29`.
- **Task 7** (`cell#31`): push `-u`, reuse-or-create a draft PR, `gh pr view`. Expected: a
  PR URL and JSON containing `"isDraft": true`.
- **Task 8** (`cell#34`): append a second line, commit, push, print the commit count.
  Expected: `✅ same pull request, now 2 commit(s) on the branch`.

### Your turn · cells 36–37
**Student-owned — do not fill this in, per `AGENTS.md`.** They edit one section of
`project/CHARTER.md` in their editor, then `cell#37` stages, commits, and pushes it (all
`check=False`, so an unedited charter does not blow up the cell). The charter matters beyond
this module: until its `<!-- template -->` marker is removed, every notebook quietly uses
the Deskmate seed instead of the group's own idea.

### Cleanup · cells 38–39
See P9.

### Grow · cells 40–43
Discussion only, nothing runs. See P10. This is where Friday's executive-panel questions
live.

## 5. Key terms

Definitions as worded in `docs/CONCEPTS.md`. All are introduced here — module 01 is first,
so nothing is inherited. Later decks should point back here rather than re-defining.

| Term | Definition (CONCEPTS.md) | Used in code |
|---|---|---|
| Two remotes | "`origin` = your fork, `upstream` = the course repo." | `cell#10` |
| The daily loop | "Branch → change → read the diff → commit → push → draft PR → second commit on the same PR." | `cell#20`–`cell#34` |
| `gh` CLI | "`gh` CLI for fork and PR from the terminal." | `cell#6`, `cell#31` |
| Workspace initialisation | "Workspace initialisation, and reading which artifacts come from the seed." | `cell#17` |
| Artifact | "one named, schema-validated output (`prompts`, `transcripts`, `eval_cases`, …)" | `helpers/workspace.py` `SCHEMA` |
| Workspace root | "`workspace/`, untracked, your group's own data" | `cell#17` |
| Seed root | "`data/seed/`, tracked, the Deskmate worked example" | `cell#17` output |
| Fallback | "`load()` returns the seed when yours is missing or invalid — **and prints a line saying so**" | `helpers/workspace.py:194` |
| Manifest | "`manifest.json` — which module wrote what, when" | README: "Writes: manifest, charter" |
| Schema | "required keys per artifact, in `helpers/workspace.py` (`SCHEMA`)" | `helpers/workspace.py` |
| Learn / Create / Grow | "Every notebook is three acts… **Learn** — the idea from scratch, weak version first… **Create** — … **This is the act that writes to the workspace**… **Grow** — what production would need; discussed, not built." | `cell#8`, `cell#15`, `cell#40` |
| `uv` groups are exact | "`uv sync` and `uv run --group dev` install exactly the groups you name and **remove** every group you do not." | `00_Setup/README.md` |
| *Grow* controls | "branch protection, required checks, code owners." | `cell#41`, `cell#42` |

## 6. Reading plan and references

**`docs/READING_GUIDE.md` has no module-01 entry.** Its Monday table is prompting and product
framing (modules 02 and the framing block). The guide's own header also says its daily
grouping is "not current schedule authority." So this module's reading comes from the module.

### Required, in order

1. **[GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)** —
   named under "Before you arrive" in `01_Dev_Environment/README.md`. *Get from it:* the
   branch → PR → review → merge cycle as GitHub names it, so the notebook's eight tasks read
   as one loop rather than eight commands.
2. **[`00_Setup/README.md`](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/00_Setup/README.md)**
   — *Get from it:* the four tools, the `.env` step, and the two commands that decide whether
   the room loses an hour: `make setup` and `make preflight`.
3. **Pre-class exercise** (no URL) — "Read the last five commit messages on a repository you
   work in and mark which ones a reviewer could scan; bring the list."

### Optional / after

- **[Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)**
  — pairs with the Grow section (P10).

### Grouped by provenance

| Group | Links |
|---|---|
| **Used by the prior instructor** | *None.* The Day 1 pptx module-01 slides (13–17) cite no sources at all, unlike its prompt-patterns slides. |
| **Linked in module** | GitHub flow (module README); [git downloads](https://git-scm.com/downloads), [GitHub CLI](https://cli.github.com), [uv install](https://docs.astral.sh/uv/getting-started/installation/), [VS Code](https://code.visualstudio.com) (all from the `00_Setup/README.md` tools table) |
| **Added by us** | Protected branches (already in our deck before this pass); `docs/CONCEPTS.md` as the vocabulary reference on the Resources slide |

## 7. Reinforcement questions with answers

### From the deck (`D1-M01-Q1`)

1. **Which remote do you push to, and which do you pull course updates from?** Push to
   `origin`, your fork. Pull from `upstream`, the course repo.
2. **You run `--status` and every row says `seed`. Is that a problem?** No. On a fresh clone
   all 35 artifacts resolve to the seed; that is what lets every notebook run standalone on
   the Deskmate worked example before the group has produced anything.
3. **You make a second commit on the branch and push. How many pull requests are open?**
   One. A pull request tracks its branch, so the new commit appears on the existing PR.
4. **A notebook that worked yesterday now fails with `ModuleNotFoundError`. What is the
   first thing you check?** Whether a bare `uv sync` or `uv run --group …` removed an
   optional group. Fix with `make setup`.
5. **Name one thing you did by hand today that production would enforce automatically.**
   Branch protection on `main`, required checks on every PR, or `CODEOWNERS` requesting the
   right reviewer.

### Deeper

6. **Why does Task 2 print the fast-forward command instead of running it?** Fetching is
   safe — it only updates remote-tracking branches. Merging rewrites the working tree, so the
   notebook leaves a deliberate decision to the student rather than moving their files under
   them.
7. **Task 7 opens the pull request against the student's own fork rather than the course
   repo. Why does that make the demo better?** It is safe to rerun and safe to close, needs
   no write access to the course repo, and does not fill the course repo with 30 demo PRs —
   while still being a real pull request on real GitHub.
8. **`cell#31` runs `gh pr list` before `gh pr create`. What breaks if you remove that
   check?** A rerun would attempt to create a second PR for the same branch and fail; the
   check is what makes the notebook idempotent (P9).
9. **Why is hand-writing a file in `workspace/` worse than leaving it missing?** Missing is
   honest: `load()` falls back to the seed and prints that it did. A fabricated artifact is
   silent, propagates through every downstream notebook, and ends with the group defending
   numbers nobody measured. `manifest.json` also records which module wrote what and when,
   so a reviewer can see the gap.
10. **A student's `make preflight` reports `intercepted` for the model endpoint and
    everything works in their terminal. Is there anything to do?** Yes. A private CA signed
    the cert, and their machine trusts it, but a container or fresh environment will not.
    They should keep the CA file to hand and note which variables the preflight table lists.
11. **Where does the charter matter beyond this module?** Every notebook reads it. Until its
    `<!-- template -->` line is removed, the notebooks quietly use the Deskmate seed instead
    of the group's own idea — so a group can get to Wednesday wondering why nothing reflects
    their problem.

## 8. Likely student questions and gotchas

**Environment and keys**
- *"Do I need an API key for this?"* No. This is the only Day 1 module with no model call.
  Keys matter from module 02 on; if theirs is missing, fix it now during this slot.
- `gh auth status` not logged in → `cell#6` raises. `gh auth login` in a terminal, rerun.
- `ModuleNotFoundError` on any helper import → the venv is empty or a group was removed →
  `make setup`. If `uv run --no-sync` created an empty `.venv`, this is the cause.
- *"The kernel cannot find `helpers`."* Start the notebook from inside its module folder;
  `helpers` is an installed package, so re-run `make setup` if it persists.

**Git and GitHub**
- `git fetch` permission error → the `upstream` URL is wrong (`cell#14` calls this out).
- `git switch` refuses → uncommitted changes; commit or stash first (`cell#22`).
- Push rejected → the fork's `main` may need the Task 2 fast-forward first (`cell#32`).
- *"`origin` is the course repo, not a fork."* An instructor-style clone. `cell#10` handles
  it: prints a note, adds no `upstream`, and Task 2 syncs from `origin` instead.
- *"I don't want the cleanup cell to close my PR."* Then skip `cell#39`. Worth saying aloud.

**Platform**
- Windows: Git Bash or WSL 2 required — every README command is POSIX. Long paths need a
  one-time registry change. Console encoding: `chcp 65001`.
- Intel Mac: older pins (`torch<2.3`, `transformers<5`, `onnxruntime<1.24`, `numpy<2`) are
  applied automatically; if a wheel still fails, `uv sync --group dev --reinstall`, and
  failing that use the cloud key rather than local models for the week.
- `Storage folder … already accessed by another instance` → embedded Qdrant is
  single-writer; restart the other kernel. (Bites later modules, not this one.)

**Conceptual confusions worth pre-empting**
- **Committing ≠ reviewing.** Deck question 4's whole point.
- **Fetch ≠ merge.** See Q6 above.
- **`check-day` failing on everything is normal.** It validates *your* `workspace/` and
  ignores the seed. On a fresh clone `D=1` reports 9 problems, `D=2` 18, `D=3` 24, `D=4` 33 —
  all "missing", all expected. `--status` is the more useful command day to day.
- **`workspace/` is untracked.** Students expect their work to be in git by default. It is
  not; artifacts are committed deliberately where the repo permits.
- **Schedule drift.** `helpers/workspace.py`'s `DAYS` map follows the repo's day numbering,
  not the cohort agenda, so `D=1` asks for module 04 and 05 artifacts the group will not
  produce until Tuesday. Read it as a checklist, not a gate.

## 9. Prior slides → module mapping (condensed)

Full version: `_loop/alignment/01-dev-environment.md`.

| Prior slide | Principle | Module evidence | Match |
|---|---|---|---|
| Day1.pptx #13 "Dev Environment (Miriah)" — divider, body is placeholder `text,,,` | — | — | none |
| Day1.pptx #14 "Your Environment is a Shared Workbench" + `workbench_context.json` mock | near P3 | `cell#17` | partial — right instinct, invented file, wrong vocabulary |
| Day1.pptx #15 "The Repo Keeps a History of the Work" | P5, P6 | `cell#26`, `cell#27` | partial |
| Day1.pptx #16 "A Small Change Should Have a Clear History" | P4, P5, P6 | `cell#20`–`cell#27` | partial |
| Day1.pptx #17 "Review the Change, Not Just the Successful Run" + leaked-key diff | P5 | `cell#26`, `cell#27`, `cell#29`, `00_Setup/keys.md` | **exact** — best slide in the prior set; example carried forward |
| Session01 #46 "Dev Env Check & GitHub Walkthrough — Mr Chris" | all, delivered live | whole notebook | none — title card only |

**Coverage gaps found:** eight of twelve principles had no prior slide (P1, P2, P7, P8, P9,
P10, P11, P12), consistent with Cohort 3 having delivered this as a live walkthrough from a
title card. Our revised deck adds slides for P1/P2 (`C3`), P7/P8 (`C6`), and P11/P12 (`C7`).

## 10. Open questions for Miriah

**Terminology conflicts to settle (prior slides vs. CONCEPTS.md)**

1. **"Shared workbench" vs. "workspace."** The prior deck's framing metaphor has no
   counterpart in the repo, and the repo's `workspace` has a precise meaning
   (`workspace/` yours vs. `data/seed/` tracked). I retitled the slide to use **workspace**.
   Keep the metaphor as a spoken aside, or drop it?
2. **"Saved Results" → "artifact"** and **"Dependencies & Settings" → `.env` / `uv` groups.**
   I switched to the repo's terms; the generic phrasing hid the week's most expensive trap.
3. **`workbench_context.json`** (prior slide #14) is invented — no such file exists. Removed.
   Confirm nothing downstream referenced it.
4. **"Smaller models often forget best practices when completing complex tasks"** (prior #17
   notes) has no citation and no support in the repo. I dropped the claim and kept the
   reviewable point. Do you want it back with a source?

**Missing from CONCEPTS.md** (in the code, not in the doc — reporting, not fixing)

5. **Draft pull request** — `cell#31` uses `--draft` and asserts `isDraft`; CONCEPTS.md says
   "draft PR" in the loop line but never explains draft status or why the demo uses it.
6. **`type: summary` commit convention** — taught in `cell#26`, used twice; CONCEPTS.md
   mentions commit hygiene being graded but not the convention.
7. **`git fetch` vs. fast-forward merge** — `cell#13`'s deliberate split; CONCEPTS.md's loop
   line omits the sync step entirely.
8. **Idempotent notebook + cleanup cell** — `cell#39` is a real teaching point and how the
   room reruns the demo; absent from CONCEPTS.md.
9. **`make preflight` and its open/intercepted/blocked verdicts** — in `00_Setup/README.md`
   and `Makefile:33`, but CONCEPTS.md's setup section names only `make setup` and
   `check_workspace.py`, though preflight is the one command that catches a corporate proxy
   before the room.

**Unused concepts** (in CONCEPTS.md's module-01 orbit, not exercised here)

10. `Fallback` only. The notebook never calls `load()` or `save()`, so students never see the
    seed-fallback line `load()` prints; first real use is module 02. Note that `Manifest` and
    `Schema` *are* exercised in `cell#17` even though the prose never names them — `ws.init()`
    writes `manifest.json` and records the charter, and `ws.status()` walks the `SCHEMA`
    registry. Worth naming out loud here, or leave for module 02?
11. `make check-day` and the "9 problems on D=1 is normal" expectation: Monday's wrap, not
    this slot. I put the expectation on slide `C7` because it is cheap insurance. Agree?

**READING_GUIDE gaps**

12. **No module-01 entry exists.** I built the reading slide from the module README's
    "Before you arrive" plus `00_Setup`. Should the guide gain a row, or is the module README
    the right home? (Reporting only — I did not edit the guide.)
13. READING_GUIDE's closing section lists ten titles with **no URLs**, including the
    **Concrete Idea Worksheet**, which the Day 1 framing slides cite. Our framing slides use
    an `aiaspire.ai` PDF link that predates this pass and that I could not verify from here —
    worth a check before publishing anything clickable.

**Timing and scope**

14. The revised block is 16 slides / ~29 min against a 30-minute no-code slot, with 3
    minutes on the check-your-understanding slide. If setup triage eats the room, the
    intended cut order is: `R1` (already optional, 0 min) → `C2B` → `C5B`. Confirm that
    order, and confirm `C7` (setup traps) should be protected from cuts — I treated it as
    the slot's highest-value content.
15. Prior Cohort-3 Session 02 (`RAG+Agents`) is **PNG page images with no text layer**, so it
    cannot be text-extracted. Irrelevant to module 01, but it will block later modules'
    alignment runs. Is there an original `.key`/`.pptx`/PDF-with-text somewhere?
