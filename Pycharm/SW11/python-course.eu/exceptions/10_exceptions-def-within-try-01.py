#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_exception_handling.php
#
# Errors and Exceptions
# Multiple Except Clauses
#
# We call a function within a try block and if an exception occurs inside the
# function call:


def f():
    print("start-inside f(): Let's try")
    x = int("four")
    print("end-inside f() ... before return(x)! ")
    return(x)


try:
    print("Start 'try'")
    y = f()
    print("I'm OK")
    print("End 'try'")
except ValueError as e:
    print("We got it :-) => errormessage: ", e)

print("Let's get on after 'try'....")
