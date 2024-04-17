class User:
    name = "No Name provided"
    email = ""
    password = "4321dcba"
    acount_number = 0

    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")

class Employee(User):
    base_pay = 22.50
    department = 'General'

class Customer(User):
    mailing_address = ' '
    mailing_list = True
