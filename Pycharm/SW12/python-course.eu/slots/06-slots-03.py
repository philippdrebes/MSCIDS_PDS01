#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_slots.php
#
# Slots
# Avoiding Dynamically Created Attributes
#
# Using a dictionary for attribute storage is very convenient, but it can mean
# a waste of space for objects, which have only a small amount of instance
# variables. The space consumption can become critical when creating large
# numbers of instances.
#
# Slots are a nice way to work around this space consumption problem. Instead
# of having a dynamic dict that allows adding attributes to objects
# dynamically, slots provide a static structure which prohibits additions after
# the creation of an instance.
#
# Since Python 3.3 this advantage is not as impressive any more.
#


class S():

    __slots__ = ['val']

    def __init__(self, v):
        self.val = v


x = S(42)
print(x.val)
x.val = 24
print(x.val)
print(x.__slots__)

# print(x.__dict__)
# x.new = "not possible"
