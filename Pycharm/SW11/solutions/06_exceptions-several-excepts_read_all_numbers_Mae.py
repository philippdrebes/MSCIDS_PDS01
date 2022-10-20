#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_exception_handling.php
#
# Errors and Exceptions
# Multiple Except Clauses
#
# A try statement may have more than one except clause for different
# exceptions. But at most one except clause will be executed
#
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#
# rename integer.txt, change content

# Exercise: Read all the numbers without whitespaces from the file and output them on the console

import sys

try:
    f = open('integers.txt')
    #print(type(f))             #  => https://docs.python.org/3/library/io.html

    s = f.readline()
    while s != "":
        i = int(s.strip())
        print(i)
        s = f.readline()
except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): {1}".format(errno, strerror))
    # e can be printed directly without using .args:
    # print(e)
except ValueError:
    print("No valid integer in line.")
# except:
except Exception:
    print("Unexpected error:", sys.exc_info()[0])
    raise

print("Ending")
