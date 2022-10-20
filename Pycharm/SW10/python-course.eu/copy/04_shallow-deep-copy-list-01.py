#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_deep_copy.php

# Shallow and Deep Copy
# Copying a list

# A simple list is assigned to colours1. This list is a so-called "shallow
# list", because it doesn't have a nested structure, i.e. no sublists are
# contained in the list.
#
# Review the illustration
# Review with http://www.pythontutor.com/visualize.html#mode=edit


colours1 = ["red", "blue"]
colours2 = colours1
print(colours1)
print(colours2)
print(id(colours1), id(colours2))
# both variables point to the same list object


colours2 = ["rouge", "vert"]
print(colours1)
print(colours2)
print(id(colours1), id(colours2))
# colours2 points to new list object
