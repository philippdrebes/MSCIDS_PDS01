# 05_TypeAnnotation_Tuple_Solution.py

# Question:
# How can you change the next program so that Mypy doesn't display any errors?
# The program works without any Problem ... but there is an error of thought!

# Answer: change the number of elements on line 10

from typing import List, Tuple
Artikel = Tuple[int, int, str, float]      # 4 elements in Tuple instead of 3
Einkauf = List[Artikel]


def aufsummieren(warenkorb: Einkauf) -> float:
    total = sum([anz * preis for anz, nr, txt, preis in warenkorb])
    return total


korb = [(2, 68978, "Orangen", 3.98),
        (1, 70876, "Milch", 1.19),
        (3, 87866, "Mineralwasser", 3.49)]

print("aufsummieren(korb):", aufsummieren(korb))
