# Prompt patterns

## Learn | Create | Grow

### Learn
Seven prompt patterns, each shown weak first: persona, few-shot, reasoning budget, structured output, pasted context, self-refine, meta-prompting. Why each one works, in one call each.

### Create
A pitch for your product refined against explicit criteria, a system prompt for your assistant written by the model, and every prompt of the session saved as your first corpus.

### Grow
Prompts in production are versioned like code, tested against a regression set, and routed by budget. Ask your team which pattern moved your task most, and whether it is written down anywhere.

**Estimated time:** 30 minutes
**Reads:** charter
**Writes:** prompts

## The patterns

| # | Pattern | What it does | Reach for it when |
|---|---|---|---|
| 1 | Persona | the system prompt sets voice and length | any user-facing feature |
| 2 | Few-shot | two labelled turns teach a convention | labels or formats the model cannot guess |
| 3 | Reasoning budget | `effort` trades tokens for care | multi-step problems with a trap |
| 4 | Structured output | a schema guarantees the shape | anything code parses |
| 5 | Pasted context | the document goes in the prompt | facts the model does not have |
| 6 | Self-refine | draft, critique against criteria, revise | quality bars you can write down |
| 7 | Meta-prompting | the model writes the prompt | recurring tasks, prompt variants |

## Before you arrive

- Write down the one question your users ask most, in their words, and what a good answer must contain; bring both.
- Self-refine: https://arxiv.org/abs/2303.17651

## Setup

```bash
make setup
uv run jupyter lab      # open 02_Prompt_Patterns/Prompt_Patterns.ipynb
```

Needs `OPENAI_API_KEY` and `LLM_MODEL` in `.env`. The reasoning-budget task degrades cleanly on models without one.

## Data files

None in this folder. The notebook reads the charter from the workspace and writes the `prompts` artifact.
