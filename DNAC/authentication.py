import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import sys

dnacip = "devasc-dnacenter-1.cisco.com"
username = "devnetuser"
password = "C!3c0d$Y"

def get_token(dnacip, username, password):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    post_uri = "https://"+dnacip+"/dna/system/api/v1/auth/token"
    print("\nAuthenticate: POST %s"%(post_uri))

    try:
        r = requests.post(post_uri, auth=(username, password), verify=False)
        return r.json()["Token"]

    except:
        print("Status: %s"%r.status_code)
        print("Response: %s"%r.text)
        sys.exit()

token = get_token(dnacip, username, password)
print("Returned authentication token: ", (token))