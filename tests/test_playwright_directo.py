from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        channel="chrome"   # Usa Google Chrome instalado, no Chromium de Playwright
    )

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://www.google.com", wait_until="domcontentloaded")

    print(page.title())
    print(page.url)

    input("ENTER para cerrar")

    browser.close()