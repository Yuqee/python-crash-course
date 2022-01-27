# 10-6. Addition
try:
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    res = int(num1)+int(num2)
except ValueError:
    print("The type is wrong.")
else:
    print(f"{num1} + {num2} = {res}\n")