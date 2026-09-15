"""Numbers you can defend: intervals, fingerprints, and a gate.

An eval score is one number from one run over one set of cases. Three things
go wrong with it on the way to a decision. Nobody says how far it would move
on a different draw of the same size. It gets read against a score measured
on a different case set. And the bar it has to clear lives in prose, where
"we said 0.8" is not something a script can check.

    from helpers.evals import bootstrap_ci, difference_ci, fingerprint, compare, gate

    mean, low, high = bootstrap_ci(scores)             # how far the mean would move
    delta, low, high = difference_ci(before, after)    # is the improvement real
    fp = fingerprint(cases)                            # which cases produced this
    compare({"fingerprint": fp, "scores": a}, {"fingerprint": fp, "scores": b})
    gate(scores, {"faithfulness": 0.8})                # {"passed": bool, "failed": [...]}

`compare` refuses when the fingerprints differ. 0.94 on the six cases you had
last week against 0.91 on the sixty you have now is not a regression, and a
gate that cannot tell the two apart reports whatever the case set happened to
be. Standard library plus numpy, so it runs wherever the tests do.
"""
from __future__ import annotations

import hashlib
import json
from collections.abc import Sequence


def _rng(seed: int):
    import numpy as np

    return np.random.default_rng(seed)


def _bounds(level: float) -> tuple[float, float]:
    if not 0 < level < 1:
        raise ValueError(f"level must be between 0 and 1, not {level}")
    return (1 - level) / 2 * 100, (1 + level) / 2 * 100


def bootstrap_ci(values: Sequence[float], *, n_resamples: int = 2000, seed: int = 0,
                 level: float = 0.95) -> tuple[float, float, float]:
    """The mean of `values` and the interval it would move in.

    Resample the scores with replacement, take the mean of each resample, and
    read the interval off the spread of those means. Nothing about the
    distribution is assumed, which matters because eval scores are rarely
    normal: a pass rate is a pile of zeros and ones.

    Returns `(mean, low, high)`.
    """
    import numpy as np

    arr = np.asarray(list(values), dtype=float)
    if arr.size == 0:
        raise ValueError("bootstrap_ci needs at least one value")
    lo_q, hi_q = _bounds(level)
    idx = _rng(seed).integers(0, arr.size, size=(n_resamples, arr.size))
    means = arr[idx].mean(axis=1)
    low, high = np.percentile(means, [lo_q, hi_q])
    return float(arr.mean()), float(low), float(high)


def difference_ci(a: Sequence[float], b: Sequence[float], *, n_resamples: int = 2000,
                  seed: int = 0, level: float = 0.95) -> tuple[float, float, float]:
    """How much `b` beats `a` by, and the interval on that difference.

    When the two lists are the same length they are taken as the same cases
    in the same order and resampled together, so a case both versions found
    hard does not widen the interval. Different lengths are resampled
    independently, which is the honest thing to do with unpaired runs and
    gives a wider interval for the same data.

    Returns `(mean(b) - mean(a), low, high)`. An interval that spans zero
    means the data cannot tell the two apart.
    """
    import numpy as np

    a_arr = np.asarray(list(a), dtype=float)
    b_arr = np.asarray(list(b), dtype=float)
    if a_arr.size == 0 or b_arr.size == 0:
        raise ValueError("difference_ci needs at least one value on each side")
    lo_q, hi_q = _bounds(level)
    rng = _rng(seed)
    if a_arr.size == b_arr.size:
        idx = rng.integers(0, a_arr.size, size=(n_resamples, a_arr.size))
        diffs = b_arr[idx].mean(axis=1) - a_arr[idx].mean(axis=1)
    else:
        ia = rng.integers(0, a_arr.size, size=(n_resamples, a_arr.size))
        ib = rng.integers(0, b_arr.size, size=(n_resamples, b_arr.size))
        diffs = b_arr[ib].mean(axis=1) - a_arr[ia].mean(axis=1)
    low, high = np.percentile(diffs, [lo_q, hi_q])
    return float(b_arr.mean() - a_arr.mean()), float(low), float(high)


def fingerprint(cases: Sequence[dict], *, keys: tuple[str, ...] = ("id",)) -> str:
    """Twelve hex characters naming which cases a score was measured on.

    Built from the case identities only, sorted, so the order the cases were
    run in does not matter and neither does anything the system under test
    produced. Change a case, add one, or drop one and the fingerprint changes.
    """
    identities = sorted(
        json.dumps([case.get(k) for k in keys], sort_keys=True, ensure_ascii=False, default=str)
        for case in cases
    )
    payload = json.dumps(identities, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12]


def compare(before: dict, after: dict) -> dict:
    """Per-metric deltas between two runs, or a refusal.

    Each run is `{"fingerprint": str, "scores": {metric: float}}`. The result
    is `{"comparable": bool, "delta": {metric: after - before}}` with a
    `reason` when it is not comparable. Fingerprints that differ mean the two
    runs measured different cases, and the deltas are left empty rather than
    computed over numbers that do not mean the same thing.
    """
    fp_before, fp_after = before.get("fingerprint"), after.get("fingerprint")
    if fp_before != fp_after:
        return {"comparable": False, "delta": {},
                "reason": f"different case sets ({fp_before} before, {fp_after} after)"}
    scores_before = before.get("scores") or {}
    scores_after = after.get("scores") or {}
    shared = [m for m in scores_after if m in scores_before]
    if not shared:
        return {"comparable": False, "delta": {}, "reason": "no metric in common"}
    delta = {}
    for m in shared:
        x, y = scores_before[m], scores_after[m]
        if x is None or y is None:
            continue
        delta[m] = float(y) - float(x)
    return {"comparable": True, "delta": delta, "reason": ""}


def gate(scores: dict[str, float], minimum: dict[str, float]) -> dict:
    """Hold `scores` against a minimum per metric.

    Returns `{"passed": bool, "failed": [metric, ...]}`. A metric named in
    `minimum` but absent from `scores`, or present with no value, fails: a
    number you did not measure is not a number that cleared the bar.
    """
    failed = []
    for metric, floor in minimum.items():
        value = scores.get(metric)
        if value is None or float(value) < float(floor):
            failed.append(metric)
    return {"passed": not failed, "failed": failed}
