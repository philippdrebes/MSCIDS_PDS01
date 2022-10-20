# Generator01_intro.py

# Source: https://anandology.com/python-practice-book/iterators.html

########
# Task: Create a main() function and start this main()-function.
# In this main() function you ask the user how often he wants to execute
# the generator function 'myRange ()' (i.e. how often the next() function
# should be called)
# The program should not generate an error for any number
# (i.e. create a correct error handling!)


def myRange(n):	 # myRange(...) is a 'generator function'
    i = 0
    while i < n:
        yield i
        i += 1


y = myRange(3)		# 'y' is a 'generator' (= generated object)
#                   # <generator object myRange at 0x401f30>
print("type(y): ", type(y))
print(next(y))      # 0
print(next(y))      # 1
print(next(y))      # 2
print(next(y))      # Traceback (most recent call last):
#                   # File "<stdin>", line 1, in <module>
#                   # StopIteration


# Output:
# type(y):  <class 'generator'>
# 0
# 1
# 2
# Traceback (most recent call last):
#   File "C:/Users/Erwin Mathis/PycharmProjects/IDS_Python/20191210_Block14_ListComprehension_Generator/Generator/Generator01_intro.py", line 19, in <module>
#     print(next(y))      # Traceback (most recent call last):
# StopIteration
