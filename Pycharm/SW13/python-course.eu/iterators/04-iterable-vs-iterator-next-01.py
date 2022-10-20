#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_iterable_iterator.php
#
# Iterators and Iterables
# Difference Between Iterable and Iterator
#
# An iterator can be created from an iterable by using the function 'iter'.
#
# To make this possible the class of an object needs either a method
# '__iter__', which returns an iterator, or a '__getitem__' method with
# sequential indexes starting with 0.
#
# Iterators are objects with a '__next__' method, which will be used when the
# function 'next' is called.
#
# You can call the __next__() method using the next() built-in function. This
# is how it works:


# collection (= iterable)
cities = ["Berlin", "Vienna", "Zurich"]

# iter of a iterable => an iterator
iterator_obj = iter(cities)
print(iterator_obj)

# next of an iterator => next element
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
