# Slots_Task02.py

# Slots-Task 02:
# Replace all 'to do': Important 'to do 4'!!!


class S(object):
    __slots__ = ['val']     # only the data attribute 'val' is allowed

    def __init__(self, v):
        self.val = v

# to do 1: create an object x (of type S) with value 42
x = ""                      # this codeline is wrong!!
print(x)
print(x.val)

# to do 2: change the data attribute val to the value 99
x.val = ""		            # this codeline is wrong!!
print(x.val)		        # printing of data attribute

# to do 3: add a new attribute 'new_attr' to x
#          with the string "not possible"
#          =>  what do you notice?
#          How can you correct this 'notice'?
x.val = ""		            # this codeline is wrong!!


# to do 4: output the dicts of S and x!
#          not that easy ... but solvable for you with __slots__ and __getattribute __ (...)!
