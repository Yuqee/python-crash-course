# # 11-1. City, Country
# def formatted_city_name(city, country):
#     return f"{city}, {country}".title()

# 11-2. Population
def formatted_city_name(city, country, population=''):
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city}, {country}".title()