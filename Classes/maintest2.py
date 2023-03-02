from game import Game
from player import Player
from intelligence import Intelligence
from dice import Dice
from diceHand import DiceHand
from highScore import HighScore

def main():

die = Dice()
diceHand = DiceHand(die)
command = True
    while(command):
        game_header = Game()
        print(game_header.header())
        controller = True
        #command kan göras som en egen metod? Blir lättare med färre while loop i samma metod?
        while (controller):
            try:
                choice = int(input("Select 1 for one player, 2 for two players: "))
            except:
                print("Invalid input, try again")


def players_turn(player, diceHand, name):
 
    turn = 1
    while turn == 1:
        print()
        r = True
        while(r):
            roll = diceHand.roll()
            print(f"You rolled a {roll}")
            if roll == 1:
                print("Your turn is over")
                player.set_score(0)
                turn = 2
                r = False
                roll == r
            else:
                player.set_currentScore(roll)
                player.set_score(player.get_cureentScore() + player.get_score())
                option_menu()
                choice_2 = input("-> ")
                if choice_2 == 1:
                    continue
                elif choice_2 == 2:
                    turn = 2
                elif choice_2 == 3:
                    name = input('Enter your name: ')
                    player_tag = player.get_name(name)
                elif choice_2 == 4:
                    difficulty_mode()
                else:
                    exit()
    return player_tag
    
def option_menu():
    print()
    print("Press 1 to roll the die again")
    print("Press 2 to hold")
    print("press 3 to change name")
    print("press 4 to change the difficullty level")
    print("press 5 to quit")
    
def difficulty_mode():
    while(True):
        mode = input("Enter (e) for easy mode and (h) for hard mode: ").lower()
        if mode != 'e' and mode != 'h':
            print("Invalid input, try again")
        else:
            False
        return mode

def player_style():
    play_style = True
    while (play_style):
        try:
            choice = int(input("Select 1 for one player, 2 for two players: "))
        except:
            print("Invalid input, try again")
        
    return choice

def game_header():
    die = Dice()
    diceHand = DiceHand(die)
    command = True
    while(command):
        game_header = Game()
        print(game_header.header()) #vet ej vad jag ska göra här. Ska den vara i main eller ska vi ha den här? 
        

def intelligence_turn(player, intelligence, diceHand):
    while(intelligence.get_score() < 30 and intelligence.get_score() < 100):
        roll = diceHand.roll()
        print(f"Computers score: {intelligence.get_score()}")
        if roll == 1:
            print(' The computer rolled a 1')
            intelligence.self._score(0)
        else:
            intelligence.set_score(intelligence.get_score() + intelligence.get_tempScore())
            
    return intelligence.set_score