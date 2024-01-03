# String dans string

# Un programme determinant si une chaine de caractere se trouve dans une autre
# un booleen 

# Saisir deux chaînes de caracteres
chaine_principale = input("Entrez la chaîne principale : ")
chaine_recherchee = input("Entrez la chaîne à rechercher : ")

# Vérifiez si la chaîne recherchée est présente dans la chaîne principale
if chaine_recherchee in chaine_principale:
    print(f"{chaine_recherchee} est présente dans la phrase {chaine_principale}.")
else:
    print(f"{chaine_recherchee} n'est pas présente dans la phrase {chaine_principale}.")
