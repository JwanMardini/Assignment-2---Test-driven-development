from Classes.dice import Dice
import random

class DiceHand():
    def __init__(self, die) -> Dice:
        self.numberOfRolls = 0
        self.die = die

    def roll(self, times):
        self.numberOfRolls += times
        return [random.randint(1, self.die.getfaces()) for _ in range(times)]
        #return random.randint(1, self.die.get_faces())

    def get_numberOfRolls(self):
        return self.numberOfRolls
#class DiceHand():
    #def __init__(self, die) -> Dice:
       # self.die = die

    #def roll(self, times: int):
       # return [random.randint(1, self.die.faces()) for _ in range(times)]
