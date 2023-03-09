"""Test the Histogram class."""

import unittest
from classes.histogram.histogram import Histogram
from classes.dice.dice import Dice


class TestHistogram(unittest.TestCase):
    """Test class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        die = Dice()

        res = Histogram(die)
        exp = Histogram
        self.assertIsInstance(res, exp)

    def test_get_list(self):
        """Test get_list method."""
        die = Dice()
        his = Histogram(die)

        res = his.get_list()
        exp = list
        self.assertIsInstance(res, exp)

    def test_saved_data(self):
        """Test saved_data method."""
        die = Dice()
        his = Histogram(die)
        roll = 1
        his.saved_data(roll)

        self.assertIn(roll, his.get_list())


if __name__ == '__main__':
    unittest.main()
