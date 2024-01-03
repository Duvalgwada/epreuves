# Tri à bulle

# Programme triant une liste de nombres.
# Programme devant implementer l'algorithme du tri à bulle

# definition
# L'algorithme de tri à bulles (Bubble Sort en anglais) est un algorithme simple de tri qui fonctionne en comparant et en échangeant les éléments adjacents s'ils sont dans le mauvais ordre. 
# L'algorithme passe à travers la liste plusieurs fois jusqu'à ce qu'aucun échange ne soit nécessaire, indiquant que la liste est triée.

tableau = [6, 5, 4, 3, 2, 1]

def tri_bulles(tableau):
    n = len(tableau)
    
    # Parcourir tous les éléments du tableau
    for i in range(n):
        # La dernière i-ème partie du tableau est déjà triée,
        # donc on ne la parcourt pas à nouveau
        for j in range(0, n-i-1):
            # Échanger si l'élément trouvé est plus grand que le suivant
            if tableau[j] > tableau[j+1]:
                tableau[j], tableau[j+1] = tableau[j+1], tableau[j]

# Appel de la fonction pour trier le tableau
tri_bulles(tableau)

print("Tableau trié:")
print(tableau)

