# Exercises_08_Solution.py

###########################
# Task to solve:   1:n join
###########################

# We have 2 files:
# file A: employ_departement_since.txt
# file B: department_chief.txt

# you have to merge (join) this two files:
# desired result:
# a) an output
# b) a file with following content:

# Urs,accounting,2018,Pascal
# Mike,development,2012,Giuliana
# Lila,development,2014,Giuliana
# Sandy,human resources,2019,Steve

# This task implements a simple 1:n join  (in pandas we will use 'merge()' or join())

def elementAppendAdder(liste, element):
    liste.append( element )
    return liste


# put the same lines of code into a function and then call this function twice with different parameters:
def readFile_inList(filenname):
    retlist = []
    with open( filenname, "r" ) as somewhat_in:
        for line in somewhat_in:
            my_list = line.rstrip().split( "," )
            retlist = elementAppendAdder( retlist, my_list )
        return retlist


e_d_s_list = readFile_inList("employ_department_since.txt")
d_c_list = readFile_inList("department_chief.txt")


print("*"* 60)
e_d_s_c_List = []          # join 1:n
for i in e_d_s_list:
    tempList = []
    for j in d_c_list:
        if i[1]==j[0]:         # compare 2. column in e_d_s_list with 1. column in d_c_list
            tempList = i[0] + ", " + i[1] + ", " + i[2]+ ","  + j[1]
            e_d_s_c_List = elementAppendAdder( e_d_s_c_List, tempList )

print("e_d_s_c_List: ", e_d_s_c_List)
print("*"* 60)

res1 = str(e_d_s_c_List).strip('[]')
print("res1: ", res1)

res2 = str(res1).replace(" '","")
res2 = str(res2).replace("'","")
res2 = str(res2).replace(", ",",")
print("res2: ", res2)

with open( "employ_department_since_chief.txt", "w" ) as e_d_s_out:
    countChar = 0
    countComma = 0
    for myChar in res2:
        if myChar == ",":
            countComma += 1
        if countComma%4 == 0 and countComma != 0:
            res2 = res2[: countChar] + "\n" + res2[countChar+1:]
            countComma = 0
        countChar += 1
    e_d_s_out.write( res2 )

print()
print("employ_department_since_chief.txt: ", res2, sep="\n")