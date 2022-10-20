# Ramón  V01
# Erwin  V02

# for a good visual view => use https://pythontutor.com/visualize.html#mode=display 
# and you will see all ....


class Student:
    _priv_name = 'default name'

    def __init__(self, f_name, l_name):
        self._priv_name = f_name + ' ' + l_name                 # don't do it => Now you have 2 variables with the same
                                                                # name: a class-variable AND an instance variable
                                                                # USE: https://pythontutor.com/visualize.html#mode=display 
                                                                # to show your problem! 
                                                
        print("__init__: ", self._priv_name)

        print(1, self.__dict__)
        print(2, Student.__dict__)



    @property
    def name(self):
        return(self.prop_name)

    @name.setter
    def name(self, name):
        self.prop_name = name


print(Student._priv_name)                      #  => klassenVariable ausgabe!)
stu = Student('test','stud')                   #
print("script:", stu._priv_name)               # MRO (Method Resolution Order: Object => Class => Parent Class
# print(stu.prop_name)                           # don't work!  Object has NOW no pro_name Attribute (NOT OO - like!)
print(3, stu.__dict__)
print(4, Student.__dict__)


stu.name = 'new dude'                          # @name.setter is called
print(stu.prop_name)                           # Get the attribut prop_name back!

print(5, stu.__dict__)
print(6, Student.__dict__)

print(Student._priv_name)                      # show Class_Variable !! 