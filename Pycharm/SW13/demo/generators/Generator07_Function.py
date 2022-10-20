# Generator07_Function.py

# Quelle: https://wiki.python.org/moin/Generators

#############
# Second way: We use a function to create a 'generator'!
#############

# Python provides generator functions as a convenient shortcut to building iterators.
# Lets us rewrite the above iterator as a generator function:
# a generator that yields items instead of returning a list => for 'big data' problems!!!


def firstn(n):       # firstn (...) is a function (Generator function)
    num = 0
    while num < n:
        yield num
        num += 1


sum_of_first_n = sum(firstn(10))
print("sum(firstn(10)): ", sum_of_first_n)


# Output:
# sum(firstn(10)):  45
