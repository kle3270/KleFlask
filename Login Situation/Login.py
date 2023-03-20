import sys
sys.path.append('..\Read_write_etc')
import Password_Function
import Read
import Write
import LoginFunction

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
#Main
#Addtonotes = input('What would you like to add')
#Write.Write_file_newline(Addtonotes,'Z_NotePadStorage')
