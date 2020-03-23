import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

APIC_SITEA = "https://10.54.86.4/"
APIC_SITEB = "https://10.54.86.7/"

ACI_SITES = [APIC_SITEA, APIC_SITEB]

for ACI_SITE in ACI_SITES:
    def apic_login():
        # Login to APIC

        token = ""
        err = ""

        try:
            response = requests.post(
                url=ACI_SITE+"/api/aaaLogin.json",
                headers={
                    "Content-Type": "application/json; charset=utf-8",
                },
                data=json.dumps(
                    {
                        "aaaUser": {
                            "attributes": {
                                "name": "admin",
                                "pwd": "CDALAB!0"
                            }
                        }
                    }
                ),
                verify=False
            )

            json_response = json.loads(response.content)
            token = json_response['imdata'][0]['aaaLogin']['attributes']['token']
            print('Authentication token:', token)

            print('Authentication Response Status: {status_code} \n'.format(
                status_code=response.status_code))

        except requests.exceptions.RequestException as err:
            print("HTTP Request failed")
            print(err)

        return token

    def get_tenants():
        # Get ACI Tenants

        token = apic_login()
        url=ACI_SITE+"/api/node/class/fvTenant.json"
        print('GET request resource: ', url)

        try:
            response = requests.get(
                url,
                headers={
                    "Cookie": "APIC-cookie=" + token,
                    "Content-Type": "application/json; charset=utf-8",
                },
                verify=False
            )

            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body:', json.dumps(response.json(), indent=4))

        except requests.exceptions.RequestException:
            print("HTTP Request failed")


    def get_devices():
        # Get ACI devices

        token = apic_login()
        url=ACI_SITE+"/api/node/class/topology/pod-1/topSystem.json"
        print('GET request resource: ', url)

        try:
            response = requests.get(
                url,
                headers={
                    "Cookie": "APIC-cookie=" + token,
                    "Content-Type": "application/json; charset=utf-8"
                },
                verify=False
            )

            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body:', json.dumps(response.json(), indent=4))

        except requests.exceptions.RequestException:
            print("HTTP Request failed")

    # Suppress credential warning for this exercise:
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    print('=====LIST OF TENANTS=====')
    get_tenants()
    print('=====LIST OF DEVICES=====')
    get_devices()
