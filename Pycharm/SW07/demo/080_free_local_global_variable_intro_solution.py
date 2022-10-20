#!/usr/bin/env python3

# 080_free_local_global_variable_intro_solution.py
# examples for free, local and global variables => intro

#################################################################
# Example 1:

x = 1              # x is here a 'global variable'
def foo():
   print(x)        # x is here a 'free variable





#################################################################
# Example 2:

x = 1              # x is here a 'global variable'
def foo():
   x = 2           # x is here a 'local variable'
   print(x)
                   # here we have NO 'free variable'!


#################################################################
# Example 3:

def bar():
   x = 1           # x is here a 'local variable' inside bar()
   def foo():
      y = 2        # y is here a 'local variable' inside foo()
      print(x)     # x is here a 'free variable' (not defined in foo())
      print(y)
                   # in this code-snippet there is NO 'global variable'