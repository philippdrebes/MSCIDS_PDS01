# Maybe you will need this information for an exercise ;-) !!
#
#
# Two functions, which "append" something to a list ...
#
# Question: What's the difference?
# Try it out yourself!

 

def elementAppendAdder(liste, element):
    liste.append( element )
    return liste

def elementExtendAdder(liste, element):
    liste.extend( element )
    return liste


def main():
    myList = [1, 2, 4]
    print("myList: ", myList)
    newList = elementAppendAdder( myList,99 )
    print( "AppendAdder: ", newList )


    a, b  = newList[0], newList[-1]
    print( "a, b:", a, ",", b )

    print("*"*60)

    myList = [1, 2, 4]
    print("myList: ", myList)

    newList1 = elementAppendAdder( myList, [99, 100] )
    print( "AppendAdder: ", newList1 )

    print("*"*60)

    myList = [1, 2, 4]
    print("myList: ", myList)

    newList2 = elementExtendAdder( myList, [99, 100] )
    print( "ExtendedAdder: ", newList2 )

if __name__ == "__main__":
    main()