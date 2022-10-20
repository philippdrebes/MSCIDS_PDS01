#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_implementing_a_property_decorator.php
#
# Deeper into Properties
# up to now:


class Robot:

    def __init__(self, city):
        self.city = city

    @property
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
