# Exercises_08.py

###########################
# Task to solve:   1:n join
###########################

# We have 2 files:
# file A: employ_departement_since.txt
# file B: departement_chief.txt

# you have to merge (join) this two files:
# desired result:
# a) an output
# b) a file with following content:

# Urs,accounting,2018,Pascal
# Mike,development,2012,Giuliana
# Lila,development,2014,Giuliana
# Sandy,human resources,2019,Steve

# This task implements a simple 1:n join  (in pandas we will use 'merge()' or join())

# you can start in this way ....

def elementAppendAdder(liste, element):
    liste.append( element )
    return liste

e_d_s_list = []
with open( "employ_department_since.txt","r" ) as emp_dep_sin_in:
    for line in emp_dep_sin_in:
        my_list = line.rstrip().split( "," )
        e_d_s_list = elementAppendAdder(e_d_s_list, my_list)    # line.rstrip())
    print("e_d_s_list: " ,e_d_s_list)

    for i in e_d_s_list:
        print(i[0], i[1], i[2])


# rest is your work!