from dice import Dice
import random


class DiceHand():
    def __init__(self, die) -> Dice:
        self.die = die

    def roll(self, times):
        return [random.randint(1, self.die.faces()) for _ in range(times)]
