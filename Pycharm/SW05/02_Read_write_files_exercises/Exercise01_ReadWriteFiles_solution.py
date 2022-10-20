# Read and write files
# Solution Exercise 01

fobj_in = open("names.txt")
fobj_out = open("names2.txt", "w")

output = ""
for line in fobj_in:
    if output:
        output += " " + line.rstrip() + "\n"
        fobj_out.write(output)
        output = ""
    else:
        output = line.rstrip()


fobj_in.close()
fobj_out.close()
