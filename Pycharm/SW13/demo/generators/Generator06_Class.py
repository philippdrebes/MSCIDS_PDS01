# Generator06_Class.py

# Source: https://wiki.python.org/moin/Generators

############
# First way: We use a class to create a 'generator'!
############

# Using the generator pattern (an iterable)
# So, we resort to the generator pattern.
# The following implements generator class as an iterable object.

# Issues:
# there is a lot of boilerplate
# the logic has to be expressed in a somewhat convoluted way

class firstn(object):      # we generate a class for our task

    def __init__(self, n):    # this is the 'construct function' of the class firstn
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()


sum_of_first_n = sum(firstn(10))       # firstn (....) is a constructor call !!!
print("sum(firstn(10)): ", sum_of_first_n)

# Output:
# sum(firstn(10)):  45
