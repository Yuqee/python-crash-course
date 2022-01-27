# 8-17. Styling Functions
def describe_city(name, country="China"):
    print(f"{name.title()} is in {country.title()}.")

describe_city("paris", "france")
describe_city("Chengdu")
describe_city(name="new york", country="america")

def make_shirt(size, text):
    print(f"This t-shirt is of size {size} and it prints '{text}' on it.")

make_shirt(size ="XL", text ="Hopeful")
make_shirt("S","Batman is bad.")

def make_shirt(text ="I love Python", size ="L"):
    print(f"This t-shirt is of size {size} and it prints '{text}' on it.")

make_shirt(size ="M")
make_shirt(text ="I love Java")