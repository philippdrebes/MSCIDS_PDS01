#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_exception_handling.php
#
# Errors and Exceptions
# Custom-made Exceptions
#
# It's possible to create Exceptions by defining an exception class which
# inherits from the Exception class


class MyException(Exception):
    pass


raise MyException("An exception doesn't always prove the rule!")

