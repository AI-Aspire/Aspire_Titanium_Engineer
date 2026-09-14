"""The output scrubber and the mirror normaliser."""
import strip_outputs as S
import make_marimo as M


def _nb(*texts):
    return {"metadata": {"widgets": {"state": {}}}, "cells": [
        {"cell_type": "code", "source": ["print(1)\n"], "execution_count": 1, "metadata": {},
         "outputs": [{"output_type": "stream", "name": "stdout", "text": [t]} for t in texts]}]}


def test_scrub_removes_secrets_and_internal_endpoints():
    nb = _nb("all fine\n", "key sk-abcdefghijklmnop\n", "base http://10.0.0.5:8000/v1\n", "/Users/someone/repo\n")
    changed = S.scrub(nb)
    outs = nb["cells"][0]["outputs"]
    assert changed == 4   # widgets + three outputs
    assert outs[0]["text"] == ["all fine\n"]
    for o in outs[1:]:
        assert "removed" in o["text"][0]
    assert "widgets" not in nb["metadata"]


def test_scrub_keeps_https_and_small_outputs():
    nb = _nb("see https://docs.example.com\n")
    assert S.scrub(nb) == 1   # only the widgets key
    assert "https://docs.example.com" in nb["cells"][0]["outputs"][0]["text"][0]


def test_scrub_drops_oversized_output():
    nb = _nb("x" * (S.MAX_BYTES + 1))
    S.scrub(nb)
    assert "removed" in nb["cells"][0]["outputs"][0]["text"][0]


def test_drop_all_outputs():
    nb = _nb("a", "b")
    S.scrub(nb, drop_all=True)
    assert nb["cells"][0]["outputs"] == [] and nb["cells"][0]["execution_count"] is None


def test_marimo_normalise_ignores_version_line():
    a = 'import marimo\n__generated_with = "0.24.2"\napp = marimo.App()\n'
    b = 'import marimo\n__generated_with = "0.24.3"\napp = marimo.App()\n'
    assert M._normalise(a) == M._normalise(b)


def test_child_error_skips_kernel_noise():
    """A failing own-env module must report its traceback, not a kernel warning."""
    import check_execute as E
    blob = ("[IPKernelApp] WARNING | Kernel is running over TCP without encryption.\n"
            "✗ 08_SDG_RAGAS/x.ipynb: ValueError: no testset rows\n"
            "[IPKernelApp] WARNING | to enable transport encryption\n")
    assert E._child_error(blob) == "ValueError: no testset rows"
    assert E._child_error("[IPKernelApp] WARNING | noise\nreal failure here\n") == "real failure here"
    assert E._child_error("") == "failed with no message"
