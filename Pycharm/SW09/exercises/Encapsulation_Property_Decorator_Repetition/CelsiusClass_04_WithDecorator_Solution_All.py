#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro
# 2021-10, Erwin Mathis

# CelsiusClass_04_WithDecorator_Solution_All.py

#######################
# Solution Exercise 05 : Read below ...... and follow the considerations (Überlegungen)
#######################

# => we don't have now any redundancy!
# now the program will raise an error on line 20

class Celsius:
    def __init__(self, temperature = 0):
        self.if_stat(temperature)

    def if_stat(self, temperature = 0):
        if temperature < -273:
            print("Temperature below -273 is not possible => we set -273")  # if you want: try the next line instead!
            # raise ValueError("Temperature below -273 is not possible")
            self._temperature = temperature
        else:
            self._temperature = temperature

    def to_fahrenheit(self):
        return ("{0:6.2f}".format((self.temperature * 1.8)+32))

    @property
    def temperature(self):
        #print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        #print("Setting value")
        self.if_stat(value)
                                                          #


def main():
    man = Celsius( 10 )                       # create a name 'man' (often called 'instance'
                                              # or also 'object') which is bound to a Celsius-object

    man.temperature = 37                      # set temperature
    print( man.temperature )                  # get temperature
                                              # Result: 37
    print( man.to_fahrenheit() )              # get degrees Fahrenheit
                                              # Result: 98.60000000000001

    man1 = Celsius( -280 )                    # hier we will raise an error ... or we set the value on -273
    print( man1.temperature )                 # never reached, because an error occurs before


if __name__ == "__main__":
    main()

#############
# Solution:
#  Celsius  -280  Problem solved!
#  and we don't have 2 times the same code!!!   Solved!!!


#############
# output
# 37
#  98.60
# Temperature below -273 is not possible => we set -273
# -280
