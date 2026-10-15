# String dans string

# Un programme determinant si une chaine de caractere se trouve dans une autre
# Aide du booleen 

# Saisir deux chaînes de caracteres
chaine_principale = input("Entrez la chaîne principale : ")
chaine_recherchee = input("Entrez la chaîne à rechercher : ")

# Vérifiez si la chaîne recherchée est présente dans la chaîne principale
if chaine_recherchee in chaine_principale:
    print(f"{chaine_recherchee} correspond à {chaine_principale}.")
else:
    print(f"{chaine_recherchee} ne correspond pas à {chaine_principale}.")
