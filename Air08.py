#  Mélange de deux tableaux triés

# Programme fusionnant 2 listes d'entiers triées en les gardant triées, les 2 listes seront separees par une fusion

def fusionner_listes_triees(liste1, liste2):
    resultat = []
    index1 = index2 = 0

    # Fusionner les listes triées
    while index1 < len(liste1) and index2 < len(liste2):
        if liste1[index1] < liste2[index2]:
            resultat.append(liste1[index1])
            index1 += 1
        else:
            resultat.append(liste2[index2])
            index2 += 1

    # Ajouter les éléments restants des deux listes (s'il y en a)
    resultat.extend(liste1[index1:])
    resultat.extend(liste2[index2:])

    return resultat

def main():
    # Exemple 
    liste_triee1 = [10, 20, 30, 40]
    liste_triee2 = [15, 25, 35, 50]

    resultat_fusion = fusionner_listes_triees(liste_triee1, liste_triee2)
    print(f"Liste triée après fusion : {resultat_fusion}")

if __name__ == "__main__":
    main()