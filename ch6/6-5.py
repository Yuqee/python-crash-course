# 6-5. Rivers
rivers = {
    'nile': 'egypt',
    'yangzi': 'china',
    'amazon': 'barzil'
}

for name, country in rivers.items():
    print(f"The {name.title()} runs through {country.title()}.")

print("\nThe rivers been mentioned are:")
for name in rivers.keys():
    print(f"{name}")

print("\nThe countries been mentioned are:")
for country in rivers.values():
    print(f"{country}")