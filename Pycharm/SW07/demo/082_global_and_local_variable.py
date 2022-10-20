#!/usr/bin/env python3

# 082_global_and_local_variable.py
# examples for global and local variables

# Adding s="Perl" to function f()
# What happens now? First think... ;-)

def f():
    s = "Perl"         # local variable
    print(s)

s = "Python"           # globale variable
f()
print(s)

#########
# Output:
#########
# Perl              # => comes from ...
# Python            # => comes from ...
