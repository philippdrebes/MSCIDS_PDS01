#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_exception_handling.php
#
# Errors and Exceptions
# Exception Handling
#
# An exception is an error that happens during the execution of a program.
#
# Error handling is generally resolved by saving the state of execution at the
# moment the error occurred and interrupting the normal flow of the program to
# execute a special function or piece of code, which is known as the exception
# handler.
#
# Depending on the kind of error ("division by zero", "file open error" and so
# on) which had occurred, the error handler can "fix" the problem and the
# programm can be continued afterwards with the previously saved data.
#

n = input("Please enter an integer: ")
n = int(n)

print("Ending with %d" % n)
