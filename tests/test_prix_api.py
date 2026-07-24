import requests

url = (
    "https://us1-search.doofinder.com/5/search"
    "?hashid=0f971656ce788fb047d3bb59035ce949"
    "&page=1"
    "&rpp=10"
    "&query=Aspirina"
)

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(
    url,
    headers=headers,
    timeout=20
)

print("Status:", r.status_code)
print("Content-Type:", r.headers.get("Content-Type"))

print(r.text[:1000])