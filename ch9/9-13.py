# 9-13. Dice
from random import randint

class Dice:
    def __init__(self):
        self.sides = 6

    def update_sides(self, sides):
        self.sides = sides

    def roll_die(self):
        value = randint(1, self.sides)
        print(f"This dice rolled {value}!")

dice10 = Dice()
dice10.update_sides(10)

for num in range(0,10):
    dice10.roll_die()

dice20 = Dice()
dice20.update_sides(20)

for num in range(0,10):
    dice20.roll_die()