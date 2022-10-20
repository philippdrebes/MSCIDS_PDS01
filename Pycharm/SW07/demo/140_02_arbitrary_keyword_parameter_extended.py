#!/usr/bin/env python3

# 140_02_arbitrary_keyword_parameter_extended.py
# Arbitrary Keyword Parameters  with **  (extended)
# There is also a mechanism for defining any number of keyword parameters
# in a function definition.

# function definition of 'simple' function:
def f(a,b,x,y):
    print(a,b,x,y)

# function definition of function with aritrary keyword parameter '**X':
def f2(**x):
    print(x)
    print(x.keys())
    print(*x)
    print(*x.values())



# Example 04:
# a simple function call of function f(a,b,c,d) => with 4 parameter
print("Example 04: f(**d1) *******************************")
d1 = {'a':'append', 'b':'block','x':'extract','y':'yes'}
f(**d1)


# Example 05:
# a simple function call of function f(a,b,c,d) => with 4 parameter
print("\nExample 05: f(**d2) *******************************")
d2 = {'a':'append', 'b':'block','x':'extract','y':'yes','n':'no'}
f2(**d2)




# a complex function call of function foo(fix, *args, **kwargs) => with 3 different parametertype
# fix:                              one parameter is 'fix' => 42
# variable number of parameter:     (89, 12)
# keyword parameter:                {'x': 17, 'y': 'Hallo', 'z': [3, 8, 9]}
def foo(fix, *args, **kwargs):
    print("fix:", fix)
    print("args: ", args)
    print("kwargs: ", kwargs)
    print("*args: ", *args)
    print("*kwargs: ", *kwargs)
    print("*kwargs.values(): ",*kwargs.values() )


# Example 06:
# a complex function call of foo(fix, *args, **kwargs) => with 6 parameter
print("\nExample 05: foo(...) *******************************")
foo( 42, 89, 12, x=17, y="Hallo", z=[3, 8, 9] )



#########
# Output:
#########
# Example 04: f(**d1) *******************************
# append block extract yes
#
# Example 05: f(**d2) *******************************
# {'a': 'append', 'b': 'block', 'x': 'extract', 'y': 'yes', 'n': 'no'}
# dict_keys(['a', 'b', 'x', 'y', 'n'])
# a b x y n
# append block extract yes no
#
# Example 05: foo(...) *******************************
# fix: 42
# args:  (89, 12)
# kwargs:  {'x': 17, 'y': 'Hallo', 'z': [3, 8, 9]}
# *args:  89 12
# *kwargs:  x y z
# *kwargs.values():  17 Hallo [3, 8, 9]