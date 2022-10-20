#!/usr/bin/env python3

# 081_global_and_free_variable.py
# examples for global and free variables

def f():
    print(s)             # here s is a 'free variable'

s = "Python"             # 'globale' variable s
f()

#########
# Output:
#########
# Python

# We can also access global variables within a function.
