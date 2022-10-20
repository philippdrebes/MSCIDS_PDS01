# Generator02_Expression.py

# Generator Expressions
# I want to yield 'n*n' for each 'n' in a give list 'nums'


def gen_func(nums):
    for n in nums:
        yield n*n
        # print(" ... and now perhaps some lines of other code ...")


def main():
    print("\nGenerator Expression Example")
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    my_gen = gen_func(nums)
    print("type(my_gen): ", type(my_gen))

    for i in my_gen:
        print(i, end=' ')     # remember what is 'end=' '
        #                     # "Consume" only ONE element of 'nums'


if __name__ == "__main__":
    main()

# Output:
# Generator Expression Example
# type(my_gen):  <class 'generator'>
# 1 4 9 16 25 36 49 64 81 100
