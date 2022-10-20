#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_class_and_instance_attributes.php

# Class and Instance Attributes
# Static Methods
#
# We can make public (class) attributes private as well.
#
# We want a method, which we can call via the class name or via the instance
# name without the necessity of passing a reference to an instance to it.
#
# The solution consists in static methods, which don't need a reference to an
# instance.


# just a function, outside of any class
def show_factory():
    print(Robot.factory)


class Robot:
    __counter = 0
    factory = "ABB Robotics"

    def __init__(self, name=""):
        self.name = name
        Robot.__counter += 1
        # type(self).__counter += 1

    @staticmethod                     # no self for count_robot_instances()
    def count_robot_instances():
        return Robot.__counter        # accesses a private class attribte

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")


if __name__ == "__main__":
    print(Robot.count_robot_instances())

    x = Robot("Marvin")
    x.say_hi()
    Robot.say_hi(x)
    show_factory()
    print(Robot.factory)

    print(x.count_robot_instances())
    # print(Robot.count_robot_instances(x))

    y = Robot()
    print(y.count_robot_instances())
    print(Robot.count_robot_instances())


# show_factory() kind of ugly
