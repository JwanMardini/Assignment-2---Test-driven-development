import unittest
from Classes.dice_hand import DiceHand
from Classes.dice import Dice


class test_diceHand(unittest.TestCase):
    def test_init_default_object(self):
        die = Dice()
        res = DiceHand(die)
        exp = DiceHand

        self.assertIsInstance(res, exp)

    def test_roll(self):
        die = Dice()
        obj = DiceHand(die)

        res = obj.roll()
        self.assertGreaterEqual(res, 1)
        self.assertLessEqual(res, 6)


if __name__ == "__main__":
    unittest.main()
