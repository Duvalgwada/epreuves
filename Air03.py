#  Chercher l'intrus

# Programme retournant les valeurs qui ont un nombre impair d'occurrences.
# Il compte les occurrences de chaque élément, puis retourne ceux qui n'ont pas de paire.

def valeur_sans_paire(liste):
    occurrences = {}

    # Compter le nombre d'occurrences de chaque élément dans la liste
    for element in liste:
        if element in occurrences:
            occurrences[element] += 1
        else:
            occurrences[element] = 1

    # Retourner tous les éléments avec un nombre impair d'occurrences.
    elements_sans_paire = [
        element for element, count in occurrences.items() if count % 2 != 0
    ]
    return elements_sans_paire

def main():
    # Demander à l'utilisateur de saisir les éléments séparés par des espaces.
    saisie = input("Entrez les éléments de la liste, séparés par des espaces : ")
    ma_liste = saisie.split()

    if not ma_liste:
        print("Erreur : la liste ne peut pas être vide.")
        return

    # Rechercher tous les éléments qui n'ont pas de paire.
    elements_sans_paire = valeur_sans_paire(ma_liste)

    if elements_sans_paire:
        print("Erreur : ces éléments n'ont pas de paire :")
        print(", ".join(elements_sans_paire))
    else:
        print("Aucune erreur : tous les éléments ont une paire.")

if __name__ == "__main__":
    main()