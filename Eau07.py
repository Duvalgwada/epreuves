# Majuscule

# 

def mettre_en_majuscule(chaine):
    mots = chaine.split()  # Diviser la chaîne en mots
    mots_majuscules = [mot[0].upper() + mot[1:] for mot in mots]
    chaine_majuscule = ' '.join(mots_majuscules)
    return chaine_majuscule

# Exemple
originale = "bonjour mathilde, comment vas-tu?!"
modifiee = mettre_en_majuscule(originale)
print("Originale:", originale)
print("Modifiée:", modifiee)
