#_03_student_09_exercise.py
# Source: https://betterprogramming.pub/advanced-python-9-best-practices-to-apply-when-you-define-classes-871a27af658b
# or
# 9_BestPractices_Python.pdf


# Ninth part of step 3:
# Can we also convert the other two property variables (i.e. first_name and last_name) as a property decorator?
# Answer: YES but ...
# The advantage of properties should be above all in the verification and clean value setting.
# Belly Rule: Be very careful when using property-decorators.
#
# EXERCISE:
# Change the current program so that only property-dedorators are used!
# Even if that might not be the best approach.

# Pre-condition:
# The 'my_main()' function must not be changed.
# We assume that this program is used in the praxis and much larger and should therefore not be checked again ...

class Student:
    def __init__(self, first_name, last_name):
        self.set_first_name(first_name)
        self._last_name = last_name
        self.status_verified = None
        self.guardian = None


    def get_first_name(self):
        return self._first_name


    def set_first_name(self, fname):
        if fname[0]=='S'or fname[0]=='s':
            self._first_name = "S-Name-not-allowed!"
        else:
            self._first_name = fname

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, fname):
        self._last_name = fname


    @property
    def name(self):
        print("   Getter for the name")
        return f"{self.first_name} {self.last_name}"

    @name.setter
    def name(self, name):
        print("   Setter for the name")
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


    # part of the class 'student'=> we define 2 new property's:
    first_name = property(fget=get_first_name, fset=set_first_name)
    last_name = property(fget=get_last_name, fset=set_last_name)


def my_main():
    stud01 = Student("Silvana", "Mathis")

    print("Student Name: ", stud01.first_name, stud01.last_name)

    stud01.first_name = "Sarah"
    stud01.last_name = "Steiner"

    print("Student Name: ", stud01.name)
    stud01.name = "Frank Fitzlaff"
    print("Student Name: ", stud01.name)

    stud01.first_name = "stefan"
    print("Student Name: ", stud01.name)

    stud01.first_name = "urs"
    print("Student Name: ", stud01.name)

    print("stud01.first_name: ", stud01.first_name)
    print(stud01.__dict__)
    # print(Student.__dict__)

    stud02 = Student("Tony", "Röösli")
    print("Student Name: ", stud02.name)

    stud02.first_name="Stefan"
    print("Student Name: ", stud02.name)
    print(stud02.__dict__)

if __name__ == "__main__":
    my_main()

##################
# output:
# Student Name:  S-Name-not-allowed! Mathis
#    Getter for the name
# Student Name:  S-Name-not-allowed! Steiner
#    Setter for the name
#    Getter for the name
# Student Name:  Frank Fitzlaff
#    Getter for the name
# Student Name:  S-Name-not-allowed! Fitzlaff
#    Getter for the name
# Student Name:  urs Fitzlaff
# stud01.first_name:  urs
# {'_first_name': 'urs', '_last_name': 'Fitzlaff', 'status_verified': None, 'guardian': None}
#    Getter for the name
# Student Name:  Tony Röösli
#    Getter for the name
# Student Name:  S-Name-not-allowed! Röösli
# {'_first_name': 'S-Name-not-allowed!', '_last_name': 'Röösli', 'status_verified': None, 'guardian': None}
