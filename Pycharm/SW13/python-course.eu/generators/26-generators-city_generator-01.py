#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_generators.php
#
# Generators
#
# ln -s *city_generator* city_generator.py
#
# The yield statement turns a functions into a generator. A generator is a
# function which returns a generator object. This generator object can be seen
# like a function which produces a sequence of results instead of a single
# object. This sequence of values is produced by iterating over it, e.g. with a
# for loop. The values, on which can be iterated, are created by using the
# yield statement.
#
# The word "generator" is sometimes ambiguously used to mean both the generator
# function itself and the objects which are generated by a generator.
#
# Everything which can be done with a generator can also be implemented with a
# class based iterator as well. But the crucial advantage of generators
# consists in automatically creating the methods __iter__() and next().
#
# Generators provide a very neat way of producing data which is huge or
# infinite.


def city_generator():
    yield("London")
    yield("Hamburg")
    yield("Konstanz")
    yield("Amsterdam")
    yield("Berlin")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")
