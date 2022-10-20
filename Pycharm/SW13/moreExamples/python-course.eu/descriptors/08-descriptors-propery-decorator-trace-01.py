#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_implementing_a_property_decorator.php
#
# Deeper into Properties
#
# We have a look at the way the "property" decorator could be implemented in
# Python code. By doing this the way of working will be clearer.
#
# Let's make our property implementation a little bit more talkative with some
# print functions to see what is going on.
#
# (our_property implements the descriptor protocol)
#


class chatty_property:
    """ emulation of the property class for educational purposes """

    def __init__(self, fget=None, fset=None, fdel=None):

        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        print("\n__init__ called with:")
        print(f"fget={fget}, fset={fset}, fdel={fdel}")

    def __get__(self, obj, objtype=None):
        print("\n__get__ called with:)")
        print(f"obj={obj}")
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        print("\n__set__ called with:")
        print(f"obj={obj}, value={value}")
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        print("\ngetter called with:)")
        print(f"fget={fget}")
        print(type(self))
        return type(self)(fget, self.fset, self.fdel)

    def setter(self, fset):
        print("\nsetter called with:)")
        print(f"fset={fset}")
        print(type(self))
        return type(self)(self.fget, fset, self.fdel)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel)


# ##################################################
class Robot:

    def __init__(self, city):
        self.city = city

    @chatty_property
    def city(self):
        print("The Property 'city' will be returned now:")
        return self.__city

    @city.setter
    def city(self, city):
        print("'city' will be set")
        self.__city = city


r1 = Robot("Bern")
print(r1.city)

r1.city = "Luzern"
print(r1.city)

type(Robot.city)
