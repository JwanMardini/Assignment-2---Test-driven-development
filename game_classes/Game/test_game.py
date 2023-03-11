"""Test the game class."""

import unittest
from unittest.mock import patch
from game_classes.Game.game import Game


class TestGame(unittest.TestCase):
    """Test class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Game()
        exp = Game
        self.assertIsInstance(res, exp)

    def test_header(self):
        """Test the header menu."""
        game = Game()

        res = game.header()
        exp = "***************************\n" + "--- Welcome to pig dice ---\n" + "***************************"
        self.assertEqual(res, exp)

    @patch('builtins.print')
    def test_end_game(self, output):
        """Test the end game output."""
        game = Game()
        name = "Name"
        high_score = 150

        game.end_game(name, high_score)
        exp = f"The winner is {name}, and your score is {high_score}"
        output.assert_called_with(exp)

    def test_get_turn(self):
        """Test weather the turn is one or two."""
        game = Game()

        res = game.get_turn()
        exp = 1
        self.assertEqual(res, exp)

    def test_set_turn(self):
        """Test set_turn method."""
        game = Game()
        game.set_turn(2)

        res = game.get_turn()
        exp = 2
        self.assertEqual(res, exp)

    def test_get_start_menu(self):
        """Test the start menu."""
        game = Game()

        res = game.get_startmenu()
        exp = "Enter 1 for one player game\nEnter 2 for two players game"
        self.assertEqual(res, exp)

    def test_get_option_menu(self):
        """Test the option menu."""
        game = Game()

        res = game.get_optionmenu()
        exp = '''Press 1 to change name
Press 2 to quit game\nPress 3 to roll\nPress 4 to cheat\n'''
        self.assertEqual(res, exp)

    def test_get_difficulty_menu(self):
        """Test difficulty menu."""
        game = Game()

        res = game.get_difficultymenu()
        exp = '''Enter (e) for easy mode and (h) for hard mode: '''
        self.assertEqual(res, exp)

    def test_get_rules(self):
        """Test get_rules method."""
        game = Game()

        res = game.get_rules()
        exp = """1. Players take turns with a die.
2. On a player’s turn he/she can roll a die as many times as they like.
3. If a roll is a 2, 3, 4, 5, or 6, the player adds that many points to their score for the turn.
4. A player may choose to end their turn at any time and “bank” their points.
5. If a player rolls a 1, they lose all their unbanked points and their turn is over."""
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
