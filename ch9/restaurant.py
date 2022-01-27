class Restaurant:
    """Define restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Constructe a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This restaurant named {self.restaurant_name}.")
        print(f"Its cuisine type is: {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} has opened.")

    def set_number_served(self, number):
        if number < self.number_served:
            print("Error!")
        else:
            self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number