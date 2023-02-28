class Game:
    def __init__(self):
        self._header = "***************************\n" + "--- Welcome to pig dice ---\n" + "***************************\n"
        

    def header(self):
        return self._header
    
    def end_game(self, name, highScore):
        print(f"The winner is {name}, and your score is {highScore}")
