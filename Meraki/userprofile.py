import requests
import json
import merakiapi

url = "https://api.meraki.com/api/v0/organizations"
api_key = merakiapi.api_key

headers = {
    "X-Cisco-Meraki-API-Key": api_key,
}

orgs = requests.get(url, headers = headers)
print(json.dumps(orgs.json(), indent=4))