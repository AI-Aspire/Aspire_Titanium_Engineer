# Keys and endpoints

Everything is OpenAI-compatible. Set three values in `.env`:

| Variable | Cloud | Self-hosted or local |
|---|---|---|
| `OPENAI_API_KEY` | your key | any non-empty string |
| `OPENAI_BASE_URL` | leave blank | `http://host:port/v1` |
| `LLM_MODEL` | `gpt-4.1-mini` | the model id the server reports |

Embeddings default to the same endpoint. Set `EMBED_BASE_URL` and
`EMBED_MODEL` only if they live somewhere else.

Optional keys, each needed by one or two modules and named in that module's
README: `TAVILY_API_KEY` (web research), `COHERE_API_KEY` (reranking), the
voice services (`STT_BASE`, `TTS_BASE`).

Never commit `.env`. It is in `.gitignore`. `make scrub` removes keys from
notebook outputs, and CI fails if one gets through.
