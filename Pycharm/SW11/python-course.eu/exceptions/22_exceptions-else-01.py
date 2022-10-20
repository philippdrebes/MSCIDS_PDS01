#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_exception_handling.php
#
# Errors and Exceptions
# else Clause
#
# Starting point
#

# import sys
# file_name = sys.argv[1]
file_name = 'integers.txt'

text = []
try:
    fh = open(file_name, 'r')
    text = fh.readlines()                 # we use now readlines() NOT readline()
    fh.close()
except IOError:
    print('cannot open', file_name)
    fh.close()

if text:
    print(text[0])

