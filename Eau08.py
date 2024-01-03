# Chiffre only

# Programme verifiant si une chaime de caractere contient que des chiffres

# methode 'isdigit()'

def est_numerique(chaine):
    return chaine.isdigit()

# Exemple d'utilisation
chaine1 = "12345"
chaine2 = "12abc34"
chaine3 = ""

print(est_numerique(chaine1))  # Devrait renvoyer True
print(est_numerique(chaine2))  # Devrait renvoyer False
print(est_numerique(chaine3))  # Devrait renvoyer False

