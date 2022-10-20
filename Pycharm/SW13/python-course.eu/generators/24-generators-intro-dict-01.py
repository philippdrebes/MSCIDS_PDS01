#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_generators.php
#
# Generators
# Introduction
#
# The sequential base types as well as the majority of the classes of the
# standard library of Python support iteration. The dictionary data type dict
# supports iterators as well. In this case the iteration runs over the keys of
# the dictionary.
#
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range


capitals = {"France": "Paris", "Netherlands": "Amsterdam",
            "Germany": "Berlin", "Switzerland": "Bern", "Austria": "Vienna"}

for country in capitals:
    print("The capital city of " + country + " is " + capitals[country])
