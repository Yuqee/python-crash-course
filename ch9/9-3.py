# 9-3. Users
class User:
    """A class for user."""
    def __init__(self, first_name, last_name):
        """Construct a user"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Print a user's info"""
        print(f"First name: {self.first_name}.")
        print(f"Last name: {self.last_name}.")

    def greet_user(self):
        """Greet a user"""
        print(f"Hello, {self.first_name} {self.last_name}.")

user1 = User("Tom", "Ford")
user1.describe_user()
user1.greet_user()

user2 = User("James", "Bond")
user2.describe_user()
user2.greet_user()

user3 = User("Lana", "Delray")
user3.describe_user()
user3.greet_user()