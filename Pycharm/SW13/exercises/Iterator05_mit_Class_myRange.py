# Iterator05_mit_Class_myRange.py

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
# Task:   Change the function main() so that a number 'x' is requested from the user.
#         The sum of all numbers between 1 to x should be calculated with the MyRange-Class
def main():
    try:
        y = MyRange(7)
        print("type(y):", type(y))
        print(y.next())
        print(y.next())
        print(y.next())

        y.next()
    except StopIteration:
        print("Iteration fertig!")


if __name__ == "__main__":
    main()

# Output:
# type(y): <class '__main__.MyRange'>
# 0
# 1
# 2
