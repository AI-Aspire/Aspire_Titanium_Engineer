import marimo

__generated_with = "0.24.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Voice deep research

    A research panel you can hear: a planner splits a question, three researchers read your corpus, an aggregator drafts, a critic attacks, and a judge decides. The questions are the failure modes named in your capability report.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    A speech round trip, then a research panel: a planner, researchers with tools, a critic, and a judge that sends drafts back, each role in its own voice.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    Questions derived from your capability report, a full narrated session over your corpus, and the sessions saved to your workspace.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    Production voice needs turn-taking rules, barge-in, and latency budgets per role. Tell your team what the critic caught that the researchers missed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 40 minutes
    **Reads:** capability_report
    **Writes:** voice_sessions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    This module has its own environment. Open it from this folder with `uv sync` and `uv run jupyter lab`. The speech services are optional: without them the panel runs as text and each cell says so. The chat model and the speech endpoints come from the repository `.env`.
    """)
    return


@app.cell
def _():
    import asyncio, re, textwrap, threading

    from IPython.display import Audio, Markdown, display

    from helpers.config import KEY, LLM_BASE, LLM_MODEL, TAVILY_KEY, require, budget
    from helpers import workspace as ws
    from voice_panel.agents import LLM
    from voice_panel.voice import STT_BASE, TTS_BASE, VOICE_MAP, stt_ok, tts_ok

    require("OPENAI_API_KEY")

    _LOOP = asyncio.new_event_loop()
    threading.Thread(target=_LOOP.run_forever, daemon=True).start()

    def run_async(coro):
        """Run a coroutine on one background loop and wait for it. Works in Jupyter and in a script."""
        return asyncio.run_coroutine_threadsafe(coro, _LOOP).result()

    llm = LLM()
    SPEAK, HEAR = tts_ok(), stt_ok()
    WEB = bool(TAVILY_KEY)
    REPORT = ws.load("capability_report")
    print(f"chat model  {LLM_MODEL}")
    print(f"TTS {TTS_BASE}: {'✅ voices ready' if SPEAK else '⚠️ not reachable, the panel runs as text'}")
    print(f"STT {STT_BASE}: {'✅ transcriber ready' if HEAR else '⚠️ not reachable, questions are typed'}")
    print(f"web search: {'✅ Tavily' if WEB else 'ℹ corpus only, no TAVILY_API_KEY set'}")
    print(f"✅ capability report from the {ws.source('capability_report')} ({len(REPORT.split())} words)")
    return (
        Audio,
        HEAR,
        LLM_MODEL,
        Markdown,
        REPORT,
        SPEAK,
        VOICE_MAP,
        WEB,
        budget,
        display,
        llm,
        re,
        run_async,
        textwrap,
        ws,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the chat model, one line per speech service, the web search mode, and a ✅ line naming the workspace or the seed. Stop here if the ✅ line is missing: the capability report is written by the agent harness notebook, or the seed carries it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Learn
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 1 of 6 — Voice in, voice out

    Two OpenAI-compatible HTTP services do the speech work. One transcribes audio to text, the other synthesizes text in a named voice. Prove the round trip before building anything on it: synthesize one line, play it, then transcribe the audio back and compare. Each role in the panel gets its own voice, so you can tell who is talking.
    """)
    return


@app.cell
def _(Audio, HEAR, SPEAK, VOICE_MAP, display, run_async):
    from voice_panel.voice import synthesize, transcribe

    LINE = "The agent answered from a stale page, and the judge did not notice."
    if SPEAK:
        wav = run_async(synthesize(LINE, voice=VOICE_MAP["system"]))
        display(Audio(wav))
        print(f"{len(wav) / 1024:.0f} KB of audio")
        if HEAR:
            print("STT heard:", run_async(transcribe(wav)))
    else:
        print("⚠️ no TTS service reachable; skipping the round trip")
    for role, voice in VOICE_MAP.items():
        print(f"{role:<11} {voice}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see an audio player, the clip size, the transcribed sentence with at most a word changed, and the role-to-voice map. Stop here if the transcript comes back empty: the STT service is up but rejects WAV input, so check `STT_MODEL` in `.env`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 6 — Turn the report into questions

    The capability report has a pass-rate table and a worst-failure section. A task that did not pass every run is a failure mode. Each one becomes a research question for the panel: why does the agent fail there, and what would fix it. Read the questions before you run anything; they are what the whole session is about.
    """)
    return


@app.cell
def _(REPORT, budget, re, textwrap):
    def failure_modes(report: str) -> list[dict]:
        """Rows of the pass-rate table that did not pass every run, worst first."""
        rows = re.findall('^\\|\\s*([^|\\s]+)\\s*\\|\\s*([^|]+?)\\s*\\|\\s*(\\d+)\\s*/\\s*(\\d+)\\s*\\|', report, re.M)
        modes = [{'task': t, 'category': c, 'passed': int(p), 'runs': int(n)} for t, c, p, n in rows if n.isdigit() and int(n) > 0 and (int(p) < int(n))]
        return sorted(modes, key=lambda m: m['passed'] / m['runs'])

    def worst_failure(report: str) -> str:
        m = re.search('## Worst failure\\s*\\n(.+?)(?:\\n## |\\Z)', report, re.S)
        return textwrap.shorten(m.group(1).strip(), 400) if m else ''
    MODES = failure_modes(REPORT)
    QUESTIONS = [f"Why does the agent fail the {m['category']} task {m['task']} ({m['passed']} of {m['runs']} runs passed), and what change to the agent, its tools, or its corpus would fix it?" for m in MODES]
    if not QUESTIONS:
        QUESTIONS = ['The capability report shows no failing task. What would the first real failure look like, and which eval case would catch it?']
    QUESTIONS = QUESTIONS[:budget(2, 1)]
    print('worst failure:', worst_failure(REPORT) or '(no worst-failure section)')
    for _q in QUESTIONS:
        print('-', _q)
    return (QUESTIONS,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the worst-failure summary and one or two research questions that name a task id and a category. Stop here if the list falls back to the no-failure question while your report shows failing tasks: the table regex did not match your report's columns.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which failure mode would you have picked by hand, and does the pass-rate table agree with your gut?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 6 — The planner

    Every role in the panel is a plain chat call with its own system prompt in `voice_panel/agents.py`. The planner goes first: it splits the question into three angles that cover different facets, not three rephrasings. Run it on the first question and read the split. If the angles overlap, the three researchers will read the same pages.
    """)
    return


@app.cell
def _(QUESTIONS, llm, run_async):
    from voice_panel.agents import plan
    PLAN = run_async(plan(llm, QUESTIONS[0]))
    print(PLAN['plan'])
    for _i, angle in enumerate(PLAN['angles'], 1):
        print(f'  {_i}. {angle}')
    return (PLAN,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see one sentence describing the split and three numbered angles. Stop here if the three angles are near-identical: the planner prompt is not asking for distinct facets, so edit it before the researchers run.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 6 — A researcher with tools

    A researcher writes two or three search queries, runs them over your corpus, reads the best pages, and writes a short cited brief. Web search joins in only when a Tavily key is set. Run one researcher on one angle and read the brief against the pages it cites. The evidence is the product; the prose is packaging.
    """)
    return


@app.cell
def _(PLAN, WEB, llm, run_async, textwrap):
    from voice_panel import tools
    from voice_panel.agents import research

    hits = tools.search(PLAN["angles"][0], max_results=3)
    for h in hits:
        print(f"{h['score']:>3}  {h['path']:<40} {h['title']}")
    if hits:
        print("\n", textwrap.shorten(tools.fetch(hits[0]["path"])["text"], 300))

    FINDING = run_async(research(llm, PLAN["angles"][0], web=WEB))
    print("\nqueries:", FINDING["queries"])
    print("sources:", FINDING["sources"])
    print("\n" + FINDING["finding"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see ranked corpus hits with scores, a page excerpt, the researcher's queries, its sources, and a brief of four to eight sentences. Stop here if the brief cites nothing: the queries missed every page, so widen the search terms or check the corpus.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which page did the researcher lean on, and would you have chosen it? Name one claim in the brief that its sources do not support.

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Create
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5 of 6 — The full narrated session

    The orchestrator runs the loop: plan, three researchers in parallel, aggregate, then critic and judge until the judge passes the draft or the round cap hits. Every step is an event. The narrator compresses long events to one spoken line and synthesizes it in the role's voice. Tool calls are shown, never spoken. The web app in this folder streams the same events to a browser: `uv run uvicorn web.server:app --port 8000`.
    """)
    return


@app.cell
def _(QUESTIONS, SPEAK, WEB, budget, llm, run_async, textwrap):
    from voice_panel.narrate import VoiceNarrator
    from voice_panel.orchestrator import run_research
    SESSIONS = []
    for _i, _q in enumerate(QUESTIONS, 1):
        _narrator = VoiceNarrator(llm, speak=SPEAK)
        result = run_async(run_research(_q, _narrator.on_event, max_rounds=budget(2, 1), llm=llm, web=WEB))
        SESSIONS.append({'id': f'v{_i:02d}', 'question': _q, 'answer': result['final'], 'rounds': result['rounds'], 'score': result['verdict'].get('score'), 'spoken': _narrator.transcript(), 'wav': _narrator.full_wav() if SPEAK else b''})
        print(f"[v{_i:02d}] {result['rounds']} round(s), judge score {result['verdict'].get('score')}")
        for seg in _narrator.transcript():
            if seg['kind'] != 'tool':
                print(f"  {seg['role']:<11} {textwrap.shorten(seg['text'], 110)}")
        print()
    return SESSIONS, VoiceNarrator, run_research


@app.cell
def _(Audio, Markdown, SESSIONS, display):
    s = SESSIONS[0]
    if s["wav"]:
        display(Audio(s["wav"]))
    display(Markdown(f"## {s['question']}\n\n" + s["answer"]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see one spoken line per role in order, the judge's verdict per round, then an audio player for the whole session and the final answer. Stop here if the judge passes in round one with a score under 0.7: the judge prompt's threshold and its verdict disagree.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 6 of 6 — Save the sessions

    One row per question: the question, the final answer, the rounds it took, the judge's score, and the spoken lines. Saving them makes the panel's answers part of your workspace, where the deep-research report and the risk register can read them.
    """)
    return


@app.cell
def _(LLM_MODEL, SESSIONS, ws):
    ROWS = [{"id": s["id"], "question": s["question"], "answer": s["answer"], "rounds": s["rounds"],
             "judge_score": s["score"], "spoken": [x for x in s["spoken"] if x["kind"] != "tool"],
             "spoken_aloud": bool(s["wav"]), "model": LLM_MODEL} for s in SESSIONS]
    ws.save("voice_sessions", ROWS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with one row per question. Stop here if it says zero rows: a session above raised, so rerun Task 5 and read its error.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    The critic's objection and the judge's verdict are both one model call. When did they disagree, and which one would you trust in front of a user?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Give the judge a stricter bar: edit its prompt in `voice_panel/agents.py` so it demands a source for every claim, restart the kernel, and rerun one session with a round cap of three. Compare the rounds and the score with the row you saved. Explain to a teammate what the extra round cost and what it changed in the answer.
    """)
    return


@app.cell
def _(
    QUESTIONS,
    SESSIONS,
    VoiceNarrator,
    WEB,
    llm,
    run_async,
    run_research,
    textwrap,
):
    _narrator = VoiceNarrator(llm, speak=False)
    strict = run_async(run_research(QUESTIONS[0], _narrator.on_event, max_rounds=3, llm=llm, web=WEB))
    print(f"rounds {strict['rounds']} vs {SESSIONS[0]['rounds']}; score {strict['verdict'].get('score')} vs {SESSIONS[0]['score']}")
    print(textwrap.shorten(strict['final'], 500))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Grow
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## From prototype to production

    | What we built | Production equivalent |
    |---|---|
    | Three fixed researchers over a term-overlap corpus search | Dynamic fan-out over a retrieval service with per-agent budgets |
    | One session per question, held in memory | Persistent sessions with resumable traces and cost accounting |
    | A judge that is one chat call | A verifier ensemble with citation checks and a human review queue |
    | Segments concatenated into one WAV | Streaming duplex audio with barge-in and turn-taking |
    | Localhost speech services and a Tavily key | Managed speech and search with SLAs, quotas, and observability |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - Audio retained only as long as the transcript needs it.
    - A latency budget per turn, measured.
    - The critic and judge loop bounded by a round limit.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    The `advanced/` folder holds two reference files from a cascaded voice agent whose turn-taking is a switchable state machine: push-to-talk, a silence timeout, and semantic end-of-turn, where the model decides whether you have finished speaking. It also has barge-in. Reference code, not a runnable app.

    - Read `advanced/session.py` and draw its state machine. Then add one state to the web app: end the turn after 700 ms of silence instead of on button release.
    - Run the end-of-turn judge from `advanced/llm.py` over the spoken lines in your saved sessions. How often would it have cut a speaker off?
    - Split the final answer into claims and confirm each against its cited page before the narrator speaks it.
    """)
    return


if __name__ == "__main__":
    app.run()
