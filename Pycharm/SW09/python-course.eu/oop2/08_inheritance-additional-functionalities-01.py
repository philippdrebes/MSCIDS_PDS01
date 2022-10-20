#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_inheritance.php

# Overriding

# A subclass often needs additional methods with additional
# functionalities, which do not exist in the superclass

# https://docs.python.org/3/library/random.html
# https://docs.python.org/3/library/random.html#random.random
# https://docs.python.org/3/library/random.html#random.uniform

import random


class Robot:

    def __init__(self, name):
        self.name = name
        self.health_level = random.random()

    def say_hi(self):
        print("Hi, I am " + self.name)

    def needs_a_doctor(self):
        if self.health_level < 0.8:
            return True
        else:
            return False


class PhysicianRobot(Robot):

    def say_hi(self):
        print("Everything will be okay! ")
        print(self.name + " takes care of you!")

    def heal(self, robo):
        robo.health_level = random.uniform(robo.health_level, 1)
        print(robo.name + " has been healed by " + self.name + "!")


doc = PhysicianRobot("Dr. Frankenstein")

rob_list = []
for i in range(2):
    x = Robot("Marvin_" + str(i))
    if x.needs_a_doctor():
        print("health_level of " + x.name +
              " before healing: ", x.health_level)
        doc.heal(x)
        print("health_level of " + x.name +
              " after healing: ", x.health_level)
    rob_list.append((x.name, x.health_level))

print(rob_list)
