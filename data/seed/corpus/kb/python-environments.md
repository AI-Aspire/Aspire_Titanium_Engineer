# Python environments

The engineering standard is `uv` with one environment per repository.

## The optional-group problem

`uv sync` is exact. It removes anything not in the groups it was asked for.
So a plain `uv sync` silently uninstalls an optional group you installed on
purpose, and the next notebook fails with `ModuleNotFoundError` even though
you changed nothing. Repositories that follow the standard provide
`make setup`, which keeps groups that are already present.

## Intel Macs

Several packages stopped publishing Intel macOS wheels. Pin `torch<2.3`,
`transformers<5`, `onnxruntime<1.24`, and `numpy<2` on Intel, or use a cloud
model for the week.

## Local vector stores

The embedded Qdrant store is single-writer. "Storage folder already accessed
by another instance" means a second kernel holds the folder. Restart the other
kernel.

## Proxies

If wheel downloads hang on the office network, set `HTTPS_PROXY` to the value
on the intranet networking page.
