#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_exception_handling.php
#
# Errors and Exceptions
# else Clause
#
# An else clause will be executed if the try clause doesn't raise an exception.
#
# The main difference is that in the first case, all statements of the try
# block can lead to the same error message "cannot open ...", which is wrong

# import sys
# file_name = sys.argv[1]

# Exercise: Read all the numbers from the integers.txt file
#           and create tow lists that contains the numbers WITHOUT any whitespaces
#           as 'number' => Solution A   and as 'String'  =>  Solution B

# Solution A:    [42, 24, 34, 23, 1, 0, 42, 15]
# Solution B:    ['42', '24', '34', '23', '1', '0', '42', '15']



file_name = 'integers.txt'

text = []
try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    print("else ...")
    text = fh.readlines()
    fh.close()

if text:
    print(text)
    mytext = []
    t = ""
    for t in text:
        #print(t)
        # print(t.strip())
        # mytext.append(int(t.strip()))
        mytext.append(t.strip())
    print(mytext)

