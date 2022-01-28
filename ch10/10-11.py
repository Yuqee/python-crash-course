# 10-11. Favorite Number

# Writer
import json

favorite_number = input("What is your favorite number? ")
with open('favorite_number.json', 'w') as f:
    json.dump(favorite_number, f)

# Reader
# import json

with open('favorite_number.json') as f:
    favorite_number = json.load(f)
    print(f"I know your favorite num! It's {favorite_number}")