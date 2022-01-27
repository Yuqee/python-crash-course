# 9-5. Login Attempts
class User:
    """A class for user."""
    def __init__(self, first_name, last_name):
        """Construct a user"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def increment_login_attempts(self):
        """Increment login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0"""
        self.login_attempts = 0

user1 = User("James", "Bond")
print(f"{user1.first_name} {user1.last_name} has attempted to login for\
 {user1.login_attempts} times.")

user1.increment_login_attempts()
print(f"{user1.first_name} {user1.last_name} has attempted to login for\
 {user1.login_attempts} times.")

user1.increment_login_attempts()
print(f"{user1.first_name} {user1.last_name} has attempted to login for\
 {user1.login_attempts} times.")

user1.increment_login_attempts()
print(f"{user1.first_name} {user1.last_name} has attempted to login for\
 {user1.login_attempts} times.")

user1.increment_login_attempts()
print(f"{user1.first_name} {user1.last_name} has attempted to login for\
 {user1.login_attempts} times.")

user1.reset_login_attempts()
print(f"{user1.first_name} {user1.last_name} has attempted to login for\
 {user1.login_attempts} times.")