#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Attributes

# We can dynamically create arbitrary new attributes for existing
# instances of a class.
# This is not the way to properly create instance attributes.


class Robot:
    pass


x = Robot()
y = Robot()
z = Robot()

# mae
# print(x.__dict__)
# print(y.__dict__)


x.name = "Marvin"                  #  während der Laufzeit kann man einem Objekt Instanz-Variablen / Attribut / Komponente
                                   #  z.B. name oder build_year  beifügen.
x.build_year = "1979"

y.name = "Caliban"
y.build_year = "1993"

print(x.name)
print(y.build_year)


# The instances possess dictionaries __dict__, which they use to
# store their attributes and their corresponding values

print(x.__dict__)      # alles über das Objekt x ausgeben! in einem Dict!
print(y.__dict__)


z.vorname = "Gustav"
print(z.__dict__)

y.vorname = "Anna"
print(y.__dict__)
