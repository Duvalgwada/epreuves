#  Split

# A revoir

# Programme decoupant une de caractere en tableau
# (separatuer: espace, tabulation, retours à la ligne)

def ma_fonction(chaine, string_separateur=None):
    # Extraire la chaîne de la liste
    chaine = chaine[0]
    
    # Votre algorithme pour diviser la chaîne en utilisant le séparateur
    if string_separateur is not None:
        # Utiliser le séparateur fourni
        tableau = chaine.split(string_separateur)
    else:
        # Si le séparateur n'est pas spécifié, utiliser l'espace, la tabulation et le retour à la ligne comme séparateurs
        tableau = chaine.split(" ")  # Espace
        tableau = [element for sous_tableau in tableau for element in sous_tableau.split("\t")]  # Tabulation
        tableau = [element for sous_tableau in tableau for element in sous_tableau.split("\n")]  # Retour à la ligne
    
    return tableau

def main():
    # Espace 
    chaine0 = ["Bonjour les gars"]
    resultat1 = ma_fonction(chaine0)
    print(resultat1)

    # Tabulation
    chaine1 = ["Bonjour\tles\tgars"]
    resultat2 = ma_fonction(chaine1, "\t")
    print(resultat2)

    # Retour à la ligne
    chaine2 = ["Bonjour\nles\ngars"]
    resultat3 = ma_fonction(chaine2, "\n")
    print(resultat3)

if __name__ == "__main__":
    main()