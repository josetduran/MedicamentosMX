from services.browser_service import BrowserService

with BrowserService(headless=False) as page:

    page.goto(
        "https://www.farmaciasguadalajara.com/",
        wait_until="domcontentloaded"
    )

    page.wait_for_timeout(3000)

    print(page.content())

    input("ENTER para cerrar...")