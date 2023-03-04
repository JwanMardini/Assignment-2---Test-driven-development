import unittest
from Classes.player import Player


class test_Player(unittest.TestCase):
    def test_init_default_object(self):
        player = Player("Name", 0)
        exp = Player
        self.assertIsInstance(player, exp)

    def test_get_Name(self):
        exp = "Name"
        player = Player(exp, 0)

        res = player.get_name()
        self.assertEqual(res, exp)

    def test_get_score(self):
        exp = 10
        player = Player("Name", exp)

        res = player.get_score()
        self.assertEqual(res, exp)

    def test_set_name(self):
        player = Player("Name", 0)

        exp = "Test"
        player.set_name(exp)
        res = player.get_name()
        self.assertEqual(res, exp)

    def test_set_score(self):
        player = Player("Name", 0)

        exp = 10
        player.set_score(exp)
        res = player.get_score()
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
