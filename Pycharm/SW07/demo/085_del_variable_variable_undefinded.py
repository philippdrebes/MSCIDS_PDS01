#!/usr/bin/env python3

# 085_del_variable_variable_undefinded.py
# examples for delete variable and call it

# there is finally no variable x defined ... => error


x = 42
print ("x: ", x)
del x
print(x)               # error message -

#########
# Output:
#########
# Traceback (most recent call last):
#   File "C:/Users/Erwin Mathis/PycharmProjects/IDS_Python/Kap14_Functions_english/085_del_variable_variable_undefinded.py", line 15, in <module>
#     print(x)               # error message -
# NameError: name 'x' is not defined
# x:  42

