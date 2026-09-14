"""Notebook UI niceties: a spinner for blocking calls, a progress bar for harness
loops, and styled result tables.

The live, animated pieces (``spinner``, ``track``) are built on IPython display
handles + HTML, *not* on rich's ``Live``. Under ``nbconvert`` rich's progress/spinner
serialize to an empty Jupyter widget — they leave a blank cell in the saved notebook —
whereas a display handle saves a clean final frame. rich is used only for ``table``,
which it renders as HTML the notebook keeps.
"""
import html
import itertools
import threading
import time
from contextlib import contextmanager

from IPython.display import display, HTML


class _Handle:
    """A display handle that tolerates not having one.

    `display(..., display_id=True)` returns a handle inside a Jupyter kernel
    and None everywhere else: marimo, a plain script, a pytest run. Calling
    `.update()` on that None used to raise from a daemon thread, which killed
    the notebook with an error that pointed at the spinner rather than at the
    work it was wrapping.
    """

    __slots__ = ("_h",)

    def __init__(self, obj):
        try:
            self._h = display(obj, display_id=True)
        except Exception:                      # no frontend at all
            self._h = None

    def update(self, obj) -> None:
        if self._h is not None:
            try:
                self._h.update(obj)
            except Exception:                  # a frontend that went away mid-run
                self._h = None

_FRAMES = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"      # braille spinner
from helpers.brand import PRIMARY as _BLUE  # slate-700


@contextmanager
def spinner(label: str = "thinking", *, clear: bool = True):
    """Animate a dim spinner + elapsed time while a blocking call runs.

        with spinner("calling the judge"):
            resp = client.chat.completions.create(...)   # no streamed output to show

    A daemon thread redraws the frame; on exit the line is wiped (``clear=True``) so
    the saved notebook shows only the result, or left as a "✓ done" tick otherwise.
    """
    handle = _Handle(HTML(""))
    stop = threading.Event()
    start = time.monotonic()

    def _spin():
        for frame in itertools.cycle(_FRAMES):
            if stop.is_set():
                break
            secs = time.monotonic() - start
            handle.update(HTML(
                f'<span style="opacity:0.6;font-style:italic">{frame} '
                f'{html.escape(label)}… {secs:0.0f}s</span>'
            ))
            time.sleep(0.1)

    thread = threading.Thread(target=_spin, daemon=True)
    thread.start()
    try:
        yield
    finally:
        stop.set()
        thread.join(timeout=0.5)
        if clear:
            handle.update(HTML(""))
        else:
            secs = time.monotonic() - start
            handle.update(HTML(
                f'<span style="opacity:0.6;font-style:italic">✓ '
                f'{html.escape(label)} ({secs:0.0f}s)</span>'
            ))


def _bar(label, n, total, secs, suffix):
    frac = n / total if total else 1.0
    width = 24
    filled = round(width * frac)
    bar = "█" * filled + "░" * (width - filled)
    pct = f"{frac * 100:0.0f}%"
    return HTML(
        '<span style="font-family:ui-monospace,Menlo,monospace;font-size:0.9em">'
        f'{html.escape(label)} '
        f'<span style="color:{_BLUE}">{bar}</span> '
        f'{n}/{total} ({pct}) · {secs:0.0f}s '
        f'<span style="opacity:0.6">{html.escape(suffix)}</span></span>'
    )


def track(iterable, label: str = "working", *, total: int = None):
    """Wrap a loop with a live progress bar that saves a clean final frame.

        for spec in track(tasks, "trajectories"):
            run_trajectory(spec)

    Pass ``total`` when the iterable has no ``len`` (a generator). The bar redraws
    after each item and ends on a full bar, so the executed notebook keeps a tidy
    "12/12 (100%)" rather than an empty widget.
    """
    if total is None:
        try:
            total = len(iterable)
        except TypeError:
            iterable = list(iterable)
            total = len(iterable)
    handle = _Handle(_bar(label, 0, total, 0.0, ""))
    start = time.monotonic()
    n = 0
    for item in iterable:
        yield item
        n += 1
        handle.update(_bar(label, n, total, time.monotonic() - start, ""))


def table(df, *, title: str = None, float_fmt: str = "{:.3f}", index_label: str = ""):
    """Render a pandas DataFrame as a styled rich table (saved as HTML by nbconvert).

    Keep the DataFrame for any downstream maths — this is just the pretty view.
    """
    from rich.console import Console
    from rich.table import Table

    t = Table(title=title, header_style="bold", title_style="bold")
    t.add_column(df.index.name or index_label)
    for col in df.columns:
        t.add_column(str(col), justify="right")
    for idx, row in df.iterrows():
        cells = [str(idx)]
        for v in row:
            cells.append(float_fmt.format(v) if isinstance(v, float) else str(v))
        t.add_row(*cells)
    Console().print(t)
