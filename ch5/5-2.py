# 5-2. More Conditional Tests
names = ['mike', 'tom', 'marry']
my_name = 'billion'

print("Is my name == 'mike'? I preidct False.")
print(my_name == 'mike')

names.insert(2, 'Billion')

print("Is my name in names? I preidct False.")
print(my_name in names)

for i in range(0,len(names)):
    names[i] = names[i].lower()

print("Is my name in names? I preidct True.")
print(my_name in names)

num1 = 400
num2 = 200

print("Is num1 and num2 greater than 200? I preidct False.")
print((num1 > 200) and (num2 > 200))

print("Is num1 or num2 greater than 200? I preidct True.")
print((num1 > 200) or (num2 > 200))
