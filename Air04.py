#  Un seul à la fois

# Programme affichant une chaine de caractere en evitant les caracteres identiques adjacents

def supprimer_doublons_adjacents(chaine):
    resultat = ""

    # Parcourir la chaîne caractère par caractère
    for i in range(len(chaine)):
        # Vérifier si le caractère actuel est différent du caractère suivant
        if i == len(chaine) - 1 or chaine[i] != chaine[i + 1]:
            resultat += chaine[i]

    return resultat

def main():
    # Exemple d'utilisation
    chaine_originale = "Hello milady,   bien ou quoi ??"
    chaine_resultante = supprimer_doublons_adjacents(chaine_originale)

    print("Chaine originale:", chaine_originale)
    print("Chaine sans caractères identiques adjacents:", chaine_resultante)

if __name__ == "__main__":
    main()
# Excellent