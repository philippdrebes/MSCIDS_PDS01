#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_iterable_iterator.php
#
# Iterators and Iterables
# Check On being an Iterable or an Iterator
#
# The module collection.abc has the functionalities we need

from collections.abc import Iterator, Iterable

cities_list = ["Berlin", "Frankfurt", "Geneva"]
cities_iterator = iter(cities_list)

print("Let's test 'cities_list':")
print("Iterator: ", isinstance(cities_list, Iterator))
print("Iterable: ", isinstance(cities_list, Iterable))

print("The same thing for  'cities_iterator':")
print("Iterator: ", isinstance(cities_iterator, Iterator))
print("Iterable: ", isinstance(cities_iterator, Iterable))

print("Some more stuff:")
a = "foo bar"
print("Iterator: ", isinstance(a, Iterator))
print("Iterable: ", isinstance(a, Iterable))
