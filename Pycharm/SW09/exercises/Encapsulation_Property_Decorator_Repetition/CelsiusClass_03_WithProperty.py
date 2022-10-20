#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro
# 2021-10, Erwin Mathis

# CelsiusClass_03_WithProperty.py

###############
# Exercise 03 : Read below ...... and follow the considerations (Überlegungen)
###############



# Our programmes try to solve the work with a new solution: With 'property'!!
# ... and  with a "private variable": _temperature           => that's new!!!

# comment out the line 27 and 31 => is everthing clear?
# Please check the output with the debugger!!!

class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return ("{0:6.2f}".format((self.temperature * 1.8)+32))

    def get_temperature(self):
        # print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        # print("Setting value")
        if value < -273:
            print("Error: Temperature below -273 is not possible => we set -273 ")
            #raise ValueError("Temperature below -273 is not possible")
            self._temperature = -273
        else:
            self._temperature = value

    temperature = property( get_temperature, set_temperature )               # new on update02

def main():
    man = Celsius( 10 )                       # create a name 'man' (often called 'instance'
                                              # or also 'object') which is bound to a Celsius-object

    man.temperature = 37                      # set temperature
    print( man.temperature )                  # get temperature
                                              # Result: 37
# NEW:
    print( man.__dict__ )                     # ...only to show our local Variable-Dictionary!
                                              # its '_temperature' NOT 'temperature'

    print( man.to_fahrenheit() )              # get degrees Fahrenheit
                                              # Result: 98.60000000000001

    man1 = Celsius( -280 )
    print( man1.temperature )                 # ...no temperatur <-273  !!!
                                              # solved!!!

# NEW:
    print( man1.__dict__ )                     # ...only to show our local Variable-Dictionary!

if __name__ == "__main__":
    main()



###################
# output
# 37
# {'_temperature': 37}
#  98.60
# Error: Temperature below -273 is not possible => we set -273
# -273
# {'_temperature': -273}
