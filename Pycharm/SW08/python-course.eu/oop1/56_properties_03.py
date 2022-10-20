#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_properties.php

# Properties

# We have now two ways to access or change the value of x:
# Either by using "p1.x = 42" or by "p1.set_x(42)".
#
# This way we are violating one of the fundamentals of Python:
# "There should be one-- and preferably only one --obvious way to do it."
# (see Zen of Python)


class P:

    def __init__(self, x):
        self.__set_x(x)

    def __get_x(self):
        return self.__x

    def __set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(__get_x, __set_x)


# a simple 'old' script/program
p1 = P(1001)                             # all old scripts has to run unchanged (with the new business rule!)
print("1) p1.x: ", p1.x)
p1.x = -12
print("2) p1.x: ", p1.x)

# Even though we fixed this problem by using a private getter and setter,
# the version with the decorator "@property" is the Pythonic way to do it.

# mae:
# the next line don't work now  => we get an error-message! .
# p1.set_x(42)
# print("3) p1.get_x(): ", p1.get_x())


###########
# output
# 1) p1.x:  1000
# 2) p1.x:  0


