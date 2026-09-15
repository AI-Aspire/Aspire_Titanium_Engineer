"""Browser-facing Markdown must survive conversion inside disclosures."""
import importlib.util
import sys
from pathlib import Path

from bs4 import BeautifulSoup

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location('make_marimo', SCRIPTS / 'make_marimo.py')
converter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(converter)


def test_disclosure_renders_table_quote_and_code_without_changing_source():
    source = '<details><summary>Recorded</summary>\n\n| A | B |\n|---|---|\n| 1 | 2 |\n\n> Evidence\n\n```json\n{"ok": true}\n```\n\n</details>'
    soup = BeautifulSoup(converter.render_disclosures(source), 'html.parser')
    assert soup.summary.text == 'Recorded'
    assert [c.text for c in soup.select('tbody td')] == ['1', '2']
    assert soup.blockquote.get_text(strip=True) == 'Evidence'
    assert '{"ok": true}' in soup.pre.text
    assert converter.render_disclosures('Plain **Markdown**') == 'Plain **Markdown**'
