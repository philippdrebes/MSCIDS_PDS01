# with-Anweisung
#
# Use if possible (no "mandatory (!!)") always 'with' when handling files!
# Then the file object (fobj) is always closed automatically!

print("\nPart 1: ", "*" * 60, "\n")
with open("lorem_ipsum.txt") as fobj:
    for line in fobj: 
        print(line.rstrip())
        # 'fobj' is closed automatically!!!

print("\nPart 2: ", "*" * 60, "\n")
# The example from the book still has an error in the output !!!!
# (i.e. no line break!)
# Exercise:  Try to correct this mistake yourself!

with open("lorem_ipsum.txt") as fobj_in:
    with open("lorem_ipsum_2.txt", "w") as fobj_out:
        counter = 0
        for line in fobj_in:
            counter += 1
            out = "{0:>3s} {1:s}\n".format(str(counter), line)
            fobj_out.write(out.rstrip())

with open("lorem_ipsum_2.txt") as fobj:
    for line in fobj:
        print(line.rstrip())
# 'fobj' is closed automatically!!!

print("\nPart 3: ", "*" * 60, "\n")
# Use of '\' so that you don't have to indent too much
# we use here only ONE 'with' !!!

with open("lorem_ipsum.txt", "r") as fobj_in, \
     open("lorem_ipsum_2.txt", "w") as fobj_out:
    counter = 0
    for line in fobj_in:
        counter += 1
        out_line = "{0:>5s} {1:s}\n".format(str(counter), line.rstrip())
        # out_line = "{0:>5s} {1:s}\n".format(str(counter),line)  # why doesn't this line work?
        # try out PyCharm:
        #   Settings / Editor / General / Appearance / Show whitespaces
        fobj_out.write(out_line)

with open("lorem_ipsum_2.txt") as fobj:
    for line in fobj:
        print(line.rstrip())
    fobj.close()
