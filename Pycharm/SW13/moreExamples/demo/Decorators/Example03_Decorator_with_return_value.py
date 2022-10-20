# Example03_Decorator_with_return_value.py.py

# NEW: The nested function_wrapper(x) has now a return value, because 'signCounter()'
#      must also provide a return value.
#      => as a supplement to Example02_Decorator_with_@.py

def myResultDoubler(func):
    def function_wrapper(x):
        res_loc = func(x)
        return res_loc * 2      # subfunction 'function_wrapper()  has also a return!
    return function_wrapper


def myResultTrible(func):
    def function_wrapper(x):
        res_loc = func(x)
        return res_loc * 3      # subfunction 'function_wrapper()  has also a return!
    return function_wrapper


@myResultTrible
def signCounter(x):
    return len(str(x))


# this function is only there to start "the program"!
def main():
    res01 = signCounter(3.453434)    # d.h. signCounter with decorator (myResultTrible) called!
    print("res01:", res01)
    # in preparation for the next step
    deco_func01 = myResultDoubler(signCounter)
    # singCounter (already tripled) is manually 'decorated' again (doubled)
    # see also next code example!
    print("deco_func01:", deco_func01(3.453434))
    print("Example - End!")


if __name__ == "__main__":
    main()

# Output:
# res01: 24
# deco_func01: 48
# Example - End!
