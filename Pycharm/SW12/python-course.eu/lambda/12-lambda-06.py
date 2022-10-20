#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_lambda.php
#
# Lambda, filter, reduce and map
# The map() Function
#
# If one list has fewer elements than the others, map will stop when the
# shortest list has been consumed:
#

a = [1, 2, 3]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]

l1 = list(map(lambda x, y: x+y, a, b))
l3 = list(map(lambda x, y, z: 2.5*x + 2*y - z, a, b, c))

print(l1, l3, sep="\n")
