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
    # DSPy optimizers

    Your judge scores transcripts, and you scored some of them by hand. A prompt optimizer is a search: give it those examples and a way to score agreement, and it looks for an instruction and a few demos that agree with you more often. This notebook runs three optimizers on your judge and keeps the winner.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    Prompt optimisation as a compile step: a signature, a metric, and optimisers that search for the prompt. BootstrapFewShot, MIPROv2, and GEPA on the same task.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    Training examples from your judge scores and transcripts, agreement with your hand scores as the metric, and the best program saved.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    Production optimisation reruns when the examples change and records what changed in the prompt. Tell your team which optimiser moved agreement and whether it was worth the calls.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 30 minutes
    **Reads:** judge_scores, transcripts
    **Writes:** dspy_program
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    DSPy lives in the `optim` dependency group: run `make setup-optim` once. The model comes from `.env`. DSPy caches every call on disk, so a rerun with the same examples is instant.
    """)
    return


@app.cell
def _():
    import json, random, tempfile
    from pathlib import Path

    import dspy
    import litellm
    import pandas as pd

    from helpers.config import KEY, LLM_BASE, LLM_MODEL, LLM_TIMEOUT, LLM_MAX_TOKENS, require, budget
    from helpers.llm import litellm_model
    from helpers import workspace as ws

    require("OPENAI_API_KEY")
    litellm.suppress_debug_info = True
    litellm.drop_params = True     # a self-hosted server may reject a parameter DSPy sends; drop it rather than fail

    # temperature 1.0 satisfies both plain and reasoning models. DSPy needs a
    # numeric token ceiling, so a blank LLM_MAX_TOKENS in .env becomes a high one.
    lm = dspy.LM(litellm_model(), api_base=LLM_BASE, api_key=KEY, temperature=1.0,
                 max_tokens=LLM_MAX_TOKENS or 16000, timeout=LLM_TIMEOUT, num_retries=1)
    try:
        adapter = dspy.ChatAdapter(use_json_adapter_fallback=False)   # keep every call in plain chat format
    except TypeError:
        adapter = dspy.ChatAdapter()
    dspy.configure(lm=lm, adapter=adapter)

    SCORES = ws.load("judge_scores")
    TRANSCRIPTS = ws.load("transcripts")
    print(f"✅ model {LLM_MODEL}; {len(SCORES)} judge rows; {len(TRANSCRIPTS)} transcripts; "
          f"judge scores come from the {ws.source('judge_scores')}")
    return (
        LLM_MODEL,
        Path,
        SCORES,
        TRANSCRIPTS,
        budget,
        dspy,
        json,
        lm,
        pd,
        random,
        tempfile,
        ws,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with a judge row count above ten and a transcript count of at least four. Stop here if `import dspy` fails: run `make setup-optim` and restart the kernel.
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
    ## Task 1 of 6 — Build the examples

    A training example is a question, the assistant's response, and your hand score. The hand scores sit on the judge rows as `human_score`, or on rows whose judge is `human`. The question and response come from the transcript with the same id. Split the examples into train and held-out; the optimizers never see the held-out half.
    """)
    return


@app.cell
def _(SCORES, TRANSCRIPTS, dspy, random):
    def question_and_response(t: dict) -> tuple[str, str]:
        q = next((x["content"] for x in t["turns"] if x["role"] == "user"), "")
        r = next((x["content"] for x in reversed(t["turns"]) if x["role"] == "assistant"), "")
        return str(q), str(r)


    BY_ID = {t["id"]: t for t in TRANSCRIPTS}
    HUMAN: dict[str, float] = {}
    for row in SCORES:
        hs = row.get("human_score")
        if hs is None and row.get("judge") == "human":
            hs = row.get("score")
        if hs is not None and row["id"] in BY_ID:
            HUMAN[row["id"]] = float(hs)

    SCALE = 10 if HUMAN and max(HUMAN.values()) > 5 else 5
    TOL = 1 if SCALE > 5 else 0            # "agrees" means within one point on a 10-point scale, exact on a 5-point one

    EXAMPLES = []
    for tid, hs in sorted(HUMAN.items()):
        q, r = question_and_response(BY_ID[tid])
        EXAMPLES.append(dspy.Example(question=q, response=r, score=int(round(hs))).with_inputs("question", "response"))

    random.Random(7).shuffle(EXAMPLES)
    if len(EXAMPLES) >= 4:
        cut = max(2, int(len(EXAMPLES) * 0.6))
        TRAIN, TEST = EXAMPLES[:cut], EXAMPLES[cut:]
    else:
        TRAIN = TEST = EXAMPLES
        print("⚠️ fewer than four hand-scored transcripts; train and test are the same set, so treat the numbers as a smoke test")
    print(f"{len(EXAMPLES)} hand-scored examples on a 1 to {SCALE} scale: {len(TRAIN)} train, {len(TEST)} held out")
    for ex in TRAIN[:2]:
        print(f"  [{ex.score}] Q: {ex.question[:70]}  A: {ex.response[:70]}")
    return BY_ID, SCALE, TEST, TOL, TRAIN, question_and_response


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the example count, the scale, the split, and two training rows with their hand scores. Stop here if the count is zero: no judge row carries a `human_score`, so go back to the judge notebook and score at least four transcripts by hand.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 6 — The program and the metric

    The program is one signature and one `Predict`: question and response in, an integer score out. The metric is agreement with your hand score. Score the un-optimized program on the held-out examples first. That number is the bar every optimizer has to beat, and it is often already decent.
    """)
    return


@app.cell
def _(SCALE, TEST, TOL, dspy):
    class ScoreAnswer(dspy.Signature):
        """Score a support assistant's answer to a user's question."""

        question: str = dspy.InputField()
        response: str = dspy.InputField()
        score: int = dspy.OutputField(desc="an integer score")


    INSTRUCTIONS = (f"Score a support assistant's answer from 1 to {SCALE}. {SCALE} means grounded in the product's "
                    "documentation, specific about the next step, inside the product's scope, and safe to act on. "
                    "1 means invented, vague, out of scope, or unsafe. Decline-in-one-sentence is correct for out-of-scope questions.")
    ScoreAnswer = ScoreAnswer.with_instructions(INSTRUCTIONS)


    class JudgeProgram(dspy.Module):
        def __init__(self):
            super().__init__()
            self.predict = dspy.Predict(ScoreAnswer)

        def forward(self, question, response):
            return self.predict(question=question, response=response)


    def as_int(x) -> int:
        try:
            return int(float(str(x).strip().split()[0]))
        except (ValueError, IndexError):
            return -100


    def agreement(example, pred, trace=None) -> bool:
        return abs(as_int(getattr(pred, "score", "")) - example.score) <= TOL


    def evaluate(program, examples, label: str) -> float:
        ok = 0
        for ex in examples:
            got = as_int(program(question=ex.question, response=ex.response).score)
            hit = abs(got - ex.score) <= TOL
            ok += hit
            print(f"  {'✅' if hit else '❌'} judge={got:>3}  human={ex.score:>3}  {ex.question[:60]}")
        acc = ok / max(1, len(examples))
        print(f"  {label}: {ok}/{len(examples)} agree ({acc:.0%})\n")
        return acc


    RESULTS, PROGRAMS = {}, {}
    PROGRAMS["baseline"] = JudgeProgram()
    print("baseline (no optimizer)")
    RESULTS["baseline"] = evaluate(PROGRAMS["baseline"], TEST, "baseline")
    return (
        INSTRUCTIONS,
        JudgeProgram,
        PROGRAMS,
        RESULTS,
        agreement,
        as_int,
        evaluate,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see one line per held-out example with the judge's score next to yours, then an agreement fraction. Stop here if every judge score is -100: the model is not returning an integer, so read one raw output with `lm.inspect_history(n=1)`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Where did the baseline judge and you disagree by more than one point? Was the judge too kind or too harsh, and does the instruction say anything about that case?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 6 — BootstrapFewShot

    The cheapest optimizer. It runs the program on the training examples, keeps the ones where the metric passed, and pastes them into the prompt as demonstrations. It never changes the instruction. It can only replay what the base program already gets right, which is why it is fast and why it plateaus.
    """)
    return


@app.cell
def _(JudgeProgram, PROGRAMS, RESULTS, TEST, TRAIN, agreement, evaluate):
    from dspy.teleprompt import BootstrapFewShot


    def compile_safely(name: str, fn):
        """Compile with one optimizer; a missing feature or a server error skips it and says why."""
        try:
            program = fn()
        except Exception as e:  # noqa: BLE001 - the comparison should survive one optimizer failing
            print(f"⚠️ {name} skipped: {type(e).__name__}: {str(e).splitlines()[0][:160]}")
            return None
        PROGRAMS[name] = program
        print(name)
        RESULTS[name] = evaluate(program, TEST, name)
        return program


    boot = compile_safely("bootstrap", lambda: BootstrapFewShot(
        metric=agreement, max_bootstrapped_demos=2, max_labeled_demos=4,
    ).compile(JudgeProgram(), trainset=TRAIN))
    return (compile_safely,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the held-out lines again and an agreement fraction for `bootstrap`. Stop here if it is lower than the baseline by more than one example: the demos are teaching the wrong scale, so check that the training scores match the instruction's range.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 6 — MIPROv2

    MIPROv2 proposes new instructions and demo sets, scores each candidate on the training set, and keeps the mix that scores best. It spends many more calls than bootstrap. With a small training set, keep the candidate count and trial count low or the search overfits the examples it sees.
    """)
    return


@app.cell
def _(JudgeProgram, TRAIN, agreement, budget, compile_safely):
    from dspy.teleprompt import MIPROv2

    mipro = compile_safely("mipro", lambda: MIPROv2(
        metric=agreement, auto=None, num_candidates=3,
    ).compile(JudgeProgram(), trainset=TRAIN, valset=TRAIN, num_trials=budget(5, 2), minibatch_size=len(TRAIN),
              requires_permission_to_run=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the optimizer's progress lines, then the held-out lines and an agreement fraction for `mipro`. Stop here if it is skipped with a server error: the model server rejected a structured request, so confirm `litellm.drop_params` is on and rerun.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    MIPROv2 saw only the training examples. If it beats bootstrap on the held-out set, what did it learn that the demos alone could not carry?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5 of 6 — GEPA

    GEPA reads why a guess was wrong and rewrites the instruction in response. It needs a metric that returns feedback text, not only a score. It is the newest of the three and may not exist in the installed DSPy, so the cell checks first and skips cleanly if it is missing.
    """)
    return


@app.cell
def _(JudgeProgram, TOL, TRAIN, as_int, budget, compile_safely, dspy, lm):
    def agreement_with_feedback(example, pred, trace=None, pred_name=None, pred_trace=None):
        got = as_int(getattr(pred, "score", ""))
        ok = abs(got - example.score) <= TOL
        fb = "Agrees with the human score." if ok else (
            f"The human scored this {example.score}, the judge said {got}. "
            f"{'Too kind' if got > example.score else 'Too harsh'}: reread the response for grounding, scope, and next step.")
        return dspy.Prediction(score=float(ok), feedback=fb)


    if hasattr(dspy, "GEPA"):
        gepa = compile_safely("gepa", lambda: dspy.GEPA(
            metric=agreement_with_feedback, max_metric_calls=budget(24, 8), reflection_lm=lm,
        ).compile(JudgeProgram(), trainset=TRAIN, valset=TRAIN))
    else:
        gepa = None
        print("⚠️ this DSPy has no GEPA; skipping")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see either GEPA's reflection rounds followed by the held-out lines and a fraction, or one ⚠ line saying it was skipped. Stop here if GEPA ran but every held-out score is -100: the rewritten instruction broke the output format.
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
    ## Task 6 of 6 — Compare and save

    Read the table as cost against benefit, not as a leaderboard. Then look at what each optimizer changed: the instruction, the demos, or both. Save the winner as your judge program, with its agreement and the full results table, so the release decision can name which judge it trusted.
    """)
    return


@app.cell
def _(INSTRUCTIONS, PROGRAMS, RESULTS, pd):
    BASE_INSTR = INSTRUCTIONS.strip()

    def what_changed(name: str, program) -> dict:
        pred = program.predict
        instr = (pred.signature.instructions or '').strip()
        demos = getattr(pred, 'demos', None) or []
        return {'optimizer': name, 'agreement': RESULTS[name], 'instruction': 'rewrote' if instr != BASE_INSTR else 'unchanged', 'demos': len(demos)}
    table = pd.DataFrame([what_changed(n, p) for n, p in PROGRAMS.items()]).set_index('optimizer')
    print(table.to_string())
    for _name, _program in PROGRAMS.items():
        instr = (_program.predict.signature.instructions or '').strip()
        if instr != BASE_INSTR:
            print(f'\n=== {_name} rewrote the instruction ===\n{instr[:800]}')
    return


@app.cell
def _(
    LLM_MODEL,
    PROGRAMS,
    Path,
    RESULTS,
    SCALE,
    TEST,
    TOL,
    TRAIN,
    json,
    tempfile,
    ws,
):
    best = max(RESULTS, key=lambda n: (RESULTS[n], n == "baseline"))   # ties go to the cheapest: no optimizer
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "program.json"
        PROGRAMS[best].save(str(p))
        state = json.loads(p.read_text(encoding="utf-8"))

    ws.save("dspy_program", {"optimizer": best, "agreement": RESULTS[best], "program": state, "results": RESULTS,
                             "train": len(TRAIN), "test": len(TEST), "scale": SCALE, "tolerance": TOL, "model": LLM_MODEL})
    print(f"winner: {best} at {RESULTS[best]:.0%} agreement on {len(TEST)} held-out examples")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a table with one row per program, any rewritten instruction, a ✅ line, and the winner. Stop here if the winner is `baseline` on a tie: no optimizer earned its calls on this data, and that is a legitimate result to report.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Held-out agreement moved by at most a few examples. How many hand-scored transcripts would you need before you trusted a one-example difference?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Score two more transcripts by hand, add them to the held-out set, and rerun the evaluation for every program without recompiling. Then explain to a teammate whether the ranking held, and what that says about the size of your test set.
    """)
    return


@app.cell
def _(BY_ID, PROGRAMS, TEST, dspy, evaluate, question_and_response):
    # Shape: pick two transcript ids you have not scored, read them, and put your score in the dict.
    EXTRA_SCORES = {}  # e.g. {"t05": 8, "t06": 3}
    extra = [dspy.Example(question=question_and_response(BY_ID[i])[0], response=question_and_response(BY_ID[i])[1], score=s).with_inputs('question', 'response') for i, s in EXTRA_SCORES.items() if i in BY_ID]
    if extra:
        for _name, _program in PROGRAMS.items():
            print(_name)
            evaluate(_program, TEST + extra, f'{_name} on {len(TEST) + len(extra)} examples')
    else:
        print('add two ids to EXTRA_SCORES and rerun')
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
    | A handful of hand-scored transcripts | Hundreds of labelled outputs, refreshed as the product changes |
    | One `Predict` judge with an integer output | A judge with a rationale field, calibrated per rubric aspect |
    | Three optimizers on one train/test split | Cross-validation, a fixed holdout, and a cost line per optimizer |
    | Agreement within one point | Agreement plus inter-rater reliability against several people |
    | The winner saved as JSON | A versioned prompt registry with rollback and an eval gate per release |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - Held-out examples never seen by the optimiser.
    - Optimised prompts diffed and reviewed before deployment.
    - Model calls per compile budgeted and logged.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Add a `rationale` output field before `score` and rerun the three optimizers. Does asking for the reason first change agreement, or only cost?
    - Optimize per rubric aspect: one program per aspect, one metric each, and compare which aspects the optimizers can move at all.
    - Replace agreement-within-one with a weighted metric that punishes a pass verdict on a transcript you failed more than the reverse. Watch what MIPROv2 does with the instruction.
    """)
    return


if __name__ == "__main__":
    app.run()
