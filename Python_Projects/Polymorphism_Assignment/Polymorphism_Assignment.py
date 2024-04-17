class User:
    name = "Billie Jean"
    email = "notmylover@gmail.com"
    password = "just_a_girl82"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

class Employee(User):
    base_pay = 21.50
    department = "General"
    pin_number = "8039"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.")

class Customer(User):
    mailing_address = ' '
    mailing_list = True

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_address = input("Enter your mailing address: ")
        if (entry_email == self.email and entry_address == self.mailing_address):
            print("Thank you, {}!".format(entry_name))
        else:
            print("The address or email is incorrect.")    

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()
