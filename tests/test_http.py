import requests

try:
    r = requests.get(
        "https://www.farmaciasguadalajara.com",
        timeout=(10, 60),   # 10 s para conectar, 60 s para leer
        allow_redirects=True
    )

    print("Status:", r.status_code)
    print("URL:", r.url)
    print("Server:", r.headers.get("Server"))
    print("Content-Type:", r.headers.get("Content-Type"))
    print(r.text[:500])

except Exception as e:
    print(type(e).__name__)
    print(e)