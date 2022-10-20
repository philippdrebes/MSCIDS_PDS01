#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_iterable_iterator.php
#
# Iterators and Iterables
# Classes with Iterable Instances
#
# If you want to add an iterator behavior to your class, you have to add the
# __iter__ and the __next__ method to your class.
#
# The __iter__ method returns an iterator object. If the class contains a
# __next__, it is enough for the __iter__ method to return self, i.e. a
# reference to itself:


class Reverse:
    """
    Creates Iterators for looping over a sequence backwards.
    """

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


lst = [34, 978, 42]
lst_backwards = Reverse(lst)
for el in lst_backwards:
    print(el)

print("~" * 10)

# also possible
lst.reverse()
for el in lst:
    print(el)
