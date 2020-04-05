import requests
import json
import merakiapi

api_key = merakiapi.api_key
url = "https://api.meraki.com/api/v0/organizations"

headers = {
    "X-Cisco-Meraki-API-Key": api_key,
}

orgs = requests.get(url, headers=headers)
orgs = orgs.json()
print(json.dumps(orgs, indent=4))

for org in orgs:
    print(org['id'])
    url = "https://api.meraki.com/api/v0/organizations/"+org['id']+"/networks"
    networks = requests.get(url, headers=headers)
    networks = networks.json()
    print(json.dumps(networks, indent=4))
    for network in networks:
        print(network['id'])