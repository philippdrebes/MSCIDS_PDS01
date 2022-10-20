#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_deep_copy.php

# Shallow and Deep Copy
# Copying a list
#
# We change just one element of the list of colours2 or colours1.
# Lots of beginners will be stunned that the list of colours1 has been
# "automatically" changed as well.
#
# Review the illustration
# Review with http://www.pythontutor.com/visualize.html#mode=edit


colours1 = ["red", "blue"]
colours2 = colours1
print(colours1)
print(colours2)
print(id(colours1), id(colours2))
# both variables point to the same list object


colours2[1] = "green"
print(colours1)
print(colours2)
print(id(colours1), id(colours2))
# both variables point to the same list object
