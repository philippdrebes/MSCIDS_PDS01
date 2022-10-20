# Read and write files
# Solution Exercise 02

fh = open("musicians.txt")
counter = 0
new_line = ""
for line in fh:
    line = line.rstrip()
    if counter % 3 == 0:
        if counter:
            print(new_line)
        new_line = line
    elif counter % 3 == 1:
        new_line += " " + line
    else:
        new_line += " (" + line.upper() + ")"
    counter += 1
fh.close()       