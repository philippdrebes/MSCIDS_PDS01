#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_implementing_a_property_decorator.php
#
# Deeper into Properties
#
# We have a look at the way the "property" decorator could be implemented in
# Python code. By doing this the way of working will be clearer.
#
# We define a class with the name 'our_property' so that it will not be
# mistaken for the existing 'property' class. This class can be used like the
# 'real' property class.
#
# (our_property implements the descriptor protocol)
#


class our_property:
    """ emulation of the property class  for educational purposes """

    def __init__(self, fget=None, fset=None, fdel=None):
        """Attributes of 'our_decorator'
        fget function to be used for getting an attribute value
        fset function to be used for setting an attribute value
        fdel function to be used for deleting an attribute
        """
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel)


# ##################################################
class Robot:

    def __init__(self, city):
        self.city = city

    @our_property
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
