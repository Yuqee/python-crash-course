# 7-4. Pizza Toppings
prompt = "Please enter the topping you want to add: "
topping = " "

while topping != "quit":
    print(prompt)
    topping = input()
    if(topping != "quit"):
        print(f"\n{topping.title()} is added!")