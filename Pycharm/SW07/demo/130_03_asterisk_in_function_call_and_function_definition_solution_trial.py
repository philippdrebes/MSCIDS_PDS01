#!/usr/bin/env python3

# 130_03_asterisk_in_function_call_and_function_definition_solution_trial.py
# * in function call  and * function definition (b) => practice

# Example 03: (function with no return statement!)
#             tuple p has one more element => an error occurs!
# first trial of a solution ...

# the code below doesn't work as expected
# print("f3: *******************************")
# def f3(x,y,z):
#     print(x,y,z)
#
# p = (47,11,12,16 )
# f3(*p)                      # Question ... how can we solve this challenge?


# first solution - trial:
print("f3a: *******************************")
def f3a(x,*y):
    print(x,y)

p = (47,11,12,16 )
f3a(*p)                 # …hmm goal not quite achieved!


# second solution - trial:
print("\nf3b: *******************************")
def f3b(x,*y):
    for item in y:
        x = str(x) + "," + str(item)
    print(x)

p = (47,11,12,16 )
f3b(*p)

# third elegant solution - trial:
print("\nf3c: *******************************")
def f3c(*x):
    print(*x)              # elegant isn't it?

p = (47,11,12,16 )
f3c(*p)

#########
# Output:
#########
# f3a: *******************************
# 47 (11, 12, 16)
#
# f3b: *******************************
# 47,11,12,16
#
# f3c: *******************************
# 47 11 12 16