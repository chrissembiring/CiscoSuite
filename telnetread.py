import getpass
import sys
import telnetlib

rcount = input("Enter number of routers to connect: ")
attempt = 0
# iterate list of HOSTS to which Telnet connection will be established
while attempt < int(rcount):
    HOST = input("Enter Router " + str(attempt) + " IP address:")
    user = input("Enter your telnet username: ")
    password = getpass.getpass()

    try:
        teln = telnetlib.Telnet(HOST)
        f = open("config" + str(attempt) + ".txt", "a+")

        teln.read_until("Username: ")
        teln.write(user + "\n")
        if password:
            teln.read_until("Password: ")
            teln.write(password + "\n")

        # IOS commands to be sent to router through Telnet
        teln.write("enable\n")
        teln.write("conf t\n")
        teln.write("show running-config\n")
        try:
            output = teln.read_until("end") # parsing Cisco device's output to be extracted to file
            f.write("Config for Router " + str(attempt))
            f.write(output)
            print("Config for Router " + str(attempt) + " has been saved")
            f.close()

        except:
            print("Error in saving config to .txt file")

        teln.close()

    except:
        print("Error in accessing Router " + str(attempt))

    attempt = attempt + 1
    
