# _03_student_07_base_for_property_decorator.py
# Source: https://betterprogramming.pub/advanced-python-9-best-practices-to-apply-when-you-define-classes-871a27af658b
# or
# 9_BestPractices_Python.pdf


# Seventh part of step 3:
# we also define a getter and a setter method for "name".
# Why? we'll see that in the next example!
#

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


# NEW ################################
    def get_name(self):
        print( "   Getter for the name" )
        return f"{self.first_name} {self.last_name}"

    def set_name(self, name):
        print( "   Setter for the name" )
        self.first_name, self.last_name = name.split()
# NEW end ################################
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

    # old:
    # print("Student Name: ", stud01.get_first_name(), stud01.get_last_name())

# NEW: output 'first_name' and 'last_name' in ONE method => get_name()
    print( "Student Name: ", stud01.get_name() )

# NEW: set a new name for 'stud01' with ONE method  => set_name(...)
    stud01.set_name("Frank Fitzlaff")
    print( "Student Name: ", stud01.get_name() )

    print(stud01.__dict__)
    # print(Student.__dict__)



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
# {'_first_name': 'Frank', '_last_name': 'Fitzlaff', 'status_verified': None, 'guardian': None}
