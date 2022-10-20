# Exercises_07.py

###########################
# Task to solve:   1:1 join
###########################

# We have 2 files:
# file A: employ_department.txt
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

employees = {}
with open('employ_department.txt', 'r') as emp_dep_in:
    for line in emp_dep_in:
        data = line.rstrip().split(', ')
        employees[data[0]] = {'department': data[1]}

with open('employ_since.txt', 'r') as emp_sin_in:
    for line in emp_sin_in:
        data = line.rstrip().split(', ')
        employees[data[0]]['since'] = data[1]

print('employees: ', employees)

with open('employ_department_since.txt', 'w') as output:
    for e in employees:
        line = ','.join([e, employees[e]['department'], employees[e]['since']]) + '\n'
        print(line, end='')
        output.write(line)
