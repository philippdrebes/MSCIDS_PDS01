# Exercises_09.py

###########################
# Task to solve:   n:m join
###########################

# we have 2 files:
# file A: employ_departement.txt
# file B: departement_skills.txt

# you have to merge (join) this two files:
# desired result:
# a) an output
# b) a file with following content:

# Urs,accounting,mathematics
# Urs,accounting,spreadsheet
# Mike,development,programming
# Mike,development,linux
# Lila,development,programming
# Lila,development,linux
# Sandy,human resources,spreadsheet
# Sandy,human resources,organization

# This task implements a simple n:m join  (in pandas we will use 'merge()' or join())

# you can start in this way ....

def elementAppendAdder(liste, element):
    liste.append( element )
    return liste

e_d_list = []
with open( "employ_departement.txt","r" ) as emp_dep_in:
    for line in emp_dep_in:
        my_list = line.rstrip().split( ", " )
        e_d_list = elementAppendAdder(e_d_list, my_list)    # line.rstrip())
    print("e_d_list: " ,e_d_list)

    for i in e_d_list:
        print(i[0], i[1])


# rest is your work!