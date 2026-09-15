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
    # Vibe checks and judges

    Your agent produced transcripts. You have no way yet to say whether they are any good. The trap is to wire up a model judge first. The right first step is a deliberate vibe check: a written rubric, your own verdicts, one line of reasoning each. Then a judge, checked against you.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    Why a deliberate vibe check comes before a model judge: a written rubric, your own verdicts, one line of reasoning each. Then two scorers that cannot judge at all, to fix the floor and the ceiling any judge sits between.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    A rubric and vibe checks for your product, three judges run over your transcripts, your hand scores attached, a table of where the judges disagree with each other and with you, and an interval on every agreement number.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    Production evals use a separate judge model, human calibration on a sample, and release thresholds. Bring your team one disagreement and say which evidence you trusted.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 35 minutes
    **Reads:** charter, transcripts
    **Writes:** rubric, vibe_checks, judge_scores
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    The judge model defaults to the same model that wrote the answers. That is convenient and it is a limitation, so the saved records name both.
    """)
    return


@app.cell
def _():
    import json

    import litellm
    import pandas as pd

    from helpers.config import KEY, LLM_BASE, LLM_MODEL, require
    from helpers import workspace as ws, ui
    from helpers.brand import matplotlib_style

    require("OPENAI_API_KEY")
    litellm.suppress_debug_info = True
    MODEL = LLM_MODEL if (LLM_MODEL.startswith(("openai/", "anthropic/")) or not LLM_BASE) else "openai/" + LLM_MODEL
    JUDGE_MODEL = MODEL

    def LLM(messages, **kw):
        kw.setdefault("api_key", KEY)
        if LLM_BASE and MODEL.startswith("openai/"):
            kw.setdefault("api_base", LLM_BASE)
        return litellm.completion(model=kw.pop("model", MODEL), messages=messages, **kw)

    CHARTER = ws.load("charter")
    TRANSCRIPTS = ws.load("transcripts")
    ROWS = [{"id": t["id"], "question": t["turns"][0]["content"],
             "response": next((x["content"] for x in reversed(t["turns"]) if x["role"] == "assistant"), ""),
             "tools": [c["name"] for c in t.get("tool_calls", [])],
             "evidence": "\n".join(c.get("result", "") for c in t.get("tool_calls", []))}
            for t in TRANSCRIPTS]
    print(f"✅ {len(ROWS)} transcripts to judge; model {MODEL}")
    return (
        CHARTER,
        JUDGE_MODEL,
        LLM,
        MODEL,
        ROWS,
        json,
        matplotlib_style,
        pd,
        ui,
        ws,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with a transcript count of at least four. Stop here if it is zero: run the agents notebook first, or let the seed carry it.
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
    ## Task 1 of 9 — Write the rubric

    A rubric is a list of aspects, each with one sentence on what pass looks like. Read it before judging anything. You are the judge, so you need to know what you are judging. Edit the aspects to match your charter.
    """)
    return


@app.cell
def _(ws):
    RUBRIC = {"criteria": [
        {"aspect": "grounded", "pass": "Every fact in the answer comes from the charter or a tool result."},
        {"aspect": "actionable", "pass": "The answer names the exact next step, menu path, or entitlement."},
        {"aspect": "in scope", "pass": "Out-of-scope questions are declined in one sentence, not answered."},
        {"aspect": "hands off safely", "pass": "Requests that need a person are logged and the user gets an id."},
        {"aspect": "concise", "pass": "No preamble, no repetition; a user can act on it in under a minute."},
    ]}
    ws.save("rubric", RUBRIC)
    for c in RUBRIC["criteria"]:
        print(f"{c['aspect']:<18} pass = {c['pass']}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line and five aspects with their pass definitions. Stop here if two aspects overlap: merge them, or the judges will disagree for no reason.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 9 — Write the vibe checks

    A vibe check is an input plus what a good answer must contain. Start from the example questions in your charter and add two of your own. These become the eval cases the retrieval notebooks reuse.
    """)
    return


@app.cell
def _(ws):
    VIBE_CHECKS = [
        {"id": "v01", "input": "My VPN connects but I cannot reach staging.", "expected": "Names the routing setting and the menu path; offers to open a ticket."},
        {"id": "v02", "input": "How do I get access to the analytics warehouse?", "expected": "Names the entitlement, who approves it, and the expected wait."},
        {"id": "v03", "input": "uv sync removed a package I installed.", "expected": "Explains that a plain sync drops optional groups; gives the make setup command."},
        {"id": "v04", "input": "Can you reset my colleague's MFA for me?", "expected": "Declines; MFA resets need verification with the account holder."},
        {"id": "v05", "input": "What is the capital of Peru?", "expected": "Declines in one sentence as outside the product's scope."},
    ]
    ws.save("vibe_checks", VIBE_CHECKS)
    return (VIBE_CHECKS,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with five rows. Edit the inputs to your own product before you move on; the seed inputs are about the example helpdesk.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which of your five vibe checks would the agent most plausibly fail, and what would that failure look like in a transcript?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 9 — Judge by hand first

    Read each transcript against the rubric and record a verdict: `pass`, `mixed`, or `fail`, with one line of reasoning. If you are writing a paragraph, you are being too thorough. Your verdicts are the bar the model judge is measured against.
    """)
    return


@app.cell
def _(ROWS):
    for _r in ROWS:
        print(f"=== {_r['id']} | tools: {_r['tools'] or 'none'}\nQ: {_r['question']}\nA: {_r['response'][:600]}\n")
    return


@app.cell
def _(ROWS):
    # Edit each entry. Replace the empty strings with your verdict and one line of reasoning.
    YOUR_VERDICTS = {r['id']: {'verdict': '', 'rationale': ''} for r in ROWS}
    YOUR_VERDICTS['t01'] = {'verdict': 'pass', 'rationale': 'Grounded in the charter and names the next step.'}  # example
    from helpers.config import SEED_MODE
    if SEED_MODE:
        for _r in ROWS:  # the instructors' example verdicts, so the seed carries a human column
            YOUR_VERDICTS[_r['id']] = {'verdict': 'pass', 'rationale': 'Used a tool and answered from it.'} if _r['tools'] else {'verdict': 'mixed', 'rationale': 'Answered without checking a source.'}
    SCALE = {'pass': 10, 'mixed': 5, 'fail': 0}
    HUMAN = [{'id': rid, 'judge': 'human', 'score': SCALE.get(v['verdict']), 'rationale': v['rationale']} for rid, v in YOUR_VERDICTS.items() if v['verdict']]
    print(f'{len(HUMAN)} of {len(ROWS)} transcripts judged by hand')
    return HUMAN, SCALE


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a count of how many you judged. Fill in at least four before continuing; an empty verdict is skipped.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 9 — Two dumb baselines before any judge

    Before you trust any judge, find out what the agreement number reads when no judging happens. Two scorers that cannot judge: an echo that gives every transcript the middle score, and an oracle that copies your hand score. Run both through the agreement measure the judges get later: per transcript, one minus the gap to your score over ten, then the mean. Echo is the floor a judge must clear. Oracle is the ceiling, and if it reads anything but 1.0 the measure is broken. No model call here.
    """)
    return


@app.cell
def _(HUMAN, SCALE):
    def agreement(scores: dict, human: dict) -> list:
        """Per-transcript agreement with your hand score: 1.0 is the same score, 0.0 is ten points apart."""
        return [1 - abs(scores[i] - human[i]) / 10 for i in human if i in scores]


    human_by_id = {h["id"]: h["score"] for h in HUMAN}
    assert human_by_id, "judge at least four transcripts by hand first"
    echo = {i: SCALE["mixed"] for i in human_by_id}    # has read nothing and says "mixed" every time
    oracle = dict(human_by_id)                         # cheats: copies your verdicts
    for name, scorer in [("echo", echo), ("oracle", oracle)]:
        per_row = agreement(scorer, human_by_id)
        print(f"{name:<8} agreement {sum(per_row) / len(per_row):.2f}   per transcript {per_row}")
    return agreement, echo, oracle


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see echo well below 1.0 and oracle at exactly 1.0. Stop here if oracle reads anything else: the agreement measure is wrong, and every judge number that follows would be wrong with it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which aspect was hardest to apply consistently, and what would you change in its pass definition?

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
    ## Task 5 of 9 — Build a strict judge

    A judge is another model call with a narrow job. Ask for JSON, then validate it before accepting it: an integer score from 0 to 10, a non-empty rationale, a parseable object. Malformed output is retried once and then reported, never turned into a neutral score.
    """)
    return


@app.cell
def _(JUDGE_MODEL, LLM, ROWS, json):
    def json_blocks(text: str):
        blocks, depth, start, in_str, esc = ([], 0, None, False, False)
        for i, ch in enumerate(text or ''):
            if esc:
                esc = False
                continue
            if ch == '\\' and in_str:
                esc = True
                continue
            if ch == '"':
                in_str = not in_str
                continue
            if in_str:
                continue
            if ch == '{':
                if depth == 0:
                    start = i
                depth = depth + 1
            elif ch == '}' and depth > 0:
                depth = depth - 1
                if depth == 0 and start is not None:
                    blocks.append(text[start:i + 1])
                    start = None
        return blocks

    def parse_judge(text: str) -> dict:
        for blob in reversed(json_blocks(text)):
            try:
                obj = json.loads(blob)
            except json.JSONDecodeError:
                continue
            score, rationale = (obj.get('score'), obj.get('rationale'))
            if isinstance(score, int) and (not isinstance(score, bool)) and (0 <= score <= 10) and isinstance(rationale, str) and rationale.strip():
                return {'score': score, 'rationale': rationale.strip()}
        raise ValueError(f"invalid judge reply: {(text or '')[:120]!r}")
    JUDGE_SYSTEM = 'Evaluate only the requested dimension. Reply with one JSON object: {"score": <integer 0-10>, "rationale": "<one specific sentence>"}.'

    def make_judge(name: str, template: str, retries: int=1):

        def judge(row: dict) -> dict:
            prompt = template
            for key in ('question', 'response', 'evidence'):  # replace, not format: the charter may contain braces
                prompt = prompt.replace('{' + key + '}', str(row.get(key, '')))
            messages = [{'role': 'system', 'content': JUDGE_SYSTEM}, {'role': 'user', 'content': prompt}]
            for attempt in range(retries + 1):
                if attempt:
                    messages.append({'role': 'user', 'content': 'That was invalid. Return only the JSON object.'})
                resp = LLM(messages, model=JUDGE_MODEL, temperature=0.0)
                try:
                    return {'id': row['id'], 'judge': name, **parse_judge(resp.choices[0].message.content)}
                except ValueError as e:
                    last = e
            raise RuntimeError(f'judge {name} failed twice') from last
        judge.name = name
        return judge
    smoke = make_judge('smoke', 'Question: {question}\nResponse: {response}\n\nScore how well the response answers the question.')
    repeat = [smoke(ROWS[0])['score'] for _ in range(3)]
    print('same answer, three judge calls:', repeat, 'range', max(repeat) - min(repeat))
    return (make_judge,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see three scores for the same answer and their range. A range of 0 is common at temperature 0 and is not guaranteed. Stop here if you get a RuntimeError: the model is not returning JSON, so print a raw reply and adjust the system line.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 6 of 9 — Three judges that measure different things

    An answer can be clear and wrong. It can be grounded and useless. One score cannot carry that. Build three judges: groundedness against the charter and tool evidence, actionability against the rubric, and clarity on its own. Each judges only its dimension.
    """)
    return


@app.cell
def _(CHARTER, ROWS, make_judge):
    groundedness = make_judge("groundedness", """CHARTER:
    """ + CHARTER + """

    TOOL EVIDENCE:
    {evidence}

    Question: {question}
    Response: {response}

    Score groundedness from 0 to 10. A 10 means every factual claim is supported by the charter or the tool evidence.
    Penalise plausible details that appear in neither.""")

    actionable = make_judge("actionable", """Question: {question}
    Response: {response}

    Score from 0 to 10 how actionable the response is: does it name the exact next step, setting, or entitlement,
    or decline cleanly when the question is outside scope? Do not reward length.""")

    clarity = make_judge("clarity", """Question: {question}
    Response: {response}

    Score clarity from 0 to 10: can a reader act on this on the first pass? Judge only readability,
    not whether the facts are right.""")

    JUDGES = [groundedness, actionable, clarity]
    print(groundedness(ROWS[0]))
    return (JUDGES,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see one judge result with a score and a one-sentence rationale. Stop here if the rationale talks about clarity when you asked for groundedness: the prompt is leaking dimensions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Read the groundedness rationale for the first transcript. Does it point at a line of the charter or the tool evidence, or does it restate the answer? What does that tell you about the prompt?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 7 of 9 — Score everything and save

    Run every judge on every transcript. Keep the record flat: one row per transcript per judge, with your hand score attached where you gave one. That file is the evidence, and it is what the prompt-optimisation notebook trains against.
    """)
    return


@app.cell
def _(HUMAN, JUDGES, JUDGE_MODEL, MODEL, ROWS, pd, ui, ws):
    human_by_id_1 = {h['id']: h['score'] for h in HUMAN}
    SCORES = list(HUMAN)
    for row in ui.track(ROWS, 'judging'):
        for judge in JUDGES:
            result = judge(row)
            result.update({'human_score': human_by_id_1.get(row['id']), 'judge_model': JUDGE_MODEL, 'assistant_model': MODEL})
            SCORES.append(result)
    ws.save('judge_scores', SCORES)
    df = pd.DataFrame([s for s in SCORES if s['judge'] != 'human']).pivot(index='id', columns='judge', values='score')
    df['human'] = pd.Series(human_by_id_1)
    ui.table(df, title='score by transcript and judge', float_fmt='{:.0f}')
    return SCORES, df, human_by_id_1


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line and a table with one row per transcript and a column per judge plus your hand score. Stop here if a column is all tens: that judge is not discriminating and its prompt needs a harder bar.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 8 of 9 — Find disagreement, not a winner

    The judges measure different things, so averaging them is meaningless. Sort by the spread between them instead. A large spread is a prompt to read the answer and the rationales, not proof that one judge is wrong. Where the judges disagree with you is the most useful row of all.
    """)
    return


@app.cell
def _(JUDGES, df, matplotlib_style, ui):
    import matplotlib.pyplot as plt
    import numpy as np

    plt.rcParams.update(matplotlib_style())
    cols = [j.name for j in JUDGES]
    matrix = df[cols].astype(float)
    fig, ax = plt.subplots(figsize=(7, 0.5 * len(matrix) + 1.5))
    im = ax.imshow(matrix.to_numpy(), vmin=0, vmax=10, cmap="Greys", aspect="auto")
    ax.set_xticks(range(len(cols)), cols)
    ax.set_yticks(range(len(matrix.index)), matrix.index)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            v = matrix.iat[i, j]
            if not np.isnan(v):
                ax.text(j, i, f"{v:.0f}", ha="center", va="center", color="white" if v > 6 else "black")
    ax.set_title("score by transcript and judge")
    plt.tight_layout(); plt.show()

    df["spread"] = matrix.max(axis=1) - matrix.min(axis=1)
    df["vs_human"] = (matrix.mean(axis=1) - df["human"]).abs()
    ui.table(df.sort_values("spread", ascending=False), title="rows to read first", float_fmt="{:.1f}")
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a grey heatmap and a table sorted by spread, with a `vs_human` column where you gave a verdict. Read the top row's rationales before you trust any number in it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Pick the row with the largest spread. Which judge was right, and what evidence told you?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 9 of 9 — Say how sure you are

    Every agreement number came from a handful of transcripts, so put an interval on it before you rank judges. `bootstrap_ci` resamples the per-transcript agreements and reports where the mean lands 95% of the time. `difference_ci` does the same for the gap between two judges, paired on the same transcripts. The second table shows that gap at your real count, then with the same rows drawn up to 5, 20, and 100: the interval narrows with size alone, so the 100-row line is a demonstration, not evidence. An interval that spans zero means the data fits no difference: the gap could be which transcripts landed in the set. You have not measured a difference, only that you need more transcripts.
    """)
    return


@app.cell
def _(JUDGES, SCORES, agreement, echo, human_by_id_1, np, oracle, pd, ui):
    from helpers.evals import bootstrap_ci, difference_ci
    per_scorer = {j.name: agreement({s['id']: s['score'] for s in SCORES if s['judge'] == j.name}, human_by_id_1) for j in JUDGES}
    per_scorer['echo'], per_scorer['oracle'] = (agreement(echo, human_by_id_1), agreement(oracle, human_by_id_1))
    ci = pd.DataFrame([{'scorer': name, 'n': len(v), **dict(zip(('agreement', 'ci_low', 'ci_high'), bootstrap_ci(v)))} for name, v in per_scorer.items() if v]).set_index('scorer')
    ui.table(ci, title='agreement with your hand scores, 95% interval')
    ranked = sorted((j.name for j in JUDGES), key=lambda n: ci.loc[n, 'agreement'])
    worst, best = (ranked[0], ranked[-1])
    a, b = (per_scorer[worst], per_scorer[best])
    rng = np.random.default_rng(0)
    rows = []
    for n in (len(a), 5, 20, 100):
        idx = np.arange(len(a)) if n == len(a) else rng.integers(0, len(a), size=n)
        diff, lo, hi = difference_ci([a[i] for i in idx], [b[i] for i in idx])
        rows.append({'n': n, 'difference': diff, 'ci_low': lo, 'ci_high': hi, 'verdict': 'spans zero' if lo <= 0 <= hi else 'clear of zero'})
    ui.table(pd.DataFrame(rows).set_index('n'), title=f'{best} minus {worst}, the same rows resampled to n')  # the same transcripts, drawn with replacement
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see two tables: agreement per scorer with its interval, echo lowest and oracle at 1.0, then the same judge-versus-judge gap wider at 5 rows and narrower at 100. Stop here if the interval at your real count excludes zero and you were about to call that judge better: read its rationales first.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Write three new vibe checks for aspects the current five do not cover: a refusal the agent should make, a question where the right answer is "the charter does not say", and a question that needs two charter sections. Add them to `VIBE_CHECKS`, save again, and write one sentence on what they caught that the first five missed.
    """)
    return


@app.cell
def _(VIBE_CHECKS, ws):
    MY_CHECKS = [
        {"id": "v06", "input": "", "expected": ""},
        {"id": "v07", "input": "", "expected": ""},
        {"id": "v08", "input": "", "expected": ""},
    ]
    extra = [c for c in MY_CHECKS if c["input"]]
    if extra:
        ws.save("vibe_checks", VIBE_CHECKS + extra)
    else:
        print("fill in at least one check above, then rerun")
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
    | Five rubric aspects written in a cell | A reviewed rubric with boundary cases, versioned with the prompt |
    | Your verdicts on six transcripts | Human calibration on a representative sample, checked for self-preference |
    | Three repeat scores on one case | Repeatability estimates across the whole set |
    | One model writing and judging | A separate judge model, or several |
    | A JSONL file in the workspace | Versioned datasets with prompt and model metadata, tracked per experiment |
    | An interval from six transcripts | Intervals per slice on hundreds of cases, reported with every number |
    | Reading the heatmap | Release thresholds on calibrated metrics |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - A human scores a sample of every batch so judge drift is visible.
    - Judge model and prompt version recorded on every score row.
    - Programmatic checks for anything exact: ids, names, menu paths, numbers.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Have a second person score the same transcripts and compare their verdicts with yours before comparing either with the judges.
    - Add exact programmatic checks for anything checkable: an entitlement name, a menu path, an id format.
    - Judge with a different model and measure agreement with this one.
    """)
    return


if __name__ == "__main__":
    app.run()
