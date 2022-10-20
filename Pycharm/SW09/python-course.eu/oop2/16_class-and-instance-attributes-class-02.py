#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_class_and_instance_attributes.php

# Class and Instance Attributes
# Class Attributes
#
# Instance attributes are owned by the specific instances of a class.
#
# We can also define attributes at the class level. Class attributes
# are attributes which are owned by the class itself. They will be
# shared by all the instances of the class. Therefore they have the
# same value for every instance.
#
# Usually they are placed at the top, right below the class header.


class A:
    a = "I am a class attribute!"

    def __init__(self, name="foo"):
        self.n = name


x = A()
y = A("bar")
x.a = "Hi"          # => instance attribute for x
A.a = "This is changing the class attribute"

print("1)", x.a)
print("2)", y.a)
print("3)", A.a)
