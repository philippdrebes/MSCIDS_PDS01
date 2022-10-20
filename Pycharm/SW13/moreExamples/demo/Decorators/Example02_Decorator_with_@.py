# Example02_Decorator_with_@.py

# We replace this line:
# foo = our_decorator(foo)
# through
# @our_decorator

def our_decorator(func):
    def function_wrapper(x):
        x = str(x).upper()         # "decoration": capitalize the string in argument 'x'
        func(x)
    return function_wrapper


@our_decorator      # here as a demo an "ARGUMENT-CAPITAL-WRITING DECORATOR"
def foo(x):
    print("     foo print out '" + str(x) + "'!")


# this function is only there to start "the program"!
def main():
    foo("first")
    #  foo = our_decorator( foo )  # You don't need this line anymore !!!
    foo("second")
    print("Example - End!")

if __name__== "__main__":
    main()


# Output:
#      foo print out 'FIRST'!
#      foo print out 'SECOND'!
# Example - End!
