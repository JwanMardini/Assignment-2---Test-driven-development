import unittest
from Classes.histogram import Histogram
from Classes.dice import Dice


class test_histogram(unittest.TestCase):
    def test_init_default_object(self):
        die = Dice()

        res = Histogram(die)
        exp = Histogram
        self.assertIsInstance(res, exp)

    def test_get_list(self):
        die = Dice()
        his = Histogram(die)

        res = his.get_list()
        exp = list
        self.assertIsInstance(res, exp)

    def test_savedData(self):
        die = Dice()
        his = Histogram(die)
        roll = 1
        his.savedData(roll)

        self.assertIn(roll, his.get_list())


if __name__ == '__main__':
    unittest.main()
