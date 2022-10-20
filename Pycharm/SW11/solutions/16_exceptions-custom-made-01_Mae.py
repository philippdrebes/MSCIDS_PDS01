#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_exception_handling.php
#
# Errors and Exceptions
# Custom-made Exceptions
#
# It's possible to create Exceptions by defining an exception class which
# inherits from the Exception class

# Exercise: Change the program so that it no longer raises a 'red' exception.
# raise MyException (....) must continue to be called!


class MyException(Exception):
    pass

try:
    raise MyException("An exception doesn't always prove the rule!")
except MyException as e:
    print("My own Exception called! => ", e)
