import re

#  Mélange de deux tableaux triés

# Programme fusionnant 2 listes d'entiers triées en les gardant triées, les 2 listes seront separees par une fusion

def fusionner_listes_triees(liste1, liste2):
    # preparer le tableau resultat et les positions de depart.
    resultat = []
    index1 = index2 = 0

    # Comparer les elements courants et ajouter le plus petit au resultat.
    while index1 < len(liste1) and index2 < len(liste2):
        if liste1[index1] < liste2[index2]:
            resultat.append(liste1[index1])
            index1 += 1
        else:
            resultat.append(liste2[index2])
            index2 += 1

    # Ajouter les elements restants de la premiere liste, s'il y en a.
    resultat.extend(liste1[index1:])

    # Ajouter les elements restants de la deuxieme liste, s'il y en a.
    resultat.extend(liste2[index2:])

    # Retourner le tableau fusionne.
    return resultat

def main():
    # Etape 1 : demander les deux listes, dans n'importe quel ordre.
    saisie_liste1 = input(
        "Entrez les nombres de la premiere liste, separes par des espaces ou des virgules : "
    )
    saisie_liste2 = input(
        "Entrez les nombres de la deuxieme liste, separes par des espaces ou des virgules : "
    )

    try:
        # Etape 2 : separer les saisies et convertir chaque element en entier.
        saisie_liste1 = saisie_liste1.replace("\u2212", "-")
        saisie_liste2 = saisie_liste2.replace("\u2212", "-")
        liste1 = [
            int(nombre)
            for nombre in re.split(r"[\s,]+", saisie_liste1.strip())
            if nombre
        ]
        liste2 = [
            int(nombre)
            for nombre in re.split(r"[\s,]+", saisie_liste2.strip())
            if nombre
        ]
    except ValueError:
        print("Erreur : veuillez saisir uniquement des nombres entiers.")
        return

    # Etape 3 : verifier que les deux listes contiennent au moins un nombre.
    if not liste1 or not liste2:
        print("Erreur : veuillez saisir au moins un nombre dans chaque liste.")
        return

    # Etape 4 : trier les listes pour permettre leur fusion dans l'ordre croissant.
    liste1.sort()
    liste2.sort()

    # Etape 5 : fusionner les listes triees et afficher le resultat.
    resultat_fusion = fusionner_listes_triees(liste1, liste2)
    print(f"Premiere liste triee : {liste1}")
    print(f"Deuxieme liste triee : {liste2}")
    print(f"Liste triee apres fusion : {resultat_fusion}")

if __name__ == "__main__":
    main()