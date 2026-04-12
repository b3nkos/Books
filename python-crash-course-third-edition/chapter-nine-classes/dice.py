from random import randint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


dice = Dice()

for _ in range(5):
    dice.roll_die()