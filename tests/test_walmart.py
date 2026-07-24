import requests

url = "https://super.walmart.com.mx/search?q=Aspirina"

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
    "cache/walmart_busqueda.html",
    "w",
    encoding="utf-8"
) as f:
    f.write(r.text)

print("Archivo guardado.")