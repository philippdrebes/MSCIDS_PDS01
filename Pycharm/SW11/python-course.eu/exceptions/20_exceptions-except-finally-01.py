#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_exception_handling.php
#
# Errors and Exceptions
# Combining try, except and finally
#
# "finally" and "except" can be used together for the same try block,
#

try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
    print("Thanks")
except ValueError:
    print("You should have given either an int or a float")
except ZeroDivisionError:
    print("Infinity! Because 1/0 is not defined!")
finally:
    print("There may or may not have been an exception.")

print("Bye")
