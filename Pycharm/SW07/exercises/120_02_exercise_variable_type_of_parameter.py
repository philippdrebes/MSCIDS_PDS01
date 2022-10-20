#!/usr/bin/env python3

# 120_02_exercise_variable_type_of_parameter.py
# Exercise
# Variable type of Parameters (no, object, list, tuple)
# follow the code an try to finde out how it works!!!
# advanced considerations   => self study!!

def variableParameterFunc(*x):         # 0,1 or n parameter possible!
    print("type(x):", type(x))
    print("'x': in function:", x)


def oneParameterFunc(y):               # only one parameter possible
    print("type(y):", type(y))
    print("'y': in function:", y)
    y = y * 2
    print("'y': in function:", y)


res1 = variableParameterFunc()         # no argument
print("res1:", res1)
print("*"* 40, "\n")

res2 = variableParameterFunc(34, "Do you like Python?", "Of course")    # tree arguments
print("res2:", res2)
print("*"* 40, "\n")

res3 = variableParameterFunc([4,5,6],["hi",3, 5.4])    # two arguments (lists!)
print("res3:", res3)
print("*"* 40, "\n")

i = 4;
print("main - i:", i)
res4 = oneParameterFunc( i )            # one argument: an object  (an 'int'!)
print("res4:", res4)
print("main - i:", i)
print("*"* 40, "\n")

# a list as argument
mylist = [34, "Do you like Python?", "Of course"]
print("main - mylist:", mylist)         # one argument: a list
res5 = oneParameterFunc( mylist )
print("res5:", res5)
print("main - mylist:", mylist)
print("*"* 40, "\n")

# a tuple as argument
mytuple = ([4,5,6],["hi",3, 5.4])       # one argument: a tuple (of list)
print("main - mytuple:", mytuple)
res6 = oneParameterFunc( mytuple )
print("res6:", res6)
print("main - mytuple:", mytuple)
print("*"* 40, "\n")

#########
# Output:
#########
# type(x): <class 'tuple'>
# 'x': in function: ()
# res1: None
# ****************************************
#
# type(x): <class 'tuple'>
# 'x': in function: (34, 'Do you like Python?', 'Of course')
# res2: None
# ****************************************
#
# type(x): <class 'tuple'>
# 'x': in function: ([4, 5, 6], ['hi', 3, 5.4])
# res3: None
# ****************************************
#
# main - i: 4
# type(y): <class 'int'>
# 'y': in function: 4
# 'y': in function: 8
# res4: None
# main - i: 4
# ****************************************
#
# main - mylist: [34, 'Do you like Python?', 'Of course']
# type(y): <class 'list'>
# 'y': in function: [34, 'Do you like Python?', 'Of course']
# 'y': in function: [34, 'Do you like Python?', 'Of course', 34, 'Do you like Python?', 'Of course']
# res5: None
# main - mylist: [34, 'Do you like Python?', 'Of course']
# ****************************************
#
# main - mytuple: ([4, 5, 6], ['hi', 3, 5.4])
# type(y): <class 'tuple'>
# 'y': in function: ([4, 5, 6], ['hi', 3, 5.4])
# 'y': in function: ([4, 5, 6], ['hi', 3, 5.4], [4, 5, 6], ['hi', 3, 5.4])
# res6: None
# main - mytuple: ([4, 5, 6], ['hi', 3, 5.4])
# ****************************************