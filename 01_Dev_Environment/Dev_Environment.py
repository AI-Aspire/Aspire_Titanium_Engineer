import marimo

__generated_with = "0.24.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Dev environment and the daily GitHub loop

    Almost every change you ship goes through the same steps: sync, branch, edit, review, commit, push, open a pull request. This notebook runs that loop against real GitHub with the same commands you use every day, and it starts your group's workspace.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    How a change becomes a reviewed pull request: two remotes, a branch, a diff you read, a commit message a reviewer can scan. The loop every later notebook assumes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    Your workspace initialised with your charter in it, and one real pull request opened on your fork and updated with a second commit.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    In production, branch protection, required checks, and code owners enforce what you did by hand today. Take back one question: where does your AI editor save time, and where must a person decide?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 30 minutes
    **Reads:** nothing
    **Writes:** manifest, charter
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    Each cell runs a real `git` or `gh` command through a small helper that prints the command and its output, so you always see what ran. You need the GitHub CLI logged in.
    """)
    return


@app.cell
def _():
    import re, subprocess
    from pathlib import Path

    from helpers.config import COHORT, ROOT
    from helpers import workspace as ws

    def sh(cmd, check=True, quiet=False):
        """Run a shell command, print it and its output, return stdout."""
        r = subprocess.run(cmd, shell=True, text=True, capture_output=True)
        if not quiet:
            print(f"$ {cmd}\n{((r.stdout or '') + (r.stderr or '')).rstrip()}\n")
        if check and r.returncode != 0:
            raise RuntimeError(f"command failed ({r.returncode}): {cmd}")
        return (r.stdout or "").strip()

    sh("git --version")
    sh("gh --version | head -1")
    sh("gh auth status")
    USER = sh("gh api user --jq .login", quiet=True)
    REPO_ROOT = Path(sh("git rev-parse --show-toplevel", quiet=True))
    print(f"✅ logged in as {USER}; repository root {REPO_ROOT}")
    return COHORT, REPO_ROOT, USER, re, sh, ws


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see three version lines, an auth status block, and a ✅ line with your GitHub login. Stop here if `gh auth status` says you are not logged in: run `gh auth login` in a terminal and rerun the cell.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Learn
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 1 of 8 — Know your two remotes

    You do not push straight to the course repository. You work on your own fork and send changes back as pull requests. Git tracks both as remotes: `origin` is your fork, where you push. `upstream` is the course repository, where you pull updates from.

    The cell below adds `upstream` if it is missing. If your `origin` already is the course repository, there is nothing to add.
    """)
    return


@app.cell
def _(COHORT, re, sh):
    UPSTREAM_SLUG = COHORT["cohort"]["repo"]
    UPSTREAM_URL = f"https://github.com/{UPSTREAM_SLUG}.git"

    remotes = sh("git remote -v", quiet=True)
    origin_url = sh("git remote get-url origin", quiet=True)
    m = re.search(r"github\.com[:/]+([^/]+)/(.+?)(?:\.git)?$", origin_url)
    ORIGIN_SLUG = f"{m.group(1)}/{m.group(2)}" if m else origin_url

    on_the_fork = UPSTREAM_SLUG.lower() not in ORIGIN_SLUG.lower()
    have_upstream = any(line.split()[0] == "upstream" for line in remotes.splitlines() if line.strip())

    print(f"origin → {ORIGIN_SLUG}")
    if on_the_fork and not have_upstream:
        sh(f"git remote add upstream {UPSTREAM_URL}")
        print("✅ added the upstream remote")
    elif on_the_fork:
        print("✅ upstream already configured")
    else:
        print("ℹ origin is the course repository itself, so there is no separate upstream")
    sh("git remote -v")
    return ORIGIN_SLUG, on_the_fork


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see `origin` and, on a fork, `upstream`, each listed twice (fetch and push). Stop here if `origin` points somewhere you do not recognise.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 8 — Sync with upstream

    Start the day by fetching the latest course history so you are not building on stale code. Fetching updates your local copy of the remote branches without touching your files. The cell prints the one-line command that fast-forwards your `main`; run that yourself when you are ready.
    """)
    return


@app.cell
def _(on_the_fork, sh):
    sync_remote = "upstream" if on_the_fork else "origin"
    sh(f"git fetch {sync_remote}")
    sh(f"git log --oneline -5 {sync_remote}/main")
    sh("git status -sb")
    print("To fast-forward your main:")
    print(f"   git switch main && git merge --ff-only {sync_remote}/main && git push origin main")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the five most recent commits on the course `main` and a short status line for your branch. Stop here if the fetch fails with a permission error: your `upstream` URL is wrong.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Create
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 8 — Initialise your workspace

    The workspace is where everything your group produces this week lives. Every later notebook reads from it and writes to it. This cell creates it, copies your charter in if you have written one, and shows which artifacts currently come from the seed example.
    """)
    return


@app.cell
def _(ws):
    ws.init()
    print()
    ws.status()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line naming the workspace path, then a table where every row says `seed` or `—`. Once your group fills in `project/CHARTER.md` and removes the template marker, rerun this cell and the charter row changes to `workspace`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which artifacts does the table say come from the seed, and which one will your group replace first?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 8 — Branch for today's work

    Keep `main` clean and do your work on a branch. A clear, prefixed name tells a reviewer what it is about at a glance.
    """)
    return


@app.cell
def _(USER, sh):
    BRANCH = f"feat/{USER}-daily-loop"
    if sh(f"git branch --list {BRANCH}", quiet=True):
        sh(f"git switch {BRANCH}")
    else:
        sh(f"git switch -c {BRANCH}")
    print(f"✅ on branch {sh('git branch --show-current', quiet=True)}")
    return (BRANCH,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with the branch name. Stop here if git refuses to switch because of uncommitted changes: commit or stash them first.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5 of 8 — Make the change

    This is the step where your AI editor does most of the typing. To keep the demo small, the change is a line in `project/members.md` naming you. Treat it as a stand-in for real work.
    """)
    return


@app.cell
def _(REPO_ROOT, USER):
    members = REPO_ROOT / "project" / "members.md"
    existing = members.read_text(encoding="utf-8") if members.exists() else "# Members\n\n"
    if USER not in existing:
        existing += f"- {USER}\n"
    members.write_text(existing, encoding="utf-8")
    print(f"✅ wrote {members.relative_to(REPO_ROOT)}")
    return (members,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with the file path. Open the file and confirm your login is on its own line.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 6 of 8 — Review the diff, then commit

    Read your own diff before committing. `git add` stages the file; `git diff --staged` shows exactly what goes into the commit. Commit messages follow the `type: summary` shape so the history stays searchable.
    """)
    return


@app.cell
def _(USER, members, sh):
    sh(f"git add {members}")
    sh("git --no-pager diff --staged")
    if sh("git diff --staged --name-only", quiet=True):
        sh(f'git commit -m "docs: add {USER} to members"')
    else:
        print("Nothing staged, so it was already committed on an earlier run.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a diff with one added line and then a commit summary. Stop here if the diff shows files you did not mean to change.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    What would you look for in a diff before committing code an AI editor wrote for you?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 7 of 8 — Push and open a pull request

    The `-u` flag links your local branch to the one on your fork, so a plain `git push` knows where to go from now on. Then the GitHub CLI opens a draft pull request without leaving the terminal. It targets your own fork, so it is safe to run again and to close.
    """)
    return


@app.cell
def _(BRANCH, ORIGIN_SLUG, USER, sh):
    sh(f"git push -u origin {BRANCH}")
    existing_pr = sh(f"gh pr list --repo {ORIGIN_SLUG} --head {BRANCH} --json url --jq '.[0].url // empty'", quiet=True)
    if existing_pr:
        PR_URL = existing_pr
        print(f"pull request already open: {PR_URL}")
    else:
        PR_URL = sh(f'gh pr create --repo {ORIGIN_SLUG} --base main --head {BRANCH} --draft '
                    f'--title "docs: add {USER} to members" --body "Daily loop demo, safe to close."', quiet=True)
        print(f"✅ draft pull request opened: {PR_URL}")
    sh(f"gh pr view {BRANCH} --repo {ORIGIN_SLUG} --json url,state,isDraft")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a pull request URL and a JSON block with `"isDraft": true`. Stop here if the push is rejected: your fork's `main` may need the fast-forward from Task 2 first.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 8 of 8 — Update the open pull request

    A pull request keeps tracking its branch. Make a second commit and push it, and the same pull request picks up the change. This is how you respond when a reviewer asks for edits.
    """)
    return


@app.cell
def _(BRANCH, members, sh):
    members.write_text(members.read_text(encoding="utf-8") + f"  favourite step: opening the pull request from the terminal\n", encoding="utf-8")
    sh(f"git add {members}")
    sh('git commit -m "docs: note favourite step"', check=False)
    sh(f"git push origin {BRANCH}")
    n = sh(f"git rev-list --count main..{BRANCH}", quiet=True)
    print(f"✅ same pull request, now {n} commit(s) on the branch")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a second push and a ✅ line with a commit count of 2. Open the pull request URL and confirm both commits are listed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Fill in one section of `project/CHARTER.md` with your group, commit it on this branch, and push. Then answer: did the pull request update, and what does the diff look like to a teammate who was not in the room?
    """)
    return


@app.cell
def _(BRANCH, REPO_ROOT, sh):
    # Edit project/CHARTER.md in your editor first, then run this cell.
    charter = REPO_ROOT / "project" / "CHARTER.md"
    sh(f"git add {charter}")
    sh('git commit -m "docs: start the charter"', check=False)
    sh(f"git push origin {BRANCH}", check=False)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cleanup

    So you can run this notebook again from a clean slate, this closes the demo pull request, deletes the branch, and removes the members file. On real work you would merge instead.
    """)
    return


@app.cell
def _(BRANCH, ORIGIN_SLUG, members, sh):
    sh("git switch main", check=False)
    sh(f"gh pr close {BRANCH} --repo {ORIGIN_SLUG} --delete-branch", check=False)
    sh(f"git branch -D {BRANCH}", check=False, quiet=True)
    sh(f"git push origin --delete {BRANCH}", check=False, quiet=True)
    members.unlink(missing_ok=True)
    print("✅ cleaned up: pull request closed, branch deleted, members file removed")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Grow
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## From prototype to production

    | What we built | Production equivalent |
    |---|---|
    | Opened a pull request by hand | Templates and a `CODEOWNERS` file that request the right reviewers |
    | A branch name we agreed on | Branch protection that blocks direct pushes to `main` |
    | Read the diff ourselves | Required checks (lint, tests) that must pass before merge |
    | Synced the fork by hand | A bot that keeps forks in sync |
    | Wrote the commit message ourselves | Commit-message linting and generated changelogs |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - Branch protection on `main` so nothing merges without a review.
    - Required checks on every pull request, including the prose lint for notebooks.
    - A `CODEOWNERS` file so the right reviewer is asked automatically.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Add a `.github/pull_request_template.md` and a small action that runs the prose lint on changed notebooks, so a broken notebook cannot be merged.
    - Take a pull request from open to merged without leaving the terminal: `gh pr review --approve`, `gh pr checks`, `gh pr merge --squash --delete-branch`.
    - Set a branch protection rule that requires a review, then try to push straight to `main` and watch it get rejected.
    """)
    return


if __name__ == "__main__":
    app.run()
