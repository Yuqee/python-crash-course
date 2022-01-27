# 10-4. Guest Book
filename = 'guest_book.txt'
greeting = "Hello, please enter your name or type 'q' to quit."

name = input(greeting)

with open(filename, 'w') as file_object:
    while name != 'q':
        file_object.write(f"{greeting} {name}.\n")
        name = input(greeting)