class HighScore:

    def __init__(self) -> None:
        self._high_score = 100

    def set_high_score(self, new_high_score):
        self._high_score = new_high_score

    def get_high_score(self):
        return self._high_score
