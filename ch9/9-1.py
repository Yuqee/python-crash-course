# 9-1. Restaurant

class Restaurant:
    """Define restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Constructe a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This restaurant named {self.restaurant_name}.")
        print(f"Its cuisine type is: {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} has opened.")

my_restaurant = Restaurant("Zhuyuan", "Chinese")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()