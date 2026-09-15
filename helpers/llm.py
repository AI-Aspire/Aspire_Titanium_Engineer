"""One place that builds model clients.

Every notebook used to construct its own client and repeat the same timeout and
retry numbers. They live in `.env` now (see `helpers.config`), and these
functions are the only thing that reads them.

    from helpers import llm
    model = llm.chat_model()            # LangChain ChatOpenAI
    text  = llm.chat("one sentence on retrieval")
    vecs  = llm.embed(["a", "b"])       # (n, d) float32, L2-normalised

Every function takes keyword overrides, so a notebook that genuinely needs a
different temperature for one call says so at the call site:

    llm.chat(prompt, temperature=0)

Heavy imports sit inside the functions, so importing this module is cheap and a
missing extra fails at the call with a message naming what to install.
"""
from __future__ import annotations

import functools

from helpers import config as C

# A server that does not know `reasoning_effort` rejects the whole call. We try
# once with it, remember the refusal, and never send it again in this session.
_REASONING_OK: dict[str, bool] = {}
_REFUSAL = ("reasoning_effort", "unrecognized", "unknown", "unsupported",
            "unexpected keyword", "extra fields", "not permitted", "invalid_request")


def _looks_like_param_refusal(err: Exception) -> bool:
    msg = str(err).lower()
    return "reasoning" in msg and any(s in msg for s in _REFUSAL)


def _sampling(temperature: float | None, max_tokens: int | None,
              reasoning: str | None) -> dict:
    """The tuning to send, leaving out anything unset."""
    out: dict = {}
    t = C.LLM_TEMPERATURE if temperature is ... else temperature
    if t is not None:
        out["temperature"] = t
    m = C.LLM_MAX_TOKENS if max_tokens is ... else max_tokens
    if m:
        out["max_tokens"] = m
    r = C.LLM_REASONING_EFFORT if reasoning is ... else reasoning
    if r:
        out["reasoning_effort"] = r
    return out


# ── raw OpenAI client ────────────────────────────────────────────────────────

def _is_apim(base: str | None) -> bool:
    """The APIM gateway needs ?subscription-key= on every call and deployment-scoped URLs."""
    return bool(base and "azure-api.net" in base)


def _apim_chat_base(base: str, model: str) -> str:
    """APIM's chat endpoint lives at /deployments/{model}, not the plain root."""
    return f"{base.rstrip('/')}/deployments/{model}"


@functools.lru_cache(maxsize=8)
def client(*, base_url: str | None = None, model: str | None = None,
           timeout: float | None = None, max_retries: int | None = None):
    """A configured `openai.OpenAI`. Cached, so repeat calls reuse the connection.

    When `base_url` points at the Accenture APIM gateway, adds the deployment-scoped
    path and injects `?subscription-key=` as a default query param on every request
    (the SDK strips query params from `base_url`, so this is the only reliable hook).
    """
    from openai import OpenAI

    url = base_url or C.LLM_BASE
    kwargs = dict(
        api_key=C.KEY,
        base_url=url,
        timeout=C.LLM_TIMEOUT if timeout is None else timeout,
        max_retries=C.LLM_MAX_RETRIES if max_retries is None else max_retries,
    )
    if _is_apim(url):
        kwargs["base_url"] = _apim_chat_base(url, model or C.LLM_MODEL)
        kwargs["default_query"] = {"subscription-key": C.KEY}
    return OpenAI(**kwargs)


def complete(messages, *, model: str | None = None, temperature=..., max_tokens=...,
             reasoning=..., **kw):
    """One chat completion. Returns the raw response object.

    Retries once without `reasoning_effort` if the server rejects that field,
    so the same notebook runs against a model with a reasoning budget and one
    without.
    """
    model = model or C.LLM_MODEL
    c = client(model=model)
    params = {**_sampling(temperature, max_tokens, reasoning), **kw}
    if not _REASONING_OK.get(model, True):
        params.pop("reasoning_effort", None)
    try:
        resp = c.chat.completions.create(model=model, messages=messages, **params)
    except Exception as e:  # noqa: BLE001
        if "reasoning_effort" not in params or not _looks_like_param_refusal(e):
            raise
        _REASONING_OK[model] = False
        params.pop("reasoning_effort")
        resp = c.chat.completions.create(model=model, messages=messages, **params)
    else:
        _REASONING_OK.setdefault(model, True)
    return resp


def chat(prompt, *, system: str | None = None, **kw) -> str:
    """One call, text in and text out. `prompt` is a string or a message list."""
    messages = [{"role": "system", "content": system}] if system else []
    messages += [{"role": "user", "content": prompt}] if isinstance(prompt, str) else list(prompt)
    return (complete(messages, **kw).choices[0].message.content or "").strip()


def reasoning_of(resp) -> str:
    """The model's thinking, when the server returns it separately. Else ""."""
    msg = resp.choices[0].message
    for attr in ("reasoning_content", "reasoning"):
        v = getattr(msg, attr, None)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return ""


# ── LangChain ────────────────────────────────────────────────────────────────

_CHAT_CLASS = None


def _chat_class():
    """`ChatOpenAI`, minus the one field a self-hosted server may reject.

    LangChain names the messages an agent produces after the agent, and sends
    that `name` back on every later turn. The OpenAI API accepts it on any
    message; a self-hosted OpenAI-compatible server may accept it only on tool
    messages and refuse the whole request. When a base URL is set, the name
    is dropped from everything but tool messages before the call goes out.
    """
    global _CHAT_CLASS
    if _CHAT_CLASS is None:
        from langchain_openai import ChatOpenAI

        class ChatOpenAICompat(ChatOpenAI):
            def _get_request_payload(self, input_, *, stop=None, **kwargs):
                payload = super()._get_request_payload(input_, stop=stop, **kwargs)
                if self.openai_api_base:
                    for m in payload.get("messages", []):
                        if isinstance(m, dict) and m.get("role") != "tool":
                            m.pop("name", None)
                return payload

        _CHAT_CLASS = ChatOpenAICompat
    return _CHAT_CLASS


def chat_model(*, model: str | None = None, base_url: str | None = None,
               temperature=..., max_tokens=..., reasoning=..., **kw):
    """A configured `langchain_openai.ChatOpenAI`.

    This replaces the line every notebook used to repeat:
        ChatOpenAI(model=..., api_key=..., base_url=..., timeout=120, max_retries=1)

    APIM-aware: when base_url is the Accenture APIM gateway, uses the
    deployment-scoped path and injects `subscription-key` via default_query.
    """
    name = model or C.LLM_MODEL
    url = base_url or C.LLM_BASE
    params = _sampling(temperature, max_tokens, reasoning)
    if not _REASONING_OK.get(name, True):
        params.pop("reasoning_effort", None)
    extra: dict = {}
    if _is_apim(url):
        url = _apim_chat_base(url, name)
        extra["default_query"] = {"subscription-key": C.KEY}
    return _chat_class()(
        model=name, api_key=C.KEY, base_url=url,
        timeout=C.LLM_TIMEOUT, max_retries=C.LLM_MAX_RETRIES,
        **params, **extra, **kw,
    )


def judge_model(**kw):
    """The scoring model: a second model when `JUDGE_MODEL` is set, pinned to a
    fixed temperature so the same answer scores the same way twice."""
    kw.setdefault("temperature", C.JUDGE_TEMPERATURE)
    return chat_model(model=C.JUDGE_MODEL, **kw)


def embeddings_model(*, model: str | None = None, base_url: str | None = None, **kw):
    """A configured `langchain_openai.OpenAIEmbeddings`.

    APIM-aware: when base_url is the Accenture APIM gateway, injects
    `subscription-key` via default_query (the SDK strips query params from base_url).
    """
    from langchain_openai import OpenAIEmbeddings

    url = base_url or C.EMBED_BASE
    extra: dict = {}
    if _is_apim(url):
        # APIM's OpenAI-compatible embeddings live at the /openai root, not any /embeddings suffix.
        if url.rstrip("/").endswith("/embeddings"):
            url = url.rstrip("/")[: -len("/embeddings")]
        extra["default_query"] = {"subscription-key": C.KEY}
    return OpenAIEmbeddings(
        model=model or C.EMBED_MODEL, api_key=C.KEY, base_url=url,
        timeout=C.EMBED_TIMEOUT, max_retries=C.LLM_MAX_RETRIES,
        check_embedding_ctx_length=False,   # a self-hosted model is not tiktoken-sized
        **extra, **kw,
    )


# ── embeddings ───────────────────────────────────────────────────────────────

def embed(texts, *, batch: int | None = None, normalise: bool = True):
    """Embed a list of strings. Returns `(n, d)` float32, L2-normalised by
    default so a dot product is cosine similarity. Held in memory only.

    APIM-aware: the SDK strips `?subscription-key=` from `base_url`, so on APIM
    we bypass the SDK and POST directly with httpx.
    """
    import numpy as np

    size = batch or C.EMBED_BATCH
    out: list[list[float]] = []
    if _is_apim(C.EMBED_BASE):
        import httpx
        root = C.EMBED_BASE.rstrip("/")
        if root.endswith("/embeddings"):
            root = root[: -len("/embeddings")]
        for i in range(0, len(texts), size):
            r = httpx.post(
                root,
                params={"subscription-key": C.KEY},
                json={"model": C.EMBED_MODEL, "input": list(texts[i:i + size])},
                timeout=C.EMBED_TIMEOUT,
            )
            r.raise_for_status()
            data = sorted(r.json()["data"], key=lambda d: d["index"])
            out.extend(d["embedding"] for d in data)
    else:
        c = client(base_url=C.EMBED_BASE, timeout=C.EMBED_TIMEOUT)
        for i in range(0, len(texts), size):
            resp = c.embeddings.create(model=C.EMBED_MODEL, input=list(texts[i:i + size]))
            out.extend(d.embedding for d in resp.data)
    arr = np.asarray(out, dtype="float32")
    if normalise and len(arr):
        arr /= (np.linalg.norm(arr, axis=1, keepdims=True) + 1e-12)
    return arr


def ready(*, embeddings: bool = False) -> str:
    """A one-line banner for a setup cell. Raises if the key is missing."""
    C.require("OPENAI_API_KEY")
    line = f"✅ {C.summary()}"
    if embeddings:
        line += f"\n✅ embeddings {C.EMBED_MODEL} at {C.EMBED_BASE or 'the same endpoint'}"
    return line


def litellm_model(model: str | None = None) -> str:
    """The model name litellm needs for the configured server.

    litellm routes by a provider prefix. A self-hosted OpenAI-compatible server
    is "openai/<name>", and a name that already carries a slash (a Hugging Face
    repo id such as "unsloth/Qwen3.6-35B") is not a provider, so the prefix is
    added unless one is already there or no base URL is set.
    """
    m = model or C.LLM_MODEL
    if m.startswith(("openai/", "anthropic/")) or not C.LLM_BASE:
        return m
    return "openai/" + m

