from game import Game
from player import Player
from intelligence import Intelligence
from dice import Dice
from diceHand import DiceHand
from highScore import HighScore
from histogram import Histogram
import time


def main():
    die = Dice()
    statistics = Histogram(die)
    game = Game()
    choice_controller = True
    while (choice_controller):
        print(game.header())
        print()
        print(game.get_rules())
        print()
        print(game.get_startMenu())
        try:
            choice = int(input("-> "))
            if choice == 2:
                print()
                play = "y"
                while (play == "y"):
                    twoPlayers(statistics)
                    play = input("Do you want to play again(y/n)").lower()
                print("Goodbye")
            elif choice == 1:
                play = "y"
                while (play == "y"):
                    difficulty_mode(statistics)
                    play = input("Enter y to play again and s to show statics: ").lower()
                    if play == "s":
                        showStatistics(statistics)
                        quit()
                    
                print("Goodbye")
        except ValueError:
            print("Invalid input, try again.")
            print()
            print(game.get_startMenu())


def twoPlayers(statics):
    name = input("Enter the first player name: ")
    name2 = input("Enter the seconde player name: ")
    player = Player(name, 0)
    player2 = Player(name2, 0)
    twoPlayers_gameSetUp(player, player2, statics)


def playerTurn(player_1, player_2, turn, statics):
    die = Dice()
    diceHand = DiceHand(die)
    roll = "y"
    turnScore = 0
    while (roll == "y"):
        die_num = diceHand.roll()
        statics.savedData(roll)
        print("You rolled a ", die_num)
        print()
        if die_num == 1:
            print("You rolled a 1")
            print("Your turn is over")
            print()
            roll = "n"
            turnScore = 0
        else:
            turnScore = turnScore + die_num
            print("Your turn so far is ", turnScore)
            roll = input("Do you want to roll again(y/n)? ").lower()
    if turn.get_turn() == 1:
        turn.set_turn(2)
        if turnScore == 0:
            player_1.set_score(0)
        else:
            player_1.set_score(player_1.get_score() + turnScore)
    elif turn.get_turn() == 2:
        turn.set_turn(1)
        if turnScore == 0:
            player_2.set_score(0)
        else:
            player_2.set_score(player_2.get_score() + turnScore)


def twoPlayers_gameSetUp(player, player2, statics):
    game = Game()
    high_score = HighScore().get_highScore()
    while (player.get_score() <= high_score or player2.get_score() <= high_score):
        print(f"{player.get_name()} score: {player.get_score()}")
        print(f"{player2.get_name()} score: {player2.get_score()}")
        print()
        if game.get_turn() == 1:
            print("it is " + player.get_name() + " turn")
            print()
        elif game.get_turn() == 2:
            print("it is " + player2.get_name() + " turn")
            print()
        input("Hit enter to continue ")
        playerTurn(player, player2, game, statics)
    if player.get_score >= high_score:
        game.end_game(player.get_name(), player.get_score())
    elif player2.get_score() >= high_score:
        game.end_game(player2.get_name(), player2.get_score())
        

def difficulty_mode(statics):
    game = Game().get_defficultyMenu()
    name = input("Enter your name: ")
    player = Player(name, 0)
    computer = Intelligence(-20, 20)
    choice_controller = True
    while (choice_controller):
        try:
            print(game)
            mode = str(input("-> ").lower())
            if mode == "e":
                choice_controller = False
                computer = Intelligence(-20, - 20)
            elif mode == "h":
                choice_controller = False
                computer = Intelligence(20, 20)
        except TypeError:
            print("Invalid input, try again.")
            print()
    CPU_gameSetUp(player, computer, statics)
    


def CPU_gameSetUp(player, player2, statics):
    game = Game()
    high_score = HighScore().get_highScore()
    while (player.get_score() < high_score and player2.get_score() < high_score):
        print(f"{player.get_name()} score: {player.get_score()}")
        print(f"{player2.get_name()} score: {player2.get_score()}")
        print()
        if game.get_turn() == 1:
            print("it is " + player.get_name() + " turn")
            print()
        elif game.get_turn() == 2:
            print("it is " + player2.get_name() + " turn")
            print()
        print()
        print(game.get_optionMenu())
        controller = True
        while (controller):
            choice = input("-> ")
            if choice == "1":
                controller = False
                player_name = input("Type in the new name: ")
                player.set_name(player_name)
            elif choice == "2":
                controller = False
                exit()
            elif choice == "3":
                controller = False
                computerTurn(player, player2, game, statics)
            elif choice == "4":
                player.set_score(player.get_score() + 20)
                controller = False
            else:
                print("Invalid input, try again.")

    if player.get_score() >= high_score:
        game.end_game(player.get_name(), player.get_score())
    elif player2.get_score() >= high_score:
        game.end_game(player2.get_name(), player2.get_score())


def computerTurn(player_1, player_2, turn, statics):
    highScore = HighScore().get_highScore()
    die = Dice()
    diceHand = DiceHand(die)
    roll = "y"
    turnScore = 0
    die_num = 0
    if turn.get_turn() == 1:
        while (roll == "y"):
            die_num = diceHand.roll()
            statics.savedData(die_num)
            print("You rolled a ", die_num)
            print()
            if die_num == 1:
                print("You rolled a 1")
                print("Your turn is over")
                print()
                roll = "n"
                turnScore = 0
            else:
                turnScore = turnScore + die_num
                print("Your turn so far is ", turnScore)
                if player_1.get_score() >= highScore:
                    roll = "n"
                elif player_2.get_score() >= highScore:
                    roll = "n"
                else:
                    roll = input("Do you want to roll again(y/n)? ").lower()
    else:
        cpu_die = 0
        while (cpu_die != 1):
            cpu_die = diceHand.roll()
            statics.savedData(cpu_die)
            print(player_2.get_name(), " rolled ", cpu_die)
            time.sleep(2)
            print()
            turnScore = turnScore + cpu_die
            if turnScore > 10 and turnScore < 20:
                print(player_2.get_name(), " choosed to hold")
                print()
                break
        if cpu_die == 1:
            print("OBS!, " + player_2.get_name(), " rolled a 1")
            print(player_2.get_name() + " turn is over")
            print()

    if turn.get_turn() == 1:
        turn.set_turn(2)
        if turnScore == 0:
            player_1.set_score(0)
        else:
            player_1.set_score(player_1.get_score() + turnScore)
    elif turn.get_turn() == 2:
        turn.set_turn(1)
        if cpu_die == 1:
            player_2.set_score(player_2.get_mode())
        else:
            player_2.set_score(player_2.get_score() + turnScore)


def end_game(player1, player2):
    high_score = HighScore().get_highScore()
    game = Game()
    winner = player1 if player1.get_score() >= high_score else player2
    game.end_game(winner.get_name(), winner.get_score())
    

def showStatistics(statistics):
    my_list = statistics.get_list()
    list2 = [0] * 7
    for score in my_list:
        list2[score] += 1
    for i in range(1, len(list2)):
        print()
        print(f'{i}: {"*" * list2[i]}')


if __name__ == "__main__":
    main()
