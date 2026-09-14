# Mac

## Apple silicon

Everything installs from binary wheels. Nothing to do.

## Intel

Several packages stopped publishing Intel macOS wheels in 2025. The root
`pyproject.toml` pins older versions on Intel automatically (`torch<2.3`,
`transformers<5`, `onnxruntime<1.24`, `numpy<2`). If a wheel still fails to
build, run:

```bash
uv sync --group dev --reinstall
```

and if that fails, use the cloud key rather than local models for the week.

## Homebrew extras

```bash
brew install graphviz   # only if you render diagrams with make diagrams
```
