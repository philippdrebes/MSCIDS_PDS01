# _02_student.py
# Source: https://betterprogramming.pub/unlock-the-4-mysteries-of-self-in-python-d1913fbb8e16

# Question: What about 'self' in method greet(self, name) ?
# Better Solution to find out something about 'self': Insert some 'id(self)'
# => ??
# self is the same object like stud01 => self is ALLWAYS the calling object!!!


class Student:
    def greet(self, name):
        print("  in greet() - id(self):   ", id(self))           # NEW inserted!
        print('Good Morning, ' + name)


def my_main():
    stud01 = Student()
    print("in my_main() - id(stud01): ", id(stud01))             # NEW inserted!
    stud01.greet('John')

    print("type(Student): ", type(Student))
    print("type(stud01): ", type(stud01))

    print("isinstance(stud01,Student): ", isinstance(stud01,Student))
    print("hasattr(Student, 'greet'):  ", hasattr(Student, 'greet'))

if __name__ == "__main__":
    my_main()


###########
# output:
# in my_main() - id(stud01):  1883035483440
#   in greet() - id(self):    1883035483440
# Good Morning, John
# type(Student):  <class 'type'>
# type(stud01):  <class '__main__.Student'>
# isinstance(stud01,Student):  True
# hasattr(Student, 'greet'):   True
