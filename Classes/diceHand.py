from dice import Dice
import random


class DiceHand():
    def __init__(self) -> None:
        pass

    def roll(self):
        return random.randint(1, Dice.get_faces())
    