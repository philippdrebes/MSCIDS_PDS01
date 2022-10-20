# _02_student_01_explicit_instance_attribute.py
# Source: https://betterprogramming.pub/advanced-python-9-best-practices-to-apply-when-you-define-classes-871a27af658b
# or
# 9_BestPractices_Python.pdf


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def verify_registration_status(self):
        status = self.get_status()
        self.status_verified = (status == "registered")        # you set (on runtime!)  a new instance variable!!!

    def get_guardian_name(self):
        return self.guardian

    def set_guardian_name(self, guardian_name):
        self.guardian = guardian_name                          # you set (on runtime!) a new instance varialbe!!!

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
    status = stud01.verify_registration_status()
    print("status of ", stud01.first_name, stud01.last_name, " is: ", stud01.status_verified)
    stud01.set_guardian_name("Goodwife")
    print("guardian_name: ", stud01.get_guardian_name())

    print("*" * 50)
    stud02 = Student("Michael", "Schuhmacher")
    status = stud02.verify_registration_status()
    print("status of ", stud02.first_name, stud02.last_name, " is: ", stud02.status_verified)

    # You forgot to "set" the Guardian name ... then ...
    # To see the effect: comment out the next line!!
    # print("guardian_name: ", stud02.get_guardian_name())

if __name__ == "__main__":
    my_main()
