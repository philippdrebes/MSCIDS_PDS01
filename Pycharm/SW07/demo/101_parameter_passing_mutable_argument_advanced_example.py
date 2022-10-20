#!/usr/bin/env python3

# 101_parameter_passing_mutable_argument_advanced_example.py
# parameter passing with mutable argument
# advanced considerations   => self study!!

def f(x):
    y = x                       # to save and possibly change later ...
    print( "x: / type(x) / object-id(x): ", x, "/", type( x ), "/", id( x ) )
    print( "y: / type(y) / object-id(y): ", y, "/", type( y ), "/", id( y ) )

    # print("*" * 40 )
    # x.append( "Wau!!" )
    # print(x)
    # x = x.append("Wau!!")              # ... what is happening here ??? None - values ?? !!
    # print(x)                           # append(...) has no return-value => x = None!!!
    # x = ["Hello", "World", "!!!"]      # here I create a NEW variable x !!!
    # x = x + ["!!!"]                    # extend list 'x'
    # print(x)

    # print("*" * 40 )
    # # 2 more examples: try to understand these and before running
    # # ... and say what comes out!
    # # Example Extended 1:
    # print( "len(x):", len( x ) )
    # x_list1 = []
    # for item in x:
    #     x_list1.extend( item )
    # print( "x_list1:", x_list1 )
    #

    # # Example Extended 2:
    # x_list2 = []
    # for i in range( 0, len( x ) ):
    #     #x_list2.extend( x[i] )
    #     x_list2.append( x[i] )
    # print( "x_list2:", x_list2 )

    print("*" * 40 )
    print( "x: / type(x) / object-id(x): ", x, "/", type( x ), "/", id( x ) )
    print( "y: / type(y) / object-id(y): ", y, "/", type( y ), "/", id( y ) )

    x = 5
    print( "x: / type(x) / object-id(x): ", x, "/", type( x ), "/", id( x ) )
    print( "y: / type(y) / object-id(y): ", y, "/", type( y ), "/", id( y ) )


l = ["Hello", "l-World"]                      # l ist list => mutable!
print( "Parameter mutable (list) => ['Hello', 'l-World']" )
print( "Outside function l: / type(l) / object-id(l): ", l, "/", type( l ), "/", id( l ) )
f( l )
print( "Outside function", "*" * 20 )
print( "Outside function l: / type(l) / object-id(l): ", l, "/", type( l ), "/", id( l ) )

print( "New example", "*" * 40 )

x = ["Hello", "x-World"]  # l ist list => mutable!
print( "Parameter mutable (list) => ['Hello', 'x-World']" )
print( "Outside function x: / type(x) / object-id(x): ", x, "/", type( x ), "/", id( x ) )
f( x )
print( "Outside function", "*" * 20 )
print( "Outside function x: / type(x) / object-id(x): ", x, "/", type( x ), "/", id( x ) )

#########
# Output:
#########
# Parameter mutable (list) => ['Hello', 'l-World']
# Outside function l: / type(l) / object-id(l):  ['Hello', 'l-World'] / <class 'list'> / 2107386120704
# x: / type(x) / object-id(x):  ['Hello', 'l-World'] / <class 'list'> / 2107386120704
# y: / type(y) / object-id(y):  ['Hello', 'l-World'] / <class 'list'> / 2107386120704
# ****************************************
# x: / type(x) / object-id(x):  ['Hello', 'l-World'] / <class 'list'> / 2107386120704
# y: / type(y) / object-id(y):  ['Hello', 'l-World'] / <class 'list'> / 2107386120704
# x: / type(x) / object-id(x):  5 / <class 'int'> / 140715921905440
# y: / type(y) / object-id(y):  ['Hello', 'l-World'] / <class 'list'> / 2107386120704
# Outside function ********************
# Outside function l: / type(l) / object-id(l):  ['Hello', 'l-World'] / <class 'list'> / 2107386120704
# New example ****************************************
# Parameter mutable (list) => ['Hello', 'x-World']
# Outside function x: / type(x) / object-id(x):  ['Hello', 'x-World'] / <class 'list'> / 2107386121472
# x: / type(x) / object-id(x):  ['Hello', 'x-World'] / <class 'list'> / 2107386121472
# y: / type(y) / object-id(y):  ['Hello', 'x-World'] / <class 'list'> / 2107386121472
# ****************************************
# x: / type(x) / object-id(x):  ['Hello', 'x-World'] / <class 'list'> / 2107386121472
# y: / type(y) / object-id(y):  ['Hello', 'x-World'] / <class 'list'> / 2107386121472
# x: / type(x) / object-id(x):  5 / <class 'int'> / 140715921905440
# y: / type(y) / object-id(y):  ['Hello', 'x-World'] / <class 'list'> / 2107386121472
# Outside function ********************
# Outside function x: / type(x) / object-id(x):  ['Hello', 'x-World'] / <class 'list'> / 2107386121472