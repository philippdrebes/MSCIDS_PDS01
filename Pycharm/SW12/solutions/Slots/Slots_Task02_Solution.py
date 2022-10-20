# Slots_Task02.py

# Slots-Task 02:
# Replace all 'to do'


class S(object):
    __slots__ = ['val', 'new_attr']     # the data attribute 'val' and 'new_attr are allowed

    def __init__(self, v):
        self.val = v

# to do 1: create an object x (of type S) with value 42
x = S(42)                      # this codeline is wrong!!
print(x)
print(x.val)

# to do 2: change the data attribute val to the value 99
x.val = 99		            # this codeline is wrong!!
print(x.val)		        # printing of data attribute

# to do 3: add a new attribute 'new_attr' to x
#          with the string "not possible"
#          =>  what do you notice?
#          How can you correct this 'notice'? => insert new_attr in __slots__!!!
x.new_attr = "not possible"	    # create a new attribut => not possible

# to do 4: output the dicts of S and x!


print(vars(S))
# #print(vars(x))            # that doesn't work because S has NO dictionary for its members!
#print(x.__slots__)         # get all 'slots' as a list
#print(x.__slots__[0])      # get the name of the first 'slot'
#print(x.__getattribute__(x.__slots__[0]))   # get the value of the first slot!

d ={}
for i in x.__slots__:
    d[i]=x.__getattribute__(i)
print(d)
