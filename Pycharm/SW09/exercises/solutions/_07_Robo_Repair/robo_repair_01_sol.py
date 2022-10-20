#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro

# robo_repair_01_sol.py

class Robot:

    def __init__(self, name):
        self.name = name
        self._broken = False

    def say_hi(self):
        print("\nHi, I am " + self.name)
        if self._broken:
            print("I'm damaged")
        else:
            print("I'm OK")

    def damage(self):
        print("My name is "+ self.name + ". Sorry, I am out of 'order' now!")
        self._broken = True


class RepairRobot(Robot):

    def say_hi(self):
        super().say_hi()
        print("I ("+ self.name+") repair things")

    def fix(self, robo):
        print(self.name + " has repaired " + robo.name + "!!")
        robo._broken = False

def my_main():
    robi = Robot("Robi")
    mechi = RepairRobot("Mechi")
    robi.damage()

    robi.say_hi()
    mechi.say_hi()
    print("~" * 20)

    mechi.fix(robi)
    robi.say_hi()

if __name__ == "__main__":
    my_main()


######################
# output:
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
