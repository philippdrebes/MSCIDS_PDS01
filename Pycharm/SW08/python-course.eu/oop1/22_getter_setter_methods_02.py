#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Data Abstraction, Data Encapsulation, and Information Hiding
#
# add an additional attribute "build_year" with Getters and Setters


class Robot:

    def __init__(self,
                 name=None,
                 build_year=None):
        self.name = name
        self.build_year = build_year

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
        if self.build_year:
            print("I was built in " + str(self.build_year))
        else:
            print("It's not known, when I was created!")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_build_year(self, by):
        self.build_year = by

    def get_build_year(self):
        return self.build_year


x = Robot("Henry", 2008)
y = Robot()
y.set_name("Marvin")
x.say_hi()
y.say_hi()


# Our Robot class provides us with two ways to access or to
# change the "name" or the "build_year" attribute. This can be
# prevented by using private attributes, which we will explain
# later.
