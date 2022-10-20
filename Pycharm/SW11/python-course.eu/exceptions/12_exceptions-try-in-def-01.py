#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_exception_handling.php
#
# Errors and Exceptions
# Multiple Except Clauses
#
# now so that the function will catch the exception directly:
import sys

def f():
    print("start-inside f(): Let's try")
    x = 0

    try:
        x = int("four")
    except ValueError as e:
        print("We got it :-) in the function :-) => errormessage: ", e)
        # print("the program will be stopped!")
        # sys.exit()
    print("end-inside f() ... before return(",x,")! ")
    return x


try:
    print("Start 'try'")
    y = f()
    print(f"I'm OK with {y}")
    print("End 'try'")
except ValueError as e:
    print("We got it :-) in 'script' => errormessage:  ", e)


print("Let's get on after 'try'....")
