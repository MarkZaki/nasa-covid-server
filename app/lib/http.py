import requests


class HttpGetRequest:
    def __init__(self, base_url):
        self.baseUrl = base_url

    def get(self, path="/"):
        return requests.get(self.baseUrl + path).json()
