#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_iterable_iterator.php
#
# Iterators and Iterables
#
# We have seen that we can loop or iterate over various Python objects like
# lists, tuples and strings for example.
#

# iterations
for city in ["Berlin", "Vienna", "Zurich"]:
    print(city)

for city in ("Python", "Perl", "Ruby"):
    print(city)

for char in "Iteration is easy":
    print(char)


# If you call the function sum, - e.g. on a list of integer values, - you do
# iteration as well.
print(sum(range(11)))
