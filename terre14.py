# Trie ou pas (Determiner si une liste numerique est triée ou non)

# les Listes
liste1 = [9, 8, 3]
liste2 = [3, 8, 9, 12]
liste3 = [15, 12, 9, 1]

# programme afin de verifier
def est_liste_triee(liste):
    for i in range(len(liste) - 1):
        if liste[i] > liste[i + 1]:
            return False
    return True

# Vérification si les listes sont triées
if est_liste_triee(liste1):
    print("liste1 est triée.")
else:
    print("liste1 n'est pas triée.")

if est_liste_triee(liste2):
    print("liste2 est triée.")
else:
    print("liste2 n'est pas triée.")

if est_liste_triee(liste3):
    print("liste3 est triée.")
else:
    print("liste3 n'est pas triée.")