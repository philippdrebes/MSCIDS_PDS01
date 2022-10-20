# _05_student_instance_method_without_self.py
# Source: https://betterprogramming.pub/unlock-the-4-mysteries-of-self-in-python-d1913fbb8e16

# Question: Is it possible to program instance-methods without 'self'
# Answer:   Yes ... with an other first-parameter

class Student:
    # original
    # def greet(self, name):
    #     print("  in greet() - id(self):   ", id(self))
    #     print('Good Morning, ' + name)

# NEW ###############################
    def greet(gugus_object, name):
        print("  in greet() - id(self):   ", id(gugus_object))
        print('Good Morning, ' + name)
# NEW  end ##########################


def my_main():
    stud01 = Student()
    print("in my_main() - id(stud01): ", id(stud01))
    stud01.greet('John')

    Student.greet( stud01, "Bill" )

    print("*"* 50 )
    self = 99                                               # new: self is here a local variable ...!
    print("self: ", self)                                   # new
    print("type(self): ", type(self))                       # new
    print("*"* 50 )

    print("type(Student): ", type(Student))
    print("type(stud01): ", type(stud01))

    print("isinstance(stud01,Student): ", isinstance(stud01,Student))
    print("hasattr(Student, 'greet'):  ", hasattr(Student, 'greet'))


if __name__ == "__main__":
    my_main()


###########
# output:
# in my_main() - id(stud01):  2718770478384
#   in greet() - id(self):    2718770478384
# Good Morning, John
#   in greet() - id(self):    2718770478384
# Good Morning, Bill
# **************************************************
# self:  99
# type(self):  <class 'int'>
# **************************************************
# type(Student):  <class 'type'>
# type(stud01):  <class '__main__.Student'>
# isinstance(stud01,Student):  True
# hasattr(Student, 'greet'):   True
