import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://sandboxsdwan.cisco.com:8443/j_security_check'
login_body = {
    'j_username': 'devnetuser',
    'j_password': 'Cisco123!'
}

session = requests.session()
response = session.post(url, data=login_body, verify=False)

if not response.ok or response.text:
    print('login failure')
    import sys
    sys.exit(1)

else:
    print ('login successful')

url = 'https://sandboxsdwan.cisco.com:8443/dataservice/device'

device_response = session.get(url, verify=False).json()['data']

for device in device_response:
    print(f"Hostname: {device['host-name']}")
    ip = device['local-system-ip']
    print(f"IP: {device['local-system-ip']}")
    print(f"Model: {device['device-model']}")
    vpn_url = f"https://sandboxsdwan.cisco.com:8443/dataservice/device/ipsec/outbound?deviceId={ip}"
    vpn_response = session.get(vpn_url, verify = False).json()['data']

    for tunnel in vpn_response:
        if vpn_response.index(tunnel) == 0:
            print('First VPN tunnel')
        else:
            print('Next tunnel')
        print(tunnel['dest-ip'])
        print(tunnel['remote-tloc-address'])
    print(' ')