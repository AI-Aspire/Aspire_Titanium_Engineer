# Demo app

A Streamlit starter that reads your workspace and answers questions over your
corpus with your agent. Run it from the repository root:

```bash
uv run streamlit run project/app/app.py
```

| File | What it does |
|---|---|
| `app.py` | the page: title from your charter, a sidebar listing every artifact and its source, a chat, and a "Score this demo" form that writes `scorecard` |
| `agent.py` | keyword retrieval over the corpus pages, then one chat completion that answers from those pages only |

Replace `agent.py` with the agent you built. The app needs one function:
`answer(question) -> {"answer": str, "pages": [str]}`. Keep the sidebar: the
judges use it to see which artifacts your demo draws on.
