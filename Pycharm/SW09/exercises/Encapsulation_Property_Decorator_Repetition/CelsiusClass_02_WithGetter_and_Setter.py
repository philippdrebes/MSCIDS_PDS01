#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro
# 2021-10, Erwin Mathis

# CelsiusClass_02_WithGetter_and_Setter.py

###############
# Exercise 02 : Read below ...... and follow the considerations (Überlegungen)
###############



# Our programmers heard something about
# a) encapsulation (private variables!) and
# b) and getter- and setter-methods and
# c) also about exception handling ... (will come in future!)
# Voilà: hier the work of our programmers




class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)                  # new on update01

    def to_fahrenheit(self):
        return ("{0:6.2f}".format((self.get_temperature() * 1.8) + 32))


    def get_temperature(self):                             # new on update01
        return self._temperature                           # _temperature will give us problems ...!

    def set_temperature(self, value):                      # new on update01
        if value < -273:
            print("Error: Temperature below -273 is not possible")
            #raise ValueError("Temperature below -273 is not possible")
        self._temperature = value                          # _temperature will give us problems ...!

##############
# Problem:
# This main()-method will no longer run ... and also other programs which use the Celsius class
# because we changed the "interface" of our class.
#
# Note: Changing an interface almost always leads to difficulties in programming.
#       In the following examples I want to show you how to avoid these difficulties.
#
##############
# def main():
#     man = Celsius( 10 )                       # create a name 'man' (often called 'instance'
#                                               # or also 'object') which is bound to a Celsius-object
#
#     man.temperature = 37                      # set temperature        # ???? realy ???? use debuger!!!!
#     print( man.temperature )                  # get temperature
#                                               # Result: 50 => _temperature = 10 (10*1.8+32 = 50!!!)
#     print( man.to_fahrenheit() )              # get degrees Fahrenheit
#                                               # Result: 50 instead of 98.60 => wrong!!!!
#
#     man1 = Celsius( -280 )
#     print( man1.temperature )                 # ...hmmm there are no temperatur <-273  !!!
#                                                # we should have to correct this 'error'!!!
#
#
# if __name__ == "__main__":
#     main()

#################
# Ok ... => What's the Problem of this solution with Getter- and Setter-methods ?
#
# Answer: All programs that have been sold in the past do not work anymore!!!!!
#
# For example: You have to change the little program above in this manner:
# uncomment the following code (and comment-out the "wrong" i.e. no longer running code above!)

def main():
    man = Celsius( 10 )                       # create a name 'man' (often called 'instance'
                                              # or also 'object') which is bound to a Celsius-object

    man.set_temperature(37)                   # set temperature
    print( man.get_temperature() )            # get temperature
                                              # Result: 37
    print( man.to_fahrenheit() )              # get degrees Fahrenheit
                                              # Result: 98.60000000000001

    man1 = Celsius( -280 )
    print( man1.get_temperature())           # ...hmmm there are no temperatures <-273  !!!
                                             #  we should have to correct this 'error'!!!


if __name__ == "__main__":
    main()

################
# And now: we have a *** new problem ***:
# We get a message like:
# 'Error: Temperature below -273 is not possible'
# but the program still sets the wrong temperatur ... BAD!

