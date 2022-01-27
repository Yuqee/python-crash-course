# 7-11. Dream Vacation
polling = {}
prompt = "If you could visit one place in the world, where would you go?"

while True:
    name = input("Please enter your name: ")
    place = input(prompt)
    active = input("Would you like another person to take this poll? (y/n)")
    polling[name] = place
    if(active == "n"):
        break

for name, place in polling.items():
    print(f"{name.title()} would like to visit {place.title()}.")