from dotenv import load_dotenv # from imports files/libraries that python community have created, dotenv: module name
import os # import files/libraries that python guys have created, directly used
class VWOLoginPage:

    def __init__(self, email_arg, password_arg):

        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        load_dotenv() #loads the file and getenv retrives the fields
        if self.email == os.getenv("USERNAME") and self.password == os.getenv("PASSWORD"):
            print("Allowed, Login Sucess")
        else:
            print("Login Failed")


email = input("Enter the vwo login email ")
password = input("Enter the vwo login password ")

vwo_object_ref = VWOLoginPage(email,password)
vwo_object_ref.login_confirm()

print(os.name)