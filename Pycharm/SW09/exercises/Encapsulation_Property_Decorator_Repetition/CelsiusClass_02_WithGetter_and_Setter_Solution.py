#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro
# 2021-10, Erwin Mathis

# CelsiusClass_02_WithGetter_and_Setter_Soltion.py

###############
# Exercise 02 : Read below ...... and follow the considerations (Überlegungen)
###############



# Our programmers heard something about
# a) encapsulation (private variables!) and
# b) and getter- and setter-methods and
# c) also about exception handling ... (will come in future!)
# Voilà: hier the work of our programmers

############
# First partial solution (that still needs to be improved!)
#
# Our programmes define instead of variabel '_temperature'  only 'temperatur'  (but now: not private!!!!)


class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)                  # new on update01

    def to_fahrenheit(self):
        return ("{0:6.2f}".format((self.get_temperature() * 1.8) + 32))


    def get_temperature(self):                             # new on update01
        #return self._temperature                          # => 'Celsius' object has no attribute 'temperature'
        return self.temperature                  #### only a temp. Solution => no encapsulation!!!
    def set_temperature(self, value):                      # new on update01
        if value < -273:
            print("Error: Temperature below -273 is not possible => we set -273!")
            self.temperature = -273
            #raise ValueError("Temperature below -273 is not possible")
        else:
            self.temperature = value             #### only temp. Solution => no encapsulation!!!

def main():
    man = Celsius( 10 )                       # create a name 'man' (often called 'instance'
                                              # or also 'object') which is bound to a Celsius-object

    man.temperature = 37                      # set temperature   => NOT VIA set_temperature(...) !
    print( man.temperature )                  # get temperature   => NOT VIA get_temperature(...) !
                                              # Result: 37
# NEW:
    print(man.__dict__)                       # ...only to show our local Variable-Dictionary!

    print( man.to_fahrenheit() )              # get degrees Fahrenheit
                                              # Result: 98.60 => correct!

    man1 = Celsius( -280 )
    print( man1.temperature )                 # ...hmmm there are no temperatur <-273  !!!
                                               # we should have to correct this 'error'!!!


if __name__ == "__main__":
    main()


############
# output:
# 37
# {'temperature': 37}
#  98.60
# Error: Temperature below -273 is not possible => we set -273!
# -273
