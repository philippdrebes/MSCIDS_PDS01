# Bsp02_Generator_intro_withExceptionHandling.py

# Source: https://anandology.com/python-practice-book/iterators.html


def myRange(n):	 # myRange(...) is a 'generator function'
    i = 0
    while i < n:
        yield i
        i += 1


def main():

    myNumber = input("Wie oft wollen Sie den Generator aufrufen? ")
    y = myRange(int(myNumber))   # 'y' is a 'generator' (= generated object)
    #                            # <generator object myRange at 0x401f30>
    i = 0
    try:
        for i in range(int(myNumber) + 1):       # why +1 ???
            print(next(y))

    except StopIteration:
        print("After ", i-1, "calls stopped!!")


if __name__ == "__main__":
    main()


# Output:
# Wie oft wollen Sie den Generator aufrufen? 5
# 0
# 1
# 2
# 3
# 4
# After  4 calls stopped!!
