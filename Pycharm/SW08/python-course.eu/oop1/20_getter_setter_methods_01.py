#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Data Abstraction, Data Encapsulation, and Information Hiding
#
# * Encapsulation is seen as the bundling of data with the
#   methods that operate on that data.
#
# * Information hiding on the other hand is the principle that
#   some internal information or data is "hidden", so that it
#   can't be accidentally changed.
#
# Data Abstraction = Data Encapsulation + Data Hiding
#
# * Encapsulation is often accomplished by providing two kinds
#   of methods for attributes:
#   - getter
#   - setter
#


class Robot:

    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


x = Robot()
x.set_name("Henry")                         # x.name = "Henry"
x.say_hi()


y = Robot()
y.set_name(x.get_name())
print(y.get_name())
