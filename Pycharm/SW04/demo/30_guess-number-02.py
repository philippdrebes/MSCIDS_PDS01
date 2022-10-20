#!/usr/bin/env python3
# https://www.python-course.eu/python3_loops.php

import random


def hello():
    print("SHALL WE PLAY A GAME?")


def guess():
    n = 10
    to_be_guessed = int(n * random.random()) + 1
    guess = 0
    for i in range(1, 5 + 1):
        guess = int(input(f"New number: ({i}): "))
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
        else:
            print("Congratulation. You made it!", i)
            break
    else:
        print("Game over")
    print("Bye")


if __name__ == "__main__":
    hello()
    guess()
    print("Over and out")
 