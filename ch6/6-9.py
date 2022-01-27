# 6-9. Favorite Places
favorite_places = {
    'peter': ['paris', 'london', 'chengdu'],
    'wendy': ['dali'],
    'kayla': ['soul', 'chengdu']
    }

for name in favorite_places.keys():
    print(f"\nName your favorite places, {name.title()}.")
    print("My favorite places are:")
    for place in favorite_places[name]:
        print(f"\t{place.title()}")