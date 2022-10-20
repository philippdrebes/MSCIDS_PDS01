#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
# https://www.python-course.eu/python3_iterable_iterator.php
#
# Iterators and Iterables
# Difference Between Iterable and Iterator
#
# So what is the difference between an iterable and an iterator?
#
# You can iterate with a for loop over iterators and iterables. Every iterator
# is also an iterable, but not every iterable is an iterator.
#
# A list is iterable but a list is not an iterator.
# An iterator can be created from an iterable by using the function 'iter'.
#
# Iterators are objects with a '__next__' method, which will be used when the
# function 'next' is called.
#

# collections
list1 = list(range(10))
range1 = range(10)

# an iterator
map_iterator1 = map(lambda i: i**2, range(10))

print("~" * 10)

# all of the above are iterable
print("\n1) ")
for j in list1:
    print(j, end=";")

print("\n2) ")
for j in range1:
    print(j, end=";")

print("\n3) ")
for j in map_iterator1:
    print(j, end=";")


print("~" * 10)
print("\n4) ")
print(list(list1))
print(list(range1))
print(list(map_iterator1))
# map_iterator1 is "consumed" => empty


print("~" * 10)
print("\n5) ")

# map_iterator1 is an iterator => next is available
map_iterator1 = map(lambda i: i**2, range(10))
try:
    while True:
        j = next(map_iterator1)
        print(j, end=";")
        # a = 1 / 0
except StopIteration:
    pass

print("")

# this is (totally) OK - and preferred
map_iterator1 = map(lambda i: i**2, range(10))
for j in map_iterator1:
    print(j, end=";")


print("~" * 10)
print("\n6) ")
# an iterable does have __iter__
# an iterator does have __iter__and __next__

print("\nlist1: ", dir(list1))
print("\nrange1: ", dir(range1))
print("\nmap_iterator1: ", dir(map_iterator1))
# j = next(range1)
