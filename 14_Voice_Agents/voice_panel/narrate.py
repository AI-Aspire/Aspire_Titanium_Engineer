"""Turn pipeline Events into spoken audio: the voice layer over the orchestrator.

Two jobs:
  1. spoken_line(): a long research brief or draft should not be read aloud verbatim
     (minutes of monotone). Short events are spoken as-is; long ones are compressed to
     a concise, in-persona spoken line ("here is what I found", "my objection is").
  2. VoiceNarrator: synthesizes each line in the role's voice and serializes them
     (a lock) so parallel researchers narrate in order, not on top of each other.
     With speak=False it keeps the spoken lines as text and skips synthesis, so the
     same loop runs when no TTS service is reachable.

Plug VoiceNarrator.on_event straight into orchestrator.run_research as the on_event hook.
"""
from __future__ import annotations

import asyncio
import io

import numpy as np
import soundfile as sf

from .voice import strip_markdown, synthesize, voice_for

_PERSONA = {
    "researcher": ("You are a researcher on a live panel. In ONE or TWO spoken sentences, first "
                   "person, tell the room the single most important thing you found. No preamble, "
                   "no markdown."),
    "aggregator": ("You are the synthesizer on a live panel. In TWO spoken sentences, say what the "
                   "combined answer concludes so far. Conversational, no markdown."),
    "critic": ("You are the adversarial critic on a live panel. In ONE or TWO sharp spoken "
               "sentences, voice your single strongest objection. No preamble."),
    "final": ("Summarize this research answer for a listener in 3 to 5 spoken sentences: the bottom "
              "line first, then the main supporting points. Natural and spoken, no markdown, no URLs."),
}


async def spoken_line(llm, ev) -> str:
    """The concise thing this event should SAY (vs. the full text it carries)."""
    if ev.kind == "final":
        return strip_markdown(await llm.chat(_PERSONA["final"], ev.text))
    if ev.kind == "status" or len(ev.text) < 280:
        return strip_markdown(ev.text)
    persona = _PERSONA.get(ev.role)
    if not persona:
        return strip_markdown(ev.text)[:400]
    return strip_markdown(await llm.chat(persona, ev.text))


class VoiceNarrator:
    """Collects spoken segments (role, voice, text, wav) in order; optional live `sink`."""

    def __init__(self, llm, sink=None, *, speak: bool = True):
        self.llm = llm
        self.sink = sink                 # async fn(segment) for live streaming (web app)
        self.speak = speak
        self.segments: list[dict] = []
        self._lock = asyncio.Lock()

    async def on_event(self, ev):
        # Tool calls (search / fetch) are surfaced to the UI so it is visible what each
        # researcher is doing, but they are NOT spoken. No TTS, no LLM summary.
        if ev.kind == "tool":
            seg = {"role": ev.role, "voice": "", "text": ev.text, "kind": "tool",
                   "wav": b"", "meta": ev.meta}
            async with self._lock:
                self.segments.append(seg)
                if self.sink:
                    await self.sink(seg)
            return

        line = (await spoken_line(self.llm, ev)).strip()
        if not line:
            return
        voice = voice_for(ev.role, ev.meta.get("rid"))
        async with self._lock:           # serialize order + synthesis across parallel emitters
            wav = await synthesize(line, voice) if self.speak else b""
            seg = {"role": ev.role, "voice": voice, "text": line, "kind": ev.kind,
                   "wav": wav, "meta": ev.meta}
            self.segments.append(seg)
            if self.sink:
                await self.sink(seg)

    def transcript(self) -> list[dict]:
        """The spoken lines without the audio bytes, for saving."""
        return [{k: s.get(k) for k in ("role", "voice", "text", "kind")} for s in self.segments]

    def full_wav(self, gap_s: float = 0.35) -> bytes:
        """Concatenate all segments into one WAV (with a short gap between speakers)."""
        chunks, sr = [], 24000
        for seg in self.segments:
            if not seg["wav"]:
                continue
            data, sr = sf.read(io.BytesIO(seg["wav"]), dtype="float32")
            if data.ndim > 1:
                data = data.mean(axis=1)
            chunks.append(data)
            chunks.append(np.zeros(int(sr * gap_s), dtype="float32"))
        if not chunks:
            return b""
        out = io.BytesIO()
        sf.write(out, np.concatenate(chunks), sr, format="WAV", subtype="PCM_16")
        return out.getvalue()
