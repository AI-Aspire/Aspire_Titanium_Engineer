"""LLM access — one OpenAI-compatible model, used as two *lanes*.

    fast lane : thinking OFF  -> low-latency conversational replies + tool calls
    deep lane : thinking ON   -> background tasks the agent delegates to itself
    judge     : thinking OFF, 1-token -> semantic end-of-turn classification

All three are the same OpenAI-compatible endpoint; the difference is purely how we call it
(`chat_template_kwargs.enable_thinking`). The stream yields typed events so the
session can forward reasoning / content / tool-call deltas straight to the browser.
"""
from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any, AsyncIterator

from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv(Path(__file__).resolve().parents[2] / ".env")
load_dotenv()

MODEL = os.getenv("LLM_MODEL", "gpt-4.1-mini")
BASE_URL = os.getenv("OPENAI_BASE_URL") or None
API_KEY = os.getenv("OPENAI_API_KEY", "EMPTY")

_IS_APIM = bool(BASE_URL and "azure-api.net" in BASE_URL)
_client_base = (f"{BASE_URL.rstrip('/')}/deployments/{MODEL}"
                if _IS_APIM else BASE_URL)
_client_extra = {"default_query": {"subscription-key": API_KEY}} if _IS_APIM else {}

client = AsyncOpenAI(base_url=_client_base, api_key=API_KEY, timeout=120, **_client_extra)


def _thinking(enabled: bool) -> dict:
    return {"chat_template_kwargs": {"enable_thinking": bool(enabled)}}


async def stream_chat(
    messages: list[dict],
    *,
    tools: list[dict] | None = None,
    thinking: bool = False,
    temperature: float = 0.7,
    max_tokens: int = 1200,
) -> AsyncIterator[dict]:
    """Stream one assistant turn.

    Yields events:
        {"type": "first_token", "ms": float}                      once
        {"type": "reasoning", "delta": str}
        {"type": "content",   "delta": str}
        {"type": "tool_calls", "calls": [{"id","name","arguments"}]}  at the end, if any
        {"type": "done", "content": str, "reasoning": str, "finish": str,
         "usage": {...}, "ms": float, "tps": float}
    """
    t0 = time.perf_counter()
    first = None
    content, reasoning = [], []
    calls: dict[int, dict] = {}
    finish = None
    usage: dict[str, Any] = {}
    kwargs: dict[str, Any] = dict(model=MODEL, messages=messages, stream=True,
                                  temperature=temperature, max_tokens=max_tokens,
                                  extra_body=_thinking(thinking),
                                  stream_options={"include_usage": True})
    if tools:
        kwargs["tools"] = tools
    stream = await client.chat.completions.create(**kwargs)
    try:
        async for chunk in stream:
            if getattr(chunk, "usage", None):
                usage = chunk.usage.model_dump()
            if not chunk.choices:
                continue
            ch = chunk.choices[0]
            d = ch.delta
            rc = getattr(d, "reasoning_content", None) or (d.model_extra or {}).get("reasoning_content")
            if rc:
                if first is None:
                    first = (time.perf_counter() - t0) * 1000
                    yield {"type": "first_token", "ms": first}
                reasoning.append(rc)
                yield {"type": "reasoning", "delta": rc}
            if d.content:
                if first is None:
                    first = (time.perf_counter() - t0) * 1000
                    yield {"type": "first_token", "ms": first}
                content.append(d.content)
                yield {"type": "content", "delta": d.content}
            for tc in d.tool_calls or []:
                slot = calls.setdefault(tc.index, {"id": tc.id or "", "name": "", "arguments": ""})
                if tc.id:
                    slot["id"] = tc.id
                if tc.function:
                    if tc.function.name:
                        slot["name"] += tc.function.name
                    if tc.function.arguments:
                        slot["arguments"] += tc.function.arguments
            if ch.finish_reason:
                finish = ch.finish_reason
    finally:
        await stream.close()
    ms = (time.perf_counter() - t0) * 1000
    if calls:
        yield {"type": "tool_calls", "calls": [calls[i] for i in sorted(calls)]}
    ctoks = usage.get("completion_tokens") or 0
    yield {"type": "done", "content": "".join(content), "reasoning": "".join(reasoning),
           "finish": finish or ("tool_calls" if calls else "stop"), "usage": usage, "ms": ms,
           "tps": (ctoks / (ms / 1000)) if ms > 0 and ctoks else 0.0}


EOT_SYSTEM = (
    "You are a turn-taking detector for a spoken conversation. You see what the user has said so far "
    "(from a speech recognizer, so there is no punctuation and words may be slightly wrong). "
    "Decide whether the user has FINISHED their turn and is waiting for a reply, or is mid-sentence / "
    "pausing to think and will continue speaking. Trailing words like 'and', 'but', 'so', 'um', an unfinished "
    "list, or an incomplete question mean INCOMPLETE. If the user announced several items ('two things', "
    "'first ...') and has not yet said all of them, it is INCOMPLETE. A complete question or statement, "
    "or a finished list, means COMPLETE. "
    "Answer with exactly one word: COMPLETE or INCOMPLETE."
)


async def end_of_turn(transcript: str) -> tuple[bool, float, str]:
    """Semantic end-of-turn judge. Returns (is_complete, ms, raw_answer)."""
    t0 = time.perf_counter()
    if not transcript.strip():
        return False, 0.0, ""
    resp = await client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": EOT_SYSTEM},
                  {"role": "user", "content": f"User so far: \"{transcript.strip()}\"\nAnswer:"}],
        max_tokens=3, temperature=1.0, extra_body=_thinking(False))
    raw = (resp.choices[0].message.content or "").strip().upper()
    ms = (time.perf_counter() - t0) * 1000
    return raw.startswith("COMPLETE"), ms, raw


def tool_result_message(call_id: str, name: str, result: Any) -> dict:
    return {"role": "tool", "tool_call_id": call_id, "name": name,
            "content": result if isinstance(result, str) else json.dumps(result, ensure_ascii=False)}


def assistant_tool_message(content: str | None, calls: list[dict]) -> dict:
    return {"role": "assistant", "content": content or None,
            "tool_calls": [{"id": c["id"], "type": "function",
                            "function": {"name": c["name"], "arguments": c["arguments"] or "{}"}}
                           for c in calls]}
