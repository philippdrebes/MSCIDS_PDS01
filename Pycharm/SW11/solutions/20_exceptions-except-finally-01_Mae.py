#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_exception_handling.php
#
# Errors and Exceptions
# Combining try, except and finally
#
# "finally" and "except" can be used together for the same try block,
#

# try:
#     x = float(input("Your number: "))
#     inverse = 1.0 / x
#     print("Thanks")
# except ValueError:
#     print("You should have given either an int or a float")
# except ZeroDivisionError:
#     print("Infinity")
# finally:
#     print("There may or may not have been an exception.")
#
# print("Bye")

# Exercise: Change the program 20_exceptions-execpt-finally-01.py so that
#           it queries until you have entered a correct number (int or float).
#           With 'q' you should be able to leave the loop again in any case.
#
# Test with the following entries:
#
# 1. four
# 2. 0
# 3. 4
# 4. 4.5
# 5. q


while True:
    try:
        x = input( "Your number: (or 'q' for quit)" )
        inverse = 1.0 / float( x )
        print( "Inverse: ", inverse )
        break
    except ValueError:
        if x == 'q':
            break
        else:
            print( "You should have given either an int or a float" )
    except ZeroDivisionError:
        print( "Infinity" )
    finally:
        print( "There may or may not have been an exception." )

if x == 'q':
    print("Ok we will try it next time again!")
else:
    print("Great, you successfully entered an integer!")
    print("Ending with %.2f" % float(x))


print("Bye")


# Test's:
# Your number: (or 'q' for quit) four
# You should have given either an int or a float
# There may or may not have been an exception.

# Your number: (or 'q' for quit)0
# Infinity
# There may or may not have been an exception.

# Your number: (or 'q' for quit)4
# Inverse:  0.25
# There may or may not have been an exception.
# Great, you successfully entered an integer!
# Ending with 4.00
# Bye

# Your number: (or 'q' for quit) 4.5
# Inverse:  0.2222222222222222
# There may or may not have been an exception.
# Great, you successfully entered an integer!
# Ending with 4.50
# Bye

# Your number: (or 'q' for quit)q
# There may or may not have been an exception.
# Ok we will try it next time again!
# Bye

