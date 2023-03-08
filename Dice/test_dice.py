"""Test the dice class."""

import unittest
from Dice.dice import Dice


class TestDice(unittest.TestCase):
    """Test class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Dice()
        exp = Dice
        self.assertIsInstance(res, exp)

    def test_get_faces(self):
        """Test the get_faces method."""
        die = Dice()

        res = die.get_faces()
        exp = 6
        self.assertEqual(res, exp)

    def test_set_faces(self):
        """Test the set_faces method."""
        die = Dice()
        die.set_faces(8)

        res = die.get_faces()
        exp = 8
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
