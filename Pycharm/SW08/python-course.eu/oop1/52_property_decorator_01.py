#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_properties.php

# Decorator - Properties

# * A method which is used for getting a value is
#   decorated with "@property".
# * The method which has to function as the setter is decorated
#   with "@x.setter"
# * If the function had been called "f", we would have to
#   decorate it with "@f.setter".

# This is the Pythonic way to do it.

########
# new business rule: only values  (0 <= value <= 1000) are correct!
# goal => the object p1 should not be created and set wrong!
#         examples: entered = 1001 => set = 1000
#                   entered -12    => set = 0)
# and
#          all old code should continue to run (unchanged!!!)
########



class P:

    def __init__(self, x):
        self.x = x

    @property                           # instead of get_x()
    def x(self):
        return self.__x

    @x.setter                           # instead of set_x()
    def x(self, x):
        if x < 0:                       # here are the new business rules!
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


# a simple 'old' script/program
p1 = P(1001)                             # all old scripts has to run unchanged (with the new business rule!)
print("1) p1.x: ", p1.x)
p1.x = -12
print("2) p1.x: ", p1.x)


#######################
# output:
# 1) p1.x:  1000
# 2) p1.x:  0
