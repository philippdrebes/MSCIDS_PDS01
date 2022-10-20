# _05_student_02_static_methods_outside.py
# Source: https://betterprogramming.pub/advanced-python-9-best-practices-to-apply-when-you-define-classes-871a27af658b
# or
# 9_BestPractices_Python.pdf


# First part of step 2:
# ... just for the sake of completeness!
# Let's rewrite the program and define the 'static method' as a normal function outside of the class.
# The call is then even easier ... (without 'Student' at the beginning)

# Have a look in the following code => NEW ...

# NEW start ################
def show_duties():
    return "Study, Play, Sleep"
# NEW end ##################

class Student:

    _count = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.status_verified = None
        self.guardian = None
        Student._count = Student.get_count() + 1


    def __repr__(self):
        return f"Student({self.first_name!r}, {self.last_name!r})"

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"

    # a simple instance-method (like other in this example e.g. verify_registration_status(...)
    def begin_study(self):
        print(f"{self.first_name} {self.last_name} begins studying.")

    # a class-method is declared with a @classmethod-decorator
    # generates a new object with a dict (=name_info) as parameter
    @classmethod
    def from_dict(cls, name_info):
        first_name = name_info['first_name']
        last_name = name_info['last_name']
        return cls(first_name, last_name)      # 'cls(...)' is the same as 'Student(....)'

    @classmethod
    def get_count(cls):
        return Student._count


# NEW commented out!!!
    # a static-method ist declared with a @staticmethod-decorator
    # could be defined also outside the class => next example!!
    # @staticmethod
    # def show_duties():
    #     return "Study, Play, Sleep"
# NEW end ###########################

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, fname):
        if fname[0] == 'S' or fname[0] == 's':
            self._first_name = "S-Name-not-allowed!"
        else:
            self._first_name = fname

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, fname):
        self._last_name = fname

    @property
    def name(self):
        #print("   Getter for the name")
        return f"{self.first_name} {self.last_name}"

    @name.setter
    def name(self, name):
        #print("   Setter for the name")
        self.first_name, self.last_name = name.split()

    def verify_registration_status(self):
        status = self.get_status()
        self.status_verified = (status == "registered")

    def get_guardian_name(self):
        return self.guardian

    def set_guardian_name(self, guardian_name):
        self.guardian = guardian_name       # e.g. "Goodman"

    def get_status(self):
        # get the registration status from a database (simulation!!!!!)
        status = self.query_database(self.first_name, self.last_name)
        return status

    def query_database(self, first_name, last_name):
        # do some crazy queries on a database
        # here only a dummy-method => simulation !!!!
        from random import randrange
        temp_status = randrange(10)
        if temp_status >= 7:
            return "not registered"
        else:
            return "registered"


def my_main():
    stud01 = Student("Jenny", "Ulrich")
    print("stud01: ", stud01)

    stud01.begin_study()          # normal instance-method-call with an object 'stud01'
                                  # this is in OO the normal way  (>95%)!
    name02 = {'first_name': "Eric", 'last_name': 'Hauser'}
    name03 = {'first_name': "Ann", 'last_name': 'Dillier'}
    name04 = {'first_name': "Jenny", 'last_name': 'Hartmann'}

    stud02 = Student.from_dict(name02)   # call a class-method with a CLASS (here 'Student')
    stud03 = Student.from_dict(name03)   # call a class-method with a CLASS (here 'Student')
    stud04 = Student.from_dict(name04)   # call a class-method with a CLASS (here 'Student')

    print("*"* 50)
    print(stud02.name)
    print(stud03.name)
    print(stud04.name)
    print("*"* 50)
    print("Actual we have " + str(Student.get_count()) + " students!")

# NEW: Call show_duties() as a function! #######
    res = show_duties()          # call a "normal" function without a preceding CLASS (here 'Student')
# NEW end ######################################
    print("Result of static-method-call: ", res)
    print("type(res): ", type(res))




if __name__ == "__main__":
    my_main()


###############
# output:
# stud01:  Student: Jenny Ulrich
# Jenny Ulrich begins studying.
# **************************************************
# Eric Hauser
# Ann Dillier
# Jenny Hartmann
# **************************************************
# Actual we have 4 students!
# Result of static-method-call:  Study, Play, Sleep
# type(res):  <class 'str'>
