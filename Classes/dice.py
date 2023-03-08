"""The class shows the attribute of the die itself"""


class Dice:
    """Method for the die are created."""

    def __init__(self) -> None:
        """initializing the attribute of the die."""
        self.__faces = 6

    def get_faces(self):
        """The die's number is returned."""
        return self.__faces

    def set_faces(self, new_faces):
        """The die's number is set to a given value."""
        self.__faces = new_faces
