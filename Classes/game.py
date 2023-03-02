class Game:
    def __init__(self):
        self._header = "***************************\n" + "--- Welcome to pig dice ---\n" + "***************************\n"
        self._turn = 1
        self._startMenu = "Enter 1 for one player game\nEnter 2 for two players game"

    def header(self):
        return self._header

    def end_game(self, name, highScore):
        print(f"The winner is {name}, and your score is {highScore}")

    def set_turn(self, new_turn):
        self._turn = new_turn

    def get_turn(self):
        return self._turn

    def set_startMenu(self, menu):
        self._startMenu = menu

    def get_startMenu(self):
        return self._startMenu
