"""The class shows the attribute of the die itself."""


class Dice:
    """Method for the die are created."""

    def __init__(self) -> None:
        """Initializing the object."""
        self.__faces = 6

    def get_faces(self):
        """Return the number of faces on the die."""
        return self.__faces

    def set_faces(self, new_faces):
        """Set the number of faces on the die a given value."""
        self.__faces = new_faces
