#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro
# 2021-10, Erwin Mathis
# https://www.python-course.eu/python3_object_oriented_programming.php

# _02_robot_properties_02_yes_sol.py

class Robot:

    def __init__(self,
                 name="",
                 build_year=None):
        self.name = name
        self.build_year = build_year

    @property
    def name(self):
        return self.__name

    @property
    def build_year(self):
        return self.__build_year

    @name.setter
    def name(self, a_name):
        if a_name:
            self.__name = a_name.upper()

    @build_year.setter
    def build_year(self, a_build_year):
        if a_build_year and a_build_year < 1995:
            self.__build_year = 1995
        else:
            self.__build_year = a_build_year

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
        if self.build_year:
            print("I was built in " + str(self.build_year))
        else:
            print("It's not known, when I was created!")


def my_main():
    x = Robot("Henry", 1990)
    y = Robot()
    y.name = "Marvin"
    y.build_year = 2000
    x.say_hi()
    y.say_hi()
    y.build_year = x.build_year + 5
    y.say_hi()


if __name__ == "__main__":
    my_main()


#################
# output:
# Hi, I am HENRY
# I was built in 1995
# Hi, I am MARVIN
# I was built in 2000
# Hi, I am MARVIN
# I was built in 2000
