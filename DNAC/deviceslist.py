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

def get_device(dnacip, headers, params, modifier):

    uri = "https://"+dnacip+"/dna/intent/api/v1/network-device"+modifier
    try:
        if params == "":
            print("\n---\nGET %s"%(uri))
        
        else:
            print("\n---\nGET %s?%s"%(uri, params))

        resp = requests.get(uri, headers = headers, params=params, verify=False)
        return resp

    except:
        print("Status: %s"%r.status_code)
        print("Response: %s"%r.text)
        sys.exit()

token = get_token(dnacip, username, password)
print("Returned Authentication token: ", (token))

headers = {"x-auth-token": token}

params = ""
modifier = "/count"
resp = get_device(dnacip, headers, params, modifier)
print("All devices count: ", json.dumps(resp.json()["response"]))

params = ""
modifier = ""
resp = get_device(dnacip, headers, params, modifier)
print(json.dumps(resp.json()["response"], indent=4))