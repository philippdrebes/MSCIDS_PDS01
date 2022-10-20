# 30_docstring_solution.py
# Solution: Use of Docstring

# very simple function that returns a simple greeting!
def say_hello(name):
    """
    Gives a person called by name xy
    a 'hello xy' back

    :param name: name of the person to be greeted
    :return: Returns a 'Hello ...'!
    """ 

    createHello = "Hello" + name
    return createHello

# now follows a 'main' function
def main():
    """
    Start the desired commands in the written
    sequence (like a script!)
    :return: nan
    """


    n = "Michael"
    n = say_hello( n )
    print( n )
    name = "Kirstin"
    greeting = say_hello( name )
    print( greeting )
    print()
    print( say_hello.__doc__)
    print( main.__doc__)


# we will use this line when using modules
# explain more detailed.
if __name__ == "__main__":
    main()