#  Chercher l'intrus

# Programme retournant la valeur d'une liste qui n'a pas de paire
# Itérer à travers la liste, compter le nombre d'occurrences de chaque élément et retourner celui qui a un nombre impair d'occurrences.

def valeur_sans_paire(liste):
    occurrences = {}

    # Compter le nombre d'occurrences de chaque élément dans la liste
    for element in liste:
        if element in occurrences:
            occurrences[element] += 1
        else:
            occurrences[element] = 1

    # Rechercher l'élément avec un nombre impair d'occurrences
    for element, count in occurrences.items():
        if count % 2 != 0:
            return element

    # Retourner None si tous les éléments ont un nombre pair d'occurrences
    return None

def main():
    # Exemple 1
    ma_liste = [1, 2, 3, 2, 1, 4, 5, 4, 3]
    valeur_sans_paire_resultat = valeur_sans_paire(ma_liste)

    if valeur_sans_paire_resultat is not None:
        print(f"La valeur sans paire est : {valeur_sans_paire_resultat}")
    else:
        print("Tous les éléments ont un nombre pair d'occurrences.")

    # Exemple 2
    ma_liste = ["Bonjour", "monsieur", "le", "comte", "bonjour"]
    valeur_sans_paire_resultat = valeur_sans_paire(ma_liste)

    if valeur_sans_paire_resultat is not None:
        print(f"La valeur sans paire est : {valeur_sans_paire_resultat}")
    else:
        print("Tous les éléments ont un nombre pair d'occurrences.")

if __name__ == "__main__":
    main()