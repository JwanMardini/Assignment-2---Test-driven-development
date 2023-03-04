from Classes.player import Player


class Intelligence(Player):
    def __init__(self, mode, score) -> None:
        super().__init__("CPU", score) # du måste extend/implement när du gör så...
        self._mode = mode

    def get_mode(self):
        return self._mode

    def set_score(self, new_score):
        self._score = new_score

    def get_score(self):
        return self._score

    # def set_tempScore(self, score):
        # self._currentScore = score

    # def get_tempScore(self):
        # return self._currentScore
