# Majuscule sur deux

# Programme permettant de mettre en majuscule une lettre /2
# Boucle et concaténer les caracteres modifies

# Programme
def majuscule_tous_les_deux(caracteres):
    resultat = ""
    for i in range(len(caracteres)):
        if i % 2 == 1:  # Si l'indice est impair (commence à 0)
            resultat += caracteres[i].upper()
        else:
            resultat += caracteres[i]
    return resultat

# Entrer la chaine de caractere
chaine_originale = "Hello world !"
chaine_modifiee = majuscule_tous_les_deux(chaine_originale)

print("Chaîne originale :", chaine_originale)
print("Chaîne modifiée  :", chaine_modifiee)

# Vérification de la longueur
if len(chaine_modifiee) != len(chaine_originale):
    print("Erreur : Les caractères ne correspondent pas.")
else:
    print("Chaîne originale :", chaine_originale)
    print("Chaîne modifiée  :", chaine_modifiee)
