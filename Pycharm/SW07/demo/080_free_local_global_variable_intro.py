#!/usr/bin/env python3

# 080_free_local_global_variable_intro.py
# examples for free, local and global variables => intro
# insert the correct word on '......'

#################################################################
# Example 1:

x = 1              # x is here a .....
def foo():
   print(x)        # x is here a .....





#################################################################
# Example 2:

x = 1              # x is here a ....
def foo():
   x = 2           # x is here a ....
   print(x)
                   # here we have NO .....


#################################################################
# Example 3:

def bar():
   x = 1           # x is here a .....
   def foo():
      y = 2        # y is here a .....
      print(x)     # x is here a .....
      print(y)
                   # in this code-snippet there is .....