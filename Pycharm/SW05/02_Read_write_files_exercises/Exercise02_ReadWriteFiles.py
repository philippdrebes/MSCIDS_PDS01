# Read and write files

# ************
# Exercise 02
# ************

# Write a program that combines three lines from the file 'musicians.txt' into one each
# and outputs them as standard output using print ().

# That means:  An output line should contain the first name, the last name and the artist name ("Künstername") or band of the artist.
# The band or artist name should be outputed in brackets and in captial letters.
# Example "Marshall Bruce Mathers III (EMINEM)"

# Brian
# Molko
# placebo
# Jim
# Morrison
# The Doors
# Ray
# Davies
# The Kinks
# Marshall Bruce
# Mathers III
# Eminem
# Andre Romelle
# Young
# Dr. Dre
# Beth
# Gibbons
# Portishead


with open("musicians.txt") as file:
    while True:
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()

        if not line3:
            break  # EOF

        print("{0} {1} ({2})".format(line1.rstrip(), line2.rstrip(), line3.rstrip().upper()))
