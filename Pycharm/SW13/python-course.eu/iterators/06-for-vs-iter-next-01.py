#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
# https://www.python-course.eu/python3_iterable_iterator.php
#
# Iterators and Iterables
# Difference Between Iterable and Iterator
#
# So what is going on behind the scenes, when a for loop is executed?
#
# The for statement calls iter() on the object which it is supposed to loop
# over. If this call is successful, the iter call will return an iterator
# object that defines the method __next__() which accesses elements of the
# object one at a time.
# The __next__() method will raise a StopIteration
# exception, if there are no further elements available. The for loop whill
# terminate as soon as it catches a StopIteration exception


cities = ["Berlin", "Vienna", "Zurich"]

for city in cities:
    print(city)


iterator_obj = iter(cities)
print(type(iterator_obj))

while iterator_obj:
    try:
        city = next(iterator_obj)
        print(city)
    except StopIteration:
        break

print("done")
