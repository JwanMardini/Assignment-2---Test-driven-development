import unittest
from unittest.mock import patch
from Classes.game import Game


class test_game(unittest.TestCase):
    def test_init_default_object(self):
        res = Game()
        exp = Game
        self.assertIsInstance(res, exp)

    def test_header(self):
        game = Game()

        res = game.header()
        exp = "***************************\n" + "--- Welcome to pig dice ---\n" + "***************************\n"
        self.assertEqual(res, exp)
    
    @patch('builtins.print')
    def test_end_game(self, output):
        game = Game()
        name = "Name"
        highScore = 150

        game.end_game(name, highScore)
        exp = f"The winner is {name}, and your score is {highScore}"
        output.assert_called_with(exp)

    def test_get_turn(self):
        game = Game()

        res = game.get_turn()
        exp = 1
        self.assertEqual(res, exp)

    def test_set_turn(self):
        game = Game()
        game.set_turn(2)

        res = game.get_turn()
        exp = 2
        self.assertEqual(res, exp)

    def test_get_startMenu(self):
        game = Game()

        res = game.get_startMenu()
        exp = "Enter 1 for one player game\nEnter 2 for two players game"
        self.assertEqual(res, exp)

    def test_get_optionMenu(self):
        game = Game()

        res = game.get_optionMenu()
        exp = '''Press 1 to change name
Press 2 to quit game\nPress 3 to roll\n Press 4 to cheat\n'''
        self.assertEqual(res, exp)

    def test_get_defficultyMenu(self):
        game = Game()

        res = game.get_defficultyMenu()
        exp = '''Enter (e) for easy mode and (h) for hard mode: '''
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
