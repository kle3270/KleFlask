#Check If Login Already Exists
def LoginCheck(Username,Password,Userlist,Passlist,identifier):
    if Username in Userlist:
        print("Logging in...")
        if Passlist[identifier] != Password:
            Authentification = 0
        else:
            Authentification = 1
    else:
        print("Your account does not exist")
    return Authentification
