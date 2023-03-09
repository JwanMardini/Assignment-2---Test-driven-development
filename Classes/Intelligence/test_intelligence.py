"""Test the Intelligence class."""

import unittest
from classes.intelligence.intelligence import Intelligence


class TestIntelligence(unittest.TestCase):
    """Test class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Intelligence("e", 0)
        exp = Intelligence
        self.assertIsInstance(res, exp)

    def test_get_mode(self):
        """Test get_mode method."""
        cpu = Intelligence("e", 2)

        res = cpu.get_mode()
        exp = "e"
        self.assertEqual(res, exp)

    def test_get_score(self):
        """Test get_score method."""
        cpu = Intelligence("e", 2)

        res = cpu.get_score()
        exp = 2
        self.assertEqual(res, exp)

    def test_set_score(self):
        """Test set_score method."""
        cpu = Intelligence("e", 2)
        cpu.set_score(4)

        res = cpu.get_score()
        exp = 4
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
