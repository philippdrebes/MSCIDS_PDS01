# an iterator. needs __next__ and __iter__
class Reverse:
    """
    Creates Iterators for looping over a sequence backwards.
    """

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self # an iterator is also in iterable, so it needs __iter__. This can just return self, b/c it's already in iterator

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

# an iterable needs __iter__. This one uses Reverse from above.
class Classroom:
    def __init__(self, students):
        self.students = students
    def __iter__(self): # called by the built=in iter function
        return Reverse(self.students) # returns an iterator


MyClassroom = Classroom(["Mark", "Agnes", "Urs", "Patricia"])

my_iterator = iter(MyClassroom)
my_other_iterator = iter(my_iterator)
print(my_iterator is my_other_iterator) # True. These are the same objects because Reverse.__iter__ returns self

print("=" * 20)

# testing whether an object is an iterator and/or an iterable
from collections.abc import Iterator, Iterable
print("MyClassroom")
print("Iterable: ", isinstance(MyClassroom, Iterable)) # True: MyClassroom has an __iter__() - method
print("Iterator: ", isinstance(MyClassroom, Iterator)) # False: MyClassroom doesn't have __next__()

print("my_iterator")
print("Iterable: ", isinstance(my_iterator, Iterable)) # True: my_iterable has an __iter__() - method
print("Iterator: ", isinstance(my_iterator, Iterator)) # True: my_iterable has a __next__() - method

print("=" * 20)
# iterating with a for loop
for student in MyClassroom:
    print(student)

print("=" * 20)
# internally, what Python translates the above for loop into is equivalent to the following
my_iterator = iter(MyClassroom)
while my_iterator:
    try:
        student = next(my_iterator)
        print(student)
    except StopIteration:
        break

# The point of the whole design of this interface is to let users create their own iterables, like Classroom above.

