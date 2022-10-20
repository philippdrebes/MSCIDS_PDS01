#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_exception_handling.php
#
# Errors and Exceptions
# Multiple Except Clauses
#
# now so that the function will catch the exception directly:

# Exercise: Remove unnecessary lines of code!


def f():
    print("Let's try")
    x = 0

    try:
        x = int("four")
    except ValueError as e:
        print("got it in the function :-) ", e)

    print("working on it")
    return x



y = f()
print(f"I'm OK with {y}")

print("Let's get on")
