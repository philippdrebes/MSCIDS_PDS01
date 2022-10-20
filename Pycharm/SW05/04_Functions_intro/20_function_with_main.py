# 20_function_with_main.py
# Programm a main() function  and ... ????
# Solution of 20_function.py

# very simple function that returns a simple greeting!
def say_hello(name):
    return "Hello " + name


# now follows a 'main' function
def main():
    n = "Michael"
    n = say_hello( n )
    print( n )
    name = "Kirstin"
    gruss = say_hello( name )
    print( gruss )

# we will use this line when using modules
# explain more detailed.
if __name__ == "__main__":
	main()


