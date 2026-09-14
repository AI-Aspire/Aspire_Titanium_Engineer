# Voice deep research

## Learn | Create | Grow

### Learn
A speech round trip, then a research panel: a planner, researchers with tools, a critic, and a judge that sends drafts back, each role in its own voice.

### Create
Questions derived from your capability report, a full narrated session over your corpus, and the sessions saved to your workspace.

### Grow
Production voice needs turn-taking rules, barge-in, and latency budgets per role. Tell your team what the critic caught that the researchers missed.

**Estimated time:** 40 minutes
**Reads:** capability_report
**Writes:** voice_sessions

## Plain English first

| Term | Meaning |
|---|---|
| STT | speech to text: audio in, a transcript out |
| TTS | text to speech: a line and a voice name in, audio out |
| Planner | the role that splits a question into three angles |
| Critic | the role that attacks the draft before the judge sees it |
| Judge | the role that passes the draft or sends it back for a revision |
| Event | one step of the loop, printed, spoken, or streamed to the browser |

## What you will do

| Task | What happens |
|---|---|
| 1 | Synthesize one line, play it, transcribe it back |
| 2 | Turn the failing tasks in your capability report into research questions |
| 3 | Run the planner and read the three angles |
| 4 | Run one researcher with the corpus and web tools |
| 5 | Run the full narrated session and listen to it |
| 6 | Save the sessions |

## Setup

This module has its own environment, separate from the repository's shared one.

```bash
cd 14_Voice_Agents && uv sync && uv run jupyter lab    # open Voice_Deep_Research.ipynb
```

Keys and endpoints come from the repository-root `.env`:

| Variable | What it is | Default |
|---|---|---|
| `OPENAI_API_KEY`, `OPENAI_BASE_URL`, `LLM_MODEL` | the chat model, as in every module | |
| `STT_BASE` | an OpenAI-compatible speech-to-text service, `POST /v1/audio/transcriptions` | `http://localhost:8001` |
| `STT_MODEL` | the model name that service expects | `parakeet-tdt-0.6b-v3` |
| `TTS_BASE` | an OpenAI-compatible text-to-speech service, `POST /api/v1/audio/speech` | `http://localhost:8002` |
| `TTS_MODEL` | the model name that service expects | `model` |
| `TTS_KEY` | bearer token for the TTS service, if it wants one | empty |
| `TAVILY_API_KEY` | optional; adds web search to the researchers | empty |

Services needed:

- The chat model. Required.
- A speech-to-text service at `STT_BASE`. Optional: without it, questions are typed.
- A text-to-speech service at `TTS_BASE` with named voices. Optional: without it, the panel runs as text and the notebook says so. The voice names in `voice_panel/voice.py` are Kokoro's; change them to match your service.
- `ffmpeg` on the host, only for the web app's microphone button (the browser records webm, the STT service wants wav).

## The web app

```bash
uv run uvicorn web.server:app --host 0.0.0.0 --port 8000     # open http://localhost:8000
./serve.sh                                                   # the same app behind HTTPS on a tailnet, so the mic works from a phone
```

Browsers allow the microphone only on `localhost` or over HTTPS. Typing a question works everywhere.

## Files

```
voice_panel/agents.py        the cast: planner, researcher, aggregator, critic, judge
voice_panel/tools.py         corpus search and fetch over the workspace, Tavily when a key is set
voice_panel/orchestrator.py  the loop, emitted as events
voice_panel/narrate.py       spoken lines per role, synthesis, one WAV per session
voice_panel/voice.py         the STT and TTS clients and the role-to-voice map
web/server.py        FastAPI and a WebSocket that streams events and audio to the browser
web/static/          the page, its script, and a stylesheet in the AI Aspire palette
advanced/            two reference files for the advanced build (a turn-taking state machine and a two-lane model client); not runnable on their own
```

## Data files

None in this folder. Reads `capability_report` from the workspace and writes `voice_sessions`. Audio is generated in memory and never written to disk.
