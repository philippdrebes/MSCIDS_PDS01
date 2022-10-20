#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_slots.php
#
# Slots
# Avoiding Dynamically Created Attributes
#
# https://docs.python.org/3.3/reference/datamodel.html#slots
# https://docs.python.org/3/reference/datamodel.html#notes-on-using-slots
#
# The attributes of objects are stored in a dictionary "__dict__".
#


class A():
    pass


a = A()
a.x = 66
a.y = "dynamically created attribute"

print(a.x, a.y, sep="\n")
print(a.__dict__)
