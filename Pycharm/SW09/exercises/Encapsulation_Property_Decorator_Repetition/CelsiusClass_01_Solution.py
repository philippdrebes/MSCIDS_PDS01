#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro
# 2021-10, Erwin Mathis

# CelsiusClass_01_Solution.py

# Adoption: We have following "business use case":
# The class Celsius below is ok! ... and many often sold!
# We have a new  requirement for this class in 'CelsiusClass_02_WithGetter_and_Setter.py'
# ... an we will run in a "Interface-Problem" !!!

# A little first problem we can solve easly:
# We dont't want the output:
# 37
# 98.60000000000001        => Format this output! => maximum 3 digits before the comma and 2 digits after the comma
# -280

###############
# Exercise 01 : Maximum 3 digits before the comma and 2 digits after the comma
###############

# A possible solution ... ;-) !!!

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature


    def to_fahrenheit(self):
        return ("{0:6.2f}".format(    (self.temperature * 1.8)+32))     # Solution
        #return ("({0:6.2f},{1:8d})".format(((self.temperature * 1.8)+32),999))     # Solution

def main():
    man = Celsius(10)             # create a name 'man' (often called 'instance'
                                  # or also 'object') which is bound to a Celsius-object

    man.temperature = 37          # set temperature
    print(man.temperature)        # get temperature
                                  # Result: 37
    print(man.to_fahrenheit())    # get degrees Fahrenheit
                                  # Result: 98.60000000000001

    man1 = Celsius(-280)
    print(man1.temperature)       # Result: -280
                                  # ...hmmm there are no temperatur <-273  !!!
                                  # we should have to correct this 'error'!!!


if __name__ == "__main__":
    main()


#############
# output:
# 37
#  98.60
# -280
