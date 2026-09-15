# Setup

Do this once, before the first morning. Budget 30 minutes. If something does
not work, the fix is usually in the troubleshooting section at the bottom.

## 1. Tools

| Tool | Why | Install |
|---|---|---|
| git | clone, branch, commit | https://git-scm.com/downloads |
| GitHub CLI (`gh`) | fork and open pull requests from the terminal | https://cli.github.com |
| uv | one Python environment for the whole repository | https://docs.astral.sh/uv/getting-started/installation/ |
| An editor | VS Code or Cursor, with the Jupyter extension | https://code.visualstudio.com |

Windows: use Git Bash or WSL for the commands below. See [windows.md](windows.md).
Mac: see [mac.md](mac.md) for the Intel-versus-Apple-silicon note.

## 2. Fork and clone

```bash
gh auth login
gh repo fork AI-Aspire/Aspire_Titanium_Engineer --clone
cd Aspire_Titanium_Engineer
```

## 3. Keys

```bash
cp .env.template .env
```

Open `.env` and set `OPENAI_API_KEY` and `LLM_MODEL`. Your instructor gives
you the values for the room. Everything is OpenAI-compatible, so a self-hosted
or local server works too; see [keys.md](keys.md).

## 4. Environment

```bash
make setup
uv run jupyter lab
```

The first `make setup` downloads a few gigabytes. Do it on a good connection.

## 5. Check

```bash
uv run python scripts/check_workspace.py --status
```

Every row should say `seed`. That means the notebooks will run on the worked
example until your group produces its own artifacts.

## Before you arrive: check the network

Corporate networks block or inspect some of the hosts the notebooks need.
Find out on your own desk, not in the room.

```bash
make preflight
```

One row per host, with a verdict.

| Verdict | What it means for you |
|---|---|
| open | The host answers and a public certificate authority signed it. Nothing to do. |
| intercepted | The host answers, but a private CA signed the certificate. A proxy is inspecting the traffic. The terminal works because your machine trusts that CA; a container or a fresh environment does not, so keep the CA file to hand and note which variables the table lists. |
| blocked | The name did not resolve or the connection did not open. Ask whoever runs the proxy to allow the host, or bring the wheels on a laptop that can reach it. |

The command exits with an error only when every host failed.

## Troubleshooting

- **`ModuleNotFoundError` in a notebook that worked before.** A plain `uv sync`
  removed an optional group. Run `make setup`, which keeps them.
- **`Storage folder ... already accessed by another instance`.** Two kernels
  hold the local vector store. Restart the other kernel.
- **Slow or failing wheel downloads on an Intel Mac.** See [mac.md](mac.md).
- **The kernel cannot find `helpers`.** Start the notebook from inside its
  module folder; the first cell adds the repository root to the path.

## One trap worth knowing

`uv sync` and `uv run --group <name>` are exact: they install the groups you
name and remove the ones you do not. So `uv run --group dev ...` silently
uninstalls the GraphRAG and prompt-optimisation packages, and the next notebook
that needs them fails with `ModuleNotFoundError` on a machine where it worked an
hour ago.

Use the make targets, which name every group they need:

```bash
make setup        # keeps the optional groups already installed
make setup-all    # the shared environment plus every optional group
make execute      # runs notebooks with all groups present
```
