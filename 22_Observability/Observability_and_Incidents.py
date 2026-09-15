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
    # Observability and incidents

    A normal outage announces itself: something returns a 500, a graph drops, a pager goes off. An AI system's worst failure keeps answering, and the answers get worse. No error, no latency spike, no alert. This notebook instruments a request path from scratch, shows which metrics stay flat through a quality regression, builds the detector that catches it, and measures where your endpoint saturates.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    A span from scratch and the convention names it maps onto, the four metrics an LLM application needs, a planted quality regression that three of them cannot see, and a drift detector with a stated lag.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    A real load test against your endpoint, the redacted traces of one instrumented request, and a monitoring file with the four metrics, the drift rule, and what may be logged.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    Production scores sampled traffic through the eval harness, not only latency. Bring your team the detection lag you can promise and the incident you would find out about last.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 40 minutes
    **Reads:** trajectories, eval_cases, corpus
    **Writes:** traces, load_test, monitoring
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    One chat model answers the instrumented request and takes the load test. The retriever is a keyword search over your corpus pages, the same shape as your agent, so the request path looks like the one you will run. Your trajectories shape the simulated week of traffic.
    """)
    return


@app.cell
def _():
    import json, re, textwrap, time, uuid
    from concurrent.futures import ThreadPoolExecutor
    from contextlib import contextmanager

    import numpy as np
    import pandas as pd

    from helpers.config import LLM_MODEL, require, budget
    from helpers import workspace as ws, ui
    from helpers.llm import complete

    require("OPENAI_API_KEY")

    CORPUS_DIR = ws.load_path("corpus")
    PAGES = {str(p.relative_to(CORPUS_DIR)): p.read_text(encoding="utf-8") for p in ws.load("corpus") if p.suffix == ".md"}
    TRAJECTORIES = ws.load("trajectories")
    EVAL_CASES = ws.load("eval_cases")
    print(f"✅ model {LLM_MODEL}; {len(PAGES)} corpus pages; {len(TRAJECTORIES)} trajectories; "
          f"{len(EVAL_CASES)} eval cases; source: {ws.source('trajectories')}")
    return (
        EVAL_CASES,
        LLM_MODEL,
        PAGES,
        TRAJECTORIES,
        ThreadPoolExecutor,
        budget,
        complete,
        contextmanager,
        json,
        np,
        pd,
        re,
        textwrap,
        time,
        ui,
        uuid,
        ws,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with the model, a page count above five, a trajectory count above three, and where the trajectories come from. Stop here if the trajectory count is zero: run the agent evals notebook first, or let the seed carry it.
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
    ## Task 1 of 6 — A span, from scratch

    Tracing sounds like a product you buy. It is a dictionary with a start time, a duration, and a parent. The context manager below records one unit of work whether or not it succeeded, because instrumentation that only records success shows a healthy dashboard during an outage. The request path is three spans under one root: retrieve over your corpus, generate with one model call, and a cheap output check. The parent id turns a pile of timings into a tree, which is the only shape that answers "which part was slow".
    """)
    return


@app.cell
def _(
    EVAL_CASES,
    LLM_MODEL,
    PAGES,
    complete,
    contextmanager,
    re,
    textwrap,
    time,
    uuid,
):
    STOP = {"a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "how", "i", "in", "is", "it", "of",
            "on", "or", "our", "should", "that", "the", "their", "to", "what", "when", "with", "my", "can", "do",
            "does", "this", "you", "your", "me", "we", "not", "but", "if", "so", "was", "will", "have", "has"}
    REFUSAL = ("outside", "can't help", "cannot help", "not able to help", "only help", "out of scope", "i can only",
               "unable to help", "not something i can")
    SYSTEM = ("You are the internal helpdesk assistant. Answer from the sections below in three sentences or fewer "
              "and name the section you used. If nothing below answers the question, say so in one sentence.")


    def terms(text: str) -> set[str]:
        return {t for t in re.findall(r"[a-z0-9][a-z0-9-]+", text.lower()) if t not in STOP}


    def sections(page: str, markdown: str) -> list[dict]:
        out = []
        for i, chunk in enumerate(re.split(r"^## ", markdown, flags=re.M)):
            title, _, body = chunk.partition("\n")
            if body.strip():
                out.append({"page": page, "title": title.strip() if i else "intro", "text": body.strip()})
        for s in out:
            s["terms"] = terms(s["page"] + " " + s["title"] + " " + s["text"])
        return out


    SECTIONS = [s for name, text in PAGES.items() for s in sections(name, text)]


    def retrieve(question: str, k: int = 3) -> list[dict]:
        q = terms(question)
        return [s for s in sorted(SECTIONS, key=lambda s: len(q & s["terms"]), reverse=True)[:k] if q & s["terms"]]


    TRACES: list[dict] = []


    @contextmanager
    def span(name: str, parent: str | None = None, **attributes):
        """One unit of work: timed, parented, and recorded whether or not it succeeded."""
        record = {"id": uuid.uuid4().hex[:8], "parent": parent, "name": name, "start": time.perf_counter(),
                  "attributes": attributes, "status": "ok"}
        try:
            yield record
        except Exception as exc:
            record["status"] = "error"
            record["error"] = f"{type(exc).__name__}: {exc}"[:200]
            raise
        finally:
            record["ms"] = round((time.perf_counter() - record["start"]) * 1000, 1)
            TRACES.append(record)


    def handle_request(question: str) -> str:
        """The request path: retrieve, generate, check. Three spans under one root."""
        with span("request", question=question, question_len=len(question)) as root:
            with span("retrieve", parent=root["id"], k=3) as r:
                hits = retrieve(question)
                r["attributes"]["hits"] = len(hits)
            with span("generate", parent=root["id"], model=LLM_MODEL) as g:
                context = "\n\n".join(f"[{s['page']} > {s['title']}]\n{textwrap.shorten(s['text'], 600)}" for s in hits)
                resp = complete([{"role": "system", "content": SYSTEM},
                                 {"role": "user", "content": f"SECTIONS:\n{context or 'No section matched.'}\n\nQUESTION: {question}"}])
                answer = (resp.choices[0].message.content or "").strip()
                usage = resp.usage
                g["attributes"].update(response_model=resp.model, tokens_in=usage.prompt_tokens if usage else 0,
                                       tokens_out=usage.completion_tokens if usage else 0)
            with span("guardrail", parent=root["id"]) as c:
                c["attributes"]["refused"] = any(p in answer.lower() for p in REFUSAL)
                c["attributes"]["empty"] = not answer
        return answer


    def print_tree(spans: list[dict], parent: str | None = None, depth: int = 0) -> None:
        for s in spans:
            if s["parent"] == parent:
                attrs = ", ".join(f"{k}={v}" for k, v in s["attributes"].items() if k != "question")
                print(f"{'  ' * depth}{s['name']:<10} {s['ms']:>9.1f} ms  {s['status']:<5} {textwrap.shorten(attrs, 90)}")
                print_tree(spans, s["id"], depth + 1)


    answer = handle_request(EVAL_CASES[0]["question"])
    print(textwrap.shorten(answer or "(empty reply)", 240), "\n")
    print_tree(TRACES)
    return REFUSAL, TRACES


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a short answer, then a tree: `request` at the top, three indented children, `generate` taking nearly all the time, and token counts on it. Stop here if `generate` is not the slowest span: something else in the path is blocking, and that is the first thing to fix.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 6 — The same span, in the names everyone else uses

    In production this is OpenTelemetry: the same three things with a wire protocol and a backend. The part worth copying now is not the SDK, which is not a dependency here, but the attribute names. Your dictionary works, and it is unreadable to every tool built to read traces, because you called it `tokens_in` and the rest of the world calls it `gen_ai.usage.input_tokens`. The cell maps the generate span onto the GenAI semantic convention names as plain dictionary keys, and keeps both the model you asked for and the model that answered. Record only the first and "the vendor changed the model under us" becomes unprovable.
    """)
    return


@app.cell
def _(TRACES: list[dict], json):
    OTEL = {"model": "gen_ai.request.model", "response_model": "gen_ai.response.model",
            "tokens_in": "gen_ai.usage.input_tokens", "tokens_out": "gen_ai.usage.output_tokens"}


    def to_otel(record: dict) -> dict:
        """Rename our attributes onto the convention names. That is the whole job."""
        out = {"span": record["name"], "ms": record["ms"], "status": record["status"]}
        for ours, theirs in OTEL.items():
            if ours in record["attributes"]:
                out[theirs] = record["attributes"][ours]
        return out


    generate_span = next(t for t in TRACES if t["name"] == "generate")
    print(json.dumps(to_otel(generate_span), indent=2))
    asked, served = generate_span["attributes"]["model"], generate_span["attributes"].get("response_model")
    print(f"\nrequest model == response model: {asked == served}  (asked for {asked!r}, served by {served!r})")
    return generate_span, to_otel


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the generate span with `gen_ai.request.model`, `gen_ai.response.model`, and the two token counts, then a line saying whether the two model names match. Stop here if the response model is empty: your server is not reporting what served the request, and you will never be able to prove a vendor changed it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Read the tree for your one request. Which span would your team have guessed was slowest, and which was? If the vendor swapped the model tonight, which line in these spans would show it the next morning?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 6 — The four metrics over a week

    Not the standard four. These are the ones specific to an LLM application: p50 and p95 latency, cost per request, refusal rate, and eval score on traffic. The cell builds a week of traffic shaped by your trajectories (how many model calls each run made, whether it passed, whether it refused) and scaled by the one request you measured. The timings are drawn, not measured, and the price is a lookup you set. From the fifth day a regression is planted: a third of the answers that would have passed now fail. Nothing else changes, so the chart asks one question: which metric can see it.
    """)
    return


@app.cell
def _(REFUSAL, TRAJECTORIES, generate_span, np, pd, ui):
    import matplotlib.pyplot as plt
    from helpers.brand import PALETTE, matplotlib_style

    PRICE_PER_1K_TOKENS = 0.0005   # a lookup from your provider's price list, in dollars; set it, do not measure it
    REQUESTS_PER_DAY = 400
    REGRESSION_DAY = 5             # planted: from this day on, REGRESSION_DROP of the answers that would pass now fail
    REGRESSION_DROP = 0.35

    CALL_MS = generate_span["ms"]                                                        # one measured call sets the time scale
    CALL_TOKENS = generate_span["attributes"]["tokens_in"] + generate_span["attributes"]["tokens_out"] or 1   # and the token scale


    def agent_said(t: dict) -> str:
        return " ".join((s.get("content") or "").lower() for s in t["steps"] if s["role"] == "assistant")


    baseline_runs = [t for t in TRAJECTORIES if t.get("variant", "baseline") == "baseline"] or TRAJECTORIES
    POOL = pd.DataFrame({"calls": [sum(s["role"] in ("assistant", "tool") for s in t["steps"]) for t in baseline_runs],
                         "passed": [bool(t["passed"]) for t in baseline_runs],
                         "refused": [any(p in agent_said(t) for p in REFUSAL) for t in baseline_runs]})
    rng = np.random.default_rng(0)


    def simulate_day(day: int) -> dict:
        """One day of traffic: each request is a run from your trajectories, timed and priced by the measured call."""
        picks = POOL.iloc[rng.integers(len(POOL), size=REQUESTS_PER_DAY)]
        calls = picks["calls"].to_numpy()
        ms = calls * CALL_MS * rng.lognormal(0.0, 0.35, size=len(calls))
        tokens = calls * CALL_TOKENS * rng.lognormal(0.0, 0.2, size=len(calls))
        regressed = (day >= REGRESSION_DAY) & (rng.random(len(calls)) < REGRESSION_DROP)
        passed = picks["passed"].to_numpy() & ~regressed
        return {"day": day, "p50_ms": int(np.percentile(ms, 50)), "p95_ms": int(np.percentile(ms, 95)),
                "cost_per_request": float(tokens.mean() / 1000 * PRICE_PER_1K_TOKENS),
                "refusal_rate": float(picks["refused"].mean()), "eval_score": float(passed.mean())}


    WEEK = pd.DataFrame([simulate_day(d) for d in range(1, 8)]).set_index("day")
    ui.table(WEEK, title=f"a week of {REQUESTS_PER_DAY} requests a day, shaped by {len(POOL)} of your runs", float_fmt="{:.5g}")

    plt.rcParams.update(matplotlib_style())
    base = WEEK.iloc[:REGRESSION_DAY - 1].mean()
    relative = WEEK / base.where(base > 0)               # a series that is zero all week has nothing to normalise
    fig, ax = plt.subplots(figsize=(8, 3.8))
    for col, marker in zip(WEEK.columns, "osd^v"):
        if relative[col].notna().all():
            ax.plot(relative.index, relative[col], marker=marker, label=col, lw=2.5 if col == "eval_score" else 1.5)
            if col == "eval_score":
                ax.annotate(col, (7, relative[col].iloc[-1]), xytext=(5, 0), textcoords="offset points", fontsize=8, va="center")
        else:
            print(f"{col} is zero in the first four days, so it is left off the chart")
    ax.axvline(REGRESSION_DAY - 0.5, color=PALETTE["neutral_300"], ls=":")
    ax.set_xlabel("day"); ax.set_ylabel("relative to the first four days"); ax.set_ylim(0.4, 1.6); ax.set_xlim(0.8, 7.8)
    ax.legend(loc="lower left", fontsize=8, ncol=3); ax.set_title("three of these are the dashboard; the fourth is the one nobody has")
    plt.tight_layout(); plt.show()
    return (
        CALL_TOKENS,
        POOL,
        PRICE_PER_1K_TOKENS,
        REGRESSION_DAY,
        REGRESSION_DROP,
        WEEK,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a seven-row table and a chart where every line sits near 1.0 for four days and only the eval score falls from the fifth day. Stop here if the eval score line does not fall: the pool has no passing runs to regress, so read your trajectories before going on.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 6 — Detect the regression, and say the lag out loud

    You cannot score every request. You can score a sample each day and watch the series move. The detector is a mean and a standard deviation: it fires when the last three days average more than 2.5 standard deviations below everything before them. Sophisticated change detection exists and is rarely why teams miss this; not looking is. Run it on the eval score, then on p95 latency with the sign flipped so a rise reads as a drop, and read which one fires. Then read when it fired, because the gap between the regression starting and the alert is a number you owe your team.
    """)
    return


@app.cell
def _(REGRESSION_DAY, REGRESSION_DROP, WEEK, np):
    def detect_drift(scores: list[float], window: int = 3, tolerance: float = 2.5) -> list[dict]:
        """Fire when the mean of the last `window` points falls `tolerance` standard deviations under everything before them."""
        alerts = []
        for i in range(window * 2, len(scores) + 1):
            baseline = np.array(scores[: i - window])
            recent = np.array(scores[i - window: i])
            threshold = baseline.mean() - tolerance * (baseline.std() or 0.01)
            if recent.mean() < threshold:
                alerts.append({"day": i, "baseline": round(float(baseline.mean()), 3),
                               "recent": round(float(recent.mean()), 3), "threshold": round(float(threshold), 3)})
        return alerts


    ALERTS = detect_drift(list(WEEK["eval_score"]))
    LATENCY_ALERTS = detect_drift(list(-WEEK["p95_ms"]))
    print("eval score:  ", ALERTS or "no alert")
    print("p95 latency: ", LATENCY_ALERTS or "no alert")

    LAG_DAYS = ALERTS[0]["day"] - REGRESSION_DAY if ALERTS else None
    DRIFT_RULE = {"metric": "eval score on sampled traffic", "window": 3, "tolerance": 2.5,
                  "regression_day": REGRESSION_DAY, "fired_on_day": ALERTS[0]["day"] if ALERTS else None, "lag_days": LAG_DAYS}
    if LAG_DAYS is None:
        print("\nthe planted drop is inside the noise: the detector cannot see a regression this small at this sample size")
    else:
        print(f"\nregression began on day {REGRESSION_DAY}, the detector fired on day {ALERTS[0]['day']}: lag {LAG_DAYS} day(s).")
        print(f"Say it as a commitment: we would notice a {REGRESSION_DROP:.0%} quality drop about {LAG_DAYS} day(s) after it starts, "
              f"with a {DRIFT_RULE['window']}-day window over daily samples. A smaller drop takes longer, or is never seen.")
    return DRIFT_RULE, LAG_DAYS


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see an alert on the eval score on the sixth day, none on latency, and a sentence stating the lag as a commitment. Stop here if the eval score alert is missing: the planted drop is smaller than the noise in your pool, so raise `REGRESSION_DROP` and ask what a real drop that size would cost.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    A shorter window notices sooner and fires on noise; a longer one is quieter and slower. Which would your users forgive first: a day of lag, or a false alarm every week? Pick a window for your prototype and say why.

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
    ## Task 5 of 6 — Load test the endpoint

    Usage spike is the one incident you can rehearse, because the failure is arithmetic. Every serving stack has a number of requests it can work on at once. Below it, more callers mean more throughput. Above it, requests queue, and more callers buy nothing but latency. You cannot guess that number: it depends on the runtime, the batch settings, the model, and the hardware. So measure it, with a few small fixed requests at rising concurrency, against whatever your `.env` points at. ⚠️ This is a real load generator aimed at a real endpoint. Point it at shared infrastructure without asking and you become the incident.
    """)
    return


@app.cell
def _(ThreadPoolExecutor, budget, complete, np, pd, time, ui, ws):
    LEVELS = budget([1, 4, 8], [1, 2])     # concurrent callers
    PER_CALLER = budget(3, 2)              # requests each caller sends
    PROBE = [{"role": "system", "content": "Reply with one word."},
             {"role": "user", "content": "Is the VPN client installed from the software centre? Answer yes or no."}]


    def one_request(_=None) -> tuple[float, bool]:
        """One small fixed request, not streamed: an early first token would hide the queue wait this is timing."""
        started = time.perf_counter()
        try:
            resp = complete(PROBE)
            ok = bool((resp.choices[0].message.content or "").strip())   # an empty reply is a failure, not a crash
        except Exception:                                                  # noqa: BLE001
            ok = False
        return (time.perf_counter() - started) * 1000, ok


    def at_concurrency(level: int, count: int) -> dict:
        wall = time.perf_counter()
        with ThreadPoolExecutor(max_workers=level) as pool:
            results = list(pool.map(one_request, range(count)))
        wall = time.perf_counter() - wall
        ms = [r[0] for r in results]
        return {"concurrency": level, "requests": count, "failed": sum(not r[1] for r in results),
                "req_per_s": round(count / wall, 3), "p50_ms": int(np.percentile(ms, 50)), "p95_ms": int(np.percentile(ms, 95))}


    one_request()                          # warm the connection so the first level is not penalised
    LOAD = [at_concurrency(c, c * PER_CALLER) for c in ui.track(LEVELS, "raising concurrency")]
    ws.save("load_test", LOAD)
    ui.table(pd.DataFrame(LOAD).set_index("concurrency"), title="throughput and latency as concurrency rises", float_fmt="{:.5g}")

    first, last = LOAD[0], LOAD[-1]
    gain_rps = last["req_per_s"] / first["req_per_s"] - 1
    gain_p50 = last["p50_ms"] / max(first["p50_ms"], 1) - 1
    LOAD_SENTENCE = (f"From {first['concurrency']} to {last['concurrency']} concurrent callers, throughput moved {gain_rps:+.0%} "
                     f"and p50 latency moved {gain_p50:+.0%}. ")
    LOAD_SENTENCE += ("Past the level where throughput flattens, extra callers buy wait, not work: rate limit before you scale."
                      if gain_p50 > gain_rps else
                      "Throughput is still rising faster than latency, so these levels have not found the saturation point; raise the top level and rerun.")
    print(LOAD_SENTENCE)
    return LOAD, LOAD_SENTENCE


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see one row per concurrency level with requests per second, p50 and p95 latency, a ✅ line for the load test, and a sentence the numbers support. Stop here if the failed column is not zero: the endpoint is refusing or timing out under load, and that is the first thing to report.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 6 of 6 — Save the traces and write the monitoring file

    Data boundaries arrive here with teeth. If questions contain customer data and your tracing backend keeps request bodies for ninety days, you have made a ninety-day copy of customer data in a system nobody classified. So the spans you save are redacted: the shape of the work in convention names, with `question_len` in place of the question. The monitoring file records the four metrics with their current values and says for each whether it was measured, looked up, or taken from the harness, then the drift rule with its lag, the load result, and what may be logged.
    """)
    return


@app.cell
def _(
    CALL_TOKENS,
    DRIFT_RULE,
    LAG_DAYS,
    LLM_MODEL,
    LOAD,
    LOAD_SENTENCE,
    PAGES,
    POOL,
    PRICE_PER_1K_TOKENS,
    REGRESSION_DROP,
    TRACES: list[dict],
    json,
    to_otel,
    ws,
):
    SAFE_TO_LOG = ["duration", "status", "token counts", "model requested and model served", "retrieval hits",
                   "question length", "eval score"]
    NOT_SAFE = ["the question", "the answer", "retrieved section text", "names inside any of them"]


    def redacted_span(record: dict) -> dict:
        """The shape of the work, not its content: enough to debug, not enough to leak."""
        row = to_otel(record)
        row.update(id=record["id"], parent=record["parent"])
        for key in ("k", "hits", "question_len", "refused", "empty"):
            if key in record["attributes"]:
                row[key] = record["attributes"][key]
        return row


    root_id = next(t["id"] for t in TRACES if t["name"] == "request")
    ONE_REQUEST = sorted((redacted_span(t) for t in TRACES if t["id"] == root_id or t["parent"] == root_id),
                         key=lambda r: r["parent"] is not None)
    assert all("question" not in r for r in ONE_REQUEST), "a span still carries the question text"
    ws.save("traces", ONE_REQUEST)

    CURRENT = [
        ("p50 / p95 latency", f"{LOAD[0]['p50_ms']} ms / {LOAD[0]['p95_ms']} ms", "measured: the load test at concurrency 1"),
        ("cost per request", f"${CALL_TOKENS / 1000 * PRICE_PER_1K_TOKENS:.5f}",
         f"lookup: {CALL_TOKENS} tokens from one measured request at ${PRICE_PER_1K_TOKENS} per 1k tokens"),
        ("refusal rate", f"{POOL['refused'].mean():.0%}", f"from your trajectories: {len(POOL)} harness runs, not live traffic"),
        ("eval score on traffic", f"{POOL['passed'].mean():.0%}", "from your trajectories: the harness pass rate, not live traffic yet"),
    ]
    lines = ["# Monitoring", "",
             f"Request path: keyword retrieval over {len(PAGES)} corpus pages plus one call to `{LLM_MODEL}`.", "",
             "## The four metrics", "", "| metric | current value | where it comes from |", "|---|---|---|"]
    lines += [f"| {m} | {v} | {src} |" for m, v, src in CURRENT]
    lines += ["", "## Drift rule", "",
              f"`detect_drift(window={DRIFT_RULE['window']}, tolerance={DRIFT_RULE['tolerance']})` over the daily eval score on sampled traffic.",
              (f"On a planted {REGRESSION_DROP:.0%} drop it fired {LAG_DAYS} day(s) after the regression began. "
               f"Commitment: a drop that size is noticed within about {LAG_DAYS + 1} days; a smaller one takes longer or is never seen.")
              if LAG_DAYS is not None else
              f"On a planted {REGRESSION_DROP:.0%} drop it did not fire within the week: the sample is too noisy for a drop this size.",
              "", "## Load", "", "| concurrency | requests | failed | req/s | p50 ms | p95 ms |", "|---|---|---|---|---|---|"]
    lines += [f"| {r['concurrency']} | {r['requests']} | {r['failed']} | {r['req_per_s']} | {r['p50_ms']} | {r['p95_ms']} |" for r in LOAD]
    lines += ["", LOAD_SENTENCE, "", "## What may be logged", "",
              "Safe to log: " + ", ".join(SAFE_TO_LOG) + ".", "", "Not safe: " + ", ".join(NOT_SAFE) + ".", "",
              "A redacted span:", "", "```json", json.dumps(ONE_REQUEST[0]), "```"]
    MONITORING = "\n".join(lines) + "\n"
    ws.save("monitoring", MONITORING)
    print(MONITORING)
    return (MONITORING,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see two ✅ lines and the monitoring file printed, with four metric rows, a drift rule with a lag, the load table, and the safe and unsafe lists. Stop here if the assertion fails: a span still carries the question text, and that must not be written anywhere.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Of the four metrics in your monitoring file, which is a measurement, which is a lookup, and which comes from the harness rather than live traffic? Which one would you have to build before launch, and who would run it?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    A normal runbook covers "the service is down". The table below is what it does not cover. Pick the one incident your prototype is most likely to have, write it into `MY_INCIDENT`, and write your first five minutes into `FIRST_FIVE_MINUTES`. The shape is always the same: is it still happening; what changed, in the order your deploy, their model, the corpus, the traffic; stop the bleeding before you understand it; then investigate. The cell appends your plan to the monitoring file.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    | Incident | How you find out | First move |
    |---|---|---|
    | Silent quality regression | The eval score, if you have it; otherwise a user, eventually | Diff the prompt, the model version, the corpus |
    | Vendor swapped the model | Behaviour changes with no deploy of yours | Pin the version, then rerun the harness |
    | Prompt injection in the wild | An output check fires, or a user reports something odd | Keep the input; add it to the regression set |
    | Cost spike | The bill, or a cost-per-request alert | Find the loop: a retry, or an agent that never stops |
    | Usage spike | Latency, then errors, then a queue | Rate limit before you scale |
    | Corpus poisoned | Answers confidently cite something wrong | Find the document and treat it as injection |
    """)
    return


@app.cell
def _(MONITORING, ws):
    MY_INCIDENT = ""             # one row from the table, in your words
    FIRST_FIVE_MINUTES = ""      # what you do, in order, before you understand why

    if MY_INCIDENT and FIRST_FIVE_MINUTES:
        ws.save("monitoring", MONITORING + f"\n## Incident: {MY_INCIDENT}\n\n{FIRST_FIVE_MINUTES}\n")
    else:
        print("fill in MY_INCIDENT and FIRST_FIVE_MINUTES, then rerun")
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
    | A `span` context manager and a list | The OpenTelemetry SDK, a collector, sampling, and a backend |
    | Four attribute names copied by hand | The GenAI semantic conventions emitted by an instrumentation library |
    | A simulated week in a table | Prometheus and Grafana, or your cloud's equivalent |
    | A mean-and-stdev drift detector | The same rule per slice, seasonality handled, an on-call rota |
    | A pass rate over your trajectories | A continuous sample of live traffic scored by your eval harness |
    | A few dozen requests at three concurrency levels | A scheduled load test on a replica, the vendor's rate limits in the plan |
    | A redaction function | A data-loss-prevention policy enforced at the collector, audited |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - The eval score runs on sampled live traffic before launch, with the detection lag written next to it.
    - A cost-per-request alert exists before the first invoice, not after it.
    - Prompts and responses are classified before any collector retains them, and the retention period is a decision someone signed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Run this notebook as an ops console: `uv run marimo run 22_Observability/Observability_and_Incidents.py --headless -p 8080`, point `handle_request` at your prototype, and leave it open on a screen. The eval harness and the console are the same file.
    - Alert on cost per request, not total cost. Total cost rises with success; cost per request rising means a loop, and it catches a runaway agent on the first day rather than on the first invoice.
    - Run `detect_drift` over your own judge scores, if you have been recording them, and find out whether anything moved that nobody noticed.
    """)
    return


if __name__ == "__main__":
    app.run()
