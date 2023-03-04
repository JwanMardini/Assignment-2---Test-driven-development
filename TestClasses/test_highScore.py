import unittest
from Classes.highScore import HighScore


class test_HighScore(unittest.TestCase):
    def test_init_default_object(self):
        res = HighScore()
        exp = HighScore
        self.assertIsInstance(res, exp)

    def test_get_highScore(self):
        obj = HighScore()

        res = obj.get_highScore()
        exp = 100
        self.assertEqual(res, exp)

    def test_set_highScore(self):
        obj = HighScore()
        obj.set_highScore(200)

        res = obj.get_highScore()
        exp = 200
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
