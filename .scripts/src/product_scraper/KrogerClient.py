import requests
import json
import simple_cache
from base64 import b64encode
from product_scraper import kroger_login

class KrogerClient:
    def __init__(self, host):
        self.host = host
        self.bearer = self.__get_token()

    def get_location(self, zipcode, radius=5):
        url = f"{self.host}/locations"\
            f"?filter.zipCode.near={zipcode}"\
            f"&filter.radiusInMiles={radius}"\
            f"&filter.chain=Fred"
        return self.__get(url)

    def get_products(self, term, location_id, limit=4):
        url = f"{self.host}/products"\
            f"?filter.locationId={location_id}"\
            f"&filter.term={term}"\
            f"&filter.limit={limit}"
        return self.__get(url)

    def __get(self, url):
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.bearer}"
        }

        response = requests.get(url, headers=headers)
        return json.loads(response.text)

    @simple_cache.cache_it("access_token.cache", 1800)
    def __get_token(self):
        url = f"{self.host}/connect/oauth2/token"
        body = {
            "grant_type": "client_credentials",
            "scope": kroger_login.scopes
        }

        client_bytes = f"{kroger_login.client_id}:{kroger_login.client_secret}".encode("ascii")
        secret = b64encode(client_bytes).decode("ascii")
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Authorization': f"Basic {secret}"
        }
        response = requests.post(url, data=body, headers=headers)
        return json.loads(response.text).get('access_token')
