"""FastAPI + WebSocket server for the voice research panel.

A question arrives typed or as a push-to-talk recording; the pipeline streams each
step to the browser as a JSON metadata frame followed by a binary WAV frame (the
role's spoken line), and the front-end builds a live research tree and plays the
audio in order.

Run (from the module folder):
    uv run uvicorn web.server:app --host 0.0.0.0 --port 8000
"""
from __future__ import annotations

import json
import shutil
import subprocess
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# `voice_panel` and `helpers` are installed packages (see this module's
# pyproject.toml), so they import by name from any working directory.
from voice_panel.agents import LLM
from voice_panel.narrate import VoiceNarrator
from voice_panel.orchestrator import run_research
from voice_panel.voice import STT_BASE, TTS_BASE, transcribe, tts_ok, voice_for

HERE = Path(__file__).resolve().parent


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.llm = LLM()
    app.state.speak = tts_ok()
    yield


app = FastAPI(title="Voice research panel", lifespan=lifespan)
app.mount("/static", StaticFiles(directory=str(HERE / "static")), name="static")


@app.get("/", response_class=HTMLResponse)
async def index():
    return (HERE / "static" / "index.html").read_text()


@app.get("/api/status")
async def status():
    return {"status": "ok", "tts": app.state.speak, "stt_base": STT_BASE, "tts_base": TTS_BASE}


@app.get("/api/roles")
async def roles():
    return {"roles": [
        {"role": "planner", "voice": voice_for("planner")},
        {"role": "researcher-1", "voice": voice_for("researcher", 0)},
        {"role": "researcher-2", "voice": voice_for("researcher", 1)},
        {"role": "researcher-3", "voice": voice_for("researcher", 2)},
        {"role": "aggregator", "voice": voice_for("aggregator")},
        {"role": "critic", "voice": voice_for("critic")},
        {"role": "judge", "voice": voice_for("judge")},
    ]}


def _to_wav(audio: bytes) -> bytes:
    """Browser MediaRecorder gives webm/opus; the STT service wants wav. Convert via ffmpeg."""
    if audio[:4] == b"RIFF":
        return audio
    if not shutil.which("ffmpeg"):
        return audio
    p = subprocess.run(["ffmpeg", "-i", "pipe:0", "-ar", "16000", "-ac", "1", "-f", "wav", "pipe:1"],
                       input=audio, capture_output=True)
    return p.stdout or audio


async def _run(ws: WebSocket, question: str):
    async def sink(seg: dict):
        await ws.send_json({
            "type": "segment", "role": seg["role"], "voice": seg["voice"],
            "kind": seg["kind"], "text": seg["text"],
            "meta": {k: v for k, v in (seg.get("meta") or {}).items() if k in ("rid", "angle", "tool", "arg")},
            "audio_bytes": len(seg["wav"]),
        })
        if seg["wav"]:
            await ws.send_bytes(seg["wav"])

    await ws.send_json({"type": "question", "text": question})
    narrator = VoiceNarrator(ws.app.state.llm, sink=sink, speak=ws.app.state.speak)
    result = await run_research(question, narrator.on_event, llm=ws.app.state.llm)
    await ws.send_json({"type": "done", "final": result["final"],
                        "rounds": result["rounds"], "verdict": result.get("verdict", {})})


@app.websocket("/ws")
async def ws_research(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            msg = await ws.receive()
            if msg.get("text"):
                data = json.loads(msg["text"])
                if data.get("type") == "question" and (data.get("text") or "").strip():
                    await _run(ws, data["text"].strip())
                elif data.get("type") == "ping":
                    await ws.send_json({"type": "pong"})
            elif msg.get("bytes"):
                await ws.send_json({"type": "status", "stage": "transcribing"})
                transcript = await transcribe(_to_wav(msg["bytes"]))
                await ws.send_json({"type": "transcript", "text": transcript})
                if transcript.strip():
                    await _run(ws, transcript.strip())
                else:
                    await ws.send_json({"type": "error", "message": "Could not transcribe audio."})
    except WebSocketDisconnect:
        return
    except Exception as e:  # noqa: BLE001
        try:
            await ws.send_json({"type": "error", "message": repr(e)})
        except Exception:  # noqa: BLE001
            pass
