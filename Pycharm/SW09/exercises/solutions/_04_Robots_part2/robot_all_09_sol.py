#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro
# https://www.python-course.eu/python3_object_oriented_programming.php

# https://docs.python.org/3/library/random.html

# robot_all_09_sol.py


import random


def xstr(s):
    return '' if not s else str(s)


class Robot():

    def __init__(self,
                 name="John Doe",
                 build_year=None):
        self.name = name
        self.build_year = build_year
        self.health_level = random.random()

    def __repr__(self):
        return("Robot(\"" + self.name +
               "\"," + xstr(self.build_year) + ")")

    def __str__(self):
        return "Name: " + self.name + ", Build Year: " + xstr(self.build_year)

    def __del__(self):
        print(self.name + " says bye-bye!")

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
        if self.build_year:
            print("I was built in " + str(self.build_year))
        else:
            print("It's not known, when I was created!")

    def needs_a_doctor(self):
        if self.health_level < 0.8:
            return True
        else:
            return False


class PhysicianRobot(Robot):

    def say_hi(self):
        super().say_hi()
        print("and I am a physician!")

    def heal(self, robo):
        robo.health_level = random.uniform(robo.health_level, 1)
        print(robo.name + " has been healed by " + self.name + "!")


def my_main():
    henry = Robot( "Henry", 2008 )
    y = Robot()
    print( henry )
    print( y )
    print( "Deleting y" )
    del y
    doc = PhysicianRobot( "Dr. Frankenstein" )
    doc.say_hi()
    if henry.needs_a_doctor():
        doc.heal( henry )


if __name__ == "__main__":
    my_main()


#####################
# output:
# Name: Henry, Build Year: 2008
# Name: John Doe, Build Year:
# Deleting y
# John Doe says bye-bye!
# Hi, I am Dr. Frankenstein
# It's not known, when I was created!
# and I am a physician!
# Henry has been healed by Dr. Frankenstein!
# Henry says bye-bye!
# Dr. Frankenstein says bye-bye!
