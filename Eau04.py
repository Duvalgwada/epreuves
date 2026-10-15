# Prochain nombre premier

nombre = int(input("Écris un nombre entier : "))

# Fonction pour vérifier si un nombre est premier   
def est_nombre_premier(nombre):
    if nombre < 2:
        return False

    i = 2
    while i * i <= nombre:
        if nombre % i == 0:
            return False
        i += 1

    return True

# Fonction pour trouver le prochain nombre premier supérieur à un nombre donné
def premier_superieur(nombre):
    candidat = nombre + 1

    while not est_nombre_premier(candidat):
        candidat += 1

    return candidat

if est_nombre_premier(nombre):
    print(f"Le nombre {nombre} est premier.")
else:
    print(f"Le nombre {nombre} n'est pas premier.")

resultat = premier_superieur(nombre)
print(f"Le premier nombre premier supérieur à {nombre} est {resultat}.")
