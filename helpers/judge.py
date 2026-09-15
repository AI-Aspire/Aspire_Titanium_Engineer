"""The LLM-as-a-judge the evals notebook builds from scratch, packaged so later
notebooks can reuse it without rebuilding it. Same idea: one LLM call, JSON in, a score + rationale out.

    import sys; sys.path.insert(0, "..")
    from helpers.judge import make_judge
    relevance = make_judge("relevance",
        "Question: {question}\\nAnswer: {response}\\n\\nScore how well the answer "
        "addresses the question, 0-10.")
    relevance({"question": q, "response": a})   # -> {"judge", "score", "rationale"}
"""
import os
import json

from .config import (KEY, LLM_MODEL as _LLM_MODEL, LLM_BASE as _LLM_BASE,
                     apim_chat_client, _is_apim)


def _resolve_model() -> str:
    """The model name to call. Stripped of any provider prefix, since we call the
    OpenAI SDK directly rather than routing through litellm."""
    m = _LLM_MODEL
    if not m:
        return "gpt-4.1-mini"
    return m.removeprefix("openai/").removeprefix("anthropic/")


_MODEL = _resolve_model()

# The APIM path returns 401 through litellm (which sends Authorization: Bearer
# and cannot forward query params); the OpenAI SDK with default_query works.
# Off-APIM we still use the SDK — one code path, no litellm dependency.
_CLIENT = apim_chat_client(_MODEL)


def _chat(messages, **kw):
    # `api_key` / `api_base` may leak in from callers that assume litellm; drop them.
    kw.pop("api_key", None)
    kw.pop("api_base", None)
    # NOTE: never set max_tokens — the self-hosted model reasons before it answers.
    return _CLIENT.chat.completions.create(model=_MODEL, messages=messages, **kw)


def _json_blocks(text: str):
    """Every balanced {...} substring, ignoring braces inside string literals.
    Robust to nested objects and to braces that appear in the rationale text."""
    blocks, depth, start, in_str, esc = [], 0, None, False, False
    for i, ch in enumerate(text or ""):
        if esc:
            esc = False
            continue
        if ch == "\\":
            esc = in_str
            continue
        if ch == '"':
            in_str = not in_str
            continue
        if in_str:
            continue
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}" and depth > 0:
            depth -= 1
            if depth == 0 and start is not None:
                blocks.append(text[start:i + 1])
                start = None
    return blocks


def parse_judge_json(content: str) -> dict:
    """Pull the last balanced {...} block containing a score out of a judge reply."""
    for blob in reversed(_json_blocks(content or "")):
        try:
            obj = json.loads(blob)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict) and "score" in obj:
            return obj
    return {"score": None, "rationale": f"<unparseable: {(content or '')[:80]}>"}


def parse_json(text: str):
    """First balanced {...} block that parses as JSON, else None. General-purpose —
    the judge uses parse_judge_json, which additionally requires a "score" key."""
    for blob in _json_blocks(text or ""):
        try:
            return json.loads(blob)
        except json.JSONDecodeError:
            continue
    return None


JUDGE_SYSTEM = ('You are a careful evaluator. Always reply with a JSON object: '
                '{"score": <integer 0-10>, "rationale": "<one short sentence>"}.')


def make_judge(name: str, template: str, *, needs_reference: bool = False):
    """Turn a prompt template into a judge(row) -> {judge, score, rationale}."""
    def judge(row: dict) -> dict:
        if needs_reference and not row.get("reference"):
            return {"judge": name, "score": None, "rationale": "<no reference>"}
        # Substitute only our placeholders by name, so literal braces elsewhere in the
        # template (e.g. an embedded factsheet with JSON or {set} notation) don't trip
        # str.format. That's the difference between this and the from-scratch notebook cell.
        prompt = (template
                  .replace("{question}", str(row.get("question", "")))
                  .replace("{response}", str(row.get("response", "")))
                  .replace("{reference}", str(row.get("reference") or "")))
        resp = _chat(temperature=0.0, messages=[
            {"role": "system", "content": JUDGE_SYSTEM},
            {"role": "user", "content": prompt},
        ])
        parsed = parse_judge_json(resp.choices[0].message.content)
        return {"judge": name, "score": parsed.get("score"), "rationale": parsed.get("rationale", "")}
    judge.name = name
    return judge
