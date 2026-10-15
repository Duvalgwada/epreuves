# Index wanted

# Programme affichant le 1ere index d'un element recherhce dans le tableau.
# Le tableau est constitue de tous les arguments sauf le dernier.
# L'element recherche est le dernier argument. 
# Afficher -1 si element n'est pas trouve.

# En programmation, l'index d'un élément dans une liste est généralement un nombre entier qui 
# représente sa position dans la liste.

def trouver_index_element(tableau):
    if not tableau:
        return -1

    element_recherche = str(tableau[-1]).casefold()

    for index, element in enumerate(tableau[:-1]):
        if str(element).casefold() == element_recherche:
            return index

    return -1


chaine = input("Entrez les éléments du tableau, séparés par des espaces : ")
element_recherche = input("Entrez l'élément à rechercher : ")

elements = chaine.split()
print(trouver_index_element(elements + [element_recherche]))
