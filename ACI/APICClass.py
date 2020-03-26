# Define ACI class
class APIC:
    def __init__(self, apicIPaddress, apicHostName, apicUser, apicPass):
        self.apicIPaddress = apicIPaddress
        self.apicHostName = apicHostName
        self.apicUser = apicUser
        self.apicPass = apicPass
