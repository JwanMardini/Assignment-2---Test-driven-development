class Player:
<<<<<<< HEAD
    def __init__(self, name, score, currentScore) -> None:
=======

    def __init__(self, name, score, currentScore):
>>>>>>> 69588e0519bd8c3d032c6acaf1c77cd17899aa19
        self._name = name
        self._score = score
        self._currentScore = currentScore

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name
<<<<<<< HEAD
    
=======

>>>>>>> 69588e0519bd8c3d032c6acaf1c77cd17899aa19
    def set_score(self, new_score):
        self._score = new_score

    def get_score(self):
        return self._score
<<<<<<< HEAD
    
    def set_currentScore (self, score):
        self._currentScore = score
    
    def get_cureentScore(self):
        return self._currentScore
    
=======

    def set_tempScore(self, score):
        self._currentScore = score

    def get_tempScore(self):
        return self._currentScore
>>>>>>> 69588e0519bd8c3d032c6acaf1c77cd17899aa19
