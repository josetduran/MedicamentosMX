from bs4 import BeautifulSoup

with open(
    "cache/benavides_busqueda.html",
    encoding="utf-8"
) as f:
    soup = BeautifulSoup(f, "html.parser")

productos = soup.select(".product-item")

print("Productos:", len(productos))

for producto in productos:

    nombre = producto.select_one(".product-item-name")
    precio = producto.select_one(".price-wrapper")

    if nombre and precio:

        print(nombre.get_text(strip=True))
        print(precio.get("data-price-amount"))
        print("-" * 40)