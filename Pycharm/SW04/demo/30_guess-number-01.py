#!/usr/bin/env python3
# https://www.python-course.eu/python3_loops.php

import random


def hello():
    print("SHALL WE PLAY A GAME?")


def guess():
    n = 10
    to_be_guessed = int(n * random.random()) + 1
    guess = 0
    while guess != to_be_guessed:
        guess = int(input("New number: "))
        if guess > 0:
            if guess > to_be_guessed:
                print("Number too large")
            elif guess < to_be_guessed:
                print("Number too small")
        else:
            print("Sorry that you're giving up!")
            break
    else:
        print("Congratulation. You made it!")
    print("Bye")


if __name__ == "__main__":
    hello()
    guess()
    print("Over and out")
 