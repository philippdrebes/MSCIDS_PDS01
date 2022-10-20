# _03_student_02_getter_and_setter.py
# Source: https://betterprogramming.pub/advanced-python-9-best-practices-to-apply-when-you-define-classes-871a27af658b
# or
# 9_BestPractices_Python.pdf


# Second part of step 3:
# We try to prevent unhindered access to the attributes (instance variables)
# with getter and setter methods!
# In this example only for the instance variables 'first_name' and 'last_name'

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.status_verified = None                     # new: set ALL instance variable in 'init()
        self.guardian = None                            # new: set ALL instance variable in 'init()

# new #############################################
    def get_first_name(self):
        return self.first_name

    def set_first_name(self, fname):
        self.first_name = fname

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, fname):
        self.last_name = fname
# new end #########################################

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
    print("Student Name: ", stud01.first_name, stud01.last_name)

# we have now getter- and setter-methods ... but direct access still works
    # stud01.first_name = "Sarah"
    # stud01.last_name  = "Steiner"

    stud01.set_first_name("Sarah")
    stud01.set_last_name("Steiner")


# we have now getter- and setter-methods ... but direct access still works
    # print("Student Name: ", stud01.first_name, stud01.last_name)
    print("Student Name: ", stud01.get_first_name(), stud01.get_last_name())

if __name__ == "__main__":
    my_main()
