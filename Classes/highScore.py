class HighScore:

    def __init__(self) -> None:
        self._highScore = 10

    def set_highScore(self, new_highScore):
        self._highScore = new_highScore

    def get_highScore(self):
        return self._highScore
