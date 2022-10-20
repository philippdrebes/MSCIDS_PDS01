#!/usr/bin/env python3

# 140_01_arbitrary_keyword_parameter.py
# Arbitrary Keyword Parameters  with **
# There is also a mechanism for defining any number of keyword parameters
# in a function definition.
# To make this possible, a double asterisk "**" was introduced as a notation ...
# (for function definitions and for function calls!)


# a simple function definition to show the use of '**'
def f(**args):            # ** args means: any number of keyword parameters as dictionary
    print(args)           # very simple command => print out all keyword parameters

# Example 01:
# a simple function call of function f() => with NO arguments!
print("Example 01: f()  *******************************")
f()

# Example 02:
# a function call of function f(...) with three keyword parameter
print("\nExample 02: f(de='German',en='English',fr='French') ************")
f(de="German",en="English",fr="French")



# Example 03:
# define a dictionary 'd' and pass this variable as an argument
# here you see the first time the asterisk
print("\nExample 03: f(d) **********************")
d = {"Köln": "CGN", "Budapest": "BUD", "Saigon": "SGN"}

f(**d)                   # **d means: d has to be a dictionary


# only as a deepening for dictionaries
# print(d.values())
# print(list(d.values()))
# print(d.keys())
# print(list(d.keys()))
# print(sorted(list(d.values())))   # sort all values in a list



#########
# Output:
#########
# Example 01: f()  *******************************
# {}
#
# Example 02: f(de='German',en='English',fr='French') ************
# {'de': 'German', 'en': 'English', 'fr': 'French'}
#
# Example 03: f(d) **********************
# {'Köln': 'CGN', 'Budapest': 'BUD', 'Saigon': 'SGN'}