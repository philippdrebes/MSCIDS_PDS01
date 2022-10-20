# Exercises_08.py

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

# you can start in this way ....


employees = {}
departments = {}
with open('employ_department_since.txt', 'r') as emp_in:
    for line in emp_in:
        data = line.rstrip().split(',')
        employees[data[0]] = {'department': data[1], 'since': data[2]}

with open('department_chief.txt', 'r') as dep_chief_in:
    for line in dep_chief_in:
        data = line.rstrip().split(', ')
        departments[data[0]] = data[1]

print('employees: ', employees)
print('departments: ', departments)

with open('employ_department_since_chief.txt', 'w') as outfile:
    for e in employees:
        dep = employees[e]['department']
        line = ','.join([e, dep, employees[e]['since'], departments[dep]]) + '\n'
        print(line, end='')
        outfile.write(line)
