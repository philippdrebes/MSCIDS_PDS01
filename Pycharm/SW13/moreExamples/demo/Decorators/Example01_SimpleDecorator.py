# Example01_SimpleDecorator.py      # Addition: Without @ sign !!!

# First:The goal is to call a function 'foo(x)': prints out only the text in 'x'
# Second: The output of 'foo(x)' should be capitalized WITHOUT to change the
#         code of the function 'foo(x)'   => Solution: Use an 'nested' function!!


def our_decorator(func):
    def function_wrapper(x):
        x = str(x).upper()
        func(x)              # because no return value is expected: No assignment!
        # function_wrapper (): has NO 'return' here
    return function_wrapper  # a 'wrapping' function => wrapping does this function 'func ()' !!!


def foo(x):                  # has no return value => Otherwise funcion_wrapper should also have a
    #                        # return-value !!!
    print("foo print out '" + str(x) + "'!")


# this function is only there to start "the program"!
def main():
    foo("first")
    foo1 = our_decorator(foo)                      # foo1 => is now a 'decorator'- function
    foo1("second")


if __name__ == "__main__":
    main()


# Output:
# foo print out 'first'!
# foo print out 'SECOND'!
