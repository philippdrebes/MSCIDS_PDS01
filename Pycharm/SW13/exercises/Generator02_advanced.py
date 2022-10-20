# Bsp03_Generator.py

# This program shows that with 'yield' the status
# of the function foo () is always cached!

# Task 1: (also as a deepening for error handling!)
##########
# Change to the program in such a way that you can still see
# the end line of function foo() (=> print("**************** foo() end"))
# when your program calls the 'StopIteration' error!
# Solve this task with a correct error handling!

# Important: In order to get an error you have to comment out line 56 first!!

# Task 2:
##########
# Question: Why in the 'Output' below is the line
#           'main before 1. __next __ ():' printed out BEFORE (!!!)
#           '*********** foo () begin'?

# Output:
# main vor 1. __next__():
# **************** foo() begin
# before yield - i: 0
# main nach 1. __next__():
# .....


def foo():
    print("**************** foo() begin")
    for i in range(3):
        print("before yield - i:", i)
        yield i
        print("after yield - i:", i)
    print("**************** foo() end")  # Task 1: We never see this ouput!


def main():
    f = foo()                   # f ist ein Generator-Objekt!!!
    # print("type(f): ", type(f))
    print("\nmain vor 1. __next__():")
    f.__next__()                # now f is "started"!!!
    #                           # next(f) is Python 2.x notation
    #                           # f.__ next __() is the ObjectOriented-notation
    print("main nach 1. __next__():")

    print("\nmain vor 2. __next__():")
    f.__next__()
    print("main nach 2. __next__():")

    print("\nmain vor 3. __next__():")
    f.__next__()
    print("main nach 3. __next__():")

    print("\nmain vor 4. __next__():")
    # f.__next__()
    print("main nach 4. __next__():")


if __name__ == "__main__":
    main()


# Goal-Output:
# main vor 1. __next__():
# **************** foo() begin
# before yield - i: 0
# main nach 1. __next__():
#
# main vor 2. __next__():
# after yield - i: 0
# before yield - i: 1
# main nach 2. __next__():
#
# main vor 3. __next__():
# after yield - i: 1
# before yield - i: 2
# main nach 3. __next__():
#
# main vor 4. __next__():
# after yield - i: 2
# **************** foo() end
# Iteration stopped!
