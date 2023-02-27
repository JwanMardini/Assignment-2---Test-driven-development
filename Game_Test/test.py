import random

player1Score = 0
player2Score = 0
turn = 1


def takeTurn():
    global player1Score
    global player2Score
    global turn
    roll = "y"
    turnScore = 0
    while roll == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print("You rolled a ", die1, "and a", die2)
        if die1 == 1 and die2 == 1:
            print("You rolled a pair of 1")
            print("Your turn is over")
            print("Hit enter to continue ")
            roll = "n"
            turnScore = -1
        elif die1 == 1 or die2 == 1:
            print("You rolled a one")
            print("Your turn is over")
            roll = "n"
            turnScore = 0
        else:
            turnScore = turnScore + die1 + die2
            print("Your turn so far is ", turnScore)
            roll = input("Do you want to roll again(y/n)? ").lower()
    if turn == 1:
        turn = 2
        if turnScore == -1:
            player1Score = 0
        else:
            player1Score = player1Score + turnScore
    elif turn == 2:
        turn = 1
        if turnScore == -1:
            player2Score = 0
        else:
            player2Score = player2Score + turnScore


def gameTurn():
    global player1Score
    global player2Score
    global turn
    while player1Score < 100 and player2Score < 100:
        print("The current score is")
        print("Player 1:", player1Score)
        print("Player 2:", player2Score)
        print("Player", turn, "it is your turn")
        input("Hit enter to continue ")
        takeTurn()
    if player1Score >= 100:
        print("Player 1 wins")
    elif player2Score >= 100:
        print("Player 2 wins")


def splashScreen():
    print("----------------------")
    print("----------------------")
    print("--- Welcome to pig ---")
    print("----------------------")
    print("----------------------")
    print()


splashScreen()
play = "y"
while play == "y":
    gameTurn()
    play = input("Do you want to play again(y/n)").lower
print("Goodbye")
