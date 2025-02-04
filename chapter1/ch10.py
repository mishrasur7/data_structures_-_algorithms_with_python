class User:
    def __init__(self, first_name, last_name, username, email, location) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self) -> str:
        print(f'Name: {self.first_name} {self.last_name} \nUsername: {self.username} \nEmail: {self.email} \nLocation: {self.location}')

    def greet_user(self) -> str:
        print(f'Welcome back {self.username}!')

'''
testing with these cases

Matti= User('Matti', 'Paajanen', 'mpaajanen', 'm.paajanen@gmail.com', 'Helsinki')
Matti.describe_user()

Maila= User('Maila', 'Halonen', 'm_halonen', 'm.halonen@mtv.fi', 'Vaasa')
Maila.greet_user()

'''