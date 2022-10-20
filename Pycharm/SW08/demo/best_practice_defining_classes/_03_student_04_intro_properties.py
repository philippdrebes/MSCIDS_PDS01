# _03_student_04_intro_properties.py
# Source: https://betterprogramming.pub/advanced-python-9-best-practices-to-apply-when-you-define-classes-871a27af658b
# or
# 9_BestPractices_Python.pdf


# Fourth part of step 3:
# We introduce the property idea.
# Properties can be used to make additional verifications when an object is created or modified.

# As an example: All student first names beginning with an "S" (Sarah, Silvana, Susanna, ...)
#                may not be accepted as a student. (Sorry: Absurd ... I know  ;-) but the rule is simple to program!!)
# =>   This should not be a discrimination but ONLY an example!

class Student:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self.status_verified = None
        self.guardian = None


    def get_first_name(self):
        return self._first_name

    def set_first_name(self, fname):
        if fname[0]=='S'or fname[0]=='s':                  # new 'business-rule' (sorry for this absurd rule ;-)!)
            self._first_name = "S-Name-not-allowed!"       # new 'business-rule' (sorry for this absurd rule ;-)!)
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

# NEW: As part of the class 'student'=> we define 2 new property's:
    first_name = property(fget=get_first_name, fset=set_first_name)
    last_name = property(fget=get_last_name, fset=set_last_name)



def my_main():
    stud01 = Student("Silvana", "Mathis")              # NEW: Here we have a Problem
                                                       # Our new business rule does not "work"!!!!

    # old:
    # print("Student Name: ", stud01.first_name, stud01.last_name)

# new: we don't do things which are not 'allowed!!!!
    # print("Student Name: ", stud01._first_name, stud01._last_name, " direct access on 'proteced value' => not good!")

    print( "Student Name: ", stud01.get_first_name(), stud01.get_last_name(), " ... but 'S-firstnames' are not allowed????")

    stud01.set_first_name("Sarah")
    stud01.set_last_name("Steiner")

    print("Student Name: ", stud01.get_first_name(), stud01.get_last_name())

if __name__ == "__main__":
    my_main()
