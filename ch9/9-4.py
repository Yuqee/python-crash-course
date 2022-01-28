# 9-4. Number Served

class Restaurant:
    """Define restaurant"""

    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        """Constructe a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"This restaurant named {self.restaurant_name}.")
        print(f"Its cuisine type is: {self.cuisine_type}.")
        print(f"It has served: {self.number_served} customers.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} has opened.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, incerment):
        self.number_served += incerment

my_restaurant = Restaurant("Zhuyuan", "Chinese")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant = Restaurant("Zhuyuan", "Chinese", 6)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.set_number_served(10)
my_restaurant.describe_restaurant()
my_restaurant.increment_number_served(2)
my_restaurant.describe_restaurant()