# Read and write files
# Solution Exercise 01

fh_in  = open("musicians.txt", "r")
fh_out = open("musicians2.txt", "w")
counter = 0
new_line = ""
for line in fh_in:
    line = line.rstrip()
    if counter % 3 == 0:
        if counter:
            fh_out.write(new_line + "\n")
        new_line = line
    elif counter % 3 == 1:
        new_line += " " + line
    else:
        new_line += " (" + line.upper() + ")"
    counter += 1
fh_out.close()
fh_in.close()