#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_class_and_instance_attributes.php

# Class and Instance Attributes
# Class Methods
#
# Static methods shouldn't be confused with class methods.
#
# Like static methods class methods are not bound to instances, but unlike
# static methods class methods are bound to a class. The first parameter of a
# class method is a reference to a class, i.e. a class object. They can be
# called via an instance or the class name.


class Robot:
    __counter = 0
    _factory = "ABB Robotics"

    def __init__(self, name=""):
        self.name = name
        type(self).__counter += 1

    @classmethod                         # cls: not a reference to an instance
    def count_robot_instances(cls):      # but to the class object
        # return cls, Robot.__counter
        return cls.__counter             # accesses a private class attribte

    @classmethod
    def get_factory(cls):
        return cls._factory

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")


if __name__ == "__main__":
    print("1)", Robot.count_robot_instances())

    x = Robot("Marvin")
    x.say_hi()
    Robot.say_hi(x)

    print("2)", x.count_robot_instances())

    print("3)", Robot._factory)
    print("4)", Robot.get_factory())
    print("5)", x.get_factory())       # => class name not needed

    y = Robot()
    print("6)", y.count_robot_instances())
    print("7)", Robot.count_robot_instances())
