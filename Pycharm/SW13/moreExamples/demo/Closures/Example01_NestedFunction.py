# Example01_NestedFunction.py

# Quelle: https://www.geeksforgeeks.org/python-closures/

# Python program to illustrate nested functions
# Definition: A function which is defined inside another function
#             is known as nested function.

def outerFunction(textArg):
    text = textArg
    # print("in 'outerFunction(textArg'): ", text)

    def innerFunction():          # this is a nested function!!!
        print(text)               # look for 'text' in outerFunction!

    innerFunction()               # call innterFunction in outerFunction


def main():
    outerFunction('Hey!')


if __name__ == '__main__':
    main()

# result:
# Hey!
