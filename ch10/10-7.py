# 10-7. Addition Calculator
num = 0
res = 0
while num != 'q':
    try:
        num = input("Enter a number or 'q' to quit.")
        res += int(num)
    except ValueError:
        print("The type is wrong.")
    
print(f"The result is {res}")