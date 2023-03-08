"""The class has the responsibility of obtaining and returning the high score for given player."""


class HighScore:
    """The class has methods dealing with high score."""

    def __init__(self) -> None:
        """"Initializing an instance of High score class."""
        self._high_score = 100

    def set_high_score(self, new_high_score):
        """The function sets the high score of a player."""
        self._high_score = new_high_score

    def get_high_score(self):
        """The getter obtains the high score."""
        return self._high_score
