"""The research cast: planner, researcher, aggregator, critic, judge.

All async (the researchers run in parallel; the web app is async). The model is
whatever the repository .env names; it is called through the OpenAI client.

The researcher gathers evidence in two moves: it writes search queries, the
tools run them over your corpus (and the web when a Tavily key is set), it
reads the best pages, then it writes a short cited brief.
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

from dotenv import load_dotenv
from openai import AsyncOpenAI

from . import tools

load_dotenv(Path(__file__).resolve().parents[2] / ".env")
load_dotenv()

MODEL = os.getenv("LLM_MODEL") or "gpt-4.1-mini"
BASE = os.getenv("OPENAI_BASE_URL") or None
KEY = os.getenv("OPENAI_API_KEY") or "EMPTY"


class LLM:
    def __init__(self, model=MODEL, base=BASE, key=KEY, timeout: int = 600, temperature: float = 0.7):
        self.model = model
        self.temperature = temperature
        self.client = AsyncOpenAI(base_url=base, api_key=key, timeout=timeout)

    async def chat(self, system: str, user: str, temperature: float | None = None) -> str:
        r = await self.client.chat.completions.create(
            model=self.model, temperature=self.temperature if temperature is None else temperature,
            messages=[{"role": "system", "content": system},
                      {"role": "user", "content": user}])
        return (r.choices[0].message.content or "").strip()


def extract_json(text: str):
    """Pull the first JSON object/array out of a model reply (handles fences/prose)."""
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip(), flags=re.S)
    try:
        return json.loads(t)
    except Exception:  # noqa: BLE001
        m = re.search(r"(\{.*\}|\[.*\])", t, re.S)
        if m:
            try:
                return json.loads(m.group(1))
            except Exception:  # noqa: BLE001
                pass
    return None


# --------------------------------------------------------------------------- #
# Planner
# --------------------------------------------------------------------------- #
_PLANNER_SYS = """You are the research Planner. Given a question about a product and the agent
behind it, break it into exactly THREE distinct, complementary research angles that together
cover the question well (different facets, not three rephrasings). Return ONLY JSON:
{"plan": "<one sentence describing your split>", "angles": ["<angle 1>", "<angle 2>", "<angle 3>"]}"""


async def plan(llm: LLM, question: str) -> dict:
    out = extract_json(await llm.chat(_PLANNER_SYS, f"Question: {question}"))
    if not out or "angles" not in out or len(out.get("angles", [])) < 3:
        # fall back to a trivial split so the pipeline never stalls
        return {"plan": "Split into three general angles.",
                "angles": [f"{question}: what the documentation says",
                           f"{question}: what the transcripts and tool calls show",
                           f"{question}: what should change"]}
    out["angles"] = out["angles"][:3]
    return out


# --------------------------------------------------------------------------- #
# Researcher (queries -> tools -> read -> brief)
# --------------------------------------------------------------------------- #
_QUERY_SYS = """You are a Researcher. You will search a corpus of product documentation,
transcripts, and evaluation notes. Write two or three short search queries for your angle.
Return ONLY a JSON list of strings."""

_RESEARCH_SYNTH_SYS = """You are a Researcher. Using ONLY the evidence you gathered, write a
tight findings brief for your angle: the key facts, each followed by its source in square
brackets (the page path or URL). If the evidence is thin, say so. 4-8 sentences."""


async def research(llm: LLM, angle: str, on_tool=None, *, max_pages: int = 2, web: bool = True) -> dict:
    """Gather evidence with the tools, then write a findings brief. Returns
    {angle, queries, evidence, finding, sources, ok}. If `on_tool(tool, arg)` is given,
    it is awaited once per tool call, so a UI can show searches and fetches as they happen."""
    raw = extract_json(await llm.chat(_QUERY_SYS, f"Research angle: {angle}"))
    queries = [q for q in raw if isinstance(q, str)][:3] if isinstance(raw, list) else [angle]

    hits, evidence, sources = [], [], []
    for q in queries:
        if on_tool is not None:
            await on_tool("search", q)
        for h in tools.search(q, max_results=3):
            if h["path"] not in {x["path"] for x in hits}:
                hits.append(h)
        if web:
            for w in tools.web_search(q, max_results=3):
                if w.get("url"):
                    evidence.append(f"[{w['url']}] {w['title']}: {w['content']}")
                    sources.append(w["url"])
    for h in hits[:max_pages]:
        if on_tool is not None:
            await on_tool("fetch", h["path"])
        page = tools.fetch(h["path"])
        evidence.append(f"[{page['path']}] {page['text']}")
        sources.append(page["path"])
    ok = bool(evidence)
    body = "\n\n".join(evidence)[:6000] if ok else "[no evidence found]"
    finding = await llm.chat(_RESEARCH_SYNTH_SYS, f"Angle: {angle}\n\nEvidence gathered:\n{body}")
    return {"angle": angle, "queries": queries, "evidence": body, "finding": finding,
            "sources": list(dict.fromkeys(sources))[:6], "ok": ok}


# --------------------------------------------------------------------------- #
# Aggregator / Critic / Judge
# --------------------------------------------------------------------------- #
_AGG_SYS = """You are the Aggregator. Synthesize the researchers' findings into ONE coherent,
well-structured answer to the original question. Integrate across angles, resolve overlaps,
and keep the sources for key claims. Be direct and specific."""


async def aggregate(llm: LLM, question: str, findings: list[dict]) -> str:
    body = "\n\n".join(f"ANGLE: {f['angle']}\nFINDING: {f['finding']}\nSOURCES: {', '.join(f['sources'])}"
                       for f in findings)
    return await llm.chat(_AGG_SYS, f"Question: {question}\n\nFindings:\n{body}")


_CRITIC_SYS = """You are an adversarial Critic. Attack the draft answer: what is unsupported,
missing, one-sided, outdated, or wrong? Name specific gaps and any claims that need a source.
Be harsh and concrete. 4-8 bullet points."""


async def critique(llm: LLM, question: str, draft: str) -> str:
    return await llm.chat(_CRITIC_SYS, f"Question: {question}\n\nDraft answer:\n{draft}")


_JUDGE_SYS = """You are the Judge. Decide whether the draft answer is good enough to DELIVER to
the user, not whether it is perfect. Weigh the critic's points, but judge proportionately.

Mark satisfactory=true when the draft directly answers the question, is grounded in cited
sources, and covers the main points with no MAJOR unaddressed gap. Minor omissions, polish, or
"could go deeper" are NOT grounds to reject; a good, useful, honest answer should pass
(score >= 0.7). Reserve satisfactory=false for real problems: wrong or unsupported core claims,
a missing major dimension, or the question left substantially unanswered.

Return ONLY JSON:
{"satisfactory": true|false, "score": 0.0-1.0, "feedback": "<what must improve if not satisfactory>",
 "needs_more_research": true|false}"""


async def judge(llm: LLM, question: str, draft: str, critic_notes: str) -> dict:
    out = extract_json(await llm.chat(
        _JUDGE_SYS, f"Question: {question}\n\nDraft:\n{draft}\n\nCritic's attack:\n{critic_notes}"))
    if not out or "satisfactory" not in out:
        return {"satisfactory": True, "score": 0.5,
                "feedback": "(judge parse failed; accepting draft)", "needs_more_research": False}
    return out


_REVISE_SYS = """You are the Aggregator, revising your draft. Address the Critic's points and the
Judge's feedback: fill gaps, ground claims, cut what is unsupported. Keep the sources. Return the
improved answer only."""


async def revise(llm: LLM, question: str, draft: str, critic_notes: str, feedback: str,
                 extra_findings: list[dict] | None = None) -> str:
    extra = ""
    if extra_findings:
        extra = "\n\nNEW EVIDENCE:\n" + "\n\n".join(
            f"ANGLE: {f['angle']}\nFINDING: {f['finding']}" for f in extra_findings)
    return await llm.chat(
        _REVISE_SYS,
        f"Question: {question}\n\nCurrent draft:\n{draft}\n\nCritic:\n{critic_notes}\n\n"
        f"Judge feedback:\n{feedback}{extra}")
