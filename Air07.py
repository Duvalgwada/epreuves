import re

#  Insertion dans un tableau trié

# Programme triant une liste d'entiers saisie, puis y inserant un nouvel entier.
# le dernier argument est l'élément à ajouter

def ajouter_element_trie(liste, nouvel_element):
    # Etape 1 : commencer au debut du tableau.
    index = 0

    # Etape 2 : avancer tant que les elements sont inferieurs au nouvel element.
    while index < len(liste):
        if liste[index] < nouvel_element:
            index += 1
        else:
            break

    # Etape 3 : inserer le nouvel element a sa position pour garder le tableau trie.
    liste.insert(index, nouvel_element)

def main():
    # Etape 1 : demander les nombres, dans n'importe quel ordre, puis les separer.
    saisie_liste = input("Entrez les nombres, separes par des espaces ou des virgules : ")
    try:
        liste_triee = [
            int(nombre)
            for nombre in re.split(r"[\s,]+", saisie_liste.strip())
            if nombre
        ]
    except ValueError:
        # Arreter si un element de la saisie n'est pas un entier.
        print("Erreur : veuillez saisir uniquement des nombres entiers.")
        return

    # Etape 2 : verifier que le tableau contient au moins un nombre.
    if not liste_triee:
        print("Erreur : veuillez saisir au moins un nombre.")
        return

    # Etape 3 : trier les nombres avant d'y inserer le nouvel element.
    liste_triee.sort()
 
    # Etape 4 : demander le nombre a inserer et verifier qu'il s'agit d'un entier.
    saisie_nouvel_element = input("Entrez le nombre a inserer : ")
    try:
        nouvel_element_a_ajouter = int(saisie_nouvel_element)
    except ValueError:
        print("Erreur : veuillez saisir un nombre entier.")
        return

    # Etape 5 : inserer le nombre a la bonne position, puis afficher le tableau final.
    ajouter_element_trie(liste_triee, nouvel_element_a_ajouter)
    print(f"Liste triee apres ajout de {nouvel_element_a_ajouter} : {liste_triee}")

if __name__ == "__main__":
    main()