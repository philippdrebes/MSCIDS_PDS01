# Read and write files

# ************
# Exercise 03
# ************

# Change the solution of Exercise 02 so that the program writes the output to the file 'musicians2.txt'.

with open("musicians.txt") as file:
    with open("musicians2.txt", "w") as out:
        while True:
            line1 = file.readline()
            line2 = file.readline()
            line3 = file.readline()

            if not line3:
                break  # EOF

            out.writelines("{0} {1} ({2})\n".format(line1.rstrip(), line2.rstrip(), line3.rstrip().upper()))
