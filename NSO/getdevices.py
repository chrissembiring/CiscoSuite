import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

username = 'admin'
password = 'admin'

url = "https://10.54.86.38/restconf/data/tailf-ncs:devices/device=ios0/config"

headers = {
    'Content-Type': "application/yang-data+json"
}

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
response = requests.get(url,
                        auth=(username, password),
                        headers = headers,
                        verify = False)

print(response.text)
