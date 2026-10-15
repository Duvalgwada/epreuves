# Chiffre only

# Programme verifiant si une chaime de caractere contient que des chiffres

# methode 'isdigit()'

def nombre(chaine):
    return chaine.isdigit()

# Entrer la chaine de caractere
caractere = input("Entrez une suite de chiffres : ")

if nombre(caractere):
    print(f"La chaîne '{caractere}' contient uniquement des chiffres.")
else:
    print(f"La chaîne '{caractere}' contient des caractères non numériques aussi.")