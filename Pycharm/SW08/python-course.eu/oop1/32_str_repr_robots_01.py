#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# __str__- and __repr__-Methods

# We will extend our robot class with a repr method.
# We dropped the other methods to keep this example simple:


class Robot:

    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return "Robot('" + self.name + "', " + str(self.build_year) + ")"


if __name__ == "__main__":
    x = Robot("Marvin", 1979)

    x_str = str(x)
    print(x_str)
    print("Type of x_str: ", type(x_str))
    print("id(x): ", id(x))


    new = eval(x_str)    # wird die __init__() Methode aufgeufen mit Robot('Marvin', 1979)
    print(new)
    print("Type of new:", type(new))
    print(new.name)
    print("id(new): ", id(new))

# x_str has the value Robot('Marvin', 1979).
# eval(x_str) converts it again into a Robot instance.
