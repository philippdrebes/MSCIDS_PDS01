#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_exception_handling.php
#
# Errors and Exceptions
# Exception Handling
#
# With the aid of exception handling, we can write robust code for reading an
# integer from input:

# Exercise:    Change the program
#              so that we are not "caught" in the loop, the option should be given to quit with 'q'


while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        if n == 'q':
            break
        else:
            print("No valid integer! Please try again ...")

if n == 'q':
    print("Ok we will try it next time again!")
else:
    print("Great, you successfully entered an integer!")

    print("Ending with %d" % n)
