#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_lambda.php
#
# Lambda, filter, reduce and map
# Lambda Operator
#
# Some like it, others hate it and many are afraid of the lambda operator.
#
# The lambda operator or lambda function is a way to create small anonymous
# functions, i.e. functions without a name. These functions are throw-away
# functions, i.e. they are just needed where they have been created. Lambda
# functions are mainly used in combination with the functions filter(), map()
# and reduce().
#
# The general syntax of a lambda function is quite simple:
#
# lambda argument_list: expression
#
# The argument list consists of a comma separated list of arguments and the
# expression is an arithmetic expression using these arguments. You can assign
# the function to a variable to give it a name.
#


sum = lambda x, y: x + y               # def notation is preferred
print(sum(3, 4))
