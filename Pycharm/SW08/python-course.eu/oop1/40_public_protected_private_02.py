#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Public- Protected- and Private Attributes

# Our next task consists in rewriting our Robot class. Though
# we have Getter and Setter methods for the name and the
# build_year, we can access the attributes directly as well,
# because we have defined them as public attributes. Data
# Encapsulation means, that we should only be able to access
# private attributes via getters and setters.
#
# We have to replace each occurrence of self.name and
# self.build_year by self.__name and self.__build_year.


class Robot:
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year

    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_build_year(self, by):
        self.__build_year = by

    def get_build_year(self):
        return self.__build_year

    def __repr__(self):
        return "Robot('" + self.__name + "', " + str(self.__build_year) + ")"

    def __str__(self):
        return(
            "Name: " + self.__name +
            ", Build Year: " + str(self.__build_year))


if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    y = Robot("Caliban", 1943)
    for rob in [x, y]:
        rob.say_hi()
        if rob.get_name() == "Caliban":
            rob.set_build_year(1993)
        print("I was built in the year " + str(rob.get_build_year()) + "!")
