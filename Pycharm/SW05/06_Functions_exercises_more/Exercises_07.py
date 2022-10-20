# Exercises_07.py

###########################
# Task to solve:   1:1 join
###########################

# We have 2 files:
# file A: employ_departement.txt
# file B: employ_since.txt

# you have to merge (join) this two files:
# desired result:
# a) an output
# b) a file 'employ_department_since.txt' with following content:

# Urs,accounting,2018
# Mike,development,2012
# Lila,development,2014
# Sandy,human resources,2019

# This task implements a simple 1:1 join  (in pandas we will use 'merge()' or join())

# In a second step you try to move the same lines of code into a function
# and then call this function twice with different parameters



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