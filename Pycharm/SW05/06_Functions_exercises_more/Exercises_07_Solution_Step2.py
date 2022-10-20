# Exercises_07_Solution_Step2.py

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
# and then call this function twice with different parameters  => solved in this step2!!!!

def elementAppendAdder(liste, element):
    liste.append( element )
    return liste

# put the same lines of code into a function and then call this function twice with different parameters:
def readFile_inList(filenname):
    e_d_list = []
    with open( filenname, "r" ) as emp_dep_in:
        for line in emp_dep_in:
            my_list = line.rstrip().split( ", " )
            e_d_list = elementAppendAdder( e_d_list, my_list )  # line.rstrip())
        return e_d_list

e_d_list = readFile_inList("employ_departement.txt")

# e_d_list = []
# with open( "employ_departement.txt","r" ) as emp_dep_in:
#     for line in emp_dep_in:
#         my_list = line.rstrip().split( ", " )
#         e_d_list = elementAppendAdder(e_d_list, my_list)    # line.rstrip())
#     print("e_d_list: " ,e_d_list)
#
#     for i in e_d_list:
#         print(i[0], i[1])

e_s_list = readFile_inList("employ_since.txt")

# print("*"* 60)
# e_s_list = []
# with open( "employ_since.txt", "r" ) as emp_sin_in:
#     for line in emp_sin_in:
#         my_list = line.rstrip().split( ", " )
#         e_s_list = elementAppendAdder( e_s_list, my_list )
#     print("e_d_list: " ,e_s_list)
#
#     for i in e_s_list:
#         print(i[0], i[1])

print("*"* 60)
e_d_s_List = []          # join 1:1
for i in e_d_list:
    tempList = []
    for j in e_s_list:
        if i[0]==j[0]:
            tempList = i[0] + "," + i[1] + "," + j[1]
            e_d_s_List = elementAppendAdder( e_d_s_List, tempList )

print("e_d_s_List: ", e_d_s_List)
print("*"* 60)

res1 = str(e_d_s_List).strip('[]')
print("res1: ", res1)

res2 = str(res1).replace(" '","")
res2 = str(res2).replace("'","")
print("res2: ", res2)

with open( "employ_department_since.txt", "w" ) as e_d_s_out:
    countChar = 0
    countComma = 0
    for myChar in res2:
        if myChar == ",":
            countComma += 1
        if countComma%3 == 0 and countComma != 0:
            res2 = res2[: countChar] + "\n" + res2[countChar+1:]
            countComma = 0
        countChar += 1
    e_d_s_out.write( res2 )

print()
print("employ_department_since.txt: ", res2, sep="\n")
