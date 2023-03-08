class Game:
    def __init__(self):
        self._header = "***************************\n" + "--- Welcome to pig dice ---\n" + "***************************"
        self._turn = 1
        self._start_menu = "Enter 1 for one player game\nEnter 2 for two players game"
        self._option_menu = '''Press 1 to change name
Press 2 to quit game\nPress 3 to roll\n Press 4 to cheat\n'''
        self._difficulty_menu = '''Enter (e) for easy mode and (h) for hard mode: '''

    def header(self):
        return self._header

    def end_game(self, name, high_score):
        print(f"The winner is {name}, and your score is {high_score}")

    def set_turn(self, new_turn):
        self._turn = new_turn

    def get_turn(self):
        return self._turn

    def get_startmenu(self):
        return self._start_menu

    def get_optionmenu(self):
        return self._option_menu

    def get_difficultymenu(self):
        return self._difficulty_menu

    def get_rules(self):
        return """1. Players take turns with a die.
2. On a player’s turn he/she can roll a die as many times as they like.
3. If a roll is a 2, 3, 4, 5, or 6, the player adds that many points to their score for the turn.
4. A player may choose to end their turn at any time and “bank” their points.
5. If a player rolls a 1, they lose all their unbanked points and their turn is over."""
