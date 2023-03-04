import unittest
from Classes.dice import Dice


class test_dice(unittest.TestCase):

    def test_init_default_object(self):
        res = Dice()
        exp = Dice
        self.assertIsInstance(res, exp)

    def test_get_faces(self):
        die = Dice()

        res = die.get_faces()
        exp = 6
        self.assertEqual(res, exp)

    def test_set_faces(self):
        die = Dice()
        die.set_faces(8)

        res = die.get_faces()
        exp = 8
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
