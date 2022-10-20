#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_class_and_instance_attributes.php

# Class and Instance Attributes
# Class Methods vs. Static Methods and Instance Methods
#
# Usefulness of class methods in inheritance


class Pet:
    _class_info = "pet animals"

    @staticmethod
    def about():
        print("This class is about " + Pet._class_info + "!")


class Dog(Pet):
    _class_info = "man's best friends"


class Cat(Pet):
    _class_info = "all kinds of cats"


if __name__ == "__main__":
    Pet.about()
    Dog.about()
    Cat.about()

# This means that we have no way of differenciating between the class Pet and
# its subclasses Dog and Cat.
