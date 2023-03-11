"""Test the DiceHand class."""

import unittest
from game_classes.Dice_hand.dice_hand import DiceHand
from game_classes.Dice.dice import Dice


class TestDiceHand(unittest.TestCase):
    """Test class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        die = Dice()
        res = DiceHand(die)
        exp = DiceHand

        self.assertIsInstance(res, exp)

    def test_roll(self):
        """Test the roll method."""
        die = Dice()
        obj = DiceHand(die)

        res = obj.roll()
        self.assertGreaterEqual(res, 1)
        self.assertLessEqual(res, 6)


if __name__ == "__main__":
    unittest.main()
