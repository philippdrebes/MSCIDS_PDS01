# Read and write files

# ************
# Exercise 01
# ************

# Create a file with the name 'names.txt' in which a first name and a surname
# alternate for example like this:

# Fred
# Miller
# Eve
# Turner
# Steve
# Baker
# Elsa
# Brunner
# Hans
# Ruckli
# Silvia
# Muster

# The content of this 'names.txt'-file is to be transferred to another file 'names2.txt'.
# In the second file 'names2.txt' on every line there should be a first name and a surname
# like this output:

# Fred Miller
# Eve Turner
# Steve Baker
# Elsa Brunner
# Hans Ruckli
# Silvia Muster

with open("names.txt") as file_in:
    with open("names2.txt", "w") as file_out:
        while True:
            line1 = file_in.readline()
            line2 = file_in.readline()

            if not line2:
                break  # EOF

            file_out.writelines("{0} {1}\n".format(line1.rstrip(), line2.rstrip()))
