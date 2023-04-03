import sys
sys.path.append('..\Read_write_etc')
import Read
import Write
import LoginFunction
import CreateFile
# Useless!!!!!
class User:
    def __init__(self,username,password,numberidentification):
        self.username = username
        self.password = password
        self.identifier = numberidentification
    def add_self(self):
        Users.append(self.username)
        return Users
    def password_add(self):
        Passwords.append(self.password)
    def store_age(self,age):
        self.age = age
        return age


import cgi
print('hi')
form = cgi.FieldStorage()
searchterm =  form.getvalue('searchbox')
print(searchterm)
# Create User list
Users = Read.Joinlist_file('Z_Usernames')
Pass = Read.Joinlist_file('Z_Passwords')
Age = Read.Joinlist_file('Z_Age')

#Add all users to class
for user1 in Users:
    x = int(Users.index(user1))
    User(user1,Pass[x],x)
    numberidentification = x
#Creation
Username =input("Type in your username:")
if Username in Users:
    existing_user = True
else:
    existing_user = False


#Login
if existing_user:
    numberidentification = Users.index(Username)
    password = input("Type in your password:")
    Authentification = LoginFunction.LoginCheck(password, Pass, numberidentification)
    while Authentification != 1:
        password = input("Your password is invalid. Please type in the correct password to login: ")
        Authentification = LoginFunction.LoginCheck(password, Pass, numberidentification)
    print("You have successfully logged in.")
#Sign Up
if not existing_user:
    print("Your username does not exist, lets create an account")
    Username = input("Type in a username: ")
    while Username in Users:
        print(f"{Username} is taken")
        Username = input("Type in a username:")
    password = input("Type in a password:")
    Write.Write_file(password,'Z_Passwords')
    Write.Write_file(Username,'Z_Usernames')
    #CreateFile.Create_file_notes(Username)

#Main
Options = input("1.Quiz\n2.Notes\nWhat would you like to do today?")
#Note taking

'''if Options == "2":
    Linecount = Read.Line_Count(f'Z_{Username}Notes.txt')
    Notepadoption = input('0.Quit\n1.Write\n2.View\n3.Edit\nWhat do you want to do in your notes?')
    while Notepadoption != "0":
        if Notepadoption == '1':
            Note = input('What would you like to write in your notepad?')
            Write.Write_file(f'Line {Linecount + 1} {Note}', f'Z_{Username}Notes.txt')
        if Notepadoption == '2':
            Read.Read_file(f'Z_{Username}Notes.txt')
        if Notepadoption == '3':
           print("Sorry this is a work in progress")
        Read.Read_file(f'Z_{Username}Notes.txt')
        Lineedit = input('Which line would you like to edit?')

        Notepadoption = input('1.Write\n2.View\n3.Quit\nWhat do you want to do in your notes?')
    #Addtonotes = input('What would you like to add')
    #Write.Write_file_newline(Addtonotes,'Z_NotePadStorage')
'''
#CREATE HTML PAGE FOR NOTES
CreateFile.Create_file_html(Username)