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
    while (command):
        game_header = Game()
        print(game_header.header())
        controller = True
        #command kan göras som en egen metod? Blir lättare med färre while loop i samma metod?
        while (controller):
            try:
                choice = int(input("Select 1 for one player, 2 for two players: "))
            except ValueError:
                print("Invalid input, try again")

            if choice == 1:
                statment = True
                while (statment):
                    mode = input("Enter (e) for easy mode and (h) for hard mode: ")
                    if mode != 'e' and mode != 'h':
                        print("Invalid input, try again")
                    else:
                        statment = False
            name = str(input("Enter your name: "))
            player = Player(name, score=0, currentScore=0)
            computer = Intelligence(mode, score=0, currentScore=0)

            while (player.get_score() < 100 and computer.get_score() < 100):
            player = Player(name, score = 0, currentScore = 0)
            computer = Intelligence(mode, score = 0, currentScore = 0)
            
            ## en metod för player bör göras.
            while(player.get_score() < 100 and computer.get_score() < 100):
                print()
                print(f"{name} score: {player.get_score()}")
                print(f"Computers score: {computer.get_score()}")
                turn = 1
                if turn == 1:
                    print()
                    r = True
                    roll = diceHand.roll()
                    while (r):
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
                            print()
                            print("Press 1 to roll the die again")
                            print("Press 2 to hold")
                            print("press 3 to change name")
                            print("press 4 to change the difficullty level")
                            print("press 5 to quit")
                            choice_2 = input("-> ")
                            if choice_2 == 1:
                                continue
                            elif choice_2 == 2:
                                turn = 2
                            elif choice_2 == 3:
                                # metod ska göras
                                pass
                            elif choice_2 == 4:
                                # Intelligence
                                pass
                            else:
                                break


 if __name__ == "__main__":
    main()
