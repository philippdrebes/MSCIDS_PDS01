#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Attributes

# Attributes can be bound to class names as well.
# In this case, each instance will possess this name as well.


class Robot:
    pass


x = Robot()
Robot.brand = "Kuka"
print("1)", x.brand)       # besser wäre Robot.brand!  in x wird nichts gefunden => suche in 'Robot' nach 'brand

# mae
print("1a)", x.__dict__)
print("1b)", Robot.__dict__)

x.brand = "Thales"
# mae
print("1aa)", x.__dict__)
print("1bb)", Robot.__dict__)

print("2)", Robot.brand)
print("3)", x.brand)

# mae
print("3a)", x.__dict__)
print("3b)", Robot.__dict__)

y = Robot()
print("4)", y.brand)       # ?? gibts jetzt auch schon ein Robot.brand ????

# mae
print("4a)", y.__dict__)
print("4b)", Robot.__dict__)


Robot.brand = "Thales"
print("5)", y.brand)

print("6)", x.__dict__)
print("7)", y.__dict__)
print("8)", Robot.__dict__)


# If you try to access y.brand, Python checks first, if "brand" is a key of
# the y.__dict__ dictionary. If it is not, Python checks, if "brand" is
# a key of the Robot.__dict__. If so, the value can be retrieved.

print("10)", y.brand)

# mae
print("10)", y.__dict__)
print("10)", Robot.__dict__)

y.brand = 'AT&T'
print("11)", y.brand)

# mae
print("11)", y.__dict__)
print("11)", Robot.__dict__)

# print("20)", x.energy) # AttributeError: 'Robot' object
# has no attribute 'energy'


# mae   => wir können 'on the fly' ...(wau!!!) einem Objekt zusätliche Attritbute anhängen
#          ob das softwaretechnisch sinnvoll ist sei mal dahingestellt (meistens NEIN!).
#          Weil so die Entwickler*in rasch keinen Überblick mehr hat, welche Instanz-Variablen
#          an eine Objekt WIRKLICH gebunden sind.
#          In Normalfall sind es genau die Instanz-Variablen, welche mit __init__() "gebunden" werden!

# print("21)", getattr(x, 'energy', 100))
print("21)", setattr(x, 'energy', 100))
print("21a)", x.__dict__)
x.energy = 200
print('energy')

# mae
print("21b)", x.__dict__)
print("21)", y.__dict__)
print("21)", Robot.__dict__)
