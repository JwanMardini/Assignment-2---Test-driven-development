from dice import Dice
import random


class DiceHand():
    def __init__(self, die) -> None:
        self.die = die

    def roll(self):
        return random.randint(1, self.die.get_faces())
    