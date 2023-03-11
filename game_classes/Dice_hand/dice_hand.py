"""A class that represents die."""
import random
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class DiceHand():
    """Methods are created with different functions. An instance of die is created."""

    def __init__(self, die):
        """Initiliazing the instance. An instance of DiceHand is created."""
        self.die = die

    def roll(self):
        """Roll the dice and return a random integer between 1 and the number of faces on the die."""
        return random.randint(1, self.die.get_faces())
