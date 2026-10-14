# Trie ou pas (Determiner si une liste numerique est triée ou non)

# Saisie de la liste par l'utilisateur
chaine = input("Saisissez une liste de nombres séparés par des virgules : ")
liste = [int(x.strip()) for x in chaine.split(",") if x.strip()]

# programme afin de verifier
def est_liste_triee(liste):
    for i in range(len(liste) - 1):
        if liste[i] > liste[i + 1]:
            return False
    return True

# Vérification si la liste est triée
if est_liste_triee(liste):
    print("La liste est triée.")
else:
    print("La liste n'est pas triée.")
