# Dev environment and the daily GitHub loop

## Learn | Create | Grow

### Learn
How a change becomes a reviewed pull request: two remotes, a branch, a diff you read, a commit message a reviewer can scan. The loop every later notebook assumes.

### Create
Your workspace initialised with your charter in it, and one real pull request opened on your fork and updated with a second commit.

### Grow
In production, branch protection, required checks, and code owners enforce what you did by hand today. Take back one question: where does your AI editor save time, and where must a person decide?

**Estimated time:** 30 minutes
**Reads:** nothing
**Writes:** manifest, charter

## What you will do

| Task | What happens |
|---|---|
| 1 | Confirm `origin` is your fork and `upstream` is the course repository |
| 2 | Fetch the latest course history |
| 3 | Initialise the workspace and see which artifacts come from the seed |
| 4 | Branch for the work |
| 5 | Make a small change |
| 6 | Read the diff, commit |
| 7 | Push and open a draft pull request |
| 8 | Update the same pull request with a second commit |

## Before you start

- The GitHub CLI logged in: `gh auth login`
- A fork of the course repository, cloned: `gh repo fork <course repo> --clone`. The repository slug is in `cohort.toml`.

## Setup

```bash
make setup
uv run jupyter lab      # open 01_Dev_Environment/Dev_Environment.ipynb
```

The notebook can be run more than once. It opens the demo pull request on your own fork and the cleanup cell closes it again.

## Data files

None. The notebook writes `project/members.md` and removes it during cleanup.
