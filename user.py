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

class Previleges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges =  Previleges(privileges)