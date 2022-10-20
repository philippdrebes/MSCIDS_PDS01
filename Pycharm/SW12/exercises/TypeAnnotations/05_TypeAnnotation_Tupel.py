# 05_TypeAnnotation_Tuple.py

# in the 'typing' module there is also a 'Tuple' type ... in addition to the already known 'List' type!
# This is also a good example of a list comprehension! (We will learn that in a moment!).
# The brackets [...] can even be omitted, but then it is no longer obviously clear
# that it is a list comprehension (on line 27)!

# Note: Some Python Tip!
# 1. Generally, lists are for looping;
# 2. tuples for structs.
# 3. lists are often homogeneous;
# 4. tuples are often heterogeneous.
# 5. lists are for variable length of data
# 6. tuples length is immutable!


# Question:
# How can you change the next program so that Mypy doesn't display any errors?
# The program works without any Problem ... but there is an error of thought!

from typing import List, Tuple
Artikel = Tuple[int, str, float]
Einkauf = List[Artikel]


def aufsummieren(warenkorb: Einkauf) -> float:
    total = sum([anz * preis for anz, nr, txt, preis in warenkorb])
    return total


korb = [(2, 68978, "Orangen", 3.98),
        (1, 70876, "Milch", 1.19),
        (3, 87866, "Mineralwasser", 3.49)]


print("aufsummieren(korb):", aufsummieren(korb))
