import requests
from bs4 import BeautifulSoup

url = (
    "https://www.yza.mx/on/demandware.store/"
    "Sites-YzaMexico-Site/es_MX/Search-UpdateGrid"
    "?q=Aspirina"
    "&start=0"
    "&sz=12"
)

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}

r = requests.get(
    url,
    headers=headers,
    timeout=20
)

print("Status:", r.status_code)
print("URL:", r.url)
print("Content-Type:", r.headers.get("Content-Type"))

with open(
    "cache/yza_busqueda.html",
    "w",
    encoding="utf-8"
) as f:
    f.write(r.text)

# ← HASTA AQUÍ ya existe 'r'

soup = BeautifulSoup(r.text, "html.parser")

for i, producto in enumerate(soup.select(".product")[:3], 1):

    print("=" * 40)
    print("Producto", i)

    print(producto.get_text(" ", strip=True))
    print()

    for precio in producto.find_all(
        string=lambda t: "$" in t if t else False
    ):
        print(precio)