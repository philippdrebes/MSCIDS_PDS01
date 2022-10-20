#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_properties.php

# Properties

# But what happens if we want to change the implementation
# in the future. This is a serious argument.
#
# The attribute x can have values between 0 and 1000.
# If a value larger than 1000 is assigned, x should be set to 1000.
# Correspondingly, x should be set to 0, if the value is less than 0.


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


p1 = P(1001)
print("1) p1.get_x: ", p1.get_x())
p2 = P(-2)
print("2) p2.get_x: ", p2.get_x())



# But there is a catch: Let's assume we have designed our class
# with the public attribute and no methods. People have already
# used it a lot and they have written code like this:

p1 = P(42)
p1.x = 1001          # assignment with "." (dot) notations are made ... and now???
                     # if we use "getX() and setX() then all "." (dot) code is broken!!!

print("3) p1.get_x: ", p1.get_x())
print(p1.__dict__)




# Our new class means breaking the interface. The attribute x is
# not available anymore. That's why in Java e.g. people are
# recommended to use only private attributes with getters and
# setters, so that they can change the implementation without
# having to change the interface.
#
# => !!!!!!!!!!!!!!!!!!
# But Python offers a solution to this problem. The solution is
# called "properties". "Properties" are some kind of 'Descriptors"!!!


###################
# output:
# 1) p1.get_x:  1000
# 2) p2.get_x:  0
# 3) p1.get_x:  42
# {'_P__x': 42, 'x': 1001}
