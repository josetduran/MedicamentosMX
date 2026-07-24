import requests

url = "https://www.fahorro.com/rest/mx/V1/products-render-info"

r = requests.get(
    url,
    timeout=20
)

print(r.status_code)
print(r.headers.get("Content-Type"))
print(r.text[:500])