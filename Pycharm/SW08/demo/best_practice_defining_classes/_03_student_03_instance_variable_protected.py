# _03_student_03_instance_variable_protected.py
# Source: https://betterprogramming.pub/advanced-python-9-best-practices-to-apply-when-you-define-classes-871a27af658b
# or
# 9_BestPractices_Python.pdf


# Third part of step 3:
# We try to prevent unhindered access to the attributes (instance variables)
# with with setting our instance variables 'protected': _first_name  (it's ONLY an convention !
# In this example only for the instance variables 'first_name' and 'last_name'

class Student:
    def __init__(self, first_name, last_name):
        self._first_name = first_name     # new: proteced instance variable '_first_name'
        self._last_name = last_name       # new: proteced instance variable '_first_name'
        self.status_verified = None
        self.guardian = None


    def get_first_name(self):
        return self._first_name            # new: proteced instance variable '_first_name'

    def set_first_name(self, fname):
        self._first_name = fname           # new: proteced instance variable '_first_name'

    def get_last_name(self):
        return self._last_name             # new: proteced instance variable '_last_name'

    def set_last_name(self, fname):
        self._last_name = fname            # new: proteced instance variable '_last_name'


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
    stud01 = Student("Silvana", "Mathis")

    # old:
    # print("Student Name: ", stud01.first_name, stud01.last_name)

# new: direct access is not allowed (but still possible ...!! => Python is a dynamic language!)
    print("Student Name: ", stud01._first_name, stud01._last_name, " direct access on 'proteced value' => not good!")

# new: better but more text to write:
    print( "Student Name: ", stud01.get_first_name(), stud01.get_last_name(), " better with getters! ")

    stud01.set_first_name("Sarah")
    stud01.set_last_name("Steiner")

    print("Student Name: ", stud01.get_first_name(), stud01.get_last_name())

if __name__ == "__main__":
    my_main()
