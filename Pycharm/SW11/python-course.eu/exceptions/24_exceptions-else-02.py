#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_exception_handling.php
#
# Errors and Exceptions
# else Clause
#
# An "else clause" (not in Java, C# and so on!)  will be executed if the try clause doesn't raise an exception.
#
# The main difference is that in the first case, all statements of the try
# block can lead to the same error message "cannot open ...", which is wrong

# import sys
# file_name = sys.argv[1]

file_name = 'integers.txt'

text = []
try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
    fh.close()
else:                          # if try don't raise an exception => do all stuff in 'else':
    print("else ...")
    text = fh.readlines()
    fh.close()

if text:
    print(text[0])
