# 9-15. Lottery Analysis

from random import choice

poll = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'g', 'n', 'w']
my_ticket = [2, 'a', 6, 3]
win_ticket = []

for num in range(0,4):
    win_ticket.append(choice(poll))

count = 0
while my_ticket != win_ticket:
    win_ticket.clear()
    count += 1
    for num in range(0,4):
        win_ticket.append(choice(poll))
    print(f"You have been lost for {count} times!")
    print(f"Your ticket is: {my_ticket}")
    print(f"The winning ticket is: {win_ticket}")

print("You win the lottery!")