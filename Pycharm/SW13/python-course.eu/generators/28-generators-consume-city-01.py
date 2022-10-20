#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_generators.php
#
# Generators
#
# It's possible to create a generator object with this generator, which
# generates all the city names, one after the other:

from city_generator import city_generator

city = city_generator()
print("1)")
print(next(city))
print(next(city))

print("2)")
for c in city:
    print(c)
