# 30_docstring.py

# Use of Docstring
# Task: Add say_hello (...) and main () with
# meaningful docstring!

# very simple function that returns a simple greeting!
def say_hello (name):
     return "Hello" + name



# now follows a 'main' function
def main ():
     n = "Michael"
     n = say_hello (n)
     print (n)
     name = "Kirstin"
     greeting = say_hello (name)
     print (greeting)


# we will use this line when using modules
# explain more detailed.
if __name__ == "__main__":
    main()