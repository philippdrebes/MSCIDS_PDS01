#!/usr/bin/env python3

# 120_01_variable_length_of_parameter.py
# Variable Length of Parameters (b)
# two example: a) no parameter b) three parameter


def variableParameterFunc(*x):
    print("'x' in function:", x)

res1 = variableParameterFunc()                # no argument
print("res1:", res1)


res2 = variableParameterFunc(34, "Do you like Python?", "Of course")   # 3 arguments
print("res2:", res2)

#########
# Output:
#########
# 'x' in function: ()
# res1: None
# 'x' in function: (34, 'Do you like Python?', 'Of course')
# res2: None
