class Player:
    def __init__(self, name, score):
        self._name = name
        self._score = score
        # self._currentScore = currentScore

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_score(self, new_score):
        self._score = new_score

    def get_score(self):
        return self._score

    # def set_currentScore(self, score):
        # self._currentScore = score

    # def get_cureentScore(self):
        # return self._currentScore
