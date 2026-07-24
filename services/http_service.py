import requests


class HttpService:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/138.0 Safari/537.36"
        })

    def get(self, url, **kwargs):
        return self.session.get(
            url,
            timeout=30,
            **kwargs
        )