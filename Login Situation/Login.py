import sys
sys.path.append('..\Read_write_etc')
import Password_Function
import Read
import Write

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


# Create User list
Users = []
Users = Read.Joinlist_file('Usernames.txt')
#Creation
Username =input("Type in your username")
if Username in Users:
    existing_user = True
else:
    existing_user = False


#Login
if existing_user:
    number
    password = input("Type in your password:")
#Sign Up
if not existing_user:
    print("Your username does not exist, lets create an account")
    Username = input("Type in a username: ")
    while Username in Users:
        print(f"{Username} is taken")
        Username = input("Type in a username:")
    password = input("Type in a password:")
    Write.Write_file(password,'Passwords.txt')
    Write.Write_file(Username,'Usernames.txt')
