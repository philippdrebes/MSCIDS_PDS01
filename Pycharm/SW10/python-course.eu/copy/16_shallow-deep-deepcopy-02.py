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

lst2[2][1] = "d"
lst2[0] = "c"
print(lst1)
print(lst2)
