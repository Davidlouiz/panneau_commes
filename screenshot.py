from pathlib import Path
from tempfile import NamedTemporaryFile

from PIL import Image
from playwright.sync_api import sync_playwright

input_path = Path(__file__).parent / "panneau_commes_v6.html"
output_path = Path(__file__).parent / "panneau_preview.png"
preview_size = (1250, 1000)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(
        viewport={"width": 1250, "height": 1000}
    )  # Ratio 100 cm x 80 cm
    page.goto(f"file://{input_path}", wait_until="networkidle")
    page.evaluate("""
        const image = document.querySelector('.photo-aerial');
        const rect = image.getBoundingClientRect();
        const wm = document.createElement('div');
        wm.textContent = 'EXEMPLE';
        Object.assign(wm.style, {
            position: 'fixed',
            top: `${rect.top + rect.height * 0.64}px`,
            left: `${rect.left + rect.width / 2}px`,
            transform: 'translate(-50%, -50%) rotate(-35deg)',
            fontSize: '320pt',
            fontWeight: 'bold',
            color: 'rgba(180, 0, 0, 0.28)',
            whiteSpace: 'nowrap', pointerEvents: 'none',
            zIndex: '9999', letterSpacing: '8px',
            fontFamily: 'Helvetica, Arial, sans-serif'
        });
        document.body.appendChild(wm);
    """)
    with NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        temp_path = Path(tmp.name)
    page.locator(".page").screenshot(path=str(temp_path))
    browser.close()

with Image.open(temp_path) as image:
    preview = image.resize(preview_size, Image.LANCZOS)
    preview.save(output_path)

temp_path.unlink(missing_ok=True)

print(f"Screenshot : {output_path}")
