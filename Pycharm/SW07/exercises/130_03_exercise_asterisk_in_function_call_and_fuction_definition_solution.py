#!/usr/bin/env python3

# 130_03_exercise_asterisk_in_function_call_and_fuction_definition_solution.py
# Solution:
# * in function call an d* in function definition (d)
#
# Exercise A)
#    Write a function 'tuple2str(...)' which takes a tuple as parameter
#    and returns this tupel as String without brackets


# Exercise B)
#    Write a function 'tuple2list(...)' which takes a tuple as parameter
#    and returns this tupel as list
#    Don't use build-in function list(...)


# Exercise A: Solution proposal!
def tuple2str(*x):
    mystr = str(x)[1:-1]
    return (mystr)

# Exercise B: Solution proposal!
def tuple2list(*x):
    y = []
    for item in x:
        y.append(item)
    return y


# Exercise A: Test of function def tuple2str(....): proposal!
#             Test with 3 different tuples!
print("############ Test with tuple2str(...) ############")
p0 = (47,11,12,16)                    # tuple of int's
res0 = tuple2str(*p0)
print("res0: ", res0)

p1 = (47,11,"hallo",[3,4,'gut'])      # tuple of different datatyps
res1 = tuple2str(*p1)
print("res1: ",res1)

p2 = ()                                # empty tuple
res2 = tuple2str(*p2)
print("res2: ",res2)


# Exercise B: Test of function def tuple2list(....): proposal!
#             Test with 3 different tuples!
print("############ Test with tuple2list(...) ############ ")
p3 = (47,11,12,16)                     # tuple of int's
res0 = tuple2list(*p3)
print("res0: ", res0)


p4 = (47,11,"hallo",[3,4,'gut'])       # tuple of different datatyps
res1 = tuple2list(*p4)
print("res1: ",res1)

p5 = ()                                # empty tuple
res2 = tuple2list(*p5)
print("res2: ",res2)


#########
# Output:
#########
# ############ Test with tuple2str(...) ############
# res0:  47, 11, 12, 16
# res1:  47, 11, 'hallo', [3, 4, 'gut']
# res2:
# ############ Test with tuple2list(...) ############
# res0:  [47, 11, 12, 16]
# res1:  [47, 11, 'hallo', [3, 4, 'gut']]
# res2:  []









