# Variable with id(), is and ==
*2020-04 mae, it-gro*

**identical or just the same?**
<hr>


**id()**

* [https://docs.python.org/3/library/functions.html#id](https://docs.python.org/3/library/functions.html#id) \
  Return the “identity” of an object. 
  This is an integer which is guaranteed to be unique and 
  constant for this object during its lifetime.


**is**
  
* [https://docs.python.org/3/reference/expressions.html#is](https://docs.python.org/3/reference/expressions.html#is) \
  The operators is and is not test for an object’s identity: 
  x is y is true if and only if x and y are the same object. 
  An Object’s identity is determined using the id() function.


**value-comparisons**

* [https://docs.python.org/3/reference/expressions.html#value-comparisons ](https://docs.python.org/3/reference/expressions.html#value-comparisons) \
  The operators <, >, ==, >=, <=, and != compare the values of two objects. 
  The objects do not need to have the same type.    

Use [http://pythontutor.com/visualize.html#mode=edit](http://pythontutor.com/visualize.html#mode=edit) to see what is going on

## id()
### int


```python
a = 1
b = 1
print(id(a))
print(id(b))
```

    10914496
    10914496



```python
a = 257
b = 257
print(id(a))
print(id(b))
```

    140193238153712
    140193238153424


## id(), is, ===
### Lists


```python
a = [81, 82, 83]
print(id(a))

b = [81, 82, 83]
print (id(b))
print(a is b)
print(a == b)

c = a
print (id(c))
print(a is c)
print(a == c)
```

    140193238501512
    140193238501960
    False
    True
    140193238501512
    True
    True



```python
a = []
print(id(a))
b = []
print (id(b))
print(a is b)
print(a == b)
```

    140193238138568
    140193238481096
    False
    True


### Tuples


```python
a = (81, 82, 83)
print(id(a))

b = (81, 82, 83)
print (id(b))
print(a is b)
print(a == b)

c = a
print (id(c))
print(a is c)
print(a == c)
```

    140193238488120
    140193238489272
    False
    True
    140193238488120
    True
    True



```python
a = ()
print(id(a))
b = ()
print (id(b))
print(a is b)
print(a == b)
```

    140193444814920
    140193444814920
    True
    True


### Strings


```python
a = "Python is cool"
print(id(a))

b = "Python is cool"
print (id(b))
print(a is b)
print(a == b)

c = a
print (id(c))
print(a is c)
print(a == c)
```

    140193238171312
    140193238305648
    False
    True
    140193238171312
    True
    True



```python
a = "Python"
print(id(a)) 
b = "Python"
print (id(b))
print(a is b)
print(a == b)
```

    140193443648320
    140193443648320
    True
    True


### Lists (Colors)

Run also with [http://pythontutor.com/visualize.html#mode=edit](http://pythontutor.com/visualize.html#mode=edit)

#### Example 1


```python
colours1 = ["red", "blue"]
colours2 = colours1
colours3 = colours1
print("colours1, id:", colours1, id(colours1))
print("colours2, id:", colours2, id(colours2))
print("colours3, id:", colours3, id(colours3))

print("%s %5r, %s %5r" % ("colours1 == colours2:", colours1 == colours2, 
                          "colours1 is colours2:", colours1 is colours2) )
print("%s %5r, %s %5r" % ("colours1 == colours3:", colours1 == colours3, 
                          "colours1 is colours3:", colours1 is colours3))

print("\n ********* we change colours2 and colors3 now *********")
colours2 = ["rot", "blau"]
colours3 = ["red", "blue"]
print("colours1, id:", colours1, id(colours1))
print("colours2, id:", colours2, id(colours2))
print("colours3, id:", colours3, id(colours3))

print("\nAfter update of 'colours2 and colors3': ")
print("%s %5r, %s %5r" % ("colours1 == colours2:", colours1 == colours2, 
                          "colours1 is colours2:", colours1 is colours2))
print("%s %5r, %s %5r" % ("colours1 == colours3:", colours1 == colours3, 
                          "colours1 is colours3:", colours1 is colours3))

```

    colours1, id: ['red', 'blue'] 140193237951432
    colours2, id: ['red', 'blue'] 140193237951432
    colours3, id: ['red', 'blue'] 140193237951432
    colours1 == colours2:  True, colours1 is colours2:  True
    colours1 == colours3:  True, colours1 is colours3:  True
    
     ********* we change colours2 and colors3 now *********
    colours1, id: ['red', 'blue'] 140193237951432
    colours2, id: ['rot', 'blau'] 140193237951688
    colours3, id: ['red', 'blue'] 140193237951496
    
    After update of 'colours2 and colors3': 
    colours1 == colours2: False, colours1 is colours2: False
    colours1 == colours3:  True, colours1 is colours3: False


#### Example 2


```python
red = "red"
blue = "blue"
colours1 = [red, blue]
colours2 = [red, blue]
colours3 = [red, blue]

print("colours1, id:", colours1, id(colours1))
print("colours2, id:", colours2, id(colours2))
print("colours3, id:", colours3, id(colours3))

print("%s %5r, %s %5r" % ("colours1 == colours2:", colours1 == colours2, 
                          "colours1 is colours2:", colours1 is colours2))
print("%s %5r, %s %5r" % ("colours1 == colours3:", colours1 == colours3, 
                          "colours1 is colours3:", colours1 is colours3))

print("\n ********* we change colours2 now *********")
colours2 = ["rot", "blau"] 
print("colours1, id:", colours1, id(colours1))
print("colours2, id:", colours2, id(colours2))

print("\nAfter update of 'colours2': ")
print("%s %5r, %s %5r" % ("colours1 == colours2:", colours1 == colours2, 
                          "colours1 is colours2:", colours1 is colours2))

print("\n ********* we change blue and colors3 now *********")
blue = "blau"
colours3 = [red, blue]
print("colours1, id:", colours1, id(colours1))
print("colours3, id:", colours3, id(colours3))

print("\nAfter update of 'colours3': ")
print("%s %5r, %s %5r" % ("colours1 == colours3:", colours1 == colours3, 
                          "colours1 is colours3:", colours1 is colours3))

```

    colours1, id: ['red', 'blue'] 140193237952904
    colours2, id: ['red', 'blue'] 140193238441544
    colours3, id: ['red', 'blue'] 140193237951432
    colours1 == colours2:  True, colours1 is colours2: False
    colours1 == colours3:  True, colours1 is colours3: False
    
     ********* we change colours2 now *********
    colours1, id: ['red', 'blue'] 140193237952904
    colours2, id: ['rot', 'blau'] 140193237952968
    
    After update of 'colours2': 
    colours1 == colours2: False, colours1 is colours2: False
    
     ********* we change blue and colors3 now *********
    colours1, id: ['red', 'blue'] 140193237952904
    colours3, id: ['red', 'blau'] 140193237951688
    
    After update of 'colours3': 
    colours1 == colours3: False, colours1 is colours3: False



```python

```
