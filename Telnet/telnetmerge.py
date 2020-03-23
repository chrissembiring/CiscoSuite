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
        f = open("config.txt", "r")

        teln.read_until("Username: ")
        teln.write(user + "\n")
        if password:
            teln.read_until("Password: ")
            teln.write(password + "\n")

        # IOS commands to be sent to router through Telnet
        teln.write("enable\n")
        teln.write("conf t\n")

        # Read contents of config.txt file line by line and write through telnet
        try:
            for x in f:
                teln.write(x)

        except:
            print("Error in writing config from config.txt")

        f.close()
        teln.write("end\n")
        print("Merge config file to Router " + str(attempt) + " successful")

    except:
        print("Error in accessing Router " + str(attempt))

    attempt = attempt + 1
