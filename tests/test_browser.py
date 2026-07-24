from services.browser_service import BrowserService


with BrowserService(headless=False) as page:

    page.goto("https://www.google.com")

    print(page.title())

    input("Presiona ENTER para cerrar...")