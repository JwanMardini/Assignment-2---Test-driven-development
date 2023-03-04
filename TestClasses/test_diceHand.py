import unittest
from Classes.diceHand import DiceHand


class test_diceHand(unittest.TestCase):
    def test_init_default_object(self):
        res = DiceHand()
        exp = DiceHand

        self.assertIsInstance(res, exp)

    def test_roll(self):
        obj = DiceHand()

        res = obj.roll()
        self.assertGreaterEqual(res, 1)
        self.assertLessEqual(res, 6)


if __name__ == "__main__":
    unittest.main()
