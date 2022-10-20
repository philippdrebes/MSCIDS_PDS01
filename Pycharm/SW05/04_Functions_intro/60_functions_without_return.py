# 60_ functions_without_return.py

# Functions without return
# 'pass' is a null operation — when it is executed, nothing happens.
# It is useful as a placeholder when a statement is required syntactically,
# but no code needs to be executed

# For functions without return statements, the 'None'-object is returned!
def f():
    pass


x = f()
print( x )

x == None
print( x == None )


print("\n","*"*60,"\n")

# None is also returned if a return-statement terminates a function
# without a following expression, see example below:
def f():
    return
    # nothing follows!!!


x == None

print( x )
print( x == None )