#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_lambda.php
#
# Lambda, filter, reduce and map
# The map() Function
#
# map() can be applied to more than one list. The lists don't have to have the
# same length. map() will apply its lambda function to the elements of the
# argument lists


a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]

l1 = list(map(lambda x, y: x+y, a, b))
l2 = list(map(lambda x, y, z: x+y+z, a, b, c))
l3 = list(map(lambda x, y, z: 2.5*x + 2*y - z, a, b, c))

print(l1, l2, l3, sep="\n")

# We can see that the parameter x gets its values from the list a, while y gets
# its values from b and z from list c.
