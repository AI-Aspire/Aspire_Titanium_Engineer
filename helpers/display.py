"""Display helpers shared across the notebooks."""
import html
import time

from IPython.display import display, Markdown, HTML

from helpers.ui import _Handle   # tolerates having no Jupyter frontend (marimo, a script)


def show(text: str) -> None:
    """Render a string as Markdown in the notebook."""
    display(Markdown(text))


def _chunk_parts(chunk):
    """Pull ``(reasoning, content)`` out of one streamed chunk.

    Handles the shapes we stream from:
      - a plain ``str`` (LangChain ``chain.stream(...)`` ending in StrOutputParser),
      - an OpenAI / LiteLLM streaming chunk (``chunk.choices[0].delta``), where a
        reasoning model puts its thinking on ``delta.reasoning`` (OpenAI-style) or
        ``delta.reasoning_content`` (vLLM / DeepSeek-style) and the answer on
        ``delta.content``,
      - a LangChain message chunk (``chunk.content``, reasoning in additional_kwargs).
    Either half may be "" for a given chunk.
    """
    if chunk is None:
        return "", ""
    if isinstance(chunk, str):
        return "", chunk
    choices = getattr(chunk, "choices", None)
    if choices:
        delta = getattr(choices[0], "delta", None)
        if delta is not None:
            content = getattr(delta, "content", "") or ""
            reasoning = (getattr(delta, "reasoning", None)
                         or getattr(delta, "reasoning_content", None) or "")
            return reasoning, content
    content = getattr(chunk, "content", None)
    if isinstance(content, str):
        extra = getattr(chunk, "additional_kwargs", None) or {}
        return extra.get("reasoning_content", "") or "", content
    return "", ""


def _dim(text: str) -> str:
    """Dim, italic, whitespace-preserving HTML — used for the live reasoning trace."""
    return (
        '<div style="opacity:0.55;font-style:italic;white-space:pre-wrap;'
        f'margin-bottom:0.4em">{html.escape(text)}</div>'
    )


def stream_md(stream, *, min_interval: float = 0.08, show_reasoning: bool = True) -> str:
    """Live-render a token stream as Markdown and return the visible answer text.

    Drop-in for the OpenAI client (``stream=True``), LiteLLM (``stream=True``), and
    LangChain ``chain.stream(...)``. Uses display handles (not ``clear_output``) so
    several streamed answers can share one cell without erasing each other, and
    redraws are throttled to stay smooth over a remote / SSH-tunnelled kernel.

    For reasoning models the chain-of-thought streams *as it happens* in a dim italic
    block above the answer, then is wiped the moment the stream ends — so you watch it
    think live, but the saved notebook keeps only the answer.
    """
    reason_handle = _Handle(HTML("")) if show_reasoning else None
    answer_handle = _Handle(Markdown(""))
    full, reasoning, last = "", "", 0.0
    for chunk in stream:
        r, c = _chunk_parts(chunk)
        if r and reason_handle is not None:
            reasoning += r
        if c:
            full += c
        now = time.monotonic()
        if now - last >= min_interval:
            if reason_handle is not None and reasoning:
                reason_handle.update(HTML(_dim(reasoning)))
            answer_handle.update(Markdown(full))
            last = now
    if reason_handle is not None:
        reason_handle.update(HTML(""))          # wipe the thinking trace on finish
    answer_handle.update(Markdown(full or "_(no output)_"))
    return full


def stream_chat(stream, *, show_reasoning: bool = True, min_interval: float = 0.08) -> dict:
    """Live-render an OpenAI / LiteLLM chat-*completion* stream AND assemble tool calls.

    Like :func:`stream_md` — reasoning streams dim and italic then is wiped, content
    renders as Markdown — but built for agent turns: it also accumulates the streamed
    ``delta.tool_calls`` fragments and hands them back. Returns
    ``{"content": str, "tool_calls": [<openai-shaped dicts>]}``; ``tool_calls`` is empty
    on a plain answer turn. (``stream_md`` returns only text, which a tool-calling loop
    can't act on.)
    """
    reason_handle = _Handle(HTML("")) if show_reasoning else None
    answer_handle = _Handle(Markdown(""))
    content, reasoning, last = "", "", 0.0
    calls: dict = {}                         # delta index -> {"id","name","args"}
    for chunk in stream:
        r, c = _chunk_parts(chunk)
        if r and reason_handle is not None:
            reasoning += r
        if c:
            content += c
        choices = getattr(chunk, "choices", None)
        delta = getattr(choices[0], "delta", None) if choices else None
        for tc in (getattr(delta, "tool_calls", None) or []):
            slot = calls.setdefault(getattr(tc, "index", 0), {"id": "", "name": "", "args": ""})
            if getattr(tc, "id", None):
                slot["id"] = tc.id
            fn = getattr(tc, "function", None)
            if fn is not None:
                if getattr(fn, "name", None):
                    slot["name"] = fn.name
                if getattr(fn, "arguments", None):
                    slot["args"] += fn.arguments
        now = time.monotonic()
        if now - last >= min_interval:
            if reason_handle is not None and reasoning:
                reason_handle.update(HTML(_dim(reasoning)))
            if content:
                answer_handle.update(Markdown(content))
            last = now
    if reason_handle is not None:
        reason_handle.update(HTML(""))          # wipe the thinking trace on finish
    answer_handle.update(Markdown(content or ""))
    tool_calls = [{"id": v["id"] or f"call_{i}", "type": "function",
                   "function": {"name": v["name"], "arguments": v["args"] or "{}"}}
                  for i, v in sorted(calls.items())]
    return {"content": content, "tool_calls": tool_calls}


def _to_openai_messages(prompt_value):
    """A LangChain PromptValue / message list -> OpenAI chat-message dicts."""
    messages = prompt_value.to_messages() if hasattr(prompt_value, "to_messages") else prompt_value
    role = {"human": "user", "ai": "assistant", "system": "system", "tool": "tool"}
    return [{"role": role.get(getattr(m, "type", "human"), "user"), "content": m.content}
            for m in messages]


def stream_lc(prompt_value, llm, *, show_reasoning: bool = True, **create_kw) -> str:
    """Stream a LangChain chat model through its *own* underlying OpenAI client.

    LangChain's ``ChatOpenAI`` silently drops a reasoning model's chain-of-thought (it
    only forwards ``delta.content``), so ``chain.stream(...)`` shows nothing while the
    model thinks — which on a big-context prompt can be minutes of apparent silence.
    This reuses ``llm.root_client`` (same endpoint, key, model, temperature — no second
    client, no token cap) so the reasoning is visible: it streams dim and italic above
    the answer and is wiped on finish, the way the from-scratch notebooks do. The answer
    content streams just as it did before. Returns the answer text.

    Pipe your chain *up to the prompt* and pass its output here:

        build = {"context": ... | retriever | format_docs, "question": ...} | prompt
        stream_lc(build.invoke({"question": q}), llm)
    """
    stream = llm.root_client.chat.completions.create(
        model=llm.model_name,
        messages=_to_openai_messages(prompt_value),
        stream=True,
        temperature=llm.temperature,
        **create_kw,
    )
    return stream_md(stream, show_reasoning=show_reasoning)
