""" from game import Game
from player import Player
from intelligence import Intelligence
from dice import Dice
from diceHand import DiceHand
from highScore import HighScore


def main():
    game = Game()
    print(game.header())
    print()
    print(game.get_startMenu())
    choice = int(input("-> "))
    if choice == 2:
        print()
        play = "y"
        while ("y"):
            TwoPlayers()
            play = input("Do you want to play again(y/n)").lower
        print("Goodbye")
    elif choice == 1:
        play = "y"
        while (play == "y"):
            difficulty_mode()
        play = input("Do you want to play again(y/n)").lower
        print("Goodbye")


def players_turn(player1, player2, turn):

    die = Dice()
    diceHand = DiceHand(die)
    turnScore = 0
    while True:
        die_num = diceHand.roll()
        print("You rolled a ", die_num)

        if die_num == 1:
            print("You rolled a 1")
            print("Your turn is over")
            turnScore = 0
            break
        turnScore += die_num
        print("Your turn so far is ", turnScore)

        roll = input("Do you want to roll again(y/n)? ").lower()
        if roll != "y":
            break
        if turn.get_turn() == 1:
            player1.set_score(max(0, player1.get_score() + turnScore))
            turn.set_turn(2)
        else:
            player2.set_score(max(0, player2.get_score() + turnScore))
            turn.set_turn(1)


def difficulty_mode():
    name = input("Enter your name: ")
    player = Player(name, 0)
    
    while (True):
        mode = input("Enter (e) for easy mode and (h) for hard mode: ").lower()
        if mode == "e":
            computer = Intelligence(-20, - 20)
        elif mode == "h":
            computer = Intelligence(20, 20)
        else:
            print("Invalid input, try again")
        gamePlayofTwo(player, computer)

def player_style():
    play_style = True
    while (play_style):
        try:
            choice = int(input("Select 1 for one player, 2 for two players: "))
        except ValueError:
            print("Invalid input, try again")

    return choice


def AI_gameplay(intelligence, diceHand):
    while(intelligence.get_score() < 30 and intelligence.get_score() < 100):
        roll = diceHand.roll()
        print(f"Computers score: {intelligence.get_score()}")
        if roll == 1:
            print('The computer rolled a 1')
            intelligence.self._score(0)
        else:
            intelligence.set_score(intelligence.get_score() + intelligence.self._score())
            
    return intelligence.set_score


def player_name():
    while True:
        name = input("Enter your name: ")
        return name


def TwoPlayers(player1, player2):
    for name in range(1, 2):
        player_name()
        player1 = Player(name([0]), 0)
        player2 = Player(name([1]), 0)
    return player1, player2
    

def gamePlayofTwo(player1, player2):
    game = Game()
    high_score = HighScore().get_highScore()

    while (player1.get_score() < high_score and player2.get_score() < high_score):
        print(f"{player1.get_name()} score: {player1.get_score()}")
        print(f"{player2.get_name()} score: {player2.get_score()}")
        print()
        if game.get_turn() == 1:
            print("it is " + player1.get_name() + " turn")
            print()
        elif game.get_turn() == 2:
            print("it is " + player2.get_name() + " turn")
            print()
        input("Hit enter to continue ")
        players_turn(player1, player2, game)
    if player1.get_score >= 100:
        game.end_game(player1.get_name(), player1.get_score())
    elif player2.get_score() >= 100:
        game.end_game(player2.get_name(), player2.get_score())


def end_game(player1, player2):
    game = Game()
    winner = player1 if player1.get_score() >= 100 else player2
    game.end_game(winner.get_name(), winner.get_score())


if __name__ == "__main__":
    main()
     """
    
    


from game import Game
from player import Player
from intelligence import Intelligence
from dice import Dice
from diceHand import DiceHand
from highScore import HighScore
import time


def main():
    game = Game()
    print(game.header())
    print()
    print(game.get_startMenu())
    choice_controller = True
    while (choice_controller):
        try:
            choice = int(input("-> "))
            if choice == 2:
                print()
                play = "y"
                while (play == "y"):
                    twoPlayers()
                    play = input("Do you want to play again(y/n)").lower()
                print("Goodbye")
            elif choice == 1:
                play = "y"
                while (play == "y"):
                    difficulty_mode()
                    play = input("Do you want to play again(y/n)").lower()
                print("Goodbye")
        except ValueError:
            print("Invalid input, try again.")
            print()
            print(game.get_startMenu())


def twoPlayers():
    name = input("Enter the first player name: ")
    name2 = input("Enter the seconde player name: ")
    player = Player(name, 0)
    player2 = Player(name2, 0)
    twoPlayers_gameSetUp(player, player2)


def playerTurn(player_1, player_2, turn):
    die = Dice()
    diceHand = DiceHand(die)
    roll = "y"
    turnScore = 0
    while (roll == "y"):
        die_num = diceHand.roll()
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


def twoPlayers_gameSetUp(player, player2):
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
        playerTurn(player, player2, game)
    if player.get_score >= 10:
        game.end_game(player.get_name(), player.get_score())
    elif player2.get_score() >= 10:
        game.end_game(player2.get_name(), player2.get_score())
        

def difficulty_mode():
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
    CPU_gameSetUp(player, computer)
    


def CPU_gameSetUp(player, player2):
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
        # input("Hit enter to continue ")
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
                computerTurn(player, player2, game)
            else:
                print("Invalid input, try again.")

        # game.ingameMenu(choice, player)
        # input("Hit enter to continue \n")
        # computerTurn(player, player2, game)
    if player.get_score() >= 10:
        game.end_game(player.get_name(), player.get_score())
    elif player2.get_score() >= 10:
        game.end_game(player2.get_name(), player2.get_score())


def computerTurn(player_1, player_2, turn):
    die = Dice()
    diceHand = DiceHand(die)
    roll = "y"
    turnScore = 0
    die_num = 0
    if turn.get_turn() == 1:
        while (roll == "y"):
            die_num = diceHand.roll()
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
                if turnScore <= 10:
                    roll = "n"
                else:
                    roll = input("Do you want to roll again(y/n)? ").lower()
    else:
        cpu_die = 0
        while (cpu_die != 1):
            cpu_die = diceHand.roll()
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
    game = Game()
    winner = player1 if player1.get_score() >= 10 else player2
    game.end_game(winner.get_name(), winner.get_score())


if __name__ == "__main__":
    main()
