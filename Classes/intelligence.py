class Intelligence:
    def __init__(self, mode, score, currentScore) -> None:
        self._mode = mode
        self._score = score
        self._currentScore = currentScore
        

        

    def easy(self):
        pass


    def set_score(self, new_score):
        self._score = new_score


    def get_score(self):
        return self._score
    
    def set_tempScore (self, score):
        self._currentScore = score
    
    def get_tempScore(self):
        return self._currentScore


    