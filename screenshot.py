import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

input_path = Path(__file__).parent / "panneau_commes.html"
output_path = Path(__file__).parent / "panneau_preview.png"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(
        viewport={"width": 1122, "height": 794}
    )  # A4 landscape @ 96dpi
    page.goto(f"file://{input_path}", wait_until="networkidle")
    page.screenshot(path=str(output_path), full_page=False)
    browser.close()

print(f"Screenshot : {output_path}")
