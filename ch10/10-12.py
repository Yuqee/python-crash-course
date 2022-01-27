# 10-12. Favorite Number Remembered
import json

def writer(filename, contents):
    with open(filename, 'w') as f:
        json.dump(contents, f)

def reader(filename):
    try:
        with open(filename) as f:
            contents = json.load(f)
            return contents
    except FileNotFoundError:
        return None

if not reader('favorite_number.json'):
    favorite_number = input("What is your favorite number? ")
    writer('favorite_number.json', favorite_number)
    print(reader('favorite_number.json'))
else:
    print(reader('favorite_number.json'))