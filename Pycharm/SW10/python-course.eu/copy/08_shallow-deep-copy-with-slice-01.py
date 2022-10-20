#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_deep_copy.php

# Shallow and Deep Copy
# Copy with the Slice Operator
#
# It's possible to completely copy shallow list structures with the slice
# operator without having any of the side effects, which we have described
# above.
#
# Review with http://www.pythontutor.com/visualize.html#mode=edit


list1 = ['a', 'b', 'c', 'd']
list2 = list1[:]
list2[1] = 'x'
print(list2)
print(list1)
