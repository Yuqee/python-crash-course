# 6-10. Favorite Numbers
fav_numbers = {
    'ann': [3, 4],
    'yuqi': [6, 1, 7],
    'rita': [6],
    'mike': [0, 8],
    'joe': [6, 8],
    }

for name in fav_numbers:
    print(f"\nWhat are your favoriate numbers, {name.title()}?")
    for num in fav_numbers[name]:
        print(f"\t{num}")