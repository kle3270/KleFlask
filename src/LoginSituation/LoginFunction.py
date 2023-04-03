#Check If Login Already Exists
def LoginCheck(Password,Passlist,identifier):
    print("Logging in...")
    if Passlist[identifier] != Password:
        Authentification = 0
    else:
            Authentification = 1
    return Authentification
