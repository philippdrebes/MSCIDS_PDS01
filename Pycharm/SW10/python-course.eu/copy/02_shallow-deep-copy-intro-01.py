#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_deep_copy.php

# Shallow and Deep Copy

# We will cover the question of how to copy lists and nested lists
#
# The difference between shallow and deep copying is only relevant for compound
# objects, i.e. objects containing other objects, like lists or class
# instances.
#
# Review with http://www.pythontutor.com/visualize.html#mode=edit


x = 3
y = x
print(id(x), id(y))

y = 4
print(id(x), id(y))
print(x, y)

# things change, when we assign a new value to y. In this case y will receive a
# separate memory location
#
# But even if this internal behaviour appears strange compared to programming
# languages like C, C++ and Perl, yet the observable results of the assignments
# answer our expectations. But it can be problematic, if we copy mutable
# objects like lists and dictionaries.
#
# Python creates only real copies, if it has to, i.e. if the user, the
# programmer, explicitly demands it.
