# Entre min et max

# creer programme affichant toutes les valeurs comprises dans l'ordre croissant, minimum inclus, maximum exclus

import sys

def valeurs_entre(minimum, maximum):
    if not (isinstance(minimum, (int, float)) and isinstance(maximum, (int, float))):
        print("Erreur : Les valeurs doivent être des nombres.")
        sys.exit()

    if minimum >= maximum:
        print("Erreur : Le minimum doit être strictement inférieur au maximum.")
        sys.exit()

    for valeur in range(minimum, maximum):
        print(valeur)

input_min = input("Entrez la valeur minimum : ")
input_max = input("Entrez la valeur maximum : ")

try:
    min_val = int(input_min)
    max_val = int(input_max)
    valeurs_entre(min_val, max_val)
except ValueError:
    print("Erreur : Les valeurs doivent être des nombres entiers.")
    
