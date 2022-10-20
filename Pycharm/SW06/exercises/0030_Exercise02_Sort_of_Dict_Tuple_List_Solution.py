# Autor: Markus Blaser 

# Exercises 02 
# einige globalen Variable, welche für verschiedene Verarbeitungen verwendet werden.
input_data = [(2, 7 ,3, 5), (1,5, 2), (4, 1,8 ,6, 2, 4), (2, 3), (2, 1), (0,3,5,2,0)]
pyhtagoras = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
input_data5 = [(3, 7 ,3, 5), (1,5, 2), (3, 1,8 ,6, 2, 4), (2, 3), (2, 1), (0,3,5,2,0)]
input_data6 = [0,1,2,3,4,5]
input_data7 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
input_data8 = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
input_data9 = [{"V" : "S001"}, {"V" : "S002"}, {"VI" : "S001"}, {"VI" : "S005"}, {"VII" : "S005"},{"V" : "S009"}]
input_data10 = { 5, 10, 3, 15, 2, 20 }

# Funktionen für die Sortierfunktion
def last(n):
    return n[-1]


def first(n):
    return n[0]


def second_last(n):
    return n[-2]


def hypothenuse(n):
    return n[0]**2 + n[1]**2


def odd_or_even(n):
    return n[-2] % 2


def by_float(n):
    return n[-1]

# Eine Funktion pro Aufgabe
# Aufgabe 1
def aufgabe1(tuples):
    return sorted(tuples, key=last)


# Aufgabe 2
def aufgabe2(tuples):
    return sorted(tuples, key=first)


# Aufgabe 3
def aufgabe3(tuples):
    return sorted(tuples, key=second_last)


# Aufgabe 4
def aufgabe4(tuples):
    return sorted(tuples, key=hypothenuse)


# Aufgabe 5
def aufgabe5(tuples):
    return sorted(tuples, key=odd_or_even)


# Aufgabe 6
def aufgabe6(tuples):
    rList = list()
    for i in range(len(tuples)):
        if (i % 2) == 0 and not i == (len(tuples) - 1):
            rList.append(tuples[i + 1])
            rList.append(tuples[i])

    return rList


# Aufgabe 7
def aufgabe7(tuples):
    rList = list()
    for element in tuples:
        if len(element) != 0:
            rList.append(element)
    return rList


# Aufgabe 8
def aufgabe8(tuples):
    return sorted(tuples, key=by_float, reverse=True)


# Aufgabe 9
def aufgabe9(tuples):
    distinct_list = set()
    for element in tuples:
        e = next(iter(list(element.values())))
        if e not in distinct_list:
            distinct_list.add(e)
    return distinct_list


# Aufgabe 10
def aufgabe10(tuples):
    min = None
    max = None
    for element in tuples:
        if min is None or min > element:
            min = element
        if max is None or max < element:
            max = element
    return min, max


def main():
    menu = 99
    while menu != 0:
        menu = int(input("Welche Aufgaben soll ausgeführt werden (1 bis 10)?; Abbruch mit 0 "))

        if menu == 1:
            print("Aufgabe 1")
            print("Input:  " + str(input_data))
            print("Output: " + str(aufgabe1(input_data)))
        elif menu == 2:
            print("Aufgabe 2")
            print("Input:  " + str(input_data))
            print("Output: " + str(aufgabe2(input_data)))
        elif menu == 3:
            print("Aufgabe 3")
            print("Input:  " + str(input_data))
            print("Output: " + str(aufgabe3(input_data)))
        elif menu == 4:
            print("Aufgabe 4")
            print("Input:  " + str(pyhtagoras))
            print("Output: " + str(aufgabe4(pyhtagoras)))
        elif menu == 5:
            print("Aufgabe 5")
            print("Input:  " + str(input_data5))
            print("Output: " + str(aufgabe5(input_data5)))
        elif menu == 6:
            print("Aufgabe 6")
            print("Input:  " + str(input_data6))
            print("Output: " + str(aufgabe6(input_data6)))
        elif menu == 7:
            print("Aufgabe 7")
            print("Input:  " + str(input_data7))
            print("Output: " + str(aufgabe7(input_data7)))
        elif menu == 8:
            print("Aufgabe 8")
            print("Input:  " + str(input_data8))
            print("Output: " + str(aufgabe8(input_data8)))
        elif menu == 9:
            print("Aufgabe 9")
            print("Input:  " + str(input_data9))
            print("Output: " + str(aufgabe9(input_data9)))
        elif menu == 10:
            print("Aufgabe 10")
            print("Input:  " + str(input_data10))
            min_max = aufgabe10(input_data10)
            print("MinVal = " + str(min_max[0]) + " MaxVal = " + str(min_max[1]))


if __name__ == "__main__":
    main()