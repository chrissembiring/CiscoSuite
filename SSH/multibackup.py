import paramikomodule
import datetime
from RouterClass import Router

# Define today's date
"""
todayDate = datetime.datetime.now()
todayStr = str(todayDate.year) + '-' + str(todayDate.month) + '-' + str(todayDate.day)
"""

# Define SSH's port number
PORT_NUMBER = 22

# Define router objects to which SSH connection are to be established
## Class parameters are (IP address, hostname, EXEC username, EXEC password)
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
        ssh_client = paramikomodule.connect(device.inputIpAddr, PORT_NUMBER, device.inputUser, device.inputPassword) # Establish SSH connection to router
        print('\nConnection to ' + device.inputHostName + ' established.')
        remote_connection = paramikomodule.get_shell(ssh_client)

        paramikomodule.send_command(remote_connection, 'en') # Send "enable" command to the IOS-XE window
        # paramikomodule.send_command(remote_connection, '%') # Add privileged EXEC mode password, if any
        paramikomodule.send_command(remote_connection, 'terminal length 0') # Prevent IOS-XE output to be truncated

        output = paramikomodule.request_config(remote_connection) # Send "show running-config" command to the IOS-XE window

        outputStr = output.decode() # Decode from UTF-8 to ASCII

        list = outputStr.split('\n')
        list = list[4:-1]
        config = '\n'.join(list)

         # Open or create file with the specific format

        # Use this command if the dates are to be appended at the end of filenames.
        """
        file = device.inputHostName + '-' + todayStr + '.cfg'
        """

        file = device.inputHostName + '.cfg' # or +'.txt' if a plain textfile is preferred

        with open(file, 'w') as f:
            print('Saving config from ' + device.inputHostName)
            f.write(config)
            print('Config from ' + device.inputHostName + ' saved')

    except AuthenticationException:
        print('Authentication to ' + device.inputHostName + ' failed, please check your credentials.')

    except SSHException as sshException:
        print('Unable to establish SSH connection. Check the server\'s IP address or if the server is powered on. %s', sshException)

    except BadHostKeyException as badHostKeyException:
        print('Unable to verify server\'s host key. %s', badHostKeyException)

    finally:
        paramikomodule.close(ssh_client)
        print('Connection to ' + device.inputHostName + ' is now closed.')
