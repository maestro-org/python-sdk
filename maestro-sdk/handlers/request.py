import requests
from urllib.parse import urljoin
import json

def get_request(maestro_session, endpoint, params = {}):
    headers = {
        "api-key": maestro_session.api_key,
        "content-type": "application/json"
    }
    url = urljoin(maestro_session.base_url, endpoint)
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return json.loads(response.text)
