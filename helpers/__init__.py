"""Shared helpers for the Titanium Engineer notebooks.

`helpers` is installed into the environment (see the repository's
pyproject.toml), so a notebook imports it by name from any working directory,
in Jupyter and in marimo alike. No sys.path line, and none should be added.

Every notebook starts the same way:

    from helpers import workspace as ws
    from helpers.config import LLM_MODEL, require
    from helpers.llm import chat_model

`helpers.config`, `helpers.display`, `helpers.ui`, `helpers.brand`, and
`helpers.workspace` need nothing beyond the standard library, python-dotenv,
and IPython. `helpers.judge` also needs `litellm`; `helpers.vectorstore` needs
`qdrant-client` and `langchain-qdrant` at call time.
"""
