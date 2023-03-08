"""Test the HighScore class."""

import unittest
from high_score import HighScore


class TestHighScore(unittest.TestCase):
    """Test class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = HighScore()
        exp = HighScore
        self.assertIsInstance(res, exp)

    def test_get_high_score(self):
        """Test get_high_score method."""
        obj = HighScore()

        res = obj.get_high_score()
        exp = 100
        self.assertEqual(res, exp)

    def test_set_high_score(self):
        """Test set_high_score method."""
        obj = HighScore()
        obj.set_high_score(200)

        res = obj.get_high_score()
        exp = 200
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
