#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Attributes

# Binding attributes to objects is a general concept in Python.
# Even function names can be attributed.


def f(x):
    return 42

# mae
print("1)", f.__dict__)             # output: {}



# mae
print("2)", f.__dict__)             # output: {}
print(f(99))                        # output: 42

f.x = 42
print(f.x)                          # output: 42

# mae
print("3)", f.__dict__)             # output: {'x': 42}


# This can be used as a replacement for the static function
# variables of C and C++, which are not possible in Python.


def f(x):
    f.counter = getattr(f, "counter", 0) + 1           #f.counter ist ein dynamische Attribut !!!!
    return "Monty Python"

# mae
print("4)", f.__dict__)             # output: {}


for i in range(3):
    print(f(i))                     # output: Monty Python

    #mae
    print("5-",i,")", f.__dict__)   # output: 5- 0 ) {'counter': 1}   // 5- 1 ) {'counter': 2} // 5- 2 ) {'counter': 3}

print(f.counter)                    # output: 3

# mae
print("6)", f.__dict__)             # output: 6) {'counter': 3}
