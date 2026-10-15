# Tri par sélection

# Programme  triant une liste de nombre
# Programme devant implementer l'algorithme du tri par selection

# definition
# Le tri par sélection (Selection Sort en anglais) est un algorithme de tri simple et intuitif. 
# Il fonctionne en divisant la liste en deux parties : une partie triée et une partie non triée. 
# L'algorithme sélectionne itérativement l'élément le plus petit (ou le plus grand, selon l'ordre de tri souhaité) 
# de la partie non triée et le place au début de cette partie.

# Donner les elements du tableau separes par des espaces, puis appuyer sur Entrée.
tableau = list(map(int, input("Entrez les éléments du tableau, séparés par des espaces : ").split()))

def tri_selection(tableau):
    n = len(tableau)
    
    # Parcourir tous les éléments du tableau
    for i in range(n - 1):
        # Trouver l'index du minimum dans la partie non triée
        indice_minimum = i
        for j in range(i+1, n):
            if tableau[j] < tableau[indice_minimum]:
                indice_minimum = j
        
        # Échanger l'élément minimum avec le premier élément de la partie non triée
        tableau[i], tableau[indice_minimum] = tableau[indice_minimum], tableau[i]

# Appel de la fonction pour trier le tableau
tri_selection(tableau)

print("Tableau trié:")
print(tableau)
