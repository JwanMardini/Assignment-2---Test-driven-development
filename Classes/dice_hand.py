"""A class that represents die. """
import random
from Classes.dice import Dice


class DiceHand():
    """ Methods are created with different functions. An instance of die is created.. """

    def __init__(self, die) -> Dice:
        """Initiliazing the instance. An instance of DiceHand is created."""
        self.die = die

    def roll(self):
        """The dice is rolled and it generates a random number from 1 to 6."""
        return random.randint(1, self.die.get_faces())
