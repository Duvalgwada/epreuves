# Index wanted

# A REVOIR

# Programme affichant le 1ere index d'un element recherhce dans le tableau.
# Le tableau est constitue de tous les arguments sauf le dernier.
# L'element recherche est le dernier argument. 
# Afficher -1 si element n'est pas trouve.

# En programmation, l'index d'un élément dans une liste est généralement un nombre entier qui représente sa position dans la liste.

def trouver_index_element(tableau):
    # Récupérer l'élément recherché (dernier argument)
    element_recherche = str(tableau[-1]).lower()  # Convertir en minuscules (sensibilité à la casse)

    # Les éléments du tableau sous forme de chaînes de caractères
    elements = [str(element).lower() for element in tableau[:-1]]

    print(f"Éléments dans le tableau : {elements}")

    # Rechercher l'index de l'élément dans le tableau
    for i, element in enumerate(elements):
        if element_recherche in element:
            print(f"L'élément '{element_recherche}' a été trouvé à l'index {i}.")
            return  # Ajout pour arrêter la recherche après la première correspondance

    print(f"L'élément '{element_recherche}' n'a pas été trouvé. Index: -1.")

# Exemple d'utilisation avec vos éléments
element1 = "Ceci est le monde qui contient Charlie, un homme sympa Charlie"
element2 = "test test test"
element3 = "test boom"

# Appeler la fonction avec un tableau composé des trois éléments et de l'élément à rechercher
trouver_index_element([element1, "contient"])
trouver_index_element([element2, "test"])
trouver_index_element([element3, "merde"])

