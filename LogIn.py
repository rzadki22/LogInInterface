from collections import defaultdict


class User:
    def __init__(self, user_first_name, user_last_name, user_login, user_password):
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.user_login = user_login
        self.user_password = user_password

    def __repr__(self):
        return f"""
        user_first_name = {self.user_first_name}
        self.user_last_name = {self.user_last_name}
        self.user_login = {self.user_login}
        self.user_password = {self.user_password}
    """


class Store:
    user_logins = []
    user_passwords = {}
    user_keeper = {}

    def __init__(self):
        self.current_login = None
        self.basket = {}

    def register(self, user):
        if user.user_login in self.user_logins:
            raise Exception("Login is unavailable, try another")
        self.user_logins.append(user.user_login)
        self.user_passwords[user.user_login] = user.user_password
        self.user_keeper[user.user_login] = user

    def login(self, in_login, in_pass):
        # in_login = input("Type your login: ")
        if not in_login in self.user_logins:
            raise Exception("No such account!")
        # in_pass = input("Type your login: ")
        if in_pass != self.user_passwords[in_login]:
            raise Exception("Wrong password. Try log in again.")
        self.current_login = in_login

    @property
    def logout(self):
        return self.logout_function()

    def logout_function(self):
        self.current_login = None
        self.basket = {}

    def is_logged_in(func):
        def wrapper(*args):
            if not args[0].current_login:
                raise Exception("You must be logged in!")
            else:
                return func(*args)

        return wrapper

    @is_logged_in
    def buy(self, purchase, amount):
        self.basket[purchase] = amount

    def __repr__(self):
        return f"""
        current_login = {self.current_login}
        basket = {self.basket}

    """
