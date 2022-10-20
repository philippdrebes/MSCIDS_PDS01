# Iterator05_mit_Class_myRange_Solution.py

# Iterators are implemented as classes.
# Here is an iterator that works like built-in 'xrange' function.

# This class fulfills the 'iterator' protocol (next () and iter ())!!

# Solve the Task below!
#########################
class MyRange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


########
# Task: Change the function main() so that a number 'x' is requested from the user.
#       The sum of all numbers between 1 to x should be calculated with the MyRange-Class
def main():
    x = int(input("Input a number: "))
    y = MyRange(x)
    sum = 0
    while True:
        try:
            sum = sum + y.next()
        except StopIteration:
            break
    print(sum)


if __name__ == "__main__":
    main()


# Output:
# Input a number: 120
# 7140
