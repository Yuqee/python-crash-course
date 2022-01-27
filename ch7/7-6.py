# 7-6. Three Exits
# version 1
prompt = "Please enter the topping you want to add: "
topping = " "

while topping != "quit":
    print(prompt)
    topping = input()
    if(topping != "quit"):
        print(f"\n{topping.title()} is added!")


# version 2
# prompt = "Please enter the topping you want to add: "
# topping = " "
# active = True

# while active:
#     print(prompt)
#     topping = input()
#     if(topping != "quit"):
#         print(f"\n{topping.title()} is added!")
#     else:
#         active = False

# version 3
# prompt = "Please enter the topping you want to add: "
# topping = " "

# while True:
#     print(prompt)
#     topping = input()
#     if(topping != "quit"):
#         print(f"\n{topping.title()} is added!")
#     else:
#         break

# message = "Please enter your age: "
# age = " "

# version 1
# message = "Please enter your age: "
# age = " "
# while age != "quit":
#     age = input(message)
#     if age != "quit":
#         age = int(age)
#         if(age < 3):
#             print("\nThis movie ticket is free.")
#         elif(3 <= age <= 12):
#             print("\nThis movie ticket costs $10.")
#         else:
#             print("\nThis movie ticket costs $15.")

# version 2 
# message = "Please enter your age: "
# age = " "
# active = True

# while active:
#     age = input(message)
#     if age != "quit":
#         age = int(age)
#         if(age < 3):
#             print("\nThis movie ticket is free.")
#         elif(3 <= age <= 12):
#             print("\nThis movie ticket costs $10.")
#         else:
#             print("\nThis movie ticket costs $15.")
#     else:
#         active = False

# version 3 
# message = "Please enter your age: "
# age = " "

# while True:
#     age = input(message)
#     if age != "quit":
#         age = int(age)
#         if(age < 3):
#             print("\nThis movie ticket is free.")
#         elif(3 <= age <= 12):
#             print("\nThis movie ticket costs $10.")
#         else:
#             print("\nThis movie ticket costs $15.")
#     else:
#         break