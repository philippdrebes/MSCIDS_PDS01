#!/usr/bin/env python3

# 083_global_and_local_variable.py
# examples for global and local variables

# What happens at the next code snippet?
# Think first... # ;-)


def f():
    print(s)            # output of ....
    s = "Perl"          # definition a local variable
    print(s)            # ouput von ....

s = "Python"            # globale variable
f()
print(s)


#########
# Output:
#########
# Traceback (most recent call last):
#   File "C:/Users/Erwin Mathis/PycharmProjects/IDS_Python/Kap14_Functions_english/83_global_and_local_variable.py", line 13, in <module>
#     f()
#   File "C:/Users/Erwin Mathis/PycharmProjects/IDS_Python/Kap14_Functions_english/83_global_and_local_variable.py", line 8, in f
#     print(s)            # output of ....
# UnboundLocalError: local variable 's' referenced before assignment

