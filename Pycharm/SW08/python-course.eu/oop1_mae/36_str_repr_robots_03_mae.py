#!/usr/bin/env python3

# env is a program under linux which starts different "environments" e.g. python3 ...!

# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# __str__- and __repr__-Methods

# Now it's time to extend our class with a user
# friendly __str__ method.
# x_repr can still be turned into a Robot object.


class Robot:

    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        print("in __repr__")
        return "Robot(\"" + self.name + "\"," + str(self.build_year) + ")"

    def __str__(self):
        print("in __str__")
        return "Name: " + self.name + ", Build Year: " + str(self.build_year)


if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    print(x, id(x))

    x_repr = repr(x)
    print(x_repr, type(x_repr))

    #mae
    print("*"* 60)

    new = eval(x_repr)
    print(new, id(new))
    print("Type of new:", type(new))
    print(new.name)

    # mae
    print("*"* 60)

    new.name = "Mr. Eval"
    print(new.name)
    print(x.name)


