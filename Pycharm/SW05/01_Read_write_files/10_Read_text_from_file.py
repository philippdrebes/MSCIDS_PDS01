# read an file (and ouput the content)
# the file "lorem_ipsum.txt" has to be on the same directory as Python file!

fobj = open("lorem_ipsum.txt")
print("fobj: ", fobj)  # fobj is a (file-)object form type '_io.TextIOWrapper'
fobj.close()

print("\n", "*" * 60, "\n")

fobj = open("lorem_ipsum.txt")
for line in fobj:
    print(line.rstrip())
    # print(line)
    # print(line, end="")
fobj.close()
