"""The histogram plots the rolled die face and how many times that number reaccurs."""
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class Histogram:
    """Methods for storing the number of rolls."""

    def __init__(self, die) -> None:
        """Init the die instance of Histogram Class."""
        self._die = die
        self._list = []

    def saved_data(self, roll):
        """Append the roll data to a list."""
        self._list.append(roll)

    def get_list(self):
        """List is returned."""
        return self._list
