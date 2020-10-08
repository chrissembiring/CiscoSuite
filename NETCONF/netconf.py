from ncclient import manager

router = {
    "host": "ios-xe-mgmt-latest.cisco.com",
    "port": "10000",
    "username": "developer",
    "password": "Cisco12345"
}

netconf_filter = """
  <filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
        <name>GigabitEthernet2</name>
      </interface>
    </interfaces>

"""


with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
    m.close_session()