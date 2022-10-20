# _01_student.py
# Source: https://betterprogramming.pub/unlock-the-4-mysteries-of-self-in-python-d1913fbb8e16

# Question: What about 'self' in method greet(self, name) ?
# Solution (not completely!): Student has an attribut 'greet' ... and stud01 is an instance (object) of Student

class Student:
    def greet(self, name):
        print('Good Morning, ' + name)


def my_main():
    stud01 = Student()
    stud01.greet('John')

    print("type(Student): ", type(Student))
    print("type(stud01): ", type(stud01))

    print("isinstance(stud01,Student): ", isinstance(stud01,Student))
    print("hasattr(Student, 'greet'):  ", hasattr(Student, 'greet'))

if __name__ == "__main__":
    my_main()


###########
# output:
# Good Morning, John
# type(Student):  <class 'type'>
# type(stud01):  <class '__main__.Student'>
# isinstance(stud01,Student):  True
# hasattr(Student, 'greet'):   True
