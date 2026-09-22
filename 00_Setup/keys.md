# Keys and endpoints

Everything is OpenAI-compatible. Set three values in `.env`:

| Variable | Cloud | Self-hosted or local | Behind a gateway |
|---|---|---|---|
| `OPENAI_API_KEY` | your key | any non-empty string | as the guide says |
| `OPENAI_BASE_URL` | leave blank | `http://host:port/v1` | the gateway URL |
| `LLM_MODEL` | `gpt-4.1-mini` | the model id the server reports | the model the gateway serves |

> **Running this in a corporate environment?** Follow your cohort's setup guide
> over this file. Calls may go through an API gateway rather than straight to a
> provider, which changes three things: `OPENAI_BASE_URL` points at the gateway,
> there may be an extra subscription key to set (for example `APIM_KEY`), and the
> model names are whatever the gateway serves — not the defaults above. A VPN may
> also have to be connected before any call, which otherwise shows up as `401`
> and looks like a bad key. Get the URL, keys, and model names from the guide,
> never from a chat message.

Embeddings default to the same endpoint. Set `EMBED_BASE_URL` and
`EMBED_MODEL` only if they live somewhere else.

Optional keys, each needed by one or two modules and named in that module's
README: `TAVILY_API_KEY` (web research), `COHERE_API_KEY` (reranking), the
voice services (`STT_BASE`, `TTS_BASE`).

Two modules also need an optional **dependency group**, which is separate from
any key. `make setup-optim` installs DSPy for module 15; `make setup-graph`
installs spaCy, networkx, and rdflib for module 16. `make setup` keeps whatever
groups are already installed, but a bare `uv sync` or `uv run --group dev`
**removes** every group it does not name — which is why a notebook that worked
an hour ago can fail with `ModuleNotFoundError`. If a package is definitely
installed and the import still fails, check which Jupyter kernel is selected
before reinstalling anything.

Never commit `.env`. It is in `.gitignore`. `make scrub` removes keys from
notebook outputs, and CI fails if one gets through.
