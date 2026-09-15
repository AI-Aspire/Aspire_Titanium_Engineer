# Prompt patterns

## Learn | Create | Grow

### Learn
Try persona, few-shot examples, reasoning effort, requested output formats, and pasted context in an interactive coding assistant.

### Create
Refine a draft, generate and test an instruction, and apply the patterns to your own product.

### Grow
Test prompts across representative inputs and check both format and facts.

**Estimated time:** 30 minutes

## Setup

Open `Prompt_Patterns.ipynb` alongside your coding assistant. Follow the prompts and compare the responses.

The notebook is a reading guide with no executable cells. `Prompt_Patterns.py` is its generated marimo mirror.

Product documentation: [Codex](https://developers.openai.com/codex/), [Claude Code](https://code.claude.com/docs/en/overview), [VS Code Copilot](https://code.visualstudio.com/docs/agents/overview).

## Examples

Recorded examples use `gpt-5.6-luna` through the OpenAI Responses API, with no tools or repository instructions. Effort is low except for the xhigh pelican comparison. Exact conversation history and results are in [recording data](data/recorded_responses.json).

The pelican images show measured generation times, excluding rendering.

## Course integration

This lesson does not write workspace artifacts. Readers of `prompts` use existing workspace data or the seed example.

## Tool reference for your assistant

Task 4 compares requested JSON with API-enforced output structure. From this directory, run `uv run --no-sync python prompt_tools.py compare`. Students ask for the experiment in an interactive coding assistant; they do not type this command.

`prompt_tools.py` defines the `ProductBrief` fields and `client.chat.completions.parse` call. It compares a plain JSON request with schema enforcement on the same input and requested fields. Use `--text` for the supplied Deskmate paragraph; omitting it loads the active charter. This uses the repository's configured model/API key, independently of coding-assistant authentication. It writes no workspace artifacts.

Inspect actual validation, refusal, and finish status. A supported endpoint can enforce shape; it cannot establish factual accuracy. Both calls may succeed, and unsupported endpoints may fail. The recorded Deskmate run is `data/recorded_schema_experiment.json`.
