# 8-5. Cities
def describe_city(name, country="China"):
    print(f"{name.title()} is in {country.title()}.")

describe_city("paris", "france")
describe_city("Chengdu")
describe_city(name="new york", country="america")