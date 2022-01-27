# 6-11. Cities
cities = {
    'chengdu': {'country': 'china', 'population': 80000000, 'fact': 'haven',},
    'new york': {'country': 'america', 'population': 10000000, 'fact': 'big apple',},
    'paris': {'country': 'france', 'population': 20000000, 'fact': 'romance',},
    }

for city, info in cities.items():
    print(f"\n{city.title()}:")
    for category, value in info.items():
        print(f"\t {category}: {value}")