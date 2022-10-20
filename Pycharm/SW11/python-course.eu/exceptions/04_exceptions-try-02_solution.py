#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_exception_handling.php
#
# Errors and Exceptions
# Exception Handling
#
# With the aid of exception handling, we can write robust code for reading an
# integer from input:


while True:
    try:
        n = input("Please enter an integer: ")
        if n == 'q':
            break
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
if n != 'q':
    print("Great, you successfully entered an integer!")

    print("Ending with %d" % n)
else:
    print("... ok ... see you later!")
