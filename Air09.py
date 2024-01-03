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
    # Exemple d'utilisation
    mon_tableau = ["Michel", "Albert", "Thereèse", "Benoit"]

    # Afficher le tableau original
    print(f"Tableau original : {mon_tableau}")

    # Décaler les éléments vers la gauche
    decalage_vers_la_gauche(mon_tableau)

    # Afficher le tableau après décalage
    print(f"Tableau après décalage vers la gauche : {mon_tableau}")

if __name__ == "__main__":
    main()
