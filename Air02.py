#  Concat

# Programme transformant un tableau de chaine de caractere en une seule chaine de caractere
# Espacé d'un separateur donné en dernier argument du programme 

def concatener_tableau(tableau, separateur):
    # Utiliser la méthode join pour concaténer les éléments du tableau avec le séparateur
    chaine_concatenee = separateur.join(tableau)
    return chaine_concatenee

def main():
    # Demande à l'utilisateur les éléments à concaténer, séparés par des espaces.
    saisie = input("Entrez les éléments à concaténer, séparés par des espaces : ")
    chaine = saisie.split()

    # Affiche le résultat obtenu avec un espace comme séparateur.
    separateur = " "
    chaine_resultante = concatener_tableau(chaine, separateur)
    print("Avec un espace :")
    print(chaine_resultante)

    # Affiche le résultat obtenu avec une tabulation comme séparateur.
    separateur = "\t"
    chaine_resultante = concatener_tableau(chaine, separateur)
    print("Avec une tabulation :")
    print(chaine_resultante)

    # Affiche le résultat obtenu avec un retour à la ligne comme séparateur.
    separateur = "\n"
    chaine_resultante = concatener_tableau(chaine, separateur)
    print("Avec un retour à la ligne :")
    print(chaine_resultante)

if __name__ == "__main__":
    main()
