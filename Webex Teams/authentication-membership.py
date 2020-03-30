import requests
import json

# Insert Webex API as distributed by Webex Developers. Changes once every 12 hours.
access_token = api-token.api_token

url = 'https://api.ciscospark.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

params = {
    "max" : 100
}

res = requests.get(url, headers=headers, params=params)
formatted_message = """
Webex Teams API Response
---------------------------------------
Response Status Code    : {}
Response Link Header    : {}
Response Body           : {}
---------------------------------------
""".format(res.status_code, res.headers.get('Link'), json.dumps(res.json(), indent=4))
print(formatted_message)
