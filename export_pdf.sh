#!/bin/bash
# Convertit panneau_commes_v6.html en PDF via Playwright (Chromium).
# Rendu identique au navigateur, au format 100 cm × 80 cm.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
INPUT="$SCRIPT_DIR/panneau_commes_v6.html"
OUTPUT="$SCRIPT_DIR/panneau_commes.pdf"

"$SCRIPT_DIR/.venv/bin/python" - "$INPUT" "$OUTPUT" <<'PYEOF'
import sys
from playwright.sync_api import sync_playwright

input_path = sys.argv[1]
output_path = sys.argv[2]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file://{input_path}", wait_until="networkidle")
    page.pdf(
        path=output_path,
        landscape=True,
        width="1000mm",
        height="800mm",
        margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        print_background=True,
    )
    browser.close()

print(f"PDF généré : {output_path}")
PYEOF
