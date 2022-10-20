#!/usr/bin/env python3

# 090_parameter_passing_immutable_argument.py
# parameter passing with immutable argument
# => no side effekt!!

def ref_demo(x):                            # x is a parameter
    print( "id( x ), x:", id( x ), ", ", x )
    x=42
    print( "id( x ), x:", id( x ), ", ", x )

x = 9
print("id( x ), x:",id( x ),", ", x)        # x is an argumernt => immutable!!!

ref_demo( x )
print("id( x ), x:",id( x ),", ", x)

#########
# Output:
#########
# id( x ), x: 140715921905568 ,  9
# id( x ), x: 140715921905568 ,  9
# id( x ), x: 140715921906624 ,  42
# id( x ), x: 140715921905568 ,  9