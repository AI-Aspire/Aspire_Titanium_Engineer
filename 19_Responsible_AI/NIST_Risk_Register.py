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
    # NIST risk register

    Your workspace already holds the evidence a risk review needs: judge scores, retrieval scores, agent trajectories, guardrail results. This notebook reads that evidence and turns it into a risk register organised by the four NIST AI RMF functions, with no model calls.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    The NIST AI risk management framework as four functions, Govern, Map, Measure, Manage, and how each one is answered by an artifact you already produced.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    A risk register with one row per risk, derived by plain Python from your workspace, rendered as a table and saved.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    A register is only useful if someone owns each row. Tell your team which row surprised you and which risk has no evidence behind it yet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 25 minutes
    **Reads:** charter, rubric, judge_scores, ragas_scores, trajectories, capability_report, guardrail_cases, ladder_results, owasp_findings
    **Writes:** risk_register
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    No key, no model. Everything comes from the workspace, and the seed carries any artifact you have not produced yet. The OWASP findings are optional because they are written by a later exercise.
    """)
    return


@app.cell
def _():
    import re, textwrap
    from collections import defaultdict

    from helpers import workspace as ws

    CHARTER = ws.load("charter")
    RUBRIC = ws.load("rubric")
    JUDGE_SCORES = ws.load("judge_scores")
    RAGAS = ws.load("ragas_scores")
    TRAJECTORIES = ws.load("trajectories")
    CAPABILITY = ws.load("capability_report")
    GUARDRAIL_CASES = ws.load("guardrail_cases")
    LADDER_RESULTS = ws.load("ladder_results")
    try:
        OWASP = ws.load("owasp_findings")
    except FileNotFoundError:
        OWASP = []
        print("ℹ no owasp_findings yet; the register will skip that source")

    REGISTER: list[dict] = []
    print(f"✅ offline; {len(JUDGE_SCORES)} judge rows, {len(RAGAS)} ragas rows, {len(TRAJECTORIES)} trajectories, "
          f"{len(GUARDRAIL_CASES)} guardrail cases, {len(OWASP)} owasp findings; source: {ws.source('charter')}")
    return (
        CAPABILITY,
        CHARTER,
        GUARDRAIL_CASES,
        JUDGE_SCORES,
        LADDER_RESULTS,
        OWASP,
        RAGAS,
        REGISTER,
        RUBRIC,
        TRAJECTORIES,
        defaultdict,
        textwrap,
        ws,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with counts for each artifact and whether the charter comes from the workspace or the seed. Stop here if a load raises FileNotFoundError: that artifact has not been produced and the seed does not carry it.
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
    ## Task 1 of 6 — Map the risks the charter already admits

    The Map function asks where the system will be wrong. Your charter has a section that says exactly that. Each bullet under the "where it will be wrong" heading becomes one row with the function set to Map and the evidence set to the charter's own words. The status is open until an artifact proves otherwise.
    """)
    return


@app.cell
def _(CHARTER, REGISTER: list[dict], textwrap):
    def section(markdown: str, title_contains: str) -> str:
        out, keep = ([], False)
        for line in markdown.splitlines():
            if line.startswith('## '):
                keep = title_contains.lower() in line.lower()
                continue
            if keep:
                out.append(line)
        return '\n'.join(out).strip()

    def bullets(text: str) -> list[str]:
        items, current = ([], [])
        for line in text.splitlines():
            if line.lstrip().startswith(('- ', '* ')):
                if current:
                    items.append(' '.join(current))
                current = [line.lstrip()[2:].strip()]
            elif line.strip() and current:
                current.append(line.strip())
        if current:
            items.append(' '.join(current))
        return items

    def add(source: str, function: str, risk: str, evidence: str, mitigation: str, status: str='open') -> None:
        REGISTER.append({'id': f'R{len(REGISTER) + 1:02d}', 'source': source, 'function': function, 'risk': risk, 'evidence': textwrap.shorten(evidence, 160), 'owner': '', 'mitigation': mitigation, 'status': status})
    for item in bullets(section(CHARTER, 'wrong')):
        risk = item.split('. ')[0].rstrip('.')
        add('charter', 'Map', risk, item, 'Keep the detection the charter names; add an eval case that reproduces it')
    for _row in REGISTER:
        print(f"{_row['id']} [{_row['function']}] {_row['risk']}")
    return (add,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see one row per bullet in the charter's "where it will be wrong" section, each tagged Map. Stop here if the list is empty: your charter has no such section, or the heading does not contain the word wrong.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 6 — Measure what the judges found

    The Measure function asks whether you can show the risk with a number. Your judge scores are one number per transcript per judge on a 0 to 10 scale. A judge whose mean sits under 7 is reporting a weakness; a judge that disagrees with your hand score by 3 or more is a risk in the measurement itself.
    """)
    return


@app.cell
def _(JUDGE_SCORES, REGISTER: list[dict], add, defaultdict):
    by_judge = defaultdict(list)
    human = {}
    for s in JUDGE_SCORES:
        if not isinstance(s.get('score'), (int, float)):
            continue
        if s['judge'] == 'human':
            human[s['id']] = s['score']
        else:
            by_judge[s['judge']].append(s)
    for judge, _rows in sorted(by_judge.items()):
        mean = sum((r['score'] for r in _rows)) / len(_rows)
        low = [r for r in _rows if r['score'] < 5]
        print(f'{judge:<14} mean {mean:4.1f}  below 5: {len(low)}/{len(_rows)}')
        if mean < 7:
            worst = min(_rows, key=lambda r: r['score'])
            add('judge_scores', 'Measure', f'Answers score low on {judge} (mean {mean:.1f}/10)', f"{worst['id']}: {worst.get('rationale', '')}", f'Fix the transcripts the {judge} judge scored under 5, then rerun the judge')
        gaps = [(r['id'], r['score'], human[r['id']]) for r in _rows if r['id'] in human and abs(r['score'] - human[r['id']]) >= 3]
        if gaps:
            tid, js, hs = gaps[0]
            add('judge_scores', 'Measure', f'The {judge} judge disagrees with the human score', f'{tid}: judge {js}, human {hs}; {len(gaps)} such transcript(s)', 'Recalibrate the judge prompt against the hand verdicts before trusting its number')
    print(f'{len(REGISTER)} rows so far')
    return (by_judge,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see one line per judge with its mean and how many transcripts it scored under 5, then a row count that grew for every judge under 7 or in disagreement with you. Stop here if no judge names appear: the judge scores have no numeric score field.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which Measure row would a helpdesk lead find most convincing, and which would need a second judge before anyone acts on it?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 6 — Measure retrieval and agent failures

    Two more numbers. The RAGAS rows carry a faithfulness score per variant; any variant under 0.7 is a Measure risk. The trajectories carry a pass flag per task; any task whose pass rate is under 0.7 is a Measure risk, with the capability report supplying the evidence line where it mentions that task.
    """)
    return


@app.cell
def _(CAPABILITY, RAGAS, REGISTER: list[dict], TRAJECTORIES, add, defaultdict):
    def as_float(value, default=0.0) -> float:
        try:
            return float(value)
        except (TypeError, ValueError):
            return default
    for _r in RAGAS:
        faith = as_float(_r.get('faithfulness'))
        print(f"ragas {_r.get('variant', '?'):<24} faithfulness {faith:.2f}")
        if faith < 0.7:
            add('ragas_scores', 'Measure', f"Retrieval variant '{_r.get('variant', '?')}' is not faithful to its context", f'faithfulness {faith:.2f}', 'Tighten the evidence contract in the prompt; retrieve more of the right page')
    per_task = defaultdict(list)
    for t in TRAJECTORIES:
        per_task[t['task_id']].append(bool(t.get('passed')))
    report_lines = [ln.strip() for ln in CAPABILITY.splitlines() if ln.strip()]
    for task_id, flags in sorted(per_task.items()):
        rate = sum(flags) / len(flags)
        print(f'task {task_id:<10} pass rate {rate:.2f} over {len(flags)} run(s)')
        if rate < 0.7:
            mention = next((ln for ln in report_lines if str(task_id) in ln), f'{sum(flags)} of {len(flags)} runs passed')
            add('trajectories', 'Measure', f'Agent fails task {task_id} (pass rate {rate:.2f})', mention, 'Add the failing trajectory to the eval cases; fix the tool or the instruction it exposes')
    print(f'{len(REGISTER)} rows so far')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see one line per RAGAS variant and one per task, then the row count. A task under 0.7 and a variant under 0.7 each add a row. Stop here if every pass rate is 1.00 and every faithfulness is above 0.9: read the capability report before you believe it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 6 — Manage what the guardrails let through

    The Manage function asks what you do about a risk. The clearest evidence is an attack that got through. Join your guardrail cases to the ladder results: an attack case that no rung blocked becomes a Manage row. If the OWASP findings exist, every attack that succeeded becomes one too.
    """)
    return


@app.cell
def _(
    GUARDRAIL_CASES,
    LADDER_RESULTS,
    OWASP,
    REGISTER: list[dict],
    add,
    defaultdict,
):
    def is_attack(case: dict) -> bool:
        attack = case.get('attack')
        if isinstance(attack, bool):
            return attack
        return str(attack or '').strip().lower() not in {'', 'none', 'benign', 'false', '0', 'no'}
    blocked_by = defaultdict(list)
    for _r in LADDER_RESULTS:
        if _r.get('blocked'):
            blocked_by[_r['case_id']].append(str(_r.get('rung', '?')))
    leaks = [c for c in GUARDRAIL_CASES if is_attack(c) and (not blocked_by.get(c['id']))]
    attacks = [c for c in GUARDRAIL_CASES if is_attack(c)]
    print(f'{len(attacks)} attack cases, {len(leaks)} not blocked by any rung')
    for _c in leaks:
        add('ladder_results', 'Manage', f"Guardrail ladder misses attack case {_c['id']} ({_c.get('attack')})", f"input: {_c['input']}", 'Add a rung that catches this case; keep it as a regression test')
    for f in OWASP:
        if f.get('succeeded'):
            add('owasp_findings', 'Manage', f"OWASP {f.get('category', '?')} attack {f['id']} succeeded", str(f.get('evidence') or f.get('input') or ''), 'Apply the defence for that category and rerun the attack')
    print(f'{len(REGISTER)} rows so far')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the attack count, how many no rung blocked, and the row count. Stop here if every attack shows as not blocked: the `blocked` field is probably a string, and the join needs `== "true"`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    A guardrail case that was blocked at the last rung still passed the first two. Is that a Manage risk, a Measure risk, or no risk? Say why.

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5 of 6 — Govern: owners and gaps in the rubric

    The Govern function asks who is accountable and what is not measured at all. Two checks. Every rubric aspect should have a judge; an aspect with none is a Govern row, because nobody is measuring it. Then every row gets an owner. Edit `OWNERS` to name real people from your charter.
    """)
    return


@app.cell
def _(REGISTER: list[dict], RUBRIC, add, by_judge, defaultdict):
    judges = set(by_judge)
    for _c in RUBRIC.get('criteria', []):
        aspect = str(_c.get('aspect', '')).strip()
        covered = any((aspect.lower().split()[0] in j.lower() or j.lower() in aspect.lower() for j in judges)) if aspect else True
        if not covered:
            add('rubric', 'Govern', f"Rubric aspect '{aspect}' has no judge", f"pass = {_c.get('pass', '')}", 'Write a judge for this aspect, or drop it from the rubric')
    OWNERS = {'Govern': 'helpdesk lead', 'Map': 'product owner', 'Measure': 'eval owner', 'Manage': 'guardrail owner'}
    for _row in REGISTER:
    # Edit these. The charter's users section names the people who care about each function.
        _row['owner'] = OWNERS.get(_row['function'], 'unassigned')
    counts = defaultdict(int)
    for _row in REGISTER:
        counts[_row['function']] += 1
    for fn in ('Govern', 'Map', 'Measure', 'Manage'):
        print(f'{fn:<8} {counts[fn]:>2} row(s)  owner: {OWNERS[fn]}')
    return (counts,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see four lines, one per function, with a row count and an owner. Stop here if Govern is zero and Map is zero: the register has nothing a reviewer would call a governance finding, so check the rubric loaded.
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
    ## Task 6 of 6 — Render and save the register

    A register is a table people read in a meeting. Render it as markdown with the four functions in order, add a short header that says where the evidence came from, and save it as `risk_register`.
    """)
    return


@app.cell
def _(REGISTER: list[dict], counts, ws):
    ORDER = {'Govern': 0, 'Map': 1, 'Measure': 2, 'Manage': 3}
    _rows = sorted(REGISTER, key=lambda r: (ORDER[r['function']], r['id']))

    def cell(text: str) -> str:
        return str(text).replace('|', '\\|').replace('\n', ' ')
    lines = ['# Risk register', '', 'One row per risk, derived from the workspace with no model calls. Functions follow the NIST AI RMF: Govern, Map, Measure, Manage.', '', '| id | function | source | risk | evidence | owner | mitigation | status |', '|---|---|---|---|---|---|---|---|']
    for _r in _rows:
        lines.append('| ' + ' | '.join((cell(_r[k]) for k in ('id', 'function', 'source', 'risk', 'evidence', 'owner', 'mitigation', 'status'))) + ' |')
    lines += ['', '## Counts', ''] + [f'- {fn}: {counts[fn]}' for fn in ORDER]
    REGISTER_MD = '\n'.join(lines)
    from IPython.display import Markdown, display
    display(Markdown(REGISTER_MD))
    ws.save('risk_register', REGISTER_MD)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the rendered table, Govern rows first, then a ✅ line with the line count written. Stop here if the table has fewer than three rows: the seed evidence alone produces more, so a load above returned an empty list.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which row has the weakest evidence, and what artifact would you produce to strengthen it?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Add one rule of your own. Pick an artifact the register does not read yet, such as `ots_results` or `agentic_runs`, decide which function a failure in it belongs to, and write the loop that adds rows. Explain to a teammate why you chose that function.
    """)
    return


@app.cell
def _(REGISTER: list[dict], ws):
    # Shape: load an artifact, loop over rows, call add(source, function, risk, evidence, mitigation).
    try:
        OTS = ws.load('ots_results')
    except FileNotFoundError:
        OTS = []
    for _r in OTS:
        pass  # your rule here
    print(f'{len(REGISTER)} rows in the register')
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
    | Rules in one notebook over seven artifacts | A risk register in the governance tool, linked to tickets |
    | Thresholds of 0.7 and 7 picked by hand | Thresholds agreed with the owner and reviewed each release |
    | Owners as role names in a dict | Named people with a review date per row |
    | A markdown table saved to the workspace | A living register with history, sign-off, and audit trail |
    | Status always open | Status moves to mitigated or accepted with evidence attached |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - An owner on every register row.
    - The register regenerated before every release, not edited by hand.
    - Rows with no evidence flagged, not hidden.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Give each row a severity from likelihood and impact, derived from the numbers that produced it, and sort the table by severity.
    - Diff two runs of the register and print rows that appeared, disappeared, or changed status.
    - Write the register as a checklist the demo judges tick, one line per row, and attach it to the scorecard.
    """)
    return


if __name__ == "__main__":
    app.run()
