# Entre min et max

# creer programme affichant toutes les valeurs comprises entre 2 nombres dans l'ordre croissant, minimum inclus, maximum exclus

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

# Exemple 1
minimum = 20
maximum = 25
valeurs_entre(minimum, maximum)

# Exemple 2
minimum = 25
maximum = 20
valeurs_entre(minimum, maximum)

# Exemple 3 (avec une valeur non numérique)
minimum = "hello"
valeurs_entre(minimum, 30)
