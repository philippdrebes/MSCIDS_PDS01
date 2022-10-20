# The read () and readlines () methods
# Read the text to this examples!
# import locale

# print(locale.getpreferredencoding())

lorem_1a = open("lorem_ipsum.txt")
print("type(lorem_1a): ", type(lorem_1a))   # <class '_io.TextIOWrapper'>
print("lorem_1a: ", lorem_1a)               # <_io.TextIOWrapper name='lorem_ipsum.txt' mode='r' encoding='cp1252'>


lorem_1 = open("lorem_ipsum.txt").readlines()    # ....hmmm no need of close() method?
print("type(lorem_1): ", type(lorem_1))          # <class 'list'>
print("With 'readlines()': ", lorem_1)           # the result is a 'list' of strings


# we can select the third element of the list:
print("lorem_[2]: ", lorem_1[2])

print("\n", "*" * 60, "\n")
# What is the difference between read() and readlines()?
# read() puts the hole file-text in a "string"
# readlines(): every line is an element of a list

lorem_2a = open("lorem_ipsum.txt")
print("type(lorem_2a): ", type(lorem_2a))
print("lorem_2a: ", lorem_2a)


lorem_2 = open("lorem_ipsum.txt").read()
print("type(lorem_2): ", type(lorem_2))
print("With 'read()': ", lorem_2)

print(lorem_2[8:18])


print("\n", "*" * 60, "\n")
# readlines): reads one line of the textfile

lorem_3 = open("lorem_ipsum.txt").readline()
print("type(lorem_3): ", type(lorem_3))
print("With 'readline()': ", lorem_3)

print(lorem_3[8:18])

print("\n", "*" * 60, "\n")
