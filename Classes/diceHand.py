from dice import Dice
import random


class DiceHand:
    def __init__(self) -> None:
        self._die = Dice()

    def roll(self):
        return random.randint(1, self._die.get_faces())
