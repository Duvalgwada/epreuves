# Différence minimum absolue

# Programme affichant la différence minimum absolue (nombre absolu) entre 2 elements d'un tableau constitué de nombres.
# On peut renseigner des nombres negatifs

tableau1 = [5, 1, 19, 21]
tableau2 = [20, 5, 1, 19, 21]
tableau3 = [-8, -6, 4]

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
resultat1 = difference_minimale_absolue(tableau1)
resultat2 = difference_minimale_absolue(tableau2)
resultat3 = difference_minimale_absolue(tableau3)

# Affichez les résultats
print(f"La différence minimale absolue pour tableau1 est : {resultat1}")
print(f"La différence minimale absolue pour tableau2 est : {resultat2}")
print(f"La différence minimale absolue pour tableau3 est : {resultat3}")
