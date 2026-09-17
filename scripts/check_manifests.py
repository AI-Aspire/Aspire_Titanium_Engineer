#!/usr/bin/env python3
"""Hold a Kubernetes manifest to the checks a platform review greps for first.

    python scripts/check_manifests.py deploy/k8s.yaml      # one or more files
    python scripts/check_manifests.py -                    # a manifest on stdin
    python scripts/check_manifests.py                      # every */deploy/*.yaml

Every Deployment must run as non-root with a read-only root filesystem, drop
every capability, forbid privilege escalation, pin its image to a tag, declare
requests and limits, carry a readiness and a liveness probe, and have a
PodDisruptionBudget when it runs more than one replica. A Service must select
it. When a check fails, the fix is the manifest, not the check.

The YAML parser here is deliberately small: block-style mappings, sequences,
scalars, comments, and `---` documents, plus `{}`, `[]`, and a flat `[a, b]`.
That covers the manifests the course writes, and it means the check runs with
the standard library alone. PyYAML is not a declared dependency of this
repository, and a check that needs an undeclared package is a check that
silently stops running.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
OK, BAD = "✓", "✗"
_KEY = re.compile(r"^[A-Za-z0-9_.\-/]+:(\s|$)")


# ── a small block-YAML parser ─────────────────────────────────────────────────

def parse_yaml(text: str) -> list:
    """Every document in `text`, as nested dicts, lists, and scalars."""
    docs = []
    for chunk in re.split(r"^---\s*$", text, flags=re.M):
        lines = []
        for raw in chunk.splitlines():
            line = re.sub(r"(^|\s)#.*$", "", raw.replace("\t", "  ")).rstrip()
            if line.strip():
                lines.append(line)
        if lines:
            value, i = _parse(lines, 0, _indent(lines[0]))
            if i < len(lines):
                raise ValueError(f"cannot parse line: {lines[i].strip()!r}")
            docs.append(value)
    return docs


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _is_item(line: str) -> bool:
    s = line.lstrip()
    return s == "-" or s.startswith("- ")


def _parse(lines: list[str], i: int, indent: int):
    if _is_item(lines[i]):
        return _parse_seq(lines, i, indent)
    return _parse_map(lines, i, indent)


def _parse_map(lines: list[str], i: int, indent: int):
    out: dict = {}
    while i < len(lines) and _indent(lines[i]) == indent and not _is_item(lines[i]):
        line = lines[i].strip()
        if not _KEY.match(line):
            raise ValueError(f"expected 'key: value', got {line!r}")
        key, _, rest = line.partition(":")
        key, rest = key.strip(), rest.strip()
        i += 1
        if rest:
            out[key] = _scalar(rest)
        elif i < len(lines) and _indent(lines[i]) > indent:
            out[key], i = _parse(lines, i, _indent(lines[i]))
        elif i < len(lines) and _indent(lines[i]) == indent and _is_item(lines[i]):
            out[key], i = _parse_seq(lines, i, indent)      # a list at its key's indent
        else:
            out[key] = None
    return out, i


def _parse_seq(lines: list[str], i: int, indent: int):
    out: list = []
    while i < len(lines) and _indent(lines[i]) == indent and _is_item(lines[i]):
        item = lines[i].lstrip()[1:].strip()
        inner = indent + 2
        if _KEY.match(item):
            lines[i] = " " * inner + item             # `- key: v` opens a mapping
            value, i = _parse_map(lines, i, inner)
            out.append(value)
        elif item:
            out.append(_scalar(item))
            i += 1
        else:
            i += 1
            if i < len(lines) and _indent(lines[i]) > indent:
                value, i = _parse(lines, i, _indent(lines[i]))
                out.append(value)
            else:
                out.append(None)
    return out, i


def _scalar(s: str):
    if s == "{}":
        return {}
    if s == "[]":
        return []
    if s.startswith("[") and s.endswith("]"):
        return [_scalar(x.strip()) for x in s[1:-1].split(",") if x.strip()]
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    if s == "true":
        return True
    if s == "false":
        return False
    if s in ("null", "~"):
        return None
    for cast in (int, float):
        try:
            return cast(s)
        except ValueError:
            pass
    return s


# ── the checks ────────────────────────────────────────────────────────────────

def check(name: str, docs: list) -> list[str]:
    """Every problem with the manifest, in the words a reviewer would use."""
    problems: list[str] = []
    docs = [d for d in docs if isinstance(d, dict)]
    kinds = {d.get("kind") for d in docs}
    deployments = [d for d in docs if d.get("kind") == "Deployment"]
    services = [d for d in docs if d.get("kind") == "Service"]
    if not deployments:
        return [f"{name}: no Deployment found"]

    for dep in deployments:
        spec = dep.get("spec") or {}
        pod = ((spec.get("template") or {}).get("spec")) or {}
        labels = ((spec.get("template") or {}).get("metadata") or {}).get("labels") or {}
        pod_sc = pod.get("securityContext") or {}
        if pod_sc.get("runAsNonRoot") is not True:
            problems.append(f"{name}: pod has no `runAsNonRoot: true`; containers run as root by "
                            f"default, and this is the most common review finding")
        for c in pod.get("containers") or []:
            cname = c.get("name", "?")
            sc = c.get("securityContext") or {}
            if sc.get("readOnlyRootFilesystem") is not True:
                problems.append(f"{name}: container `{cname}` has no readOnlyRootFilesystem")
            if (sc.get("capabilities") or {}).get("drop") != ["ALL"]:
                problems.append(f"{name}: container `{cname}` does not drop ALL capabilities")
            if sc.get("allowPrivilegeEscalation") is not False:
                problems.append(f"{name}: container `{cname}` allows privilege escalation")
            image = str(c.get("image", ""))
            if ":" not in image.rsplit("/", 1)[-1] or image.endswith(":latest"):
                problems.append(f"{name}: container `{cname}` image is not pinned to a tag")
            res = c.get("resources") or {}
            if not res.get("requests") or not res.get("limits"):
                problems.append(f"{name}: container `{cname}` is missing resource requests or limits")
            for probe in ("readinessProbe", "livenessProbe"):
                if not c.get(probe):
                    problems.append(f"{name}: container `{cname}` has no {probe}")
        if (spec.get("replicas") or 1) > 1 and "PodDisruptionBudget" not in kinds:
            problems.append(f"{name}: replicas > 1 but no PodDisruptionBudget; a node drain can evict "
                            f"every replica at once, so the second replica buys nothing")
        selected = any(set(((s.get("spec") or {}).get("selector") or {}).items()) <= set(labels.items())
                       and (s.get("spec") or {}).get("selector") for s in services)
        if not selected:
            problems.append(f"{name}: no Service selects the pods of Deployment "
                            f"`{(dep.get('metadata') or {}).get('name', '?')}`")
    return problems


def check_text(name: str, text: str) -> list[str]:
    try:
        docs = parse_yaml(text)
    except ValueError as exc:
        return [f"{name}: not parseable as block YAML: {exc}"]
    return check(name, docs)


def main(argv: list[str]) -> int:
    if argv:
        sources = [(a, sys.stdin.read() if a == "-" else Path(a).read_text(encoding="utf-8")) for a in argv]
    else:
        paths = sorted(ROOT.glob("*/deploy/*.yaml")) + sorted(ROOT.glob("project/deploy/*.yaml"))
        sources = [(str(p.relative_to(ROOT)), p.read_text(encoding="utf-8")) for p in paths]
    if not sources:
        print(f"{BAD} no manifests found")
        return 1
    problems = [p for name, text in sources for p in check_text(name, text)]
    for p in problems:
        print(f"{BAD} {p}")
    if problems:
        return 1
    print(f"{OK} {len(sources)} manifest(s) pass the platform-review checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
