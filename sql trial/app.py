import sys

from dbhelper import DBHelper


class Flipkart:
    def __init__(self):
        self.db = DBHelper()
        self.menu()

    def menu(self):
        user_input = input("""
1. Register
2. Login
3. Exit
Enter your choice: """)

        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit()

    def register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if self.db.add_user(name, email, password):
            print("Registration successful")
        else:
            print("Email already registered")

        self.menu()

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if self.db.check_user(email, password):
            print("Login successful")
        else:
            print("Incorrect email or password")

        self.menu()


Flipkart()
