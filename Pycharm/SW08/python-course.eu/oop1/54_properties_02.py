#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_properties.php

# Properties ("only" ... the older way!)

# Alternatively, we could have used a different syntax
# without decorators to define the property


class P:

    def __init__(self, x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    # https://docs.python.org/3/library/functions.html#property
    x = property(get_x, set_x)


# # a simple 'old' script/program
# p1 = P(1001)                             # all old scripts has to run unchanged (with the new business rule!)
# print(p1.x)
# p1.x = -12
# print(p1.x)

# a simple 'old' script/program
p1 = P(1001)                             # all old scripts has to run unchanged (with the new business rule!)
print("1) p1.x: ", p1.x)
p1.x = -12
print("2) p1.x: ", p1.x)

# mae:
# it works also with old ("pre" decorator_property style) e.g. get_x() and set_x() ...
p1.set_x(42)
print("3) p1.get_x(): ", p1.get_x())

###########
# output
# 1) p1.x:  1000
# 2) p1.x:  0
# 3) p1.get_x():  42
