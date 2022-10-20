#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_deep_copy.php

# Shallow and Deep Copy
# Using the Method deepcopy from the Module copy
#
# A solution to the described problems provide the module "copy". This module
# provides the method "deepcopy", which allows a complete or deep copy of an
# arbitrary list, i.e. shallow and other lists.
#
# Review the illustration
# Review with http://www.pythontutor.com/visualize.html#mode=edit

from copy import deepcopy

lst1 = ['a', 'b', ['ab', 'ba']]
lst2 = deepcopy(lst1)

print("1)", lst1)
print("2)", lst2)
print("3)", id(lst1))
print("4)", id(lst2))
print("5)", id(lst1[0]))
print("6)", id(lst2[0]))
print("7)", id(lst2[2]))
print("8)", id(lst1[2]))

# We can see by using the id function that the sublist has been copied, because
# id(lst2[2]) is different from id(lst1[2]). An interesting fact is that the
# strings are not copied: lst1[0] and lst2[0] reference the same string.
