# Exercises_09.py

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

# you can start in this way ....

employees = {}
departments = {}
with open('employ_department.txt', 'r') as emp_in:
    for line in emp_in:
        data = line.rstrip().split(', ')
        employees[data[0]] = data[1]

with open('department_skills.txt', 'r') as dep_in:
    for line in dep_in:
        data = line.rstrip().split(', ')

        if data[0] in departments:
            departments[data[0]].append(data[1])
        else:
            departments[data[0]] = [data[1]]

print('employees: ', employees)
print('departments: ', departments)

with open('employ_department_skills.txt', 'w') as outfile:
    for e in employees:
        dep = employees[e]
        for skill in departments[dep]:
            line = ','.join([e, dep, skill]) + '\n'
            print(line, end='')
            outfile.write(line)
