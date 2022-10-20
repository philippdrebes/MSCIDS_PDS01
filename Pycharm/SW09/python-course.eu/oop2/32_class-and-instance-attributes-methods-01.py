#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_class_and_instance_attributes.php

# Class and Instance Attributes
# Class Methods vs. Static Methods and Instance Methods
#
# Usefulness of class methods in inheritance


class Pet:
    _class_info = "pet animals"

    def about(self):
        print("This class is about " + self._class_info + "!")


class Dog(Pet):
    _class_info = "man's best friends"


class Cat(Pet):
    _class_info = "all kinds of cats"


if __name__ == "__main__":
    p = Pet()
    p.about()
    d = Dog()
    d.about()
    c = Cat()
    c.about()

# awful design
#
# We had to create instances of the Pet, Dog and Cat classes to be able to ask
# what the class is about
