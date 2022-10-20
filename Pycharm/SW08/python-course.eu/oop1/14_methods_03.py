#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Methods

# "self" is not a Python keyword. It's just a naming convention.


class Robot:

    def say_hi(self):             # weil eingerückt gehört diese Methode zur Klasse Robot
                                  # self ist ein "verstecktes" Pointer, dass auf das aufrufende Objekt zeigt
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")


x = Robot()                   # was passiert hier genau?
x.name = ""
Robot.say_hi(x)
y = Robot()
y.name = "Marvin"
Robot.say_hi(y)

# Robot.say_hi(x) and x.say_hi() are equivalent.
# x.say_hi() can be seen as an "abbreviated" form.
x.say_hi()
y.say_hi()
