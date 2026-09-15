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
    # Release decision

    A plausible answer is not a shippable one. This notebook runs two versions of your assistant against the eval cases you wrote, scores both with DeepEval, and turns the scores into a ship or hold decision with the failing tests named.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    A release decision as pass/fail evidence: a contract of eval cases, two versions of the assistant, and three metrics per case with a judge on your own endpoint.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    Both versions run over your eval cases, one result row per metric, and a release decision written from the numbers.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    Rerun before the demo and read the decision aloud. Bring your team one pass and one failure and say which metric caught it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 40 minutes
    **Reads:** eval_cases, corpus
    **Writes:** deepeval_results, release_decision
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    The chat model comes from `.env` and doubles as the judge. DeepEval runs locally; no account, no login. The cell opts out of its telemetry and its own `.env` loading so the repository's settings win.
    """)
    return


@app.cell
def _():
    import json, os, re, textwrap, time

    os.environ.setdefault("DEEPEVAL_DISABLE_DOTENV", "1")
    os.environ.setdefault("DEEPEVAL_TELEMETRY_OPT_OUT", "YES")

    from langchain.agents import create_agent
    from langchain.tools import tool
    from langchain_core.messages import AIMessage, ToolMessage
    from langchain_openai import ChatOpenAI
    from openai import OpenAI

    from helpers.config import KEY, LLM_BASE, LLM_MODEL, require, budget
    from helpers import workspace as ws
    from helpers.llm import chat_model, client

    require("OPENAI_API_KEY")
    llm = chat_model()
    client = client()

    EVAL_CASES = ws.load("eval_cases")
    CORPUS_DIR = ws.load_path("corpus")
    PAGES = [{"name": str(p.relative_to(CORPUS_DIR)), "text": p.read_text(encoding="utf-8")}
             for p in sorted(CORPUS_DIR.rglob("*.md"))]
    CASES = EVAL_CASES[:budget(6, 2)]
    print(f"✅ model {LLM_MODEL}; {len(CASES)} of {len(EVAL_CASES)} eval cases; {len(PAGES)} corpus pages; "
          f"source: {ws.source('eval_cases')}")
    return (
        AIMessage,
        CASES,
        LLM_MODEL,
        PAGES,
        ToolMessage,
        client,
        create_agent,
        json,
        llm,
        re,
        textwrap,
        time,
        tool,
        ws,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with the model, how many cases will run, and a page count over three. Stop here if the case count is zero: write the eval cases first, or let the seed carry them.
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
    ## Task 1 of 7 — Read the contract before any model runs

    Each eval case is a question and a reference answer. Two teammates should reach the same pass or fail verdict from the reference alone, and the reference must be answerable from the corpus. Read every case now, before you see a model output, so the model's habits do not become your criteria.
    """)
    return


@app.cell
def _(CASES):
    import pandas as pd
    for _c in CASES:
        assert _c.get('reference', '').strip(), f"case {_c['id']} has no reference answer"
    pd.DataFrame(CASES)[['id', 'question', 'reference']]
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a table with one row per case and a non-empty reference in each. Stop here if the assertion fires: a case without a reference cannot be scored for correctness, so fix the eval cases first.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 7 — Version one, the prompt-only answerer

    The first version is the prototype most teams demo first: a system prompt and the question, no retrieval. It sounds fine and it invents. Keep it, because an eval earns its keep by telling two versions apart, and this is the version it must catch.
    """)
    return


@app.cell
def _(CASES, llm, textwrap):
    V1_SYSTEM = 'You are the internal helpdesk assistant. Answer the question directly and briefly.'

    def answer_v1(question: str) -> dict:
        reply = llm.invoke([{'role': 'system', 'content': V1_SYSTEM}, {'role': 'user', 'content': question}])
        return {'answer': reply.content if isinstance(reply.content, str) else str(reply.content), 'contexts': []}
    _sample = answer_v1(CASES[0]['question'])
    print(CASES[0]['question'])
    print('v1:', textwrap.shorten(_sample['answer'], 300))
    return (answer_v1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the first question and a confident short answer. Stop here if the answer is empty: the model call failed silently, so check the endpoint in your `.env`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Read the v1 answer against the reference. Which claims in it does the corpus support, and which did the model supply on its own?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 7 — Version two, the retrieval agent

    The second version retrieves before it answers. A keyword search over the corpus pages is the tool, `create_agent` is the loop, and the system prompt tells the model to answer only from what the tool returned. The `run` helper keeps the tool results, because an answer without its evidence cannot be attributed.
    """)
    return


@app.cell
def _(
    AIMessage,
    CASES,
    PAGES,
    ToolMessage,
    create_agent,
    llm,
    re,
    textwrap,
    tool,
):
    STOP = {'a', 'an', 'and', 'are', 'as', 'at', 'be', 'for', 'from', 'how', 'i', 'in', 'is', 'it', 'of', 'on', 'or', 'the', 'to', 'what', 'when', 'with', 'my', 'can', 'do', 'you', 'me'}

    def terms(text: str) -> set[str]:
        return {t for t in re.findall('[a-z0-9][a-z0-9-]+', text.lower()) if t not in STOP}

    def retrieve(question: str, k: int=2) -> list[dict]:
        q = terms(question)
        ranked = sorted(PAGES, key=lambda p: len(q & terms(p['text'])), reverse=True)
        return [p for p in ranked[:k] if q & terms(p['text'])]

    @tool
    def search_corpus(query: str) -> str:
        """Search the knowledge base for the pages most relevant to the query."""
        hits = retrieve(query)
        if not hits:
            return 'No page matched.'
        return '\n\n'.join((f"[{p['name']}]\n{textwrap.shorten(p['text'], 1200)}" for p in hits))
    V2_SYSTEM = 'You are the internal helpdesk assistant. Call search_corpus before answering.\nAnswer only from what the tool returned and name the page in brackets. If the pages do not answer the question, say so.'
    agent = create_agent(model=llm, tools=[search_corpus], system_prompt=V2_SYSTEM)

    def answer_v2(question: str) -> dict:
        result = agent.invoke({'messages': [{'role': 'user', 'content': question}]})
        answers, contexts = ([], [])
        for m in result['messages']:
            if isinstance(m, AIMessage) and m.content:
                answers.append(m.content if isinstance(m.content, str) else str(m.content))
            elif isinstance(m, ToolMessage):
                contexts.append(str(m.content))
        return {'answer': answers[-1] if answers else '', 'contexts': contexts}
    _sample = answer_v2(CASES[0]['question'])
    print('v2:', textwrap.shorten(_sample['answer'], 300))
    print('contexts:', len(_sample['contexts']))
    return answer_v2, retrieve


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a v2 answer that names a page in brackets and a context count of one or more. Stop here if the context count is zero: the agent answered without calling the tool, so the system prompt is not steering it.
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
    ## Task 4 of 7 — Produce every output, both versions

    Both versions answer every case. Each run keeps the answer and its retrieval context together. For v2 that context is what the tool returned. For v1, which retrieved nothing, it is the pages it should have used, so faithfulness measures whether a prompt-only answer contradicts the knowledge base.
    """)
    return


@app.cell
def _(CASES, answer_v1, answer_v2, retrieve, textwrap, time):
    RUNS: list[dict] = []
    for _c in CASES:
        for version, fn in (('v1', answer_v1), ('v2', answer_v2)):
            started = time.perf_counter()
            out = fn(_c['question'])
            contexts = out['contexts'] or [f"[{p['name']}]\n{textwrap.shorten(p['text'], 1200)}" for p in retrieve(_c['question'])]
            RUNS.append({'test': _c['id'], 'version': version, 'question': _c['question'], 'reference': _c['reference'], 'answer': out['answer'], 'contexts': contexts or ['No page matched.'], 'latency_s': round(time.perf_counter() - started, 1)})
            print(f"{_c['id']:<8} {version}  {RUNS[-1]['latency_s']:>5}s  {textwrap.shorten(out['answer'], 90)}")
    return (RUNS,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see two lines per case, v1 then v2, each with a latency and the start of the answer. Stop here if any answer is blank: that run will fail every metric, and you want to know now whether that is the model or the harness.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Pick one case where v1 and v2 disagree. Without a judge, which do you believe, and what in the corpus settles it?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5 of 7 — Connect DeepEval to your endpoint and pick three metrics

    DeepEval's metrics are judge prompts that expect JSON. The wrapper below appends the requested schema to the prompt, sends it to your endpoint, parses the first JSON object, and retries once with the validation error. A malformed verdict becomes an error, never an invented score. Three metrics, each blaming a different component: relevancy and faithfulness for the generator, a G-Eval correctness check against your reference for the product.
    """)
    return


@app.cell
def _(LLM_MODEL, client, json):
    from pydantic import BaseModel
    from deepeval.models import DeepEvalBaseLLM
    from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric, GEval
    from deepeval.test_case import LLMTestCase, SingleTurnParams


    def first_json_object(text: str) -> str:
        start = text.find("{")
        if start < 0:
            raise ValueError("judge returned no JSON object")
        depth, quoted, escaped = 0, False, False
        for i in range(start, len(text)):
            ch = text[i]
            if quoted:
                if escaped:
                    escaped = False
                elif ch == "\\":
                    escaped = True
                elif ch == '"':
                    quoted = False
            elif ch == '"':
                quoted = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    return text[start:i + 1]
        raise ValueError("judge returned an incomplete JSON object")


    class EndpointJudge(DeepEvalBaseLLM):
        """DeepEval judge over the OpenAI-compatible endpoint in .env."""

        def __init__(self, model_name: str):
            self.model_name = model_name
            super().__init__(model=model_name)

        def load_model(self):
            return client

        def get_model_name(self) -> str:
            return self.model_name

        def generate(self, prompt: str, schema: type[BaseModel] | None = None, **kwargs):
            contract = ""
            if schema is not None:
                contract = ("\n\nOUTPUT CONTRACT\nReturn exactly one JSON object and no markdown. It must validate "
                            "against this JSON Schema:\n" + json.dumps(schema.model_json_schema()))
            messages = [{"role": "user", "content": prompt + contract}]
            last_error = None
            for _ in range(2):
                if last_error:
                    messages.append({"role": "user", "content": f"That failed validation: {last_error}. Return one corrected JSON object only."})
                text = client.chat.completions.create(model=self.model_name, messages=messages, temperature=0).choices[0].message.content or ""
                if schema is None:
                    return text
                try:
                    return schema.model_validate_json(first_json_object(text))
                except Exception as exc:
                    last_error = str(exc)
                    messages.append({"role": "assistant", "content": text})
            raise ValueError(f"judge output failed schema validation twice: {last_error}")

        async def a_generate(self, prompt: str, schema: type[BaseModel] | None = None, **kwargs):
            return self.generate(prompt, schema=schema, **kwargs)


    judge = EndpointJudge(LLM_MODEL)
    THRESHOLDS = {"answer_relevancy": 0.7, "faithfulness": 0.8, "correctness": 0.7}


    def metric_suite() -> dict:
        return {
            "answer_relevancy": AnswerRelevancyMetric(threshold=THRESHOLDS["answer_relevancy"], model=judge, async_mode=False),
            "faithfulness": FaithfulnessMetric(threshold=THRESHOLDS["faithfulness"], model=judge, async_mode=False),
            "correctness": GEval(
                name="Correctness",
                evaluation_steps=[
                    "Compare the actual output with the expected output.",
                    "Check every setting, menu path, role, wait time, and command the expected output names.",
                    "Penalise a contradiction, an invented step, or an omitted step that would change what the user does.",
                    "Do not penalise concise wording or accurate extra detail.",
                ],
                evaluation_params=[SingleTurnParams.INPUT, SingleTurnParams.ACTUAL_OUTPUT, SingleTurnParams.EXPECTED_OUTPUT],
                threshold=THRESHOLDS["correctness"], model=judge, async_mode=False,
            ),
        }


    print(judge.get_model_name(), list(metric_suite()))
    return LLMTestCase, THRESHOLDS, metric_suite


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the judge model name and the three metric names. Stop here if the import of `deepeval` fails: it is in the root environment, so run `make setup` from the repository root.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 6 of 7 — Score every run and save the results

    One test case per run, three metrics each. Each result row keeps the test id, the version, the metric, the score, whether it passed its threshold, and the judge's reason. A judge that errors is recorded as a failed row with the error, because failing closed is what makes a gate worth trusting. This is the long cell.
    """)
    return


@app.cell
def _(
    LLMTestCase,
    RUNS: list[dict],
    THRESHOLDS,
    metric_suite,
    pd,
    textwrap,
    ws,
):
    RESULTS: list[dict] = []
    for _r in RUNS:
        case = LLMTestCase(name=f"{_r['version']}::{_r['test']}", input=_r['question'], actual_output=_r['answer'], expected_output=_r['reference'], retrieval_context=_r['contexts'])
        for name, metric in metric_suite().items():
            _row = {'test': _r['test'], 'version': _r['version'], 'metric': name, 'threshold': THRESHOLDS[name]}
            try:
                metric.measure(case, _show_indicator=False)
                _row.update(score=round(float(metric.score), 3), passed=bool(metric.is_successful()), reason=textwrap.shorten(metric.reason or '', 300), error=None)
            except Exception as exc:
                _row.update(score=None, passed=False, reason=None, error=f'{type(exc).__name__}: {exc}'[:200])
            RESULTS.append(_row)
            print(f"{_r['test']:<8} {_r['version']}  {name:<17} {(_row['score'] if _row['score'] is not None else 'error'):>6}  {('pass' if _row['passed'] else 'FAIL')}")
    ws.save('deepeval_results', RESULTS)
    pd.DataFrame(RESULTS).pivot(index=['version', 'test'], columns='metric', values='score')
    return (RESULTS,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see one line per test, version, and metric, a ✅ line, and a pivot of scores with v1 and v2 side by side. Stop here if a whole column is error: the judge is not returning JSON, so print one `metric.reason` and read what came back.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Find a run where faithfulness passed and correctness failed. What does that combination say about the retrieved pages versus the answer?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 7 of 7 — Write the release decision

    Turn the result rows into a decision a script could check. The case set is fingerprinted first, so a decision made over different cases cannot be read against this one. Each version gets a mean score per metric, with an errored row counting as zero. `compare` gives the delta from v1 to v2 and refuses when the fingerprints differ. `gate` holds v2 against the minimum per metric in `MINIMUM` and names every metric under its bar. Ship v2 when the gate passes, no metric drops against v1 by more than `TOLERANCE`, and no judge errored. Otherwise hold, naming the failing metric. Save the decision as markdown a judge can read in a minute.
    """)
    return


@app.cell
def _(CASES, LLM_MODEL, RESULTS: list[dict], THRESHOLDS, ws):
    from collections import defaultdict
    from IPython.display import Markdown, display
    from helpers.evals import compare, fingerprint, gate
    MINIMUM = {'answer_relevancy': 0.7, 'faithfulness': 0.8, 'correctness': 0.7}
    # The lowest mean score per metric v2 must clear, and the drop against v1 that
    # counts as noise rather than a regression. Revisit both in "Your turn".
    TOLERANCE = 0.05
    CASE_SET = fingerprint(CASES)
    METRICS = list(THRESHOLDS)

    def mean_scores(version: str) -> dict[str, float]:
        out = {}
        for name in METRICS:
            rows = [r for r in RESULTS if r['version'] == version and r['metric'] == name]
            out[name] = round(sum((r['score'] or 0.0 for r in rows)) / max(len(rows), 1), 3)
        return out
    SCORES = {v: mean_scores(v) for v in ('v1', 'v2')}
    RUN = {v: {'fingerprint': CASE_SET, 'scores': SCORES[v]} for v in SCORES}
    COMPARISON = compare(RUN['v1'], RUN['v2'])
    GATE = gate(SCORES['v2'], MINIMUM)
    regressed = [m for m, d in COMPARISON['delta'].items() if d < -TOLERANCE]
    errors = sum((1 for row in RESULTS if row['error']))
    by_case = defaultdict(list)
    for _row in RESULTS:
        by_case[_row['version'], _row['test']].append(_row)
    case_pass = {k: all((x['passed'] for x in v)) for k, v in by_case.items()}
    rate = {v: sum((case_pass[v, c['id']] for c in CASES)) / len(CASES) for v in ('v1', 'v2')}
    failing = {v: [c['id'] for c in CASES if not case_pass[v, c['id']]] for v in ('v1', 'v2')}
    ship = GATE['passed'] and COMPARISON['comparable'] and (not regressed) and (errors == 0)
    decision = 'SHIP v2' if ship else 'HOLD'
    lines = [f'# Release decision: {decision}', '', f'Model `{LLM_MODEL}`, {len(CASES)} eval cases, case set `{CASE_SET}`, three DeepEval metrics per case.', '', '| version | pass rate | failing tests |', '|---|---|---|']
    for v in ('v1', 'v2'):
        lines.append(f"| {v} | {rate[v]:.0%} | {', '.join(failing[v]) or 'none'} |")
    lines += ['', '## Gate on v2, mean score per metric', '', '| metric | minimum | v1 | v2 | delta | gate |', '|---|---|---|---|---|---|']
    for m in METRICS:
        delta = COMPARISON['delta'].get(m)
        lines.append(f"| {m} | {MINIMUM.get(m, 0):.2f} | {SCORES['v1'][m]:.2f} | {SCORES['v2'][m]:.2f} | {delta:+.2f} | {('FAIL' if m in GATE['failed'] else 'pass')} |" if delta is not None else f"| {m} | {MINIMUM.get(m, 0):.2f} | {SCORES['v1'][m]:.2f} | {SCORES['v2'][m]:.2f} | not comparable | {('FAIL' if m in GATE['failed'] else 'pass')} |")
    comparable = 'same case set' if COMPARISON['comparable'] else f"not comparable: {COMPARISON['reason']}"
    lines += ['', f"Gate: {('passed' if GATE['passed'] else 'failed on ' + ', '.join(GATE['failed']))}. Comparison v1 to v2: {comparable}. Judge errors: {errors}.", '', '## Why', '']
    if ship:
        lines.append(f'v2 clears every minimum, drops no metric against v1 by more than {TOLERANCE:.2f}, and no judge errored.')
    else:
        reasons = [f"the gate failed on {', '.join(GATE['failed'])}"] if GATE['failed'] else []
        reasons += [f"the versions are not comparable ({COMPARISON['reason']})"] if not COMPARISON['comparable'] else []
        reasons += [f"v2 regressed on {', '.join(regressed)} by more than {TOLERANCE:.2f}"] if regressed else []
        reasons += [f'{errors} judge error(s) must be resolved'] if errors else []
        lines.append('Hold because ' + '; '.join(reasons) + '.')
    lines += ['', '## Failing metrics on v2', '']
    for _row in RESULTS:
        if _row['version'] == 'v2' and (not _row['passed']):
            lines.append(f"- {_row['test']} {_row['metric']} {_row['score']}: {_row['reason'] or _row['error']}")
    if not failing['v2']:
        lines.append('- none')
    DECISION_MD = '\n'.join(lines)
    display(Markdown(DECISION_MD))
    print(f"{decision}: gate {('passed' if GATE['passed'] else 'failed on ' + ', '.join(GATE['failed']))}; case set {CASE_SET}")
    ws.save('release_decision', DECISION_MD)
    return (case_pass,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the rendered decision with the case set fingerprint, a gate table with a FAIL on every metric under its minimum, a printed verdict line, and a ✅ line. Stop here if the gate fails on a metric whose per-case rows all passed: the mean is below the bar because a judge error scored zero.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Add a deterministic check as a fourth verdict. Pick two or three words from each reference that any correct answer must contain, test the answers for them with whole-word matching, and count how often the string check and the judge disagree. Then change one entry in `MINIMUM` or the `TOLERANCE`, rerun the decision, and say which metric the gate names now. Explain to a teammate which check you would trust in a release gate and why that bar is the right one.
    """)
    return


@app.cell
def _(RUNS: list[dict], case_pass, re):
    # Shape: MUST[test id] = words a correct answer must contain; a whole-word match; a row per run.
    MUST: dict[str, list[str]] = {}

    def has_word(text: str, word: str) -> bool:
        return re.search('(?<![a-z0-9])' + re.escape(word.lower()) + '(?![a-z0-9])', text.lower()) is not None
    for _r in RUNS:
        words = MUST.get(_r['test'], [])
        if words:
            missing = [w for w in words if not has_word(_r['answer'], w)]
            judge_pass = case_pass[_r['version'], _r['test']]
            print(f"{_r['test']} {_r['version']}: string {('pass' if not missing else 'FAIL ' + str(missing))}; judge {('pass' if judge_pass else 'FAIL')}")
    if not MUST:
        print('fill MUST with words per test id, then rerun')
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
    | A handful of eval cases with one reference each | Hundreds of cases mined from real failures, versioned with the app |
    | Three DeepEval metrics with guessed thresholds | At most five metrics, thresholds calibrated against human labels |
    | The same model as assistant and judge | A separate judge model, checked for agreement with hand verdicts |
    | A notebook loop that prints failures | `deepeval test run` in CI, blocking the merge on a regression |
    | One pass rate per version | Per-case and per-component gates, so one layer's regression cannot hide in the average |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - The contract under version control; a case is only removed with a reason.
    - Thresholds agreed before scoring.
    - The decision names the failing tests, never only a pass rate.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Add a contextual recall metric and split the blame: a v2 failure with low recall belongs to retrieval, one with high recall belongs to the prompt.
    - Run every case three times and report the spread per metric; a threshold inside the spread is not a gate.
    - Write hand verdicts for every run before you read the scores, then report where the judge disagrees with you and which side was right.
    """)
    return


if __name__ == "__main__":
    app.run()
