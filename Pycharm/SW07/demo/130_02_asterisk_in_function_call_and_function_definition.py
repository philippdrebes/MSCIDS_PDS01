#!/usr/bin/env python3

# 130_02_asterisk_in_function_call_and_function_definition.py
# * in function call  and * function definition (b) => practice
# A few examples at a glance:


# Example 03: (function with no return statement!)
#             tuple p has one more element => an error occurs!
print("f3: *******************************")
def f3(x,y,z):
    print(x,y,z)

p = (47,11,12,16 )
f3(*p)                      # Question ... how can we solve this challenge?

#########
# Output:
#########
# Traceback (most recent call last):
#   File "C:/Users/Erwin Mathis/PycharmProjects/IDS_Python/Kap14_Functions_english/130_02_asterisk_in_function_call_and_function_definition.py", line 14, in <module>
#     f3(*p)
# TypeError: f3() takes 3 positional arguments but 4 were given
# f3: *******************************

