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

fobj_in = open("names.txt")
fobj_out = open("names2.txt", "w")


