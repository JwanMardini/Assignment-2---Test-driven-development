from diceHandtest import DiceHand
from dice import Dice
import random
import statistics
random.seed(1)
class Histogram:
    def __init__(self, list_of_score) -> None:
        self._list = list_of_score

    def showStatistic(self):
     dice_rolled  = [0] * (self._list[0].get_faces() + 1)
     for score in self._list:
        dice_rolled[score] += 1
     for i in range(1, len(dice_rolled)):
        print(f'{i}: {"*" * dice_rolled[i]}')
        
        

dice = Dice(6)
dice_hand = DiceHand(dice)
scores = dice_hand.roll(100)
histogram = Histogram(scores)
histogram.showStatistic()

        
        
        
        ##""" dice_rolled = {}
        ##die_roll = DiceHand().roll()
        ##dice_rolled[die_roll] = 1
        
        ##dice_rolled = {num:0 for num in range(1, 7)} """