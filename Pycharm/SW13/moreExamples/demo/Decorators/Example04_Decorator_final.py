# Example04_Decorator_final.py

# Final demo with several decorators on one function:

# In the data science environment you will often find these '@' characters
# and have now hopefully learned to "love" this '@' sing !!!

def myResultDoubler(func):
    def function_wrapper(x):
        res_loc = func(x)
        return res_loc * 2
    return function_wrapper


def myResultTrible(func):
    def function_wrapper(x):
        res_loc = func(x)
        return res_loc * 3
    return function_wrapper


@myResultTrible            # you can connect (well programmed) decorators
@myResultDoubler           # several times ...  COOOOOL!
@myResultTrible
def signCounter(x):
    return len(str(x))


@myResultTrible
def listCounter(x):
    if type(x) == list:
        res = len(x)
    else:
        res = 0
    return res


# diese Funktion ist nur da um "das Programm" zu starten!
def main():
    res01 = signCounter(3.453434)
    print("*** res01:", res01)              # *** res01: 144   (8 * 3 * 2 * 3)
    myList = ["A", 2, [2, 3], (4, 6, 7, 8)]
    res03 = listCounter(myList)
    print("*** res02 List:", res03)         # *** res03 List: 12  (4 elements * 3)


if __name__ == "__main__":
    main()

# Output:
# *** res01: 144
# *** res02 List: 12
