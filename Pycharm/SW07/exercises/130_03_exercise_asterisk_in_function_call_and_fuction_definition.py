#!/usr/bin/env python3

# 130_03_exercise_asterisk_in_function_call_and_fuction_definition.py
# Exercises:
# * in function call an d* in function definition (d)
#
# Exercise A)
#    Write a function 'tuple2str(...)' which takes a tuple as parameter
#    and returns this tupel as String without brackets


# Exercise B)
#    Write a function 'tuple2list(...)' which takes a tuple as parameter
#    and returns this tupel as list
#    Don't use build-in function list(...)


# Exercise A: to do!
def tuple2str( ):

    return

# Exercise B: to do!
def tuple2list(  ):

    return


# Exercise A: Test of function def tuple2str(....):
#             Test with 3 different tuples!
print("############ Test with tuple2str(...) ############")
p0 = (47,11,12,16)                    # tuple of int's
# res0 = tuple2str(....)              # replace '....'
# print("res0: ", res0)

p1 = (47,11,"hallo",[3,4,'gut'])      # tuple of different datatyps
# res1 = tuple2str(....)              # replace '....'
# print("res1: ",res1)

p2 = ()                               # empty tuple
# res2 = tuple2str(....)              # replace '....'
# print("res2: ",res2)


# Exercise B: Test of function def tuple2list(....):
#             Test with 3 different tuples!
print("############ Test with tuple2list(...) ############ ")
p3 = (47,11,12,16)                     # tuple of int's
# res0 = tuple2list(....)              # replace '....'
# print("res0: ", res0)


p4 = (47,11,"hallo",[3,4,'gut'])       # tuple of different datatyps
# res1 = tuple2list(....)              # replace '....'
# print("res1: ",res1)

p5 = ()                                # empty tuple
# res2 = tuple2list(....)              # replace '....'
# print("res2: ",res2)


#########
# exected Output:
#########

# ############ Test with tuple2str(...) ############
# res0:  47, 11, 12, 16
# res1:  47, 11, 'hallo', [3, 4, 'gut']
# res2:
# ############ Test with tuple2list(...) ############
# res0:  [47, 11, 12, 16]
# res1:  [47, 11, 'hallo', [3, 4, 'gut']]
# res2:  []
