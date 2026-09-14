# Style

How the notebooks and READMEs are written. `scripts/nb_lint.py` enforces the
rules that can be checked mechanically; the rule id is in brackets.

## Why these rules

The people in the room have eight hours of new material a day for five days.
Most are reading a notebook while an instructor talks and a teammate asks a
question. Prose that works in that room is short, concrete, and says what to
do next. Prose that fails is a wall of text that explains three things at once
and sounds like it was generated.

## The notebook template

Every notebook is three acts, in this order, after a short front matter.
The acts follow AI Aspire's Learn, Create, Grow model: fluency first, then
building on the group's own work, then what it takes to run in production.

Front matter:

1. `# Title` and one sentence on the problem.
2. `## Learn | Create | Grow`, then `### Learn`, `### Create`, `### Grow`,
   each at most 40 words: the idea you will understand, what you will make
   on your own artifacts, what production needs and the question to take
   back to your team.
3. `**Estimated time:** N minutes`, then `**Reads:**` and `**Writes:**` naming
   the workspace artifacts.
4. `## Setup`: one code cell that ends by printing ✅ and whether the
   workspace or the seed is live.

The acts, each an H1:

5. `# Learn`: the from-scratch tasks. Show the weak version, then the strong
   one, on the same input. Imports are earned here.
6. `# Create`: the tasks that run on the group's own artifacts and write to
   the workspace, ending in `## Your turn`, one change the group makes and
   explains.
7. `# Grow`: `## From prototype to production` (a two-column table),
   `## Responsible controls` (three bullets: what must be true before this
   runs for real), and `## Grow further` (two or three stretch prompts).

Tasks are numbered across both acts: `## Task k of N — title`, each a
markdown cell, a code cell, and a checkpoint cell. `### ❓ Question` with an
`Answer:` line after every second task. The lint checks the sections exist
and the acts are in order [K002, K003].

## Cells

- One idea per markdown cell. Aim for 120 words; 150 is the ceiling [L001,
  L002].
- The first line of a task cell is plain English: what the student is about to
  do and why, no jargon, no code font.
- A checkpoint cell starts with "You should see" and ends with "Stop here if".
  At most 60 words [L003]. It names the actual expected output.
- Anything longer than 120 words goes in a `<details><summary>` block.
- Progress is visible: the task header says `Task 3 of 7` [K001].

## Sentences

- No exclamation marks [E001].
- Sentence case for every header. Capitalise the first word and proper nouns
  only [H002]. A header never ends with a colon [H001].
- At most one bold span per cell [S001]. Bold is for the one thing to notice.
- An em dash appears only in a task header [S002]. Elsewhere, start a new
  sentence.
- Headers are words, not icons. The only emoji allowed anywhere are ✅ in
  printed output, ❓ on a question header, and ⚠️ or ℹ️ on a warning or note
  [S003].
- Second person, present tense, active voice. "Run the cell. It prints the
  score."
- Numbers are in tables or on their own line, not buried in a sentence.

## Words that mean the text was generated

These fail the lint [T001 to T028]: comprehensive, leverage, robust, best
practices, "in this notebook", "now that we", key takeaways, "let's break",
"let's dive", delve, seamless, cutting-edge, state-of-the-art, powerful, unlock,
harness the power, "it's important to note", "in today's", landscape, journey,
empower, supercharge, elevate, crucial, vital, utilize, Furthermore, Moreover,
Additionally, "in conclusion", "overall,", happy coding, welcome to,
congratulations, great job, final takeaways, deep dive, under the hood, "think
of it as", "by the end of this", game-changing, transformative.

Say the specific thing instead. "Comprehensive" becomes the list. "Robust"
becomes what it survives. "Let's dive in" becomes the first instruction.

## Standing alone

A notebook never names a day, a week, a module number, or a sibling notebook,
and never says yesterday or tomorrow [P001 to P010]. Name the artifact:
"your transcripts", "the eval cases you wrote". The day and time context lives
in `docs/schedule/`.

## Diagrams

Diagrams are SVG files in `images/diagrams/`, rendered by `make diagrams` from
graphviz sources in `images/diagrams/src/`. A notebook embeds one with
`![alt](../images/diagrams/name.svg)`. Mermaid is not used because GitHub does
not render it inside a notebook.

## Suppressing a rule

Put `<!-- lint: ignore S002 -->` in the cell. Use it rarely and say why in the
same cell.
