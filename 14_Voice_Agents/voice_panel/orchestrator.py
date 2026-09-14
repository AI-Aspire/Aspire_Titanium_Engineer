"""The research loop, emitted as a stream of Events.

Everything the pipeline does is an Event(role, kind, text). A text run just prints
them; the voice layer speaks each in the role's voice; the web app pushes them over
a WebSocket. Same loop, three surfaces, which is why it is event-driven.

Flow: plan -> 3 researchers (parallel) -> aggregate -> [critic -> judge -> revise]*
until the judge is satisfied or the round cap hits -> final.
"""
from __future__ import annotations

import asyncio
from dataclasses import dataclass, field

from .agents import LLM, aggregate, critique, judge, plan, research, revise

ROLES = ["system", "planner", "researcher", "aggregator", "critic", "judge"]


@dataclass
class Event:
    role: str            # one of ROLES
    kind: str            # 'status' (short narratable) | 'speech' (substantive) | 'tool' | 'final'
    text: str
    meta: dict = field(default_factory=dict)


async def _emit(on_event, ev: Event):
    if on_event is None:
        return
    r = on_event(ev)
    if asyncio.iscoroutine(r):
        await r


async def run_research(question: str, on_event=None, *, max_rounds: int = 2,
                       llm: LLM | None = None, web: bool = True) -> dict:
    """Run the full pipeline and return {question, plan, findings, final, rounds, verdict}."""
    llm = llm or LLM()

    await _emit(on_event, Event("system", "status", f"Researching: {question}"))

    p = await plan(llm, question)
    await _emit(on_event, Event("planner", "speech", p["plan"], {"angles": p["angles"]}))

    async def one(i: int, angle: str) -> dict:
        await _emit(on_event, Event("researcher", "status",
                                    f"Researcher {i + 1} is searching and reading sources on: {angle}",
                                    {"rid": i, "angle": angle}))

        async def on_tool(tool: str, arg: str):
            # A 'tool' event: surfaced in the UI so the tool calls are visible,
            # but NOT spoken (the narrator skips kind == 'tool').
            await _emit(on_event, Event("researcher", "tool", f"{tool}({arg!r})",
                                        {"rid": i, "tool": tool, "arg": arg}))

        f = await research(llm, angle, on_tool=on_tool, web=web)
        await _emit(on_event, Event("researcher", "speech", f["finding"],
                                    {"rid": i, "angle": angle, "sources": f["sources"], "ok": f["ok"]}))
        return f

    findings = await asyncio.gather(*(one(i, a) for i, a in enumerate(p["angles"])))

    draft = await aggregate(llm, question, findings)
    await _emit(on_event, Event("aggregator", "speech", draft, {"stage": "draft"}))

    rounds = 0
    verdict = {}
    while True:
        rounds += 1
        crit = await critique(llm, question, draft)
        await _emit(on_event, Event("critic", "speech", crit))
        verdict = await judge(llm, question, draft, crit)
        msg = ("Satisfactory." if verdict.get("satisfactory")
               else verdict.get("feedback") or "Needs another pass.")
        await _emit(on_event, Event("judge", "speech",
                                    f"Round {rounds}: {'PASS' if verdict.get('satisfactory') else 'REVISE'} "
                                    f"(score {verdict.get('score')}). {msg}", {"verdict": verdict}))
        if verdict.get("satisfactory") or rounds >= max_rounds:
            break
        draft = await revise(llm, question, draft, crit, verdict.get("feedback", ""))
        await _emit(on_event, Event("aggregator", "speech", draft, {"stage": "revision", "round": rounds}))

    await _emit(on_event, Event("system", "final", draft, {"rounds": rounds, "verdict": verdict}))
    return {"question": question, "plan": p, "findings": findings,
            "final": draft, "rounds": rounds, "verdict": verdict}
