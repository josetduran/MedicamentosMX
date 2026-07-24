import requests

urls = [
    "https://www.google.com",
    "https://www.microsoft.com",
    "https://www.farmaciasguadalajara.com",
]

for url in urls:
    print(f"\nProbando: {url}")

    try:
        r = requests.get(url, timeout=20)

        print("Status:", r.status_code)
        print("Server:", r.headers.get("Server"))
        print("Content-Type:", r.headers.get("Content-Type"))

    except Exception as e:
        print(type(e).__name__, e)