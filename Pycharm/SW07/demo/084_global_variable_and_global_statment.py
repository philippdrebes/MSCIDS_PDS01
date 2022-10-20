#!/usr/bin/env python3

# 084_global_variable_and_global_statment.py
# examples for global variable and global statement

# Solution of the problem in last example with 'global-statement'
# think first... ;-) and complete the notes at the bottom of the text ...


def f():
    global s            # take from here the global variable s!!
    print(s)            # now this print() function knows what to output
    s = "Perl"          # .... (you complete)
    print(s)            # .... (you complete)

s = "Python"            # global variable
f()
print(s)


#########
# Output:
#########
# .... (you complete)
# .... (you complete)
# .... (you complete)

