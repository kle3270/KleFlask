#Find use!!!
import DATA_ReadWriteEditFiles
Usernames = DATA_ReadWriteEditFiles.Read_file('DATA_USER.txt')
Passwords = DATA_ReadWriteEditFiles.Read_file('DATA_PASS')
Userlist = Usernames.split('\n')
Passlist = Passwords.split('\n')

class User:
    usernumber = 0
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.usernumber = User.usernumber
        User.usernumber += 1
        Userlist.append(username)
        Passlist.append(password)
        DATA_ReadWriteEditFiles.Write_file(f'{username}','DATA_USER.txt')
        DATA_ReadWriteEditFiles.Write_file(f'{password}','DATA_PASS')
    def __str__(self):
        return f'{self.password}'


def LoginCheck(username,password):
    index = 0
    print('Working')
    for x in range(len(Usernames)):
        if username == Userlist[x]:
            index = x
            print('test')
            if password == Passlist[index]:
                print('try')
                return True
            else:
                return False


def listcheck():
    print(Userlist,Passlist)