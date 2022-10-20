# Example02_Closure.py

# Quelle: https://www.geeksforgeeks.org/python-closures/

# Python program to illustrate closures
# Definition: A Closure is a function object that remembers values in enclosing scopes
#             even if they are not present in memory.
# Quelle: https://samwize.com/2012/11/05/what-is-pythons-lambda-and-closure/

# Definition: Objects are data with methods attached, closures are functions with data attached.
# Quelle: https://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python

# Bsp_02_Closure.py
def outerFunction(textArg):
    text = textArg
    # print("in 'outerFunction(textArg'): ", text)

    def innerFunction():          # this is a nested function!!!
        print(text)               # look for 'text' in outerFunction!

    return innerFunction          # Note we are returning 'innerFunction' WITHOUT parenthesis
    #                             # we return the function-object NOT the result of the functon 'innerFunction()'!


def main():
    myString = "Hey!"
    myFunction = outerFunction(myString)
    print("myFunction:", myFunction)
    # print("del myString! ")
    del(myString)
    # print(myString)
    myFunction()          # call the closure!  => myFunction remembers the String "Hey!"
    myFunction()          # call the closure!
    myFunction()          # call the closure!


if __name__ == '__main__':
    main()

# result:
# myFunction: <function outerFunction.<locals>.innerFunction at 0x0000014EC85F6790>
# Hey!
# Hey!
# Hey!
