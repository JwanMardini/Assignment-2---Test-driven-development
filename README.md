Game description
--------------------------

"Pig" is a very simple game. Two players take turns; on each turn, a player rolls a six-sided die ("die" is the singular of "dice") as many times as she wishes, or until she rolls a 1. Each number she rolls, except a 1, is added to her score this turn; but if she rolls a 1, her score for this turn is zero, and her turn ends. At the end of each turn, the score for that turn is added to the player's total score. The first player to reach or exceed 100 wins.

At the start of the game the user get to decide to play one player against the computer or two players. In the one player style the difficulity level can be decided by the player, but this can not be done in two player mode. There are two difficulity levels: Easy and Hard. Cheat option exists in one player mode and in both difficulity levels, it allows your score to get additional 20 points.


How to start
--------------------------

These are the steps to get going with the game.

### 1. Check version of Python
For windows
```
PYTHON=python
make version
```

For Mac and Linux
```
export PYTHON=python3
make version
```

### Python virtual environment

Install a Python virtual environment.

```
# Create the virtual environment
make venv
```
Activation:

    For windows
    ```
    . .venv/Scripts/activate
    ```

    For Linx/Mac
    ```
    . .venv/bin/activate
    ```

Deactivation:
 Use the command `deactivate`.



### Install the requirements

Install pip and stores dependencies in `requirements.txt`.

```
make install
```

To check the installation
```
make installed
```


### Run the code

The game can be started by the following:

```
python Classes/main.py
```


### Run the linters
```
make flake8
make pylint
```

To run all
```
make lint
```


### Run the unittests

You can run the unittests like this:

```
make unittest
```

Run unittest with coverage
```
make coverage
```

