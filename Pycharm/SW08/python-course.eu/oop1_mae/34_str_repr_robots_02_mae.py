#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# __str__- and __repr__-Methods

# Now it's time to extend our class with a user
# friendly __str__ method:

class Robot:

    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        print("in __repr__")
        return "Robot('" + self.name + "', " + str(self.build_year) + ")"


    # mae
    def __str__(self):
        print("in __str__")
        return "'Name: " + self.name + ", Build Year: " + str(self.build_year) + "'"
    # def __str__(self):
    #     return "Name: " + self.name + ", Build Year: " + str(self.build_year)


if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    x_str = str(x)
    print(x_str)
    print("Type of x_str: ", type(x_str))

    #mae
    new = eval(x_str)                        # SyntaxError: invalid syntax => wenn oben in __str__ die ' ' fehlen!
    print(new)
    print("Type of new:", type(new))
