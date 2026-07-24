import requests
from bs4 import BeautifulSoup

url = "https://prixz.com/?s=Aspirina&post_type=product"

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
    timeout=20,
    allow_redirects=True
)

print("Status:", r.status_code)
print("URL:", r.url)
print("Content-Type:", r.headers.get("Content-Type"))

with open(
    "cache/prix_busqueda.html",
    "w",
    encoding="utf-8"
) as f:
    f.write(r.text)

soup = BeautifulSoup(r.text, "html.parser")

print("product:", len(soup.select(".product")))
print("products:", len(soup.select(".products")))
print("article:", len(soup.select("article")))
print("woocommerce:", len(soup.select(".woocommerce")))

for linea in r.text.splitlines():

    if "data-product-id" in linea:
        print(linea)

    if "woocommerce-LoopProduct-link" in linea:
        print(linea)

    if "price" in linea.lower():
        print(linea)

    print("----------------------------")
    print(r.text[:3000])