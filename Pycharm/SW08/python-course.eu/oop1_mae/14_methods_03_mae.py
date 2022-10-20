#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Methods

# "self" is not a Python keyword. It's just a naming convention.


class Robot:

    def say_hi(self):

        #mae
        print("a) self.__dict__: ", self.__dict__)

        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")

        #mae
        print("b) self.__dict__: ", self.__dict__)


x = Robot()
#mae
print("0)", x.__dict__)

x.name = ""
#mae
print("1)")
Robot.say_hi(x)

y = Robot()
y.name = "Marvin"

#mae
print("2)")
Robot.say_hi(y)


# Robot.say_hi(x) and x.say_hi() are equivalent.
# x.say_hi() can be seen as an "abbreviated" form.


#mae
print("3)")
x.say_hi()
print("4)")
y.say_hi()

