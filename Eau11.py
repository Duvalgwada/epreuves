# Différence minimum absolue

# Programme affichant la différence minimum absolue (nombre absolu) 
# entre 2 elements d'un tableau constitué de nombres.
# On peut renseigner des nombres negatifs14

# Donner les elements du tableau separes par des espaces, puis appuyer sur Entrée.
tableau = list(map(int, input("Entrez les éléments du tableau, séparés par des espaces : ").split()))

def difference_minimale_absolue(tableau):
    # Assurez-vous que le tableau a au moins deux éléments
    if len(tableau) < 2:
        return None  # ou une autre valeur par défaut selon vos besoins
    
    # Triez le tableau
    tableau_trie = sorted(tableau)
    
    # Initialisez la différence minimale absolue avec une valeur maximale possible
    diff_min_absolue = float('inf')
    
    # Parcourez le tableau pour trouver la différence minimale absolue
    for i in range(len(tableau_trie) - 1):
        diff_actuelle = abs(tableau_trie[i] - tableau_trie[i + 1])
        diff_min_absolue = min(diff_min_absolue, diff_actuelle)
    
    return diff_min_absolue

# Utilisez la fonction pour chaque tableau
resultat = difference_minimale_absolue(tableau)

# Affichez les résultats
print(f"La différence minimale absolue pour le tableau est : {resultat}")
