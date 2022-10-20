#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_descriptors.php
#
# Descriptors
#
# A descriptor is an object attribute with "binding behavior", one whose
# attribute access has been overridden by methods in the descriptor
# protocol. Those methods are __get__(), __set__(), and __delete__().
#
# If any of those methods are defined for an object, it is said to be a
# descriptor.
#
# Their purpose consists in providing programmers with the ability to add
# managed attributes to classes.
#
# The descriptors are introduced to get, set or delete attributes from the
# object's __dict__ dictionary via the above mentioned methods. Accessing a
# class attribute will start the lookup chain.


class A:

    ca_A = "class attribute of A"

    def __init__(self):
        self.ia_A = "instance attribute of A instance"


class B(A):

    ca_B = "class attribute of B"

    def __init__(self):
        super().__init__()
        self.ia_B = "instance attribute of B instance"


x = B()

print(x.ia_B)
print(x.ca_B)
print(x.ia_A)
print(x.ca_A)

# print(x.non_existing)

# If the looked-up value is an object defining one of the descriptor methods,
# then Python may override the default behavior and invoke the descriptor
# method instead.
#
# Descriptors provide a powerful, general purpose protocol, which is the
# underlying mechanism behind properties, methods, static methods, class
# methods, and super().
