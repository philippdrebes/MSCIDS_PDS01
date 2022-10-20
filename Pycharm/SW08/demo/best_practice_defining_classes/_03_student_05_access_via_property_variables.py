# _03_student_05_access_via_property_variables.py
# Source: https://betterprogramming.pub/advanced-python-9-best-practices-to-apply-when-you-define-classes-871a27af658b
# or
# 9_BestPractices_Python.pdf


# Fifth part of step 3:
# Exactly the same code as in the fourth part ...
#      (i.e. the problem with "Silvana" has not yet been solved ... we solve it in the next 'part'!

# New is the direct (realy!!!) access to the property-variables 'first_name' and 'last_name'.
# Ohhhhh: This allows you to make again without direct assignments,
# e.g. myFirstname = first_name (without getter / setter method)
# Have a look in the Function my_main() below!!!

class Student:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
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

# New:  As info only: 'first_name' and 'last_name' are not 'instance-variables' they are
#      'class-variables' of the type 'property object'....
#       BUT and that is funny:
#       They can be used like instance-variables!
#       Follow the proof below in the my_main () function!

def my_main():
    stud01 = Student("Silvana", "Mathis")              # NEW: Here we have a Problem
                                                       # Our new business rule does not "work"!!!!

    # old:
    # print("Student Name: ", stud01.first_name, stud01.last_name)

    # old: we don't do things which are not 'allowed!!!!
    # print("Student Name: ", stud01._first_name, stud01._last_name, " direct access on 'proteced value' => not good!")

    # old:
    # print( "Student Name: ", stud01.get_first_name(), stud01.get_last_name(), " ... but 'S-firstnames' are not allowed????")

# NEW: Direct access via property-variables (=class-variables!!!)
    print("Student Name: ", stud01.first_name, stud01.last_name, " ... but 'S-firstnames' are not allowed????")

    # old:
    # stud01.set_first_name("Sarah")
    # stud01.set_last_name("Steiner")

# NEW: direct access over our property-variables:
#      the property-variables make access much more natural again (without getter and setter methods!)
    stud01.first_name = "Sarah"
    stud01.last_name = "Steiner"

    print("Student Name: ", stud01.get_first_name(), stud01.get_last_name())

# NEW proof: first_name and last_name are 'class-variables'!!
    print(stud01.__dict__)
    print(Student.__dict__)            # new: here you will find first_name and last_name



if __name__ == "__main__":
    my_main()

##################
# output:
# Student Name:  Silvana Mathis  ... but 'S-firstnames' are not allowed????
# Student Name:  S-Name-not-allowed! Steiner
# {'_first_name': 'S-Name-not-allowed!', '_last_name': 'Steiner', 'status_verified': None, 'guardian': None}
# {'__module__': '__main__', '__init__': <function Student.__init__ at 0x000001BB76527940>,
#  'get_first_name': <function Student.get_first_name at 0x000001BB76527820>,
#  'set_first_name': <function Student.set_first_name at 0x000001BB76527700>,
#  'get_last_name': <function Student.get_last_name at 0x000001BB765273A0>,
#  'set_last_name': <function Student.set_last_name at 0x000001BB767F18B0>,
#  'verify_registration_status': <function Student.verify_registration_status at 0x000001BB767E83A0>,
#  'get_guardian_name': <function Student.get_guardian_name at 0x000001BB7EF761F0>,
#  'set_guardian_name': <function Student.set_guardian_name at 0x000001BB7EF76160>,
#  'get_status': <function Student.get_status at 0x000001BB7EF760D0>,
#  'query_database': <function Student.query_database at 0x000001BB7EF76040>,
#  'first_name': <property object at 0x000001BB764CC130>,
#  'last_name': <property object at 0x000001BB7688C900>,
#  '__dict__': <attribute '__dict__' of 'Student' objects>,
#  '__weakref__': <attribute '__weakref__' of 'Student' objects>,
#  '__doc__': None}
