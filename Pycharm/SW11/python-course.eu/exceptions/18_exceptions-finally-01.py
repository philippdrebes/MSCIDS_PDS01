#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_exception_handling.php
#
# Errors and Exceptions
# Clean-up Actions (try ... finally)
#
# The try statement can be followed by a finally clause which is always
# executed regardless if an exception occurred in a try block or not.


try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
    print("Thanks")
finally:
    print("There may or may not have been an exception.")
print("The inverse: ", inverse)

