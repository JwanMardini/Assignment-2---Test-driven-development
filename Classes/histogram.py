class Histogram:
    def __init__(self, die) -> None: 
        self._die = die
        self._list = []

    def saved_data(self, roll):
        self._list.append(roll)

    def get_list(self):
        return self._list
