# 4-11. My Pizzas, Your Pizzas
pizzas = ['pepperroni', 'mozzarella', 'becon']
friend_pizzas = pizzas[:]
pizzas.append('vegan')
friend_pizzas.append('maple')
print("My favoriate pizzas are:")
for pizza in pizzas:
  print(pizza)

print("My friend's favoriate pizzas are:")
for friend_pizza in friend_pizzas:
  print(friend_pizza)