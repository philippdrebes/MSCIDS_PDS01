# 03_TypeAnnotations_list_with_problem.py

# We would very often like to define the type of elements for lists as well.
# Type safety cannot be guaranteed with normal Python board resources.
# "Proof": See example below ...



import random


def silly_merge(x : list, y : list) -> list:
    endx = random.randint(0, len(x))  # arbitrarily (i.e. randomly) set an endpoint for x-slicing
    #print("endx:",endx)
    endy = random.randint(0, len(y))  # arbitrarily (i.e. randomly) set an endpoint for y-slicing
    #print("endy:",endy)
    return x[:endx] + y[:endy]        # output is CONSCIOUSLY (=bewusst!) different every time it is used!


# Problem 1:
# We only want to merge 'integers'.
# But a 'float' (23.5) has crept in (=einschleichen)
print(silly_merge([23.5, 27, 29, 21, 19],[101, 134, 156, 199]))


# Problem 2:
# this example also works, although it has a string 'in itself'
# the type of the elements in the list is NOT specified!
print(silly_merge([23, "step out of line", 19],[101, 134, 156, 199]))


# Question: How can we get Python to draw attention to possible errors before (!!)
#           the program has run?
#           e.g. we certainly don't want any text in the list of numbers ...
