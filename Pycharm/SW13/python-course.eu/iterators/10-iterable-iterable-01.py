#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_iterable_iterator.php
#
# Iterators and Iterables
# Check On being an Iterable or an Iterator
#
# The following function 'iterable' will return True, if the object 'obj' is an
# iterable and False otherwise.
#
# Our function 'iterable' is not necessary, or we could say 'only good for
# didactical reasons'.


def iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


for element in [34, [4, 5], (4, 5), {"a": 4}, "dfsdf", 4.5]:
    print(element, "iterable: ", iterable(element))
