#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_exception_handling.php
#
# Errors and Exceptions
# Multiple Except Clauses
#
# We add now a "raise", which generates the ValueError again, so that the
# exception will be propagated to the caller:


def f():
    print("start-inside f(): Let's try")
    x = 0

    try:
        x = int("four")
    except ValueError as e:
        print("We got it :-) in the function :-) => errormessage: ", e)
        raise                        # raise the exception to the 'caller'

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
