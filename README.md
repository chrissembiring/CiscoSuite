# CiscoSSH
Example for backing up Cisco router configuration files by SSH connection.

Before using this file, ensure the paramiko library is installed in your machine. Use "pip install paramiko" in your shell window in case paramiko has not been installed.

- multibackup.py
The multibackup.py script is used to pull the routers' running-config file and save them as separate .cfg files (or, if preferred, .txt files). Edit the routers' information and list to suit your existing infrastructure.

- multiconfig.py
The reverse of the earlier script, multiconfig.py is used to read the generated .cfg (or .txt) files line by line and send them as a command through SSH connection.

# ciscotelnet
Python3 scripts to save multiple Cisco routers' configurations and upload config from a text file.

### telnetread.py
telnetread.py is a script for a network admin to copy the existing configuration of Cisco devices.

The admin will first be prompted to enter the number of routers/switches to be accessed, followed by the IP address, username and password of the device which a telnet connection will be established.
The script will then establish a telnet connection open a .txt file named "config.txt", to which the configuration of routers will be copied and appended.
This process will be repeated as many times as the number entered in the first prompt.

### telnetmerge.py
telnetmerge.py is a script for a network admin to append configurations from a .txt file to Cisco devices.

Similar to telnetread.py, the admin will be asked to enter number of routers/switches to be accessed, followed by IP address, username and password of the device to be accessed via telnet.
After the script successfully entered the EXEC mode of the Cisco device, the script will read the .txt file named "config.txt" line by line, and write the lines to the Cisco device's command interface.

These scripts are written with assumptions in mind, as follows:

- *No prompt error checking (for now).* These scripts assume that details requested by the prompts (i.e. IP addresses, usernames and passwords) are entered correctly at the first attempt. Should these details are entered correctly, telnet connection will not be established and the script will proceed to connect to the next device instead.
- *Text file name.* The name of the .txt file "config.txt" is hardcoded. If a config.txt file is not found in the directory while running telnetread.py, that file will simply be created in the same directory the terminal is running. If the file is not found while running telnetmerge.py, the filestream will simply fail.
- *No error checking for config appended to the Cisco device.* The telnetmerge.py script assumes that the config.txt from which it sends IOS command via telnet are correctly written. There is no error check for typos, missing command etc. The script simply open the filestream, read the config.txt line by line, sends the lines through telnet, and finally closes the filestream and telnet connection before moving on to establishing connection to the next device.
- *Single config.txt file for telnetmerge.py.* The telnetmerge.py assumes that the same config file will be used to append/merge configuration of multiple Cisco devices.

Please notify me or raise issue should there be any errors or bugs found when running these scripts.
