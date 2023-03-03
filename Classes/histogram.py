from diceHand import DiceHand
import random
import statistics
random.seed(1)
class Histogram:
    def __init__(self, list_of_score) -> None:
        self._list = list_of_score

    def showStatisic():
        dice_rolled = {}
        die_roll = DiceHand().roll()
        dice_rolled[die_roll] = 1
        
        dice_rolled = {num:0 for num in range(1, 7)}
     
    for i in range(100):
         roll = random.randint(1, 6)
         dice_rolled[roll] += 1
         
def histogram_plot():
    