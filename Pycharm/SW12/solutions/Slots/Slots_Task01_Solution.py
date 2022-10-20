# Slots_Task02.py

# Slots-Task 01:
# Answer the questions below.

class A:
    pass

a = A()
a.x = 66
a.y = "dynamically created attribute"

print("a.x: ", a.x)
print("a.y: ", a.y)

# Question 0: How can one show the dict of A and a?

# Answer 0:
print("A.__dict__:", A.__dict__)
print("vars(A)   :",vars(A))
print("a.__dict__:", a.__dict__)
print("vars(a)   :",vars(a))


print("---------------")

# example 1:
b = 42       		             # create an integer object named b
# b.x = "not possible to do it"  # Question 1: WHY is it not possible now?
                                 # Question 2: In which dict is 'b' stored?


# example 2:
lst = [34, 999, 1001]	         # create in list object
#lst. x = "forget it!"           # Question 3: WHY is that also not possible?
                                 # Question 4: In which dict is lst saved?





# Answers to
# Question 1 and 3:  b and lst have no attribute x
# Question 2 and 4:  b and lst are stored in
#                    1: dictionary of the module namespace
#                    2: dictionary of the current namespace
# prove:
print("globals():", globals())
print("vars():", vars())
print("locals():", locals())


# globals() always returns the dictionary of the module namespace
# locals() always returns a dictionary of the current namespace
# vars() returns either a dictionary of the current namespace
#         (if called with no argument) or the dictionary of the argument.
# => locals() == vars() !!
# The following applies at module level: vars() == globals()
