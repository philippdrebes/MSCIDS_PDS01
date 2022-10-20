# _03_student_06_delegate_initialisation_to_set_first_name.py
# Source: https://betterprogramming.pub/advanced-python-9-best-practices-to-apply-when-you-define-classes-871a27af658b
# or
# 9_BestPractices_Python.pdf


# Sixth part of step 3:
#
# In the 5th part, the first name "Silvana" is still accepted when creating the object "Silvana" "Mathis" ...
# we have to correct that now!

# Solution: Instead of initialising the '_first_name' in the __init__()-method
#           we delegate this initialisation to the method set_first_name()

class Student:
    def __init__(self, first_name, last_name):
        # old:
        # self._first_name = first_name

# New:  delegate the initialization to the method set_first_name ():
        self.set_first_name(first_name)           # new: here we have control over the new business rule!!!
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

    # old:
    # print("Student Name: ", stud01.first_name, stud01.last_name)

    # old: we don't do things which are not 'allowed!!!!
    # print("Student Name: ", stud01._first_name, stud01._last_name, " direct access on 'proteced value' => not good!")

    # old:
    # print( "Student Name: ", stud01.get_first_name(), stud01.get_last_name(), " ... but 'S-firstnames' are not allowed????")

    # Direct access over our property-variables:
    print("Student Name: ", stud01.first_name, stud01.last_name, " ... now it's correkt!!!!")

    stud01.first_name = "Sarah"
    stud01.last_name = "Steiner"

    print("Student Name: ", stud01.get_first_name(), stud01.get_last_name())

    # print(stud01.__dict__)
    # print(Student.__dict__)



if __name__ == "__main__":
    my_main()

##################
# output:
# Student Name:  S-Name-not-allowed! Mathis  ... now it's correkt!!!!
# Student Name:  S-Name-not-allowed! Steiner
