#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro
# 2021-10, Erwin Mathis

# robo_repair_01.py

class Robot:

    def __init__(self, name):
        self.name = name
        self._broken = False

    def say_hi(self):
        print("Hi, I am " + self.name)
        if self._broken:
            print("I'm damaged")
        else:
            print("I'm OK")

    def damage(self):
        self._broken = True


class RepairRobot:

    def fix(self):
        pass

############################
# Task to do:
#
# The following code has to run without any error!!!
# First you have to uncomment all lines!
# After the uncommenting no change is allowed in this
# script-code below.
# *** RULE ***:  All changes you have to make in the classes above!!!

robi = Robot("Robi")
# mechi = RepairRobot("Mechi")       # uncomment this line!
robi.damage()

robi.say_hi()
# mechi.say_hi()                     # uncomment this line!

print("~" * 20)
# mechi.fix(robi)                    # uncomment this line!
# robi.say_hi()                      # uncomment this line!



##################################################
# Goal is following output in a my_main() method!
#
# My name is Robi. Sorry, I am out of 'order' now!
#
# Hi, I am Robi
# I'm damaged
#
# Hi, I am Mechi
# I'm OK
# I (Mechi) repair things
# ~~~~~~~~~~~~~~~~~~~~
# Mechi has repaired Robi!!
#
# Hi, I am Robi
# I'm OK
