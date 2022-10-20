# _03_student_01_base_program.py
# Source: https://betterprogramming.pub/advanced-python-9-best-practices-to-apply-when-you-define-classes-871a27af658b
# or
# 9_BestPractices_Python.pdf


# First part of step 3:   => Base program for _03*.py
# We still have unrestricted access to all attributes!
# That's against the idea of encapsulation in ObjectOrientation!
# ... but it works if we don't "prevent" it!

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.status_verified = None                     # new: set ALL instance variable in 'init()
        self.guardian = None                            # new: set ALL instance variable in 'init()

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

    stud01.first_name = "Sarah"
    stud01.last_name  = "Steiner"
    print("Student Name: ", stud01.first_name, stud01.last_name)

if __name__ == "__main__":
    my_main()
