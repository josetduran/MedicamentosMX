import requests
from urllib.parse import quote

medicamento = "Aspirina"

url = (
    "https://www.fahorro.com/catalogsearch/result/?q="
    + quote(medicamento)
)

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}

respuesta = requests.get(
    url,
    headers=headers,
    timeout=20
)

print("Status:", respuesta.status_code)
print("URL:", respuesta.url)

with open(
    "cache/fahorro_busqueda.html",
    "w",
    encoding="utf-8"
) as f:
    f.write(respuesta.text)

print("Archivo guardado.")