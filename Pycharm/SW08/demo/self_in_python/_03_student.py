# _03_student.py
# Source: https://betterprogramming.pub/unlock-the-4-mysteries-of-self-in-python-d1913fbb8e16

# Question: What happens when we call the gread(...) function like this example:
# Student.greet(stud01,"Bill")
# ... let's try ...

# Solution: same effect like in 'stud01.greet("John")' ....!

class Student:
    def greet(self, name):
        print("  in greet() - id(self):   ", id(self))
        print('Good Morning, ' + name)


def my_main():
    stud01 = Student()
    print("in my_main() - id(stud01): ", id(stud01))
    stud01.greet('John')

    Student.greet( stud01, "Bill" )                           # new inserted!

    print("type(Student): ", type(Student))
    print("type(stud01): ", type(stud01))

    print("isinstance(stud01,Student): ", isinstance(stud01,Student))
    print("hasattr(Student, 'greet'):  ", hasattr(Student, 'greet'))


if __name__ == "__main__":
    my_main()


###########
# output:
# in my_main() - id(stud01):  2086690307376
#   in greet() - id(self):    2086690307376
# Good Morning, John
#   in greet() - id(self):    2086690307376
# Good Morning, Bill
# type(Student):  <class 'type'>
# type(stud01):  <class '__main__.Student'>
# isinstance(stud01,Student):  True
# hasattr(Student, 'greet'):   True
