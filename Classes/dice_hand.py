"""A class that represents dice.  """
import random
from Classes.dice import Dice


class DiceHand():
    """ Methods are created with different functions. An instance of dice from Dice class is the attribute. """

    def __init__(self, die) -> Dice:
        """Initiliazing the object. An instance of Dice is created."""
        self.die = die

    def roll(self):
        """The dice is rolled and it generates a random number from 1 to 6."""
        return random.randint(1, self.die.get_faces())
