#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_properties.php


# Decorator-Property-Exercise:
#
# To do:    Find out what's wrong with this code ... and why it's wrong.
#           If you comment out the # - lines => you will see the solution!
#           Correct the code!

class P:

    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        # print("In @property, self:", self, "/", self.__x)
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
            # print( "In @x.setter, self, __x:", self, "/", self.__x )
        elif x > 1000:
            self.__x = 1000
            # print( "In @x.setter, self, __x:", self, "/", self.__x )
        else:
            self.__x = x
            # print( "In @x.setter, self, __x:", self, "/", self.__x )



# a simple 'old' script/program
p1 = P(1001)                             # all old scripts has to run unchanged (with the new business rule!)
print("1) p1.x: ", p1.x)
p1.x = -12
print("2) p1.x: ", p1.x)



###########
# output:
###########
# 1) p1.x:  1001
# 2) p1.x:  0
