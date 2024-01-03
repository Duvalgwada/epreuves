# Prochain nombre Premier

import sys

n = int(input("Entrez un nombre premier : "))

def est_nombre_premier(nombre):
    if nombre <= 1:
        return False
    if nombre == 2:
        return True
    if nombre % 2 == 0:
        return False
    for i in range(3, int(nombre**0.5) + 1, 2):
        if nombre % i == 0:
            return False
    return True

def premier_superieur(n):
    if n <= 1:
        n = 2
    else:
        n += 1

    while True:
        if est_nombre_premier(n):
            return n
        n += 1

resultat = premier_superieur(n)
print(f"Le premier nombre premier supérieur à {n} est {resultat}")
