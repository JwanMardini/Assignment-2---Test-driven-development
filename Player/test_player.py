"""Test the Player class."""

import unittest
from Player.player import Player


class TestPlayer(unittest.TestCase):
    """Test class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        player = Player("Name", 0)
        exp = Player
        self.assertIsInstance(player, exp)

    def test_get_name(self):
        """Test get_name method."""
        exp = "Name"
        player = Player(exp, 0)

        res = player.get_name()
        self.assertEqual(res, exp)

    def test_get_score(self):
        """Test get_score method."""
        exp = 10
        player = Player("Name", exp)

        res = player.get_score()
        self.assertEqual(res, exp)

    def test_set_name(self):
        """Test set_name method."""
        player = Player("Name", 0)

        exp = "Test"
        player.set_name(exp)
        res = player.get_name()
        self.assertEqual(res, exp)

    def test_set_score(self):
        """Test set_score method."""
        player = Player("Name", 0)

        exp = 10
        player.set_score(exp)
        res = player.get_score()
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
