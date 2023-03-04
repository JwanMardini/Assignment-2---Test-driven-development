from Classes.dice import Dice
import random


class DiceHand():
    def __init__(self, die) -> Dice:
        self.die = die

    def roll(self):
        return random.randint(1, self.die.get_faces())
