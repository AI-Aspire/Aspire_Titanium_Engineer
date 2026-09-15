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
    # Release pipeline

    A release decision that lives in a notebook is a wish. This notebook turns yours into a pipeline: a gate that exits 1, a manifest a security review can read, a canary verdict that refuses to promote on noise, an authorisation check that runs before retrieval, and a checklist of what only your platform team can answer.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    A release gate as one line in a pipeline, the eight properties of a manifest a platform team greps for, and why a canary at forty samples cannot tell an improvement from luck.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    The gate, the manifest check, and the canary verdict run on your own eval results and written to the workspace, then an authorisation check over your corpus and a deployment checklist with the unknowns marked.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    A deployment is a conversation with whoever runs the platform. Bring them the manifest and the checklist, and ask what is wrong with them.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 40 minutes
    **Reads:** deepeval_results, release_decision, eval_cases, trajectories, tools_catalog, corpus
    **Writes:** eval_gate, canary_verdict, deploy_checklist
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    No key, no model, no cluster. Everything reads from the workspace, with the seed as fallback, plus the two files in `deploy/` beside this notebook. The two scripts the pipeline calls live in the repository's `scripts/` folder, and the cells below run them the way a pipeline step would: as a subprocess with an exit code.
    """)
    return


@app.cell
def _():
    import math, re, subprocess, sys
    from collections import defaultdict

    import pandas as pd
    from IPython.display import Markdown, display

    from helpers import workspace as ws
    from helpers.config import ROOT, LLM_MODEL, LLM_BASE
    from helpers.evals import fingerprint, gate
    from helpers.paths import local

    RESULTS = ws.load("deepeval_results")
    DECISION = ws.load("release_decision")
    EVAL_CASES = ws.load("eval_cases")
    TRAJECTORIES = ws.load("trajectories")
    TOOLS = ws.load("tools_catalog")
    CORPUS_DIR = ws.load_path("corpus")
    PAGES = [{"name": str(p.relative_to(CORPUS_DIR)), "text": p.read_text(encoding="utf-8")}
             for p in sorted(CORPUS_DIR.rglob("*.md"))]

    DEPLOY = local("deploy")
    SCRIPTS = ROOT / "scripts"
    VERSIONS = sorted({r["version"] for r in RESULTS})
    print(f"✅ offline; {len(RESULTS)} result rows over versions {VERSIONS}; {len(EVAL_CASES)} eval cases; "
          f"{len(PAGES)} corpus pages; deploy files {sorted(p.name for p in DEPLOY.iterdir())}; "
          f"source: {ws.source('deepeval_results')}")
    return (
        DECISION,
        DEPLOY,
        EVAL_CASES,
        LLM_BASE,
        LLM_MODEL,
        Markdown,
        PAGES,
        RESULTS,
        ROOT,
        SCRIPTS,
        TOOLS,
        TRAJECTORIES,
        VERSIONS,
        defaultdict,
        display,
        fingerprint,
        gate,
        math,
        pd,
        re,
        subprocess,
        sys,
        ws,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with the result row count, two version names, the eval case and corpus page counts, and the two deploy files. Stop here if the versions list has fewer than two entries: the canary needs a baseline and a candidate, so run the eval notebook that writes the results first.
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
    ## Task 1 of 6 — A pass rate per metric, and the average that hides a failure

    Your eval results are one row per test, version, and metric. The first gate most teams write averages everything into one number and compares it with a bar. Compute that, then the pass rate of each metric on its own, and hold the candidate version to a floor per metric with `gate`. The floors in `MINIMUM` are yours to edit. The saved gate records them, the rates, and a fingerprint of the cases it measured, so the result says what was tested and against what.
    """)
    return


@app.cell
def _(
    EVAL_CASES,
    RESULTS,
    VERSIONS,
    defaultdict,
    display,
    fingerprint,
    gate,
    pd,
    ws,
):
    def pass_rates(rows: list[dict]) -> dict[str, dict[str, float]]:
        """{version: {metric: fraction of rows that passed}}. An errored row counts as a failure."""
        seen, hits = (defaultdict(int), defaultdict(int))
        for r in rows:
            key = (r['version'], r['metric'])
            seen[key] += 1
            hits[key] += 1 if r.get('passed') and (not r.get('error')) else 0
        out = defaultdict(dict)
        for (version, metric), n in seen.items():
            out[version][metric] = round(hits[version, metric] / n, 3)
        return dict(out)
    RATES = pass_rates(RESULTS)
    BASELINE, CANDIDATE = (VERSIONS[0], VERSIONS[-1])
    BAR = 0.8
    for _v in VERSIONS:
        mean = sum(RATES[_v].values()) / len(RATES[_v])
        print(f"{_v}: mean pass rate {mean:.2f}, {('clears' if mean >= BAR else 'under')} the bar of {BAR}")  # the weak gate: one average
    display(pd.DataFrame(RATES).T)
    MINIMUM = {metric: BAR for metric in RATES[CANDIDATE]}
    VERDICT = gate(RATES[CANDIDATE], MINIMUM)  # the strong one: every metric visible
    print(f"{CANDIDATE} per metric: {('passed' if VERDICT['passed'] else 'FAILED on ' + ', '.join(VERDICT['failed']))}")
    MEASURED = [{'id': t} for t in sorted({r['test'] for r in RESULTS})]  # edit the floors here
    EVAL_GATE = {'passed': VERDICT['passed'], 'failed': VERDICT['failed'], 'minimum': MINIMUM, 'version': CANDIDATE, 'rates': RATES[CANDIDATE], 'cases_measured': len(MEASURED), 'cases_written': len(EVAL_CASES), 'fingerprint': fingerprint(MEASURED), 'fingerprint_all_cases': fingerprint(EVAL_CASES)}
    print(f"fingerprint {EVAL_GATE['fingerprint']} over {len(MEASURED)} of {len(EVAL_CASES)} cases")
    ws.save('eval_gate', EVAL_GATE)
    return BAR, BASELINE, CANDIDATE


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the mean per version, a table with one row per version and one column per metric, a per-metric verdict for the candidate, a fingerprint line, and a ✅ line. Stop here if the table has one column: the results carry a single metric, and a gate over one number is the weak version again.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 6 — The same gate as a script, and the line that runs it

    A gate is only a gate when a pipeline can call it and read the answer. `scripts/release_gate.py` does what the cell above did and turns the verdict into an exit code: 0 ships, 1 stops the job. Run it twice as a subprocess, with a floor the candidate clears and with the floor you meant, and read the exit codes. Then find the one line in `deploy/deploy.yml` that calls it. Everything else in that file is a build and a deploy any app would need.
    """)
    return


@app.cell
def _(BAR, DEPLOY, ROOT, SCRIPTS, re, subprocess, sys):
    def run_script(name: str, *args: str, stdin: str | None=None) -> int:
        """Run one of the repository's scripts the way a pipeline step would, and print what it said."""
        proc = subprocess.run([sys.executable, str(SCRIPTS / name), *args], input=stdin, capture_output=True, text=True, cwd=ROOT)
        print((proc.stdout + proc.stderr).strip())
        print(f'exit code {proc.returncode}\n')
        return proc.returncode
    run_script('release_gate.py', '--min-score', '0.5')
    run_script('release_gate.py', '--min-score', str(BAR))
    WORKFLOW = (DEPLOY / 'deploy.yml').read_text(encoding='utf-8')
    for _n, line in enumerate(WORKFLOW.splitlines(), 1):
        if 'release_gate' in line:
            print(f'deploy.yml line {_n}: {line.strip()}')
    print('steps:', ' -> '.join(re.findall('- name: (\\w[\\w ]*)', WORKFLOW)))
    return (run_script,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the rate table twice, exit code 0 on the low floor and 1 on the real one, then the workflow line that calls the gate and the four step names. Stop here if both exit codes are 0: the candidate clears every floor, so rerun with a floor of 0.99 and confirm the gate can refuse.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    The gate reads results a judge wrote earlier. What has to be true about that judge run for an exit code of 0 to mean the release is safe, and which of those things does the script check?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 6 — A manifest a security review can read

    `deploy/k8s.yaml` describes the demo app as a Deployment, a Service, and a PodDisruptionBudget. Eight properties in it are what a platform team greps for before reading anything else: non-root, a read-only filesystem, every capability dropped, no privilege escalation, an image pinned to a tag, requests and limits, two probes, and a disruption budget once there is more than one replica. `scripts/check_manifests.py` asserts all eight with no YAML library. Run it on the file, then break one property in memory and run it again on standard input.
    """)
    return


@app.cell
def _(DEPLOY, run_script):
    MANIFEST = (DEPLOY / "k8s.yaml").read_text(encoding="utf-8")
    NEEDLES = ["runAsNonRoot: true", "readOnlyRootFilesystem: true", "- ALL", "allowPrivilegeEscalation: false",
               "demo-app:0.1.0", "requests:", "limits:", "readinessProbe:", "livenessProbe:", "kind: PodDisruptionBudget"]
    for needle in NEEDLES:
        print(f"{'✅' if needle in MANIFEST else 'missing'} {needle}")
    print()

    run_script("check_manifests.py", "-", stdin=MANIFEST)

    BROKEN = MANIFEST.replace("runAsNonRoot: true", "runAsNonRoot: false")   # one line, the most common finding
    assert BROKEN != MANIFEST
    run_script("check_manifests.py", "-", stdin=BROKEN)
    return (MANIFEST,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see ten ✅ lines, a pass line from the check with exit code 0, then one failure line naming the pod that runs as root with exit code 1. Stop here if the first run already fails: the manifest beside this notebook was edited, so read the failure line and fix the property it names.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 6 — Rolling, canary, shadow, and a verdict that refuses to promote on noise

    The workflow does a rolling update, which answers one question: does the new version start and stay up. A worse model passes that. A canary sends a slice of real traffic to the candidate; a shadow copies traffic to it and discards the replies. Both produce a pass rate on a sample, and a sample of forty moves around. Write the verdict from scratch: latency is a hard gate, too few samples is a hold, and after that the difference of two proportions with its 95% interval decides. Then apply it to your own two versions.
    """)
    return


@app.cell
def _(BASELINE, CANDIDATE, RESULTS, defaultdict, display, math, pd, ws):
    def naive_verdict(baseline_pass: float, candidate_pass: float) -> str:
        return 'promote' if candidate_pass > baseline_pass else 'hold'

    def canary_verdict(baseline_pass: float, baseline_n: int, candidate_pass: float, candidate_n: int, *, min_samples: int, p95_ms: float | None, p95_limit_ms: float) -> dict:
        """Promote, hold, or rollback. Hard gates first, statistics last."""
        out = {'delta': None, 'low': None, 'high': None}
        if baseline_n and candidate_n:
            se = math.sqrt(baseline_pass * (1 - baseline_pass) / baseline_n + candidate_pass * (1 - candidate_pass) / candidate_n)
            delta = candidate_pass - baseline_pass
            out = {'delta': round(delta, 3), 'low': round(delta - 1.96 * se, 3), 'high': round(delta + 1.96 * se, 3)}
        if p95_ms is not None and p95_ms > p95_limit_ms:
            return {'verdict': 'rollback', 'why': f'p95 {p95_ms:.0f} ms is over the {p95_limit_ms:.0f} ms limit', **out}
        holds = []
        if p95_ms is None:
            holds.append('p95 latency not measured')
        if candidate_n < min_samples:
            holds.append(f'{candidate_n} samples, need {min_samples}')
        if holds:
            return {'verdict': 'hold', 'why': '; '.join(holds), **out}
        interval = f"{out['delta']:+.3f} [{out['low']:+.3f}, {out['high']:+.3f}]"
        if out['high'] < 0:
            return {'verdict': 'rollback', 'why': f'worse: {interval}', **out}
        if out['low'] > 0:
            return {'verdict': 'promote', 'why': f'better: {interval}', **out}
        return {'verdict': 'hold', 'why': f'interval spans zero: {interval}', **out}
    BASE_RATE, BASE_N, MIN_SAMPLES, P95_LIMIT_MS = (0.81, 4000, 200, 1200)
    table = []
    for rate in (0.95, 0.86, 0.83, 0.72):
        for _n in (40, 400, 4000):
            _v = canary_verdict(BASE_RATE, BASE_N, rate, _n, min_samples=MIN_SAMPLES, p95_ms=900, p95_limit_ms=P95_LIMIT_MS)
            table.append({'candidate': rate, 'n': _n, 'p95_ms': 900, 'naive': naive_verdict(BASE_RATE, rate), 'verdict': _v['verdict'], 'why': _v['why']})
    _v = canary_verdict(BASE_RATE, BASE_N, 0.93, 4000, min_samples=MIN_SAMPLES, p95_ms=1500, p95_limit_ms=P95_LIMIT_MS)
    table.append({'candidate': 0.93, 'n': 4000, 'p95_ms': 1500, 'naive': naive_verdict(BASE_RATE, 0.93), 'verdict': _v['verdict'], 'why': _v['why']})
    display(pd.DataFrame(table))

    def case_pass(rows: list[dict], version: str) -> dict[str, bool]:
        """A case passes a version only when every metric passed."""
        flags = defaultdict(list)
        for r in rows:
            if r['version'] == version:
                flags[r['test']].append(bool(r.get('passed')) and (not r.get('error')))
        return {case: all(f) for case, f in flags.items()}
    base, cand = (case_pass(RESULTS, BASELINE), case_pass(RESULTS, CANDIDATE))
    base_rate, cand_rate = (sum(base.values()) / len(base), sum(cand.values()) / len(cand))
    P95_MS = None
    OWN = canary_verdict(base_rate, len(base), cand_rate, len(cand), min_samples=MIN_SAMPLES, p95_ms=P95_MS, p95_limit_ms=P95_LIMIT_MS)
    CANARY = {**OWN, 'baseline': {'version': BASELINE, 'pass_rate': round(base_rate, 3), 'n': len(base)}, 'candidate': {'version': CANDIDATE, 'pass_rate': round(cand_rate, 3), 'n': len(cand)}, 'min_samples': MIN_SAMPLES, 'p95_ms': P95_MS, 'p95_limit_ms': P95_LIMIT_MS}
    print(f"{BASELINE} {base_rate:.2f} (n={len(base)}) -> {CANDIDATE} {cand_rate:.2f} (n={len(cand)}): {OWN['verdict']}, {OWN['why']}")
    ws.save('canary_verdict', CANARY)  # the eval results carry no latency; a load test fills this in
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a thirteen-row table where naive says promote on every higher rate while verdict holds at n = 40, promotes only when the interval clears zero, and rolls back the slow row, then your own verdict and a ✅ line. Stop here if your own verdict is promote: a handful of cases cannot earn that, so check `MIN_SAMPLES`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Your own verdict holds on sample size. At your product's real request volume, how long would a canary at five percent of traffic need to run before the interval on your pass rate could clear zero, and does that make shadowing offline the only honest option?

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
    ## Task 5 of 6 — Who may read what, before retrieval

    Your app will sit behind a gateway that authenticates the user and forwards an identity in a header. Authentication says who; authorisation says what they may read, and that check is an if statement in code, never a sentence in a prompt. The trap is retrieval: an index holding pages with different access rules is an authorisation bypass. Tag your corpus pages with groups, then run the same search twice for a newcomer who may read the knowledge base only: filtering after ranking, then filtering before. Watch what the first one gives away.
    """)
    return


@app.cell
def _(EVAL_CASES, PAGES, re):
    def identity_from_headers(headers: dict) -> dict | None:
        """Trust the gateway in front of the app: read the identity it forwarded."""
        lower = {k.lower(): v for k, v in headers.items()}
        user = lower.get("x-forwarded-user", "").strip()
        if not user:
            return None
        groups = [g.strip() for g in lower.get("x-forwarded-groups", "").split(",") if g.strip()]
        return {"user": user, "groups": groups}


    def may_access(identity: dict | None, document_groups: list[str]) -> bool:
        """Authorisation: an if statement, not a prompt."""
        return bool(identity) and bool(set(identity["groups"]) & set(document_groups))


    GROUPS = {"kb": ["all-staff"], "wiki": ["all-staff"], "charter.md": ["all-staff"],
              "transcripts": ["helpdesk-agents"], "prompts": ["engineering"], "vibe_checks.md": ["engineering"]}


    def groups_of(page: dict) -> list[str]:
        return GROUPS.get(page["name"].split("/")[0], ["engineering"])


    STOP = {"a", "an", "and", "are", "as", "at", "be", "but", "for", "from", "how", "i", "in", "is", "it",
            "of", "on", "or", "the", "to", "what", "when", "with", "my", "can", "do", "you", "me"}


    def terms(text: str) -> set[str]:
        return {t for t in re.findall(r"[a-z0-9][a-z0-9-]+", text.lower()) if t not in STOP}


    def rank(pages: list[dict], query: str, k: int = 3) -> list[dict]:
        q = terms(query)
        ranked = sorted(pages, key=lambda p: len(q & terms(p["text"])), reverse=True)
        return [p for p in ranked[:k] if q & terms(p["text"])]


    def search_then_filter(query: str, identity: dict | None) -> tuple[list[str], str]:   # the trap
        hits = rank(PAGES, query)
        allowed = [p["name"] for p in hits if may_access(identity, groups_of(p))]
        hidden = [p["name"] for p in hits if p["name"] not in allowed]
        return allowed, f"{len(hits)} matched, {len(hidden)} hidden: {hidden}"


    def filter_then_search(query: str, identity: dict | None) -> tuple[list[str], str]:   # the fix
        readable = [p for p in PAGES if may_access(identity, groups_of(p))]
        hits = rank(readable, query)
        return [p["name"] for p in hits], f"{len(hits)} matched"


    newcomer = identity_from_headers({"X-Forwarded-User": "new.starter@example.com", "X-Forwarded-Groups": "all-staff"})
    QUERY = EVAL_CASES[0]["question"]
    print("query:", QUERY)
    for fn in (search_then_filter, filter_then_search):
        names, note = fn(QUERY, newcomer)
        print(f"{fn.__name__:<19} {names}  ({note})")
    print("no header at all:", identity_from_headers({}), "->", filter_then_search(QUERY, None)[0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the query, the trap line listing readable pages plus a note naming the hidden ones, the fix line with no such note, and an empty list for a request with no header. Stop here if the trap hides nothing: pick a query from a transcript so the ranking reaches a page the newcomer may not read.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ⚠️ Trusting that header is safe only when nothing can reach the app except through the gateway. A service that is addressable inside the network lets anyone set `X-Forwarded-User` to whoever they like. The checklist below asks that question, and the answer has to be no.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 6 of 6 — The deployment checklist

    Thirty questions decide whether this app can be deployed where you work, and most are answered by a person, not a file. Some the repository answers already: the health endpoint is the probe path in the manifest, the secret comes from `.env` today and a Secret on the cluster, the app keeps its conversation in process memory. The cell derives those answers from the files themselves, marks the rest unknown, and saves the list as markdown. Unknown is an answer someone can act on; a blank is not.
    """)
    return


@app.cell
def _(
    DECISION,
    LLM_BASE,
    LLM_MODEL,
    MANIFEST,
    Markdown,
    ROOT,
    TOOLS,
    TRAJECTORIES,
    defaultdict,
    display,
    re,
    ws,
):
    APP_SRC = (ROOT / 'project' / 'app' / 'app.py').read_text(encoding='utf-8')
    CONFIG_SRC = (ROOT / 'helpers' / 'config.py').read_text(encoding='utf-8')
    probe = re.search('path:\\s*(\\S+)', MANIFEST).group(1)
    secret = re.search('secretRef:\\s*\\n\\s*name:\\s*(\\S+)', MANIFEST).group(1)
    image = re.search('image:\\s*(\\S+)', MANIFEST).group(1)
    asks = re.search('requests:.*?\\n\\s*cpu:\\s*(\\S+)\\n\\s*memory:\\s*(\\S+)', MANIFEST, re.S)
    outward = [f"{t['name']} ({t['kind']})" for t in TOOLS['tools'] if t.get('kind') in ('mcp', 'utcp', 'sub-agent')]
    tool_steps = sum((1 for t in TRAJECTORIES for s in t['steps'] if s.get('role') == 'tool'))
    decision = next((ln.lstrip('# ').strip() for ln in DECISION.splitlines() if ln.startswith('# ')), 'no decision saved')
    endpoint = 'a self-hosted endpoint (OPENAI_BASE_URL is set)' if LLM_BASE else "the provider's default endpoint"
    stateful = 'session_state' in APP_SRC
    dotenv = 'load_dotenv' in CONFIG_SRC
    CHECKLIST = [('Compute', 'Where do internal apps run, and who owns that cluster?', 'unknown', '', ''), ('Compute', 'What does the app need: CPU, memory, a GPU?', 'answered', f'requests {asks.group(1)} CPU and {asks.group(2)} memory; no GPU, the model runs behind {endpoint}', 'deploy/k8s.yaml'), ('Compute', 'Is the app stateless?', 'partly' if stateful else 'answered', 'the conversation lives in st.session_state, in the process; two replicas need sticky sessions or a store' if stateful else 'no per-process state found', 'project/app/app.py'), ('Compute', 'What is the health endpoint?', 'answered', f"{probe}, Streamlit's own route, used by both probes", 'deploy/k8s.yaml'), ('Images', 'Is there an internal registry, and what is the image called?', 'partly', f'{image} is a placeholder until the registry has a name', 'deploy/k8s.yaml'), ('Images', 'Is there a base image you must start from?', 'unknown', '', ''), ('Images', 'Must an image be scanned or signed before it may run?', 'unknown', '', ''), ('Identity', 'How do users authenticate?', 'partly', 'the app has no login of its own; a gateway must terminate SSO in front of it and forward the identity', 'project/app/app.py'), ('Identity', 'Is the service reachable except through the gateway?', 'unknown', '', ''), ('Identity', 'How does the app authenticate outward, to the model?', 'answered' if dotenv else 'partly', 'an API key read from .env by helpers.config, taken from a Secret on the cluster', 'helpers/config.py'), ('Identity', 'Is workload identity available, or is it secrets?', 'unknown', '', ''), ('Secrets', 'Where do secrets live today?', 'answered', '.env at the repository root, loaded by helpers.config', 'helpers/config.py'), ('Secrets', 'Where will they live on the cluster?', 'answered', f'the Secret {secret}, injected with envFrom, never in the image', 'deploy/k8s.yaml'), ('Secrets', 'How are they rotated, and who can read them?', 'unknown', '', ''), ('Network', 'Can the app reach the internet, and through a proxy?', 'unknown', '', ''), ('Network', 'What does the app call?', 'partly', f"the model at {endpoint}; the tools catalog names {len(outward)} outward capabilities: {', '.join(outward) or 'none'}", 'tools_catalog'), ('Network', 'What is on the egress allowlist, and who adds to it?', 'unknown', '', ''), ('Network', 'Which network is it in, and what can it reach internally?', 'unknown', '', ''), ('Data', 'What classification may this app process?', 'unknown', '', ''), ('Data', 'May data leave the region?', 'unknown', '', ''), ('Data', 'How long may prompts and responses be kept?', 'partly', f'the workspace already keeps {len(TRAJECTORIES)} full trajectories with no retention rule', 'trajectories'), ('Data', 'Is there a DLP scan on egress?', 'unknown', '', ''), ('Models', 'Is there an approved internal model endpoint?', 'partly', f'today {LLM_MODEL} at {endpoint}; whether it is approved is a question for the platform team', '.env'), ('Models', 'May you download open weights, and from where?', 'unknown', '', ''), ('Models', 'What licence does the model carry, and who signs off on it?', 'unknown', '', ''), ('Legacy', 'What must this integrate with, and who owns it?', 'partly', TOOLS.get('capability', 'see the tools catalog'), 'tools_catalog'), ('Legacy', 'Is it real-time or batch?', 'answered', f'real-time: {tool_steps} tool calls made at request time across {len(TRAJECTORIES)} trajectories', 'trajectories'), ('Process', 'Who approves a deployment?', 'partly', f"the saved decision says '{decision}'; nobody is named", 'release_decision'), ('Process', 'What review gates a deployment?', 'answered', 'release_gate.py and check_manifests.py in the Gate step; both exit 1 to stop the job', 'deploy/deploy.yml'), ('Process', 'What is the rollback, and who is on call?', 'partly', 'kubectl rollout undo to the previous tag in the Deploy step; on call is unknown', 'deploy/deploy.yml')]
    assert len(CHECKLIST) == 30  # (area, question, status, answer, source)

    def render_checklist(items: list[tuple]) -> str:
        counts = defaultdict(int)
        for _, _, status, _, _ in items:
            counts[status] += 1
        lines = ['# Deployment checklist', '', f"{len(items)} questions: {counts['answered']} answered by the repository, {counts['partly']} partly, {counts['unknown']} unknown. An unknown stays on the list until a person answers it.", '']
        for area in dict.fromkeys((a for a, *_ in items)):
            lines += [f'## {area}', '', '| # | question | status | answer | source |', '|---|---|---|---|---|']
            for n, (a, q, status, answer, source) in enumerate(items, 1):
                if a == area:
                    lines.append(f"| {n} | {q} | {status} | {answer.replace('|', '/')} | {source} |")
            lines.append('')
        return '\n'.join(lines)
    _CHECKLIST_MD = render_checklist(CHECKLIST)
    display(Markdown(_CHECKLIST_MD))
    ws.save('deploy_checklist', _CHECKLIST_MD)
    return CHECKLIST, render_checklist


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the rendered checklist in nine areas with a status per row, a first line counting how many are answered, partly, and unknown, then a ✅ line. Stop here if every row says unknown: the manifest or the app source did not load, so check the paths the setup cell printed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which unknown row would stop the deployment first where you work, and which answered row would your platform team push back on?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Answer three of the unknown questions you can find out today, by asking rather than guessing, and name the one person who can answer the rest. Put the answers in `YOUR_ANSWERS` by question number and that person's role in `WHO_KNOWS`, rerun the cell, and explain to a teammate which answer changes the manifest.
    """)
    return


@app.cell
def _(CHECKLIST, render_checklist, ws):
    # Shape: YOUR_ANSWERS[question number] = what you found out and who told you; WHO_KNOWS = the role who can answer the rest.
    YOUR_ANSWERS: dict[int, str] = {}
    WHO_KNOWS = ''
    UPDATED = [(a, q, 'answered' if n in YOUR_ANSWERS else status, YOUR_ANSWERS.get(n, answer), 'asked' if n in YOUR_ANSWERS else source) for n, (a, q, status, answer, source) in enumerate(CHECKLIST, 1)]
    if len(YOUR_ANSWERS) >= 3 and WHO_KNOWS:
        _CHECKLIST_MD = render_checklist(UPDATED) + f'\nThe rest: ask {WHO_KNOWS}.\n'
        ws.save('deploy_checklist', _CHECKLIST_MD)
    else:
        print('fill YOUR_ANSWERS with three question numbers and WHO_KNOWS with a role, then rerun')
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
    | A gate script over one results file | The eval run and the gate as pipeline steps that block the merge |
    | Two YAML objects checked by eight rules | A chart or overlay per environment, checked by a policy engine |
    | A four-step workflow that deploys on a tag | Image scanning and signing, then dev, staging, and prod with promotion between them |
    | A canary verdict in one function | A rollout controller polling live metrics and aborting on its own |
    | Group membership from a header | A gateway doing OIDC, a policy engine with roles and attributes, an audit log |
    | A checklist in markdown with unknowns | An intake with an owner and a date per question, and a signed-off design document |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - The gate's floors agreed before the results exist, and changed only with a recorded reason.
    - Authorisation checked before retrieval, on every request, in code that has a test.
    - An unknown on the checklist stays visible until a named person answers it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Terraform, or your cloud's equivalent, for the two primitives you actually need: a registry to put the image in and a secret store to take the key from. Write both, run the plan, and bring the plan to whoever owns the account.
    - Model licences as infrastructure. For the model named in your `.env`, find the licence link on its model card, then the licence file in the repository, then the tag, and answer four questions: commercial use, use restrictions, thresholds, and what a fine-tune inherits. Add the answer to the checklist row that asks.
    """)
    return


if __name__ == "__main__":
    app.run()
