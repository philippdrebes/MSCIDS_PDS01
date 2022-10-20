#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_generators.php
#
# Generators
# Introduction
#
# An iterator can be seen as a pointer to a container, e.g. a list structure
# that can iterate over all the elements of this container.
#

print("~" * 10)
cities = ["Paris", "Berlin", "Hamburg", "Frankfurt", "London", "Vienna",
          "Amsterdam", "Den Haag"]

for location in cities:
    print("location: " + location)


print("~" * 10)
other_cities = ["Strasbourg", "Freiburg", "Stuttgart", "Vienna / Wien",
                "Hannover", "Berlin", "Zurich"]

city_iterator = iter(other_cities)
while city_iterator:
    try:
        city = next(city_iterator)
        print(city)
    except StopIteration:
        break
