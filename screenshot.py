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
    page.evaluate("""
        const wm = document.createElement('div');
        wm.textContent = 'EXEMPLE';
        Object.assign(wm.style, {
            position: 'fixed', top: '50%', left: '50%',
            transform: 'translate(-50%, -50%) rotate(-35deg)',
            fontSize: '72pt', fontWeight: 'bold',
            color: 'rgba(180, 0, 0, 0.28)',
            whiteSpace: 'nowrap', pointerEvents: 'none',
            zIndex: '9999', letterSpacing: '8px',
            fontFamily: 'Helvetica, Arial, sans-serif'
        });
        document.body.appendChild(wm);
    """)
    page.screenshot(path=str(output_path), full_page=False)
    browser.close()

print(f"Screenshot : {output_path}")
