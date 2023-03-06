from player import Player


class Intelligence(Player):
    def __init__(self, mode, score) -> None:
        super().__init__("CPU", score)
        self._mode = mode

    def get_mode(self):
        return self._mode

    def set_score(self, new_score):
        self._score = new_score

    def get_score(self):
        return self._score
