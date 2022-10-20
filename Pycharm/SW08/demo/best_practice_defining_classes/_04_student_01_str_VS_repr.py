# _04_student_01_str_VS_repr.py
# Source: https://betterprogramming.pub/advanced-python-9-best-practices-to-apply-when-you-define-classes-871a27af658b
# or
# 9_BestPractices_Python.pdf


# First part of step 4:
# Two special methods, __repr__ and __str__, are essential for creating proper string representations
# of your custom class, which will give the code readers more intuitive information about your classes.

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.status_verified = None
        self.guardian = None

# NEW ###################################
    def __repr__(self):
        return f"Student({self.first_name!r}, {self.last_name!r})"

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"
# NEW end ###############################

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
# NEW ##############
    print("stud01.__str__():  ", stud01.__str__())
    print("stud01.__repr__(): ", stud01.__repr__())


    print("*"* 50)
    # with __repr__() and eval you can create a an new Student-object:
    stud02 = eval(stud01.__repr__())
    print("stud02: ", stud02)
# New end ##########


if __name__ == "__main__":
    my_main()


###############
# output:
# stud01:  Student: Jenny Ulrich
# stud01.__str__():   Student: Jenny Ulrich
# stud01.__repr__():  Student('Jenny', 'Ulrich')
# **************************************************
# stud02:  Student: Jenny Ulrich

