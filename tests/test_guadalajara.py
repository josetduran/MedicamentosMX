from services.browser_service import BrowserService

with BrowserService(headless=False) as page:

    page.goto(
        "https://www.farmaciasguadalajara.com/",
        wait_until="domcontentloaded"
    )

    print("Título:", page.title())

    input("Presiona ENTER para cerrar...")