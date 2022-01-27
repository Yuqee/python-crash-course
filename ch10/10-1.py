# 10-1. Learning Python
filename = 'Learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)

outcomes = ''
for line in lines:
    outcomes += line.strip()
    print(line.strip())

print(outcomes)