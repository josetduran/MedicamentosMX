from services.browser_service import BrowserService

with BrowserService(headless=False) as page:

    print("Abriendo Google...")

    page.goto(
        "https://www.google.com",
        wait_until="networkidle",
        timeout=60000
    )

    print("Título:", page.title())
    print("URL:", page.url)

    input("Presiona ENTER para cerrar...")