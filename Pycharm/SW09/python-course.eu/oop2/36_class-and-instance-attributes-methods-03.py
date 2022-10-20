#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_class_and_instance_attributes.php

# Class and Instance Attributes
# Class Methods vs. Static Methods and Instance Methods
#
# Usefulness of class methods in inheritance
#
# That's the way to go


class Pet:
    _class_info = "pet animals"

    @classmethod
    def about(cls):
        print("This class is about " + cls._class_info + "!")


class Dog(Pet):
    _class_info = "man's best friends"


class Cat(Pet):
    _class_info = "all kinds of cats"


class Fish(Pet):
    pass


if __name__ == "__main__":
    Pet.about()
    Dog.about()
    Cat.about()
    Fish.about()
