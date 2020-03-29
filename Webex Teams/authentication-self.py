import requests
import json

# Insert Webex API as distributed by Webex Developers. Changes once every 12 hours.
access_token = ''

url = 'https://api.ciscospark.com/v1/people/me'

headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

params = {
    "max": 1
}

res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent = 4))
