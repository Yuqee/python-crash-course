# 10-3. Guest
filename = 'guest.txt'

num = int(input("How many guest?"))
with open(filename, 'w') as file_object:
    for k in range(0, num):
        name = input("Please enter your name: ")
        file_object.write(f"{name}\n")