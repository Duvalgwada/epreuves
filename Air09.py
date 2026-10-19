import re

#  Rotation vers la gauche

# Programme decalant tous les elements d'un tableau vers la gauche.
# Le premier element devient le dernier à chaque rotation

def decalage_vers_la_gauche(tableau):
    # Vérifier si le tableau est vide ou a un seul élément
    if len(tableau) <= 1:
        return tableau

    # Décaler les éléments vers la gauche
    premier_element = tableau.pop(0)
    tableau.append(premier_element)

    return tableau

def main():
    # Saisir les elements separes par des espaces ou des virgules.
    saisie = input(
        "Entrez les elements a faire pivoter, separes par des espaces ou des virgules : "
    )
    elements_saisis = re.split(r"[\s,]+", saisie.strip())
    if not saisie.strip():
        print("Erreur : veuillez saisir au moins un element.")
        return

    # Convertir les entiers en nombres et conserver les autres elements comme texte.
    mon_tableau = []
    for element in elements_saisis:
        if not element:
            continue
        try:
            mon_tableau.append(int(element))
        except ValueError:
            mon_tableau.append(element)

    # Afficher le tableau original
    print(f"Tableau original : {mon_tableau}")

    # Décaler les éléments vers la gauche
    decalage_vers_la_gauche(mon_tableau)

    # Afficher le tableau après décalage
    print(f"Tableau après décalage vers la gauche : {mon_tableau}")

if __name__ == "__main__":
    main()
