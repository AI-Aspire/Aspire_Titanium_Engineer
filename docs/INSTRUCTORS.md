# Instructors

Per cohort, fill in the table and link it from the front page. Names go here
and nowhere else in the repository.

| Role | Name | Reach |
|---|---|---|
| Lead instructor | | |
| Instructor | | |
| Teaching assistant | | |
| Programme operations | | |

## Before the cohort

- Set `cohort.toml` and run `make banner`.
- Run `make check` and `make execute` on a clean clone with the keys the room will use.
- Run `uv run python scripts/check_workspace.py --seed` and read the seed capability report; it is what the first demo shows.
- Print `docs/schedule/day1.md`.

## Each day

- The last block is `make check-day D=N`. Nobody leaves with a red workspace.
- Collect one question per group for the next morning's feedback block.

## Day 4 and day 5

Day 4 is your pick of four modules from 14 to 23; `docs/schedule/day4.md`
says when each one earns its slot. Day 5 is optional and built from what the
cohort asks for. If it holds a demo day, the judges score with
`project/DEMO_SCORECARD.md`, each group's own harness runs in the room, and
the rows are written to the workspace as the `scorecard` artifact.
