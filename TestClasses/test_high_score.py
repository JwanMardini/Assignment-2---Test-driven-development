import unittest
from Classes.high_score import HighScore


class TestHighScore(unittest.TestCase):
    def test_init_default_object(self):
        res = HighScore()
        exp = HighScore
        self.assertIsInstance(res, exp)

    def test_get_high_score(self):
        obj = HighScore()

        res = obj.get_high_score()
        exp = 100
        self.assertEqual(res, exp)

    def test_set_high_score(self):
        obj = HighScore()
        obj.set_high_score(200)

        res = obj.get_high_score()
        exp = 200
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
