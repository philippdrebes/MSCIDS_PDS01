#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro
# 2021-10, Erwin Mathis

# CelsiusClass_04_WithDecorator.py

###############
# Exercise 04 : Read below ...... and follow the considerations (Überlegungen)
###############

# Our programmes tried to solve the work with a new solution: With 'decorator'!! (see below!)

# BUT now we have a problem:
# We get NO (!!!) error on '-280' ... Why??
# What's wrong => correct it!
# Use
#    a) http://pythontutor.com/visualize.html#mode=edit  or
#    b) the debugger inside PyCharm (that's very good!)
# to detect the error.
#
# Recommendation: Comment out the line 23 and 37 => is everthing clear?

class Celsius:
    def __init__(self, temp=0):
        self._temperature = temp

    def to_fahrenheit(self):
        return ("{0:6.2f}".format((self.temperature * 1.8)+32))

    @property                                             # new on update03
    def temperature(self):                                # new on update03
        #print("Getting value")
        return self._temperature

    @temperature.setter                                   # new on update03
    def temperature(self, value):
        #print("Setting value")
        if value < -273:
            print("Error: Temperature below -273 is not possible => we set -273 ")
            # raise ValueError("Temperature below -273 is not possible")
            self._temperature = value
        else:
            self._temperature = value

                                              # WAU: no property-object now => it's replaced with decorators!


def main():
    man = Celsius( 10 )                       # create a name 'man' (often called 'instance'
                                              # or also 'object') which is bound to a Celsius-object

    man.temperature = 37                      # set temperature
    print( man.temperature )                  # get temperature
                                              # Result: 37
    print( man.to_fahrenheit() )              # get degrees Fahrenheit
                                              # Result: 98.60000000000001

    man1 = Celsius( -280 )                    #  ...hmmm there are no temperatur <-273  !!!
    print( man1.temperature )                 # but now we have a new problem:
                                              # Celsius  -280 should invoke an ValueError ...
                                              # and nothing happens!!!

                                              # What's wrong => correct it!
                                              # use http://pythontutor.com/visualize.html#mode=edit
                                              # to detect the error!

if __name__ == "__main__":
    main()



###########
# output:    (no error-message ... that's the problem!)
# 37
#  98.60
# -280
