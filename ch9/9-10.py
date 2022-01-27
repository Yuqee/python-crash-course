# 9-10. Imported Restaurant

from restaurant import Restaurant

restaurant = Restaurant("Zhuyuan", "Chinese")
print(f"This restaurant has served {restaurant.number_served} people.")

restaurant.number_served = 3
print(f"This restaurant has served {restaurant.number_served} people.")

restaurant.set_number_served(5)
print(f"This restaurant has served {restaurant.number_served} people.")

restaurant.increment_number_served(2)
print(f"This restaurant has served {restaurant.number_served} people.")
restaurant.describe_restaurant()