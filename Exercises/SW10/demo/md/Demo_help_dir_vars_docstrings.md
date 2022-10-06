# help(), docstrings, dir(), vars()
*2020-04, Bruno Grossniklaus, https://github.com/it-gro*

**Some useful built-in helper functions**
<hr>

**built-in-functions**

* [https://docs.python.org/3/library/functions.html#built-in-functions](https://docs.python.org/3/library/functions.html#built-in-functions) \
    The Python interpreter has a number of functions and types built into it that
    are always available.


**help()**

*  [https://docs.python.org/3/library/functions.html#help](https://docs.python.org/3/library/functions.html#help) \
    Invoke the built-in help system. (This function is intended for interactive
    use.) If no argument is given, the interactive help system starts on the
    interpreter console. If the argument is a string, then the string is looked up
    as the name of a module, function, class, method, keyword, or documentation
    topic, and a help page is printed on the console.


**docstrings**

* [https://www.python.org/dev/peps/pep-0008/#documentation-strings](https://www.python.org/dev/peps/pep-0008/#documentation-strings) \
    Write docstrings for all public modules, functions, classes, and
    methods. Docstrings are not necessary for non-public methods, but you should
    have a comment that describes what the method does. This comment should appear
    after the def line.
  * [https://realpython.com/documenting-python-code](https://realpython.com/documenting-python-code)
    * [https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings](https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings)


**dir()**

* [https://docs.python.org/3/library/functions.html#dir](https://docs.python.org/3/library/functions.html#dir) \
    Without arguments, return the list of names in the current local scope. With an
    argument, attempt to return a list of valid attributes for that object.


**vars()**

* [https://docs.python.org/3/library/functions.html#vars](https://docs.python.org/3/library/functions.html#vars) \
    Return the __dict__ attribute for a module, class, instance, or any other
    object with a __dict__ attribute.
    


<hr>

## help()
* [https://docs.python.org/3/library/functions.html#help](https://docs.python.org/3/library/functions.html#help)


```python
# help()
```


```python
help(print)
```

    Help on built-in function print in module builtins:
    
    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
    


## docstrings
* [https://www.python.org/dev/peps/pep-0008/#documentation-strings](https://www.python.org/dev/peps/pep-0008/#documentation-strings)
* [https://www.python.org/dev/peps/pep-0257](https://www.python.org/dev/peps/pep-0257)


```python
"""
This is our Robot class

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque nulla ex,
auctor varius est vel, aliquam semper dui. Ut auctor quam dui, ac volutpat nisi
fringilla et. Aenean lobortis lacus ac eros vehicula cursus. Duis varius
tristique tincidunt. Nullam euismod sodales ante, vitae aliquam felis volutpat
et.

"""

class Robot:
    '''
    Our Robot
    
    They are everywhere...
    Etiam auctor eu quam a ornare. Vivamus purus nisi, dapibus volutpat tortor et,
    aliquet laoreet lectus. Phasellus id lectus vel turpis elementum
    porttitor. Nunc iaculis interdum massa eget gravida.
    '''

    def __init__(self, name):
        '''
        @param name: the robots name
        
        Morbi placerat aliquet quam in accumsan. Maecenas et mauris tincidunt,
        ultricies mi id, imperdiet velit. Suspendisse at ultrices lacus, eget rutrum
        massa. Donec et elit ac diam porttitor aliquam. Nunc tristique convallis elit
        sed porttitor. Curabitur eu nibh mollis, facilisis tortor id, cursus augue.
        
        '''
        self.name = name
        self._broken = False

    def say_hi(self):
        '''
        Be friendly    
        :return:
        '''
        print("Hi, I am " + self.name)

    def get_id(self):
        '''
        Get the internal id string 
        :return: id string
        '''
        id = ""
        for i in self.name:
            id += str(ord(i))
        return id

r = Robot("Marvin")
print(r.get_id())


```

    7797114118105110



```python
help(Robot)
```

    Help on class Robot in module __main__:
    
    class Robot(builtins.object)
     |  Our Robot
     |  
     |  They are everywhere...
     |  Etiam auctor eu quam a ornare. Vivamus purus nisi, dapibus volutpat tortor et,
     |  aliquet laoreet lectus. Phasellus id lectus vel turpis elementum
     |  porttitor. Nunc iaculis interdum massa eget gravida.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, name)
     |      @param name: the robots name
     |      
     |      Morbi placerat aliquet quam in accumsan. Maecenas et mauris tincidunt,
     |      ultricies mi id, imperdiet velit. Suspendisse at ultrices lacus, eget rutrum
     |      massa. Donec et elit ac diam porttitor aliquam. Nunc tristique convallis elit
     |      sed porttitor. Curabitur eu nibh mollis, facilisis tortor id, cursus augue.
     |  
     |  get_id(self)
     |      Get the internal id string 
     |      :return: id string
     |  
     |  say_hi(self)
     |      Be friendly    
     |      :return:
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    



```python
help(r.get_id)
```

    Help on method get_id in module __main__:
    
    get_id() method of __main__.Robot instance
        Get the internal id string 
        :return: id string
    


<hr>

## dir()
* [https://docs.python.org/3/library/functions.html#dir](https://docs.python.org/3/library/functions.html#dir) \
The default dir() mechanism behaves differently with different types of
objects, as it attempts to produce the most relevant, rather than complete,
information:
     * If the object is a module object, the list contains the names of the module’s
       attributes.
     * If the object is a type or class object, the list contains the names of its
       attributes, and recursively of the attributes of its bases.
     * Otherwise, the list contains the object’s attributes’ names, the names of
       its class’s attributes, and recursively of the attributes of its class’s
       base classes.



* [https://docs.python.org/3/library/stdtypes.html#special-attributes](https://docs.python.org/3/library/stdtypes.html#special-attributes)



```python
dir()
```




    ['In',
     'Out',
     'Robot',
     '_',
     '__',
     '___',
     '__builtin__',
     '__builtins__',
     '__doc__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     '_dh',
     '_i',
     '_i1',
     '_i2',
     '_i3',
     '_i4',
     '_i5',
     '_i6',
     '_ih',
     '_ii',
     '_iii',
     '_oh',
     'exit',
     'get_ipython',
     'quit',
     'r']




```python
dir(Robot)
```




    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     'get_id',
     'say_hi']




```python
dir(r)
```




    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     '_broken',
     'get_id',
     'name',
     'say_hi']




```python
r.__dict__
```




    {'name': 'Marvin', '_broken': False}




```python
r.__doc__
```




    '\n    Our Robot\n    \n    They are everywhere...\n    Etiam auctor eu quam a ornare. Vivamus purus nisi, dapibus volutpat tortor et,\n    aliquet laoreet lectus. Phasellus id lectus vel turpis elementum\n    porttitor. Nunc iaculis interdum massa eget gravida.\n    '



<hr>

## vars()
* [https://docs.python.org/3/library/functions.html#vars](https://docs.python.org/3/library/functions.html#var) \
    Return the __dict__ attribute for a module, class, instance, or any other
    object with a __dict__ attribute.



```python
vars(r)
```




    {'name': 'Marvin', '_broken': False}


