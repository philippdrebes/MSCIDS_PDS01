#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro
# 2021-10, Erwin Mathis

# CelsiusClass_04_WithDecorator_Solution.py

#######################
# Solution Exercise 04 : Read below ...... and follow the considerations (Überlegungen)
#######################

# ... But ... on the end ...

############
# Exercice 05: Program our example with no redundancy!
############

class Celsius:
    def __init__(self, temperat=0):
        if temperat < -273:
            print("Temperature below -273 is not possible => we set -273")
            #raise ValueError("Temperature below -273 is not possible")
            self._temperature = -273
        else:
            self._temperature = temperat

    def to_fahrenheit(self):
        return ("{0:6.2f}".format((self.temperature * 1.8)+32))

    @property                                             # new on update03
    def temperature(self):                                # new on update03
        #print("Getting value")
        return self._temperature

    @temperature.setter                                   # new on update03
    def temperature(self, value):
        if value < -273:
            # print("Setting value")
            print("Temperature below -273 is not possible => we set -273")
            #raise ValueError("Temperature below -273 is not possible")
            self._temperature = -273
        else:
            self._temperature = value


     # WAU: no property-object now!!!    new on update03


def main():
    man = Celsius( 10 )                       # create a name 'man' (often called 'instance'
                                              # or also 'object') which is bound to a Celsius-object

    man.temperature = 37                      # set temperature
    print( man.temperature )                  # get temperature
                                              # Result: 37
    print( man.to_fahrenheit() )              # get degrees Fahrenheit
                                              # Result: 98.60

    man1 = Celsius( -280 )                    #  ...hmmm there are no temperatur <-273  !!!
    print( man1.temperature )                 # but now we have a new problem:
                                              # Celsius  -280 should invoke an ValueError ...
                                              # and nothing happens!!!

                                              # What's wrong? => use the Debugger!!!

if __name__ == "__main__":
    main()

##############
#  Solution:  Celsius  -280  Problem solved!
#  But now we have 2 times the same code!!!

##############
# output
# 37
#  98.60
# Temperature below -273 is not possible => we set -273
# -273
