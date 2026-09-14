"""Voice in, voice out: speech-to-text and multi-voice text-to-speech.

Both are OpenAI-compatible HTTP services, configured in the repository .env:
  STT: POST {STT_BASE}/v1/audio/transcriptions  (multipart file + model) -> {"text": ...}
  TTS: POST {TTS_BASE}/api/v1/audio/speech       ({model,input,voice,response_format}) -> WAV bytes

Each pipeline role gets its own voice, so you hear who is speaking.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

import httpx
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[2] / ".env")
load_dotenv()

STT_BASE = os.getenv("STT_BASE", "http://localhost:8001")
STT_MODEL = os.getenv("STT_MODEL", "parakeet-tdt-0.6b-v3")
TTS_BASE = os.getenv("TTS_BASE", "http://localhost:8002")
TTS_MODEL = os.getenv("TTS_MODEL", "model")
TTS_KEY = os.getenv("TTS_KEY", "")

# Role -> voice. Researchers are keyed by index so the three sound distinct.
VOICE_MAP = {
    "system": "af_heart",        # host / narrator
    "planner": "am_puck",
    "aggregator": "af_nicole",
    "critic": "bm_george",       # stern
    "judge": "am_fenrir",        # authoritative
    "researcher": ["bf_emma", "am_michael", "af_bella"],  # by rid 0/1/2
}


def voice_for(role: str, rid: int | None = None) -> str:
    v = VOICE_MAP.get(role, "af_heart")
    if isinstance(v, list):
        return v[(rid or 0) % len(v)]
    return v


def _headers() -> dict:
    return {"Authorization": f"Bearer {TTS_KEY}"} if TTS_KEY else {}


def stt_ok(timeout: float = 4.0) -> bool:
    """True when the speech-to-text service answers its health check."""
    try:
        return httpx.get(f"{STT_BASE}/health", timeout=timeout).status_code == 200
    except Exception:  # noqa: BLE001
        return False


def tts_ok(timeout: float = 4.0) -> bool:
    """True when the text-to-speech service lists its voices."""
    try:
        return httpx.get(f"{TTS_BASE}/api/v1/audio/voices", headers=_headers(), timeout=timeout).status_code == 200
    except Exception:  # noqa: BLE001
        return False


async def transcribe(audio: bytes, filename: str = "question.wav") -> str:
    async with httpx.AsyncClient(timeout=60) as c:
        r = await c.post(f"{STT_BASE}/v1/audio/transcriptions",
                         files={"file": (filename, audio, "audio/wav")},
                         data={"model": STT_MODEL})
        r.raise_for_status()
        return (r.json().get("text") or "").strip()


async def synthesize(text: str, voice: str = "af_heart") -> bytes:
    """Synthesize one chunk of speech -> WAV bytes (24kHz mono). Empty text -> b''."""
    text = strip_markdown(text).strip()
    if not text:
        return b""
    async with httpx.AsyncClient(timeout=120) as c:
        r = await c.post(
            f"{TTS_BASE}/api/v1/audio/speech",
            headers=_headers(),
            json={"model": TTS_MODEL, "input": text, "voice": voice, "response_format": "wav"})
        r.raise_for_status()
        return r.content


# --------------------------------------------------------------------------- #
# Text prep for speech
# --------------------------------------------------------------------------- #
_MD = [
    (re.compile(r"```.*?```", re.S), " "),      # code blocks
    (re.compile(r"`([^`]*)`"), r"\1"),
    (re.compile(r"^\s*#{1,6}\s*", re.M), ""),    # headers
    (re.compile(r"\*\*([^*]*)\*\*"), r"\1"),
    (re.compile(r"\*([^*]*)\*"), r"\1"),
    (re.compile(r"https?://\S+"), " "),          # do not read URLs aloud
    (re.compile(r"^\s*[-*]\s+", re.M), ""),      # bullet markers
    (re.compile(r"\[([^\]]*)\]\([^)]*\)"), r"\1"),
]


def strip_markdown(text: str) -> str:
    for pat, repl in _MD:
        text = pat.sub(repl, text)
    return re.sub(r"[ \t]+", " ", text).strip()


_SENT = re.compile(r"(?<=[.!?])\s+")


def sentences(text: str) -> list[str]:
    """Split into sentences for chunked (low-latency) TTS streaming."""
    return [s.strip() for s in _SENT.split(strip_markdown(text)) if s.strip()]
