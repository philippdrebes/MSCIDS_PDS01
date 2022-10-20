#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_deep_copy.php

# Shallow and Deep Copy
# Copy with the Slice Operator
#
# But as soon as a list contains sublists, we have another difficulty: The
# sublists are not copied but only the references to the sublists.
#
# Review the illustration
# Review with http://www.pythontutor.com/visualize.html#mode=edit


lst1 = ['a', 'b', ['ab', 'ba']]
lst2 = lst1[:]

lst2[0] = 'c'

print(lst1)
print(lst2)
