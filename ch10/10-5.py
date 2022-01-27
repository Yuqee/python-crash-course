# 10-5. Programming Poll
filename = 'respones.txt'
respons = input("Why do you like programming?")

with open(filename, 'w') as file_object:
    while respons != 'q':
        file_object.write(f"{respons}\n")
        respons = input("Why do you like programming?")