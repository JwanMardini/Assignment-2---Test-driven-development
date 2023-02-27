class Dice:

    def __init__(self) -> None:
        self.__faces = 6

    def get_faces(self):
        return self.__faces

    def set_faces(self, new_faces):
        self.__faces = new_faces
