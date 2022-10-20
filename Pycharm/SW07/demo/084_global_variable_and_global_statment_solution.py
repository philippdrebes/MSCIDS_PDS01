#!/usr/bin/env python3

# 084_global_variable_and_global_statment_solution.py
# examples for global variable and global statement - Solution

# Solution of the problem in last example with 'global-statement'
# think first... ;-) and complete the notes at the bottom of the text ...


def f():
    global s            # take from here the global variable s!!
    print(s)            # now this print() function knows what to output: global variable 's'
    s = "Perl"          # change the global variable => danger! (PLEASE never do it so!!!)
    print(s)            # print the new value of the global varialbe 's'

s = "Python"            # global variable
f()
print(s)                # we see: the function f() has changed the global variable 's'


#########
# Output:
#########
# Python
# Perl
# Perl

