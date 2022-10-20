# Examples for the output
# summary chapter 12 in book: "Einführung in Python", Bernd Klein, Hanser Verlag)

# ****************************************************
# print – Function 01: Basic Operations 
# ****************************************************

print("\nprint – function 01: ","*"* 60)


import sys                      # or the output e.g. in standard error channel

a = 42
b = 99
c = 66

print("a:", a)                  # print a value
print(a, b, c, sep=";")         # print multiple values with separator
print(a, b, c, sep="")          # print multiple values with separator


# ************************************************* ************************
# print - Function 02: How do you open a file? / Error output
# ************************************************* ************************
# print - In the data science environment, outputs often have to be routed into a 'data stream',
# because they cannot be displayed sensibly on the # screen:



print("\nprint – function 02: ","*"* 60)

fh = open("daten.txt", "w")
print("42 is the answer, but what was the question?", file=fh)
fh.close()
print("The text was correctly saved in a file!")

# additional output (here only as an example) on sys.stderr
print("Error: 42", file = sys.stderr)   # output in a different color!


# ******************************************
# print – Function 03: C-style praxis
# ******************************************

print("\nprint – function 03: ","*"* 60)

# C-style string formatting
print("Article: %5d, Price: %6.2f" % (453, 59.058))

print("Price: %6.2f " % (23.789))
print("Price: %6.2f " % (0.039))
print("Price: %6.2f " % (119.9))
print("Price: %6.2f " % (23))
print("Price: %6.2f " % (2424.17))     # what happens if the number has more than 6 characters?
print("Price: %6.2f " % (24241.7))     # what happens if the number has more than 6 characters?
print("Price: %6.2f " % (242417))      # what happens if the number has more than 6 characters?
print("Price: %6.2f " % (2424170))     # what happens if the number has more than 6 characters?


# ****************************************************
# print – Function 04: pythonic way
# ****************************************************

# In Python practice we often find the "old" Python way:
# That means the programmer uses the string-method 'format ()':
#
# As always, the following syntax applies: object.methode (parameters)

# object: this is a string with special brackets inside: {}
# method: format (...)
# Parameters: the values which should be inserted in the {} in the same order
# Examples with numbers, strings and variables:

print("\nprint – function 04: ","*"* 60)

# example with numbers as parameter
coordinates1 = "The coordinates are ({},{}).".format(5,10)
print(coordinates1)
coordinates2 = "The first argument is called '{}'. The second argument is called '{}'".format(5,10)
print(coordinates2)

# example with 'strings' as parameter
print("The first argument is called: {}\nThe second argument \
is called: {}".format("James", "Meier"))   # \n: new Line!

# example with variables as parameter
price = 23
movie = "Bohemian Rhapsody"
print("One of the best movies is called '{}'\
and costs {} CHF.".format(movie, price)) # meaning of ' ?



# ***************************************************
# print – Function 05: "NEW"  f-Strings  (Python 3.6)
# ***************************************************

# newer (since Python 3.6)  output technology with f-strings:
# Instead of working with the 'format (...) method,
# the desired value is immediately written into the
# brackets {...}  and a leading 'f' is set in front of the string:



print("\nprint – function 05: ","*"* 60)

# Examples as above ... but now with f-strings

# example with numbers as parameter
coordinates1 = f"The coordinates are ({5},{10})."
print(coordinates1)
coordinates2 = f"The first argument is called '{5}'. The second argument is called '{10}'"
print(coordinates2)

# example with 'strings' as parameter
print(f"The first argument is called: {'James'}\nThe second argument \
is called: {'Meier'}")                                  # \n: new Line!

# example with variables as parameter
price = 23
movie = "Bohemian Rhapsody"
print(f"One of the best movies is called '{movie}'\
and costs {price} CHF.")                                # meaning of ' ?
