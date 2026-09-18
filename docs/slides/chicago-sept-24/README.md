# Chicago · September 24 slide outlines

This directory is the review set for the Chicago September 24 cohort. It is
prepared for Chris and the instructional team to review the concept coverage,
speaker notes, layouts, research links, and module handoffs before anything is
transferred into Google Slides.

## Decks

One directory per day, holding the Markdown source and the rendered HTML. The
Markdown is the source of truth; the HTML is generated from it and is there so
a reviewer can page through the deck without installing anything. **Quote the
slide title, not a slide number, when giving notes** — numbering shifts as
slides are added.

| Day | Source | Rendered |
|---|---|---|
| Day 1 · Prototype and retrieve | [`day1/day1.md`](day1/day1.md) | [`day1/day1.html`](day1/day1.html) |
| Day 2 · Retrieval and agent evals | [`day2/day2.md`](day2/day2.md) | [`day2/day2.html`](day2/day2.html) |
| Day 3 · Agents in practice | [`day3/day3.md`](day3/day3.md) | [`day3/day3.html`](day3/day3.html) |
| Day 4 · Advanced prototyping | [`day4/day4.md`](day4/day4.md) | [`day4/day4.html`](day4/day4.html) |
| Day 5 · Demo day and optional modules | [`day5/day5.md`](day5/day5.md) | [`day5/day5.html`](day5/day5.html) |

Regenerate the HTML after editing any Markdown, so the two never disagree:

```bash
for n in 1 2 3 4 5; do
  marp --no-stdin --html --allow-local-files \
    -o docs/slides/chicago-sept-24/day$n/day$n.html \
       docs/slides/chicago-sept-24/day$n/day$n.md
done
uv run --no-project python scripts/marp_to_pptx.py 1 2 3 4 5   # PowerPoint, untracked
```

The day files are Marp-compatible outlines. Each slide includes concise
projected copy plus speaker notes, a named Google Slides layout template, and
relevant sources. Slides are intentionally short so instructors can explain
the idea before the related notebook walkthrough.

The [facilitator script](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/docs/slides/chicago-sept-24/facilitator-script.md) holds the detailed preparation material. Slide notes are intentionally short cue bullets so instructors can rehearse without reading a script.

## Selected module references

The module metadata in the day files links directly to the corresponding
repository README:

| Day | Module | Instructor |
| --- | --- | --- |
| 1 | [01 · Dev Environment](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/01_Dev_Environment/README.md) | Miriah |
| 1 | [02 · Prompt Patterns](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/02_Prompt_Patterns/README.md) | Eli |
| 1 | [03 · Agents 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/03_Agents_101/README.md) | Beric |
| 1 | [04 · Vibe Checks and Judges](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/04_Vibe_Checks_and_Judges/README.md) | Beric |
| 1 | [05 · RAG](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/05_RAG/README.md) | Beric |
| 2 | [06 · Advanced Retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/06_Advanced_Retrieval/README.md) | Eli |
| 2 | [07 · Agentic Retrieval](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/07_Agentic_Retrieval/README.md) | Eli |
| 2 | [08 · SDG / RAGAS](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/08_SDG_RAGAS/README.md) | Beric |
| 3 | [09 · Agent Evals](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/09_Agent_Evals/README.md) | Eli |
| 3 | [10 · Agent Memory](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/10_Agent_Memory/README.md) | Beric |
| 3 | [11 · Agent Architecture](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/11_Agent_Architecture/README.md) | Rohit |
| 3 | [13 · Guardrails 101](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/13_Guardrails_101/README.md) | Rohit |
| 4 | [17 · Deep Research](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/17_Deep_Research/README.md) | Eli |
| 4 | [18 · Off-the-Shelf Guardrails](https://github.com/AI-Aspire/Aspire_Titanium_Engineer/blob/main/18_Off_The_Shelf_Guardrails/README.md) | Beric |

## Scope of this review branch

Only the five day Markdown files and this README belong in this review. HTML,
PDF, PPTX, preview files, generated edit guides, scripts, and other working
files are intentionally excluded so the review stays focused on the teaching
content. Chris can add or revise instructor-specific information in a later
pass.
