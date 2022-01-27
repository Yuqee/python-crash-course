# 7-5. Movie Tickets
message = "Please enter your age: "
age = " "

while age != "quit":
    age = input(message)
    if age != "quit":
        age = int(age)
        if(age < 3):
            print("\nThis movie ticket is free.")
        elif(3 <= age <= 12):
            print("\nThis movie ticket costs $10.")
        else:
            print("\nThis movie ticket costs $15.")