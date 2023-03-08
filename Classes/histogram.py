"""The histogram plots the rolled die face and how many times that number reaccurs. """


class Histogram:
    """Methods for storing the number of rolls."""

    def __init__(self, die) -> None:
        """Init the die instance of Histogram Class."""
        self._die = die
        self._list = []

    def saved_data(self, roll):
        """The function appends the number of rolls to a list."""
        self._list.append(roll)

    def get_list(self):
        """The list is returned."""
        return self._list
