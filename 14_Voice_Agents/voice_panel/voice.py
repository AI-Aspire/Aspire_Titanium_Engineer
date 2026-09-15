"""Voice in, voice out: speech-to-text and multi-voice text-to-speech.

Two backends, one API:

Local path (STT_BASE/TTS_BASE point at localhost):
  STT: POST {STT_BASE}/v1/audio/transcriptions  (multipart file + model) -> {"text": ...}
  TTS: POST {TTS_BASE}/api/v1/audio/speech      ({model,input,voice,response_format}) -> WAV bytes

Azure AI Speech path (auto-detected when STT_BASE_URL contains cognitiveservices.azure.com):
  STT: Azure Speech REST API   (real-time recognition, no local install needed)
  TTS: Azure Neural TTS REST   (SSML -> WAV, no local install needed)
  Needs STT_API_KEY / TTS_API_KEY and STT_BASE_URL / TTS_BASE_URL in .env.
  Both keys can interpolate from a single SPEECH_KEY (see .env.template).

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

# ── local services (Parakeet + Kokoro) ──────────────────────────────────────
STT_BASE = os.getenv("STT_BASE", "http://localhost:8001")
STT_MODEL = os.getenv("STT_MODEL", "parakeet-tdt-0.6b-v3")
TTS_BASE = os.getenv("TTS_BASE", "http://localhost:8002")
TTS_MODEL = os.getenv("TTS_MODEL", "model")
TTS_KEY = os.getenv("TTS_KEY", "")

# ── Azure AI Speech ──────────────────────────────────────────────────────────
# -04's split env vars (SPEECH_KEY drives both via ${SPEECH_KEY} in .env).
STT_BASE_URL = os.getenv("STT_BASE_URL", "").rstrip("/")
STT_API_KEY = os.getenv("STT_API_KEY", "")
TTS_BASE_URL = os.getenv("TTS_BASE_URL", "").rstrip("/")
TTS_API_KEY = os.getenv("TTS_API_KEY", "")

# Back-compat aliases so older notebooks importing SPEECH_BASE_URL/SPEECH_KEY still work.
SPEECH_BASE_URL = STT_BASE_URL or TTS_BASE_URL
SPEECH_KEY = STT_API_KEY or TTS_API_KEY

# Azure Speech is active when USE_AZURE_SPEECH=true OR when the STT/TTS
# base URLs point at a Cognitive Services custom domain.
USE_AZURE_SPEECH = (
    os.getenv("USE_AZURE_SPEECH", "").lower() in ("1", "true", "yes")
    or "cognitiveservices.azure.com" in STT_BASE_URL
    or "cognitiveservices.azure.com" in TTS_BASE_URL
)

# ── voice maps ───────────────────────────────────────────────────────────────
# Kokoro voices (local path). Researchers are keyed by index so the three sound distinct.
VOICE_MAP = {
    "system": "af_heart",        # host / narrator
    "planner": "am_puck",
    "aggregator": "af_nicole",
    "critic": "bm_george",       # stern
    "judge": "am_fenrir",        # authoritative
    "researcher": ["bf_emma", "am_michael", "af_bella"],  # by rid 0/1/2
}

# Azure Neural voices (cloud path) — same roles, same persona feel.
AZURE_VOICE_MAP = {
    "system":     "en-US-JennyNeural",
    "planner":    "en-US-GuyNeural",
    "aggregator": "en-US-AriaNeural",
    "critic":     "en-GB-RyanNeural",
    "judge":      "en-US-DavisNeural",
    "researcher": ["en-GB-SoniaNeural", "en-US-AndrewNeural", "en-US-EmmaNeural"],
}


def voice_for(role: str, rid: int | None = None) -> str:
    vm = AZURE_VOICE_MAP if USE_AZURE_SPEECH else VOICE_MAP
    v = vm.get(role, "en-US-JennyNeural" if USE_AZURE_SPEECH else "af_heart")
    if isinstance(v, list):
        return v[(rid or 0) % len(v)]
    return v


def _headers() -> dict:
    return {"Authorization": f"Bearer {TTS_KEY}"} if TTS_KEY else {}


def stt_ok(timeout: float = 4.0) -> bool:
    """True when the speech-to-text service answers its health check."""
    if USE_AZURE_SPEECH:
        # Azure Speech has no health endpoint; a GET on the root returns 200 if reachable.
        try:
            return httpx.get(STT_BASE_URL, timeout=timeout).status_code < 500
        except Exception:  # noqa: BLE001
            return False
    try:
        return httpx.get(f"{STT_BASE}/health", timeout=timeout).status_code == 200
    except Exception:  # noqa: BLE001
        return False


def tts_ok(timeout: float = 4.0) -> bool:
    """True when the text-to-speech service is reachable."""
    if USE_AZURE_SPEECH:
        try:
            return httpx.get(TTS_BASE_URL, timeout=timeout).status_code < 500
        except Exception:  # noqa: BLE001
            return False
    try:
        return httpx.get(f"{TTS_BASE}/api/v1/audio/voices", headers=_headers(), timeout=timeout).status_code == 200
    except Exception:  # noqa: BLE001
        return False


# ── public API (same signature regardless of backend) ───────────────────────

async def transcribe(audio: bytes, filename: str = "question.wav") -> str:
    """Speech -> text. Routes to Azure AI Speech or local Parakeet based on USE_AZURE_SPEECH."""
    if USE_AZURE_SPEECH:
        return await _azure_transcribe(audio)
    async with httpx.AsyncClient(timeout=60) as c:
        r = await c.post(f"{STT_BASE}/v1/audio/transcriptions",
                         files={"file": (filename, audio, "audio/wav")},
                         data={"model": STT_MODEL})
        r.raise_for_status()
        return (r.json().get("text") or "").strip()


async def synthesize(text: str, voice: str = "af_heart") -> bytes:
    """Synthesize one chunk of speech -> WAV bytes (24kHz mono). Empty text -> b''.

    Routes to Azure Neural TTS or local Kokoro based on USE_AZURE_SPEECH.
    """
    text = strip_markdown(text).strip()
    if not text:
        return b""
    if USE_AZURE_SPEECH:
        return await _azure_synthesize(text, voice)
    async with httpx.AsyncClient(timeout=120) as c:
        r = await c.post(
            f"{TTS_BASE}/api/v1/audio/speech",
            headers=_headers(),
            json={"model": TTS_MODEL, "input": text, "voice": voice, "response_format": "wav"})
        r.raise_for_status()
        return r.content


# ── Azure AI Speech implementations ─────────────────────────────────────────

async def _azure_transcribe(audio: bytes) -> str:
    """Azure Speech-to-Text via the resource's custom domain (VNet-safe), no local install."""
    url = f"{STT_BASE_URL}/stt/speech/recognition/conversation/cognitiveservices/v1"
    async with httpx.AsyncClient(timeout=60) as c:
        r = await c.post(
            url,
            params={"language": "en-US", "format": "simple"},
            headers={"Ocp-Apim-Subscription-Key": STT_API_KEY,
                     "Content-Type": "audio/wav; codecs=audio/pcm; samplerate=16000"},
            content=audio,
        )
        r.raise_for_status()
        return (r.json().get("DisplayText") or "").strip()


async def _azure_synthesize(text: str, voice: str) -> bytes:
    """Azure Neural TTS via the resource's custom domain (VNet-safe) — SSML -> WAV bytes."""
    ssml = (
        f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">'
        f'<voice name="{voice}">{text}</voice>'
        f'</speak>'
    )
    url = f"{TTS_BASE_URL}/tts/cognitiveservices/v1"
    async with httpx.AsyncClient(timeout=120) as c:
        r = await c.post(
            url,
            headers={"Ocp-Apim-Subscription-Key": TTS_API_KEY,
                     "Content-Type": "application/ssml+xml",
                     "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm"},
            content=ssml.encode(),
        )
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
