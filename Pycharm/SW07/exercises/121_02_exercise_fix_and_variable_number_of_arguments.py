#!/usr/bin/env python3

# 121_02_exercise_fix_and_variable_number_of_arguments.py
# exercise
# Variable Length of Parameters (c)
# a fixed number of positional parameters + followed by any number of parameters

# maybe you need this: Settings - Editor - File Encoding - Project Encoring - UTF8


# give is a list of 'records' (in a file)
# you know:
# first column: surname
# second column: first name
# followed by 0, 1, n sports (in german: "Sportarten")
# e.g.
# Unternährer	Tanja	fitness	gymnastics	handball	volleyball	tennis	surfing
# Juchler	Fritz	soccer	gymnastics	tennis

# Exercise A)
#    Write a function how can read the lines of this file an print out on screen
#    in a function 'sports_per_member_in_list(...) in this way:

#    surname firstname [list of sports]
#    e.g:
#    Unternährer Tanja ['fitness', 'gymnastics', 'handball', 'volleyball', 'tennis', 'surfing']
#    Juchler Fritz ['soccer', 'gymnastics', 'tennis']


# # Exercise B)
#    Write a function how can read the lines of this file an print out on screen
#    in a function 'last_sport_per_member(...) in this way:

#    surname firstname last_sport_in_sportlist
#    e.g.:
#    Unternährer Tanja surfing
#    Juchler Fritz tennis

# in this function we have: two fix parameter: surname, firstname
#                           in *sports are 0,1,n sports
def sports_per_member_in_list():
    pass
# your work


# in this function we have: two fix parameter: surname, firstname
#                           in *sports are 0,1,n sports
def last_sport_per_member():
    pass
# your work


print("\nExercise A: ","*"* 60)

# your work

print("\nExercise B: ","*"* 60)

# your work

#########
# Output:
#########
# Exercise A:  ************************************************************
# Unternährer Tanja ['fitness', 'gymnastics', 'handball', 'volleyball', 'tennis', 'surfing']
# Juchler Fritz ['soccer', 'gymnastics', 'tennis']
# Müller Patricia ['fitness', 'volleyball']
# Fischer Hans ['fitness', 'surfing']
# Aebi Jonas ['soccer', 'handball', 'tennis']
# Amrein Sandra ['gymnastics', 'volleyball', 'surfing']
# Elia Aron ['soccer', 'tennis']
# Hediger Nicole ['handball', 'surfing']
# Geisseler Lukas ['fitness', 'handball', 'tennis']
# Hertwig Pasal ['soccer', 'surfing']
# Jordi Cécile ['fitness', 'tennis']
# Wertz Andrea ['gymnastics', 'volleyball']
# Sprenger Robin ['soccer', 'tennis']
# Wyss Marco ['fitness', 'handball', 'volleyball', 'tennis', 'surfing']
#
# Exercise B:  ************************************************************
# Unternährer Tanja surfing
# Juchler Fritz tennis
# Müller Patricia volleyball
# Fischer Hans surfing
# Aebi Jonas tennis
# Amrein Sandra surfing
# Elia Aron tennis
# Hediger Nicole surfing
# Geisseler Lukas tennis
# Hertwig Pasal surfing
# Jordi Cécile tennis
# Wertz Andrea volleyball
# Sprenger Robin tennis
# Wyss Marco surfing