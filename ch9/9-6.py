# 9-6. Ice Cream Stand
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

class IceCreamStand(Restaurant):
    """IceCreamStand is a special kind of restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ('Milk', 'Chocolate', 'Coconut', 'Blueberry')

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)

mystand = IceCreamStand("LALA", "Desert")
mystand.display_flavors()
print(mystand.number_served)
mystand.describe_restaurant()