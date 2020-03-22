from netmiko import Netmiko
from netmiko import ConnectHandler
from RouterClass import Router

# Define SSH's port number
PORT_NUMBER = 22

# Define router objects to which SSH connection are to be established
SR1 = Router('10.54.86.103', 'SR-CDA-1', 'admin', 'CDALAB!0')
SR2 = Router('10.54.86.84', 'SR-CDA-2', 'admin', 'CDALAB!0')
AGG1 = Router('10.54.86.100', 'AGG-CDA-1', 'admin', 'CDALAB!0')
AGG2 = Router('10.54.86.89', 'AGG-CDA-2', 'admin', 'CDALAB!0')
PAG1 = Router('10.54.86.92', 'PAG-CDA-1', 'admin', 'CDALAB!0')
PAG2 = Router('10.54.86.95', 'PAG-CDA-2', 'admin', 'CDALAB!0')
CSG1 = Router('10.54.86.91', 'CSG-CDA-1', 'admin', 'CDALAB!0')
CSG2 = Router('10.54.86.90', 'CSG-CDA-2', 'admin', 'CDALAB!0')
XTC = Router('10.54.86.80', 'XTC-CDA-1', 'admin',  'CDALAB!0')
VRR = Router('10.54.86.81', 'VRR-CDA-1', 'admin', 'CDALAB!0')

# Array of routers as defined above
devices = [SR1, SR2, AGG1, AGG2, PAG1, PAG2, CSG1, CSG2, XTC, VRR]

for device in devices:
    try:

        labRouter = {
            'device_type': 'cisco_ios',
            'ip': device.inputIpAddr,
            'username': device.inputUser,
            'password': device.inputPassword,
            'port': PORT_NUMBER,
            # 'secret': '%',     # Add secret password, if any
            'verbose': True
        }

        connectRouter = ConnectHandler(**labRouter)
        prompt = connectRouter.find_prompt()
        print(prompt)
        print('Entering Privileged EXEC mode...')
        connectRouter.enable()

        fileName = device.inputHostName + '.cfg' # or '.txt', depending on file format

        commmandList = connectRouter.send_config_from_file(fileName)
        print(commmandList)

        connectRouter.disconnect()
        print('Connection to ' + device.inputHostName + ' is now closed.')
