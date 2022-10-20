#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_properties.php

# Properties

# We have to observe the following issues:
# * Will the value of "our_attribute" be needed by the possible users
#   of our class?
# * If not, we can or should make it a private attribute.
# * If it has to be accessed, we make it accessible as a
#   public attribute
# * We will define it as a private attribute with the
#   corresponding property, if and only if we have to do some
#   checks or transformation of the data.
# * Alternatively, you could use a getter and a setter, but
#   using a property is the Pythonic way to deal with it.


class OurClass:

    def __init__(self, a):
        self.our_attribute = a


x = OurClass(10)
print(x.our_attribute)
