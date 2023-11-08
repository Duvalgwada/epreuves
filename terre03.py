# Afficher l'alphabet, à partir d'une lettre donnée

# Votre chaîne de caractères
alpha = "abcdefghijklmnopqrstuvwxyz"

# Creer la boucle
while True:
   
    # Demander quelle lettre taper
    lettre = input("Tapez une lettre (ou 'qq' pour quitter): ")

    # Programme pour quitter la boucle
    if lettre == 'qq':
        break

    # Programme definissant ce qui vient apres la dite lettre
    if len(lettre) == 1 and lettre.isalpha() and lettre in alpha:
        index = alpha.index(lettre)
        resultat = alpha[index + 1:]
        print("Caractères après la lettre :", resultat)
    else:
        print("Veuillez taper une seule lettre valide présente dans la chaîne de caractères.")
