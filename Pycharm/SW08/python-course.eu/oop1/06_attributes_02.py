#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Attributes

# Attributes can be bound to class names as well.
# In this case, each instance will possess this name as well.


class Robot:
    pass


x = Robot()
# x. name = "Marvin "
print(x.__dict__)
print(Robot.__dict__)

Robot.brand = "Kuka"
print(x.__dict__)
print(Robot.__dict__)
print("0)", Robot.brand)
print("1)", x.brand)       # besser wäre Robot.brand!  in x wird nichts gefunden => suche in 'Robot' nach 'brand

x.brand = "Thales"         # Wau: ich füge jetzt bewusst (?) auch dem Objekt x ein Attribut 'brand' hinzu
print("2)", Robot.brand)
print("3)", x.brand)

y = Robot()
print("4)", y.brand)       # ?? gibts jetzt auch schon ein Robot.brand ????  ja und das wird aufgerufen
                            # weil es im Objekt y noch keine 'brand'-Attribut hat

Robot.brand = "Thales"
print("5)", y.brand)

print("6)", x.__dict__)
print("7)", y.__dict__)
print("8)", Robot.__dict__)


# If you try to access y.brand, Python checks first, if "brand" is a key of
# the y.__dict__ dictionary. If it is not, Python checks, if "brand" is
# a key of the Robot.__dict__. If so, the value can be retrieved.

print("10)", y.brand)                  # hier wird in die Klasse hinaufgesprungen und dieses Attribut ausgegeben!
y.brand = 'AT&T'
print("11)", y.brand)



#print("20)", x.energy)   # AttributeError: 'Robot' object
# has no attribute 'energy'

print("21)", getattr(x, 'energy', 100))


print(x.__dict__)    # klären!
