# Savoir si des arguments sont Pair ou Impair

while True:
    try:
        nombre = int(input("Entrez un nombre (ou '0' pour quitter) : "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue

    if nombre == 0:
        break  # Quitter la boucle si l'utilisateur entre 0

    if nombre % 2 == 0:
        print(f"{nombre} est un nombre pair.")
    else:
        print(f"{nombre} est un nombre impair.")
