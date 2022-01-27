# 8-6. City Names:
def city_country(name, country):
    formatted = f"{name.title()}, {country.title()}"
    return formatted

print(city_country("Santiago", "Chile"))
print(city_country("Chengdum", "China"))
print(city_country("paris", "france"))