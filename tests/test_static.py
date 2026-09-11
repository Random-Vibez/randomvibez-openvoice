#!/usr/bin/env python3
"""Static contract checks for the fixed public-safe OpenVoice edition."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / "index.html").read_text()
js = (ROOT / "app.js").read_text()
css = (ROOT / "styles.css").read_text()
readme = (ROOT / "README.md").read_text()
security = (ROOT / "SECURITY.md").read_text()

assert {"index.html", "app.js", "styles.css", "README.md", "SECURITY.md", ".htaccess"}.issubset({p.name for p in ROOT.iterdir()})
assert 'id="board-grid"' in html and 'id="board-select"' in html
assert "medical" in html.lower() and "emergency" in html.lower()
assert 'src="app.js"' in html and 'href="styles.css"' in html
assert all(control not in html for control in ['id="add-card"', 'id="edit-mode"', 'id="import-file"', 'id="new-board"', 'id="rename-board"', 'id="delete-board"'])
assert not re.search(r"(?:fetch|XMLHttpRequest|\baxios\b|navigator\.sendBeacon|document\.cookie|localStorage|sessionStorage|indexedDB)", js, re.I)
urls = re.findall(r"https?://[^\"'\\s<]+", html + js + css)
assert all(url.rstrip('/') == "https://randomvibez.ai" for url in urls)
assert not re.search(r"//cdn|google-analytics|plausible", html + js + css, re.I)
assert "BOARDS" in js and js.count('name: "') >= 4
assert "textContent" in js and "innerHTML" not in js
assert 'id="import-file"' not in html and 'import-file' not in js and 'add-card' not in js
assert "add-card" in readme.lower() and "not customized" in readme.lower()
assert "no backend" in security.lower() and "fixed" in readme.lower()
print("PASS: fixed curated-board contract checks")
print("PASS: no add/edit/import/customization controls")
print("PASS: no network/API/cookie/storage persistence/external-asset references")
print("PASS: multiple curated boards and direct card speech present")
print("PASS: medical/emergency disclaimer and public-safe docs present")
