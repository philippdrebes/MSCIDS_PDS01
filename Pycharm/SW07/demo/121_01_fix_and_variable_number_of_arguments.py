#!/usr/bin/env python3

# 121_01_fix_and_variable_number_of_arguments.py
# Variable Length of Parameters (c)
# a fixed number of positional parameters + followed by any number of parameters

# in this function we have: one fix parameter: 'city'
#                           all other parameters ar in 'other_cities' !
def locations(city, *other_cities):
    print("city, other_cities:", city, other_cities)    # other_cities is a tuple!


locations("Berlin")          # only one (fix) argument

locations("Berlin", "Freiburg", "Stuttgart", "Konstanz")  # one fix argument and 3 more ....

# locations()                  # error => one fix argument is necessary!

#########
# Output:
#########
# city, other_cities: Berlin ()
# city, other_cities: Berlin ('Freiburg', 'Stuttgart', 'Konstanz')