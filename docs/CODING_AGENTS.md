# Using a coding assistant

The conversation guides work with Codex, Claude Code, GitHub Copilot in VS Code,
or another coding assistant that can read the repository and run terminal commands.
The assistant operates the experiment tools; you inspect evidence and make decisions.

## Start here

Open the repository in your chosen assistant. Use a session with file and terminal
tools in the same environment as the shared Python dependencies. Ask it to read
`AGENTS.md` and the lesson README before running experiments. Review normal tool
approval prompts. A chat mode that only answers questions cannot run these tools.

For VS Code Copilot, use an agent-capable chat session with file and terminal tools.
See [VS Code chat](https://code.visualstudio.com/docs/agents/run/chat-view) and
[tool controls](https://code.visualstudio.com/docs/agents/run/tools).
The module README documents commands for the assistant; students send the quoted
messages instead of typing those commands themselves.

## Keep comparisons controlled

- Start a new conversation for independent comparisons. Keep the same conversation
  for a draft and its revision.
- Select a fixed model rather than automatic model routing. Keep effort, tools,
  and attached context unchanged except for the variable being tested.
- New conversations can still inherit repository instructions, memory, and editor
  context. Inspect supplied context and tool calls; a fresh chat is not proof that
  the assistant has seen no product information.

## Reasoning effort

Use the actual reasoning-effort control when available. Asking the model to
  “think harder” is a different prompt, not a verified setting change. If your
  model has no control, use a supported model for both trials or inspect the
  recorded comparison. Restore the original setting afterward.

Controls vary by product. In VS Code, supported models expose Thinking Effort in
the [model picker](https://code.visualstudio.com/docs/agent-customization/language-models#configure-thinking-effort).
Claude Code offers [conversation commands](https://code.claude.com/docs/en/commands)
and [effort controls](https://code.claude.com/docs/en/model-config#adjust-effort-level).
For Codex and other assistants, use the model and conversation controls exposed
by your installed client; the lesson does not require any particular slash command.

## Two separate models

The model chatting with you is separate from the models called by the Python
experiment tools. Those tools use the repository's `.env` configuration and API
credentials. Signing into Copilot, Codex, or Claude Code does not configure those
credentials. Keep the two model identities visible when comparing results.

Ask the assistant to execute the documented tool and show its output. Its own
file search is not a substitute for the retriever or agent loop being measured.
Save measured artifacts only when you choose; conversation exports are not required.
