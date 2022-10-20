#!/usr/bin/env python3

# 130_01_asterisk_in_function_call_and_function_definition.py
# * in function call  and * function definition (b) => practice
# A few examples at a glance:


# Example 01: (function with no return statement!)
print("f1: *******************************")
def f1(x,y,z):
    print(x,y,z)       # no return statement!

p = (47,11,12)
f1(*p)
f1(p[0],p[1],p[2])   # does exactly the same thing! ... but much more complicated!
                       # and you have to know how many elements are in the tuple!!!

# Example 02: (function with a return statement!)
print("f2: *******************************")
def f2(*args):
    # print("type(args), args: ", type(args), args)
    return args        # returns an tuple

res01 = f2(3,4,5,6)
print("type(res01), res01 :", type(res01), res01 )

lst1 = [4, 6, 12, 22,45]
res02 = f2(*lst1)
print("type(res02),res02: ", type(res02),res02)



#########
# Output:
#########
# f1: *******************************
# 47 11 12
# 47 11 12
# f2: *******************************
# type(res01), res01 : <class 'tuple'> (3, 4, 5, 6)
# type(res02),res02:  <class 'tuple'> (4, 6, 12, 22, 45)