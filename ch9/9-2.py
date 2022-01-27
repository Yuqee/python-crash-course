# 9-2. Three Restaurants
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

dinner1 = Restaurant("Shengruxiahua", "Thai")
dinner2 = Restaurant("Finsh and Chips", "British")
dinner3 = Restaurant("Les de Caris", "French")

dinner1.describe_restaurant()
dinner2.describe_restaurant()
dinner3.describe_restaurant()