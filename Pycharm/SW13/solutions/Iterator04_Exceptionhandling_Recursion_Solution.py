# Iterator04_Exceptionhandling_Recursion_Solution.py

# Repe and deepening of exception handling and recursion!
# Application example for SELF-defined "Iterator" i.e.
# the Fibo class is an iterator because it provides the
# two methods __iter __ () and __next __ ()!

# Your Task: Try to find out how large can you choose the 'index' in this program?
############
# Answer:   The number can be as large as you like (with enough patience when calculating).
#           Python does not have an integer limit.
#           Fibo(500000) => approx. 5 seconds a number with 104513 digits ... ans so on!

class Fibo:
    limit = 1

    def __init__(self):
        # default constructor
        self.prev = 0
        self.cur = 1
        self.n = 1

    def __iter__(self):  # define the iter() function
        return self

    def __next__(self):  # define the next() function
        if self.n < Fibo.limit:  # Limit to 10
            # calculate fibonacci
            result = self.prev + self.cur
            self.prev = self.cur
            self.cur = result
            self.n += 1
            return result
        else:
            raise StopIteration  # raise exception


def main():

    Fibo.limit = int(input("Calculate Fibonacci up to which index? (> 2!) "))
    # init the iterator
    iterator = iter(Fibo())
    print(0)
    print(1)
    a = 0
    # Try to print infinite time until it gets an exception
    while True:
        # print the value of next fibonacci up to 10th fibonacci
        try:
            # print(next(iterator))
            a = next(iterator)

        except StopIteration:
            print("no more Elements in the 'callable-collection'.")
            break  # break the loop
    print("Fibo(", Fibo.limit, ") = ", a)


if __name__ == "__main__":
    main()

# Output:
# Calculate Fibonacci up to which index? (> 2!) 100
# 0
# 1
# no more Elements in the 'callable-collection'.
# Fibo( 100 ) =  354224848179261915075
