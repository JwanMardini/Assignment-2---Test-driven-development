"""The class has the responsibility of obtaining and returning the high score for given player."""
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class HighScore:
    """The class has methods dealing with high score."""

    def __init__(self) -> None:
        """Init object."""
        self._high_score = 100

    def set_high_score(self, new_high_score):
        """Set the high score of a player."""
        self._high_score = new_high_score

    def get_high_score(self):
        """Get the high score of player."""
        return self._high_score
