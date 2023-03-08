"""The class represents the player and its attributes."""


class Player:
    """The methods and attribute of the player."""
    def __init__(self, name, score):
        """Init of the name and score of the player."""
        self._name = name
        self._score = score

    def set_name(self, name):
        """The name of the player is set."""
        self._name = name

    def get_name(self):
        """The name of the player is returned."""
        return self._name

    def set_score(self, new_score):
        """The score of the player is set."""
        self._score = new_score

    def get_score(self):
        """The score of the player is returned."""
        return self._score
