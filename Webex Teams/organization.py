import requests
import json
import api-token

access_token = api-token.api_token

url = 'https://api.ciscospark.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

params = {
    'email': ''
}

res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent = 4))
