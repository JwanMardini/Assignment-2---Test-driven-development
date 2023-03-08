"""The intelligence class represents the CPU as a player. The class is inherited from Player class."""
from Classes.player import Player


class Intelligence(Player):
    """Methods for the CPU to function."""
    def __init__(self, mode, score) -> None:
        """Init a mode instance of Intelligence Class."""
        super().__init__("CPU", score)
        self._mode = mode

    def get_mode(self):
        """The mode instance is returned."""
        return self._mode

    def set_score(self, new_score):
        """The score for the CPU player is set."""
        self._score = new_score

    def get_score(self):
        """The score for the CPU player is returned."""
        return self._score
