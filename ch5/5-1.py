# 5-1. Conditional Tests
cars = ["subaru", "audi", "bmw", "benz", "ford"]
my_car = "audi"

print("Is my car == 'subaru'? I predict False")
print(my_car == 'subaru')

print("Is my car == 'bmw'? I predict False")
print(my_car == 'bmw')

print("Is my car == 'audi'? I predict True")
print(my_car == 'audi')

print("Is my car in cars? I predict True")
print(my_car in cars)

cars.remove("audi")

print("Is my car in cars? I predict False")
print(my_car in cars)

print("Is my car not in cars? I predict True")
print(my_car not in cars)

my_car = "benz"

print("Is my car == 'subaru'? I predict False")
print(my_car == 'subaru')

print("Is my car == 'bmw'? I predict False")
print(my_car == 'bmw')

print("Is my car == 'audi'? I predict True")
print(my_car != 'audi')


print("Is my car == 'benz'? I predict True")
print(my_car == 'benz')

print("Is my car in cars? I predict True")
print(my_car in cars)