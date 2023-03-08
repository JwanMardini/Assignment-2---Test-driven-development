import time
from Classes.game import Game
from Classes.player import Player
from Classes.intelligence import Intelligence
from Classes.dice import Dice
from Classes.dice_hand import DiceHand
from Classes.high_score import HighScore
from Classes.histogram import Histogram


def main():
    die = Dice()
    statistics = Histogram(die)
    game = Game()
    choice_controller = True
    while choice_controller:
        print(game.header())
        print()
        print(game.get_rules())
        print()
        print(game.get_startmenu())
        try:
            choice = int(input("-> "))
            if choice == 2:
                print()
                play = "y"
                while play == "y":
                    two_players(statistics)
                    play = input("Do you want to play again(y/n)").lower()
                print("Goodbye")
            elif choice == 1:
                play = "y"
                while play == "y":
                    difficulty_mode(statistics)
                    play = input("Enter y to play again and s to show statics: ").lower()
                    if play == "s":
                        show_statistics(statistics)
                        quit()
                print("Goodbye")
        except ValueError:
            print("Invalid input, try again.")
            print()
            print(game.get_startmenu())


def two_players(statics):
    name = input("Enter the first player name: ")
    name2 = input("Enter the seconde player name: ")
    player = Player(name, 0)
    player2 = Player(name2, 0)
    twoplayers_gamesetup(player, player2, statics)


def player_turn(player_1, player_2, turn, statics):
    die = Dice()
    dice_hand = DiceHand(die)
    roll = "y"
    turn_score = 0
    while roll == "y":
        die_num = dice_hand.roll()
        statics.saved_data(roll)
        print("You rolled a ", die_num)
        print()
        if die_num == 1:
            print("You rolled a 1")
            print("Your turn is over")
            print()
            roll = "n"
            turn_score = 0
        else:
            turn_score = turn_score + die_num
            print("Your turn so far is ", turn_score)
            roll = input("Do you want to roll again(y/n)? ").lower()
    if turn.get_turn() == 1:
        turn.set_turn(2)
        if turn_score == 0:
            player_1.set_score(0)
        else:
            player_1.set_score(player_1.get_score() + turn_score)
    elif turn.get_turn() == 2:
        turn.set_turn(1)
        if turn_score == 0:
            player_2.set_score(0)
        else:
            player_2.set_score(player_2.get_score() + turn_score)


def twoplayers_gamesetup(player, player2, statics):
    game = Game()
    high_score = HighScore().get_high_score()
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
        player_turn(player, player2, game, statics)
    if player.get_score >= 10:
        game.end_game(player.get_name(), player.get_score())
    elif player2.get_score() >= high_score:
        game.end_game(player2.get_name(), player2.get_score())


def difficulty_mode(statics):
    game = Game().get_difficultymenu()
    name = input("Enter your name: ")
    player = Player(name, 0)
    computer = Intelligence(-20, 20)
    choice_controller = True
    while choice_controller:
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
    cpu_gamesetup(player, computer, statics)


def cpu_gamesetup(player, player2, statics):
    game = Game()
    high_score = HighScore().get_high_score()
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
        print(game.get_optionmenu())
        controller = True
        while controller:
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
                computer_turn(player, player2, game, statics)
            elif choice == "4":
                player.set_score(player.get_score() + 20)
                controller = False
            else:
                print("Invalid input, try again.")

    if player.get_score() >= high_score:
        game.end_game(player.get_name(), player.get_score())
    elif player2.get_score() >= high_score:
        game.end_game(player2.get_name(), player2.get_score())


def computer_turn(player_1, player_2, turn, statics):
    die = Dice()
    dice_hand = DiceHand(die)
    roll = "y"
    turn_score = 0
    die_num = 0
    if turn.get_turn() == 1:
        while roll == "y":
            die_num = dice_hand.roll()
            statics.saved_data(die_num)
            print("You rolled a ", die_num)
            print()
            if die_num == 1:
                print("You rolled a 1")
                print("Your turn is over")
                print()
                roll = "n"
                turn_score = 0
            else:
                turn_score = turn_score + die_num
                print("Your turn so far is ", turn_score)
                if player_1.get_score() >= 10:
                    roll = "n"
                elif player_2.get_score() >= highScore:
                    roll = "n"
                else:
                    roll = input("Do you want to roll again(y/n)? ").lower()
    else:
        cpu_die = 0
        while cpu_die != 1:
            cpu_die = dice_hand.roll()
            statics.saved_data(cpu_die)
            print(player_2.get_name(), " rolled ", cpu_die)
            time.sleep(2)
            print()
            turn_score = turn_score + cpu_die
            if turn_score > 10 and turn_score < 20:
                print(player_2.get_name(), " choosed to hold")
                print()
                break
        if cpu_die == 1:
            print("OBS!, " + player_2.get_name(), " rolled a 1")
            print(player_2.get_name() + " turn is over")
            print()

    if turn.get_turn() == 1:
        turn.set_turn(2)
        if turn_score == 0:
            player_1.set_score(0)
        else:
            player_1.set_score(player_1.get_score() + turn_score)
    elif turn.get_turn() == 2:
        turn.set_turn(1)
        if cpu_die == 1:
            player_2.set_score(player_2.get_mode())
        else:
            player_2.set_score(player_2.get_score() + turn_score)


def end_game(player1, player2):
    high_score = HighScore().get_highScore()
    game = Game()
    winner = player1 if player1.get_score() >= high_score else player2
    game.end_game(winner.get_name(), winner.get_score())


def show_statistics(statistics):
    my_list = statistics.get_list()
    list2 = [0] * 7
    for score in my_list:
        list2[score] += 1
    for i in range(1, len(list2)):
        print()
        print(f'{i}: {"*" * list2[i]}')


if __name__ == "__main__":
    main()
