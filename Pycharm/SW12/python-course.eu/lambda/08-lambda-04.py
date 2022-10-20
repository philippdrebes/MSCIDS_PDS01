#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_lambda.php
#
# Lambda, filter, reduce and map
# The map() Function
#
# The first argument func is the name of a function and the second a sequence
# (e.g. a list) seq. map() applies the function func to all the elements of the
# sequence seq.
#


C = [39.2, 36.5, 37.3, 38, 37.8]

for f in map(lambda x: (float(9)/5)*x + 32, C):
    print("1) ", f)

F = list(map(lambda x: (float(9)/5)*x + 32, C))
print("2) ", F)

C = list(map(lambda x: (float(5)/9)*(x-32), F))
print("3) ", C)
