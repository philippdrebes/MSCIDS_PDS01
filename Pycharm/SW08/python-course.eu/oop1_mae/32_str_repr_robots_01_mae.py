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
        print("__repr__-Aufruf")
        return "Robot('" + self.name + "', " + str(self.build_year) + ")"


if __name__ == "__main__":
    x = Robot("Marvin", 1979)

    print("0)")
    x_str = str(x)                # weil str() nicht vorhanden => repr() aufgerufen!
    print("1)", x_str)

    # mae
    x_repr = repr(x)
    print("2)", x_repr)           # Beweis das hier (!!) repr() und str() gleiches Resultat ergeben!

    print("3) Type of x_str: ", type(x_str))

    # mae
    print("4)", x.__dict__)
    print("5)", Robot.__dict__)

    new = eval(x_str)

    # mae
    print("6)", new.__dict__)
    print("7)", Robot.__dict__)

    print("8)",new)                # bei Ausgabe von 'new' wieder 'repr()' aufgerufen, weil keine str() Methode hier!
    print("9) Type of new:", type(new))
    print("10)",new.name)


# x_str has the value Robot('Marvin', 1979).
# eval(x_str) converts it again into a Robot instance.
