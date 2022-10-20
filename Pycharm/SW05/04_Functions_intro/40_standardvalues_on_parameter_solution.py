# 40_standardvalues_on_parameter_solution.py

# Default values for functions
# Functions can have parameters. These parameters can standard values.

# Task: Change the two Example so that the two
# hello(...) calls and the three circumference(...) calls
# run without any error message!
# Solution:

# Example 1: 
def hello(name="Nameless"):
    print("Hello " + name + "!")

hello("Peter")

# without parameters => the standard value is used!
hello()


# Example 2:
def circumference(laenge=2, breite=1):
    return 2 * (laenge + breite)

c1 = circumference(5, 3)
print(c1)

# for the width the standard value "1" is used
c2 = circumference(5)
print(c2)

# Both standard values are now used
c3 = circumference()
print(c3)