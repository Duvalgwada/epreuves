# Majuscule

def majuscule(chaine):
    mots = chaine.split()  # Diviser la chaîne en mots
    mots_majuscules = [mot[0].upper() + mot[1:] for mot in mots]
    chaine_majuscule = ' '.join(mots_majuscules)
    return chaine_majuscule

# Entrer la chaine de caractere
chaine_originale = input("Entrez un texte : ")
chaine_modifiee = majuscule(chaine_originale)

print("Chaîne originale :", chaine_originale)
print("Chaîne modifiée  :", chaine_modifiee)
