# _05_student_methods_without_self.py
# Source: https://betterprogramming.pub/unlock-the-4-mysteries-of-self-in-python-d1913fbb8e16

# Question: Is it possible to program methods without 'self' ?
# Answer:   Yes ... for example as class-method or static-method

class Student:
    def __init__(self, name):
        self.name = name

    @classmethod
    def with_names(cls, first_name, last_name):       # cls points to 'Student'
        res = cls(first_name + ' '+last_name)         # like 'Student("Eric Muster")'
        print("cls(first_name + ' '+last_name): ", res)
        print("type(res): ", type(res))
        return res

def my_main():
    stud01 = Student.with_names("John", "Byron")
    print(stud01.name)
    print("in my_main() - id(stud01): ", id(stud01))


if __name__ == "__main__":
    my_main()


###########
# output:
# cls(first_name + ' '+last_name):  <__main__.Student object at 0x0000021C1EF99520>
# type(res):  <class '__main__.Student'>
# John Byron
# in my_main() - id(stud01):  2319802012960
