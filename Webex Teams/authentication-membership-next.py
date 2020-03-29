import requests
import json

# Insert Webex API as distributed by Webex Developers. Changes once every 12 hours.
access_token = ''

url = 'https://api.ciscospark.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

params = {
    "max" : 1
}

res = requests.get(url, headers=headers, params=params)
second_res = requests.get(res.links['next']['url'], headers=headers)
formatted_message = """
Webex Teams API Response
---------------------------------------
Response Status Code    : {}
Response Link Header    : {}
Response Body           : {}
---------------------------------------
""".format(second_res.status_code, second_res.headers.get('Link'), json.dumps(second_res.json(), indent=4))
print(formatted_message)
