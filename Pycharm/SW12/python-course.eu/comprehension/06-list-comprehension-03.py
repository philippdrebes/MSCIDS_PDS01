#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_list_comprehension.php
#
# List Comprehension
# Examples
#

colours = ["red", "green", "yellow", "blue"]
things = ["house", "car", "tree"]
coloured_things = [(x, y) for x in colours for y in things]

print(coloured_things)
