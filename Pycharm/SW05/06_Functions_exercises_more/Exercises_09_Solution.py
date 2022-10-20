# Exercises_09_Solution.py

###########################
# Task to solve:   n:m join
###########################

# we have 2 files:
# file A: employ_department.txt
# file B: department_skills.txt

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


def elementAppendAdder(liste, element):
    liste.append( element )
    return liste


# put the same lines of code into a function and then call this function twice with different parameters:
def readFile_inList(filenname):
    retlist = []
    with open( filenname, "r" ) as somewhat_in:
        for line in somewhat_in:
            my_list = line.rstrip().split( ", " )         # or split(",")
            retlist = elementAppendAdder( retlist, my_list )
        return retlist

e_d_list = readFile_inList("employ_department.txt")
d_s_list = readFile_inList("department_skills.txt")

print("*"* 60)
e_d_sk_List = []          # join n:m
for i in e_d_list:
    tempList = []
    for j in d_s_list:
        if i[1]==j[0]:
            tempList = i[0] + "," + i[1] + "," + j[1]
            e_d_sk_List = elementAppendAdder( e_d_sk_List, tempList )

print("e_d_sk_List: ", e_d_sk_List)
print("*"* 60)

res1 = str(e_d_sk_List).strip('[]')
print("res1: ", res1)

res2 = str(res1).replace(" '","")
res2 = str(res2).replace("'","")
print("res2: ", res2)

with open( "employ_department_skills.txt", "w" ) as e_d_s_out:
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
print("employ_department_skills.txt: ", res2, sep="\n")
