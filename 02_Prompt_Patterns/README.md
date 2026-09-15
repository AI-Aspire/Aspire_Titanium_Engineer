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

Open `Prompt_Patterns.ipynb` alongside Codex, Claude Code, VS Code Copilot, or another tool-enabled coding assistant. Paste the prompts and compare the responses. Start a new conversation before each independent example; keep the same conversation for self-refine. The reasoning exercise changes the actual reasoning-effort setting, then restores the previous setting.

The notebook is a reading guide with no executable cells. `Prompt_Patterns.py` is its generated marimo mirror.

Follow [Agent setup and controls](../docs/CODING_AGENTS.md) for environment requirements, fresh conversations, and optional product-specific controls.

## Examples

Each prompt has a collapsed recorded response. These are actual model-only OpenAI Responses API runs with `gpt-5.6-luna` (low effort, except the high-effort comparison), preserved in [recording data](data/recorded_responses.json). No tools or repository instructions were supplied; self-refine retains the preceding draft. These are reference conversations, not captures of a coding-agent interface. Your interactive responses may differ. Earlier Claude recordings remain in the versioned recording files.

## Course integration

This version does not save a `prompts` workspace artifact. Later notebooks use existing or seed prompts instead of these conversations. Conversation export is not required for this lesson.

## Tool reference for your assistant

Task 4 also demonstrates the original application-side schema contract. From this directory, run `uv run --no-sync python prompt_tools.py compare`. Students ask for the experiment in an interactive coding assistant; they do not type this command.

`prompt_tools.py` contains the original `ProductBrief` fields and `client.chat.completions.parse` call. It compares a plain JSON request with schema enforcement on the same active charter and requested fields. `--text` accepts an explicit input instead. This uses the repository's configured model/API key, independently of coding-assistant authentication. It writes no workspace artifacts.

Inspect actual validation, refusal, and finish status. A supported endpoint can enforce shape; it cannot establish factual accuracy. Both calls may succeed, and unsupported endpoints may fail. The real seed recording is `data/recorded_schema_experiment.json`. The other Python file remains the generated marimo guide.
