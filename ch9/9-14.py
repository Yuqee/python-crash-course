# 9-14. Lottery
from random import choice

poll = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'g', 'n', 'w']
lottery = []
for num in range(0,4):
    win = choice(poll)
    lottery.append(win)

win_ticket = ""
for win in lottery:
    win_ticket = f"{win_ticket}{win}"

print(f"People with ticket code: {win_ticket} has won this lottery.")