from game import Game
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
        while (play == "y"):
            twoPlayers()
            play = input("Do you want to play again(y/n)").lower
        print("Goodbye")
    elif choice == 1:
        play = "y"
        while (play == "y"):
            computer()
            play = input("Do you want to play again(y/n)").lower
        print("Goodbye")


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
    high_score = HighScore()
    while (player.get_score() < high_score.get_highScore() and player2.get_score() < high_score.get_highScore()):
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
    if player.get_score >= 100:
        game.end_game(player.get_name(), player.get_score())
    elif player2.get_score() >= 100:
        game.end_game(player2.get_name(), player2.get_score())


def computer():
    name = input("Enter your name: ")
    player = Player(name, 0)
    level = input("Enter (e) for easy level or (h) for hard: ")
    if level == "e":
        computer = Intelligence(-20, -20)
    elif level == "h":
        computer = Intelligence(20, 20)
    CPU_gameSetUp(player, computer)


def CPU_gameSetUp(player, player2):
    game = Game()
    high_score = HighScore()
    while (player.get_score() < high_score.get_highScore() and player2.get_score() < high_score.get_highScore()):
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
        computerTurn(player, player2, game)
    if player.get_score >= 100:
        game.end_game(player.get_name(), player.get_score())
    elif player2.get_score() >= 100:
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
                roll = input("Do you want to roll again(y/n)? ").lower()
    else:
        cpu_die = 0
        while (cpu_die != 1):
            cpu_die = diceHand.roll()
            print(player_2.get_name(), " rolled ", cpu_die)
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


if __name__ == "__main__":
    main()
