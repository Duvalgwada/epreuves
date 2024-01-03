#  Concat

# Programme transformant un tableau de chaine de caractere en une seule chaine de caractere
# Espacé d'un separateur donné en dernier argument du programme 

def concatener_tableau(tableau, separateur):
    # Utiliser la méthode join pour concaténer les éléments du tableau avec le séparateur
    chaine_concatenee = separateur.join(tableau)
    return chaine_concatenee

def main():
    # Espace
    chaine = ["je", "teste", "des", "trucs"]
    separateur = " "
    chaine_resultante = concatener_tableau(chaine, separateur)
    print(chaine_resultante)

    # Tabulation
    chaine = ["je", "teste", "des", "trucs"]
    separateur = "\t"
    chaine_resultante = concatener_tableau(chaine, separateur)
    print(chaine_resultante)

    # Retour à la ligne
    chaine = ["je", "teste", "des", "trucs"]
    separateur = "\n"
    chaine_resultante = concatener_tableau(chaine, separateur)
    print(chaine_resultante)

if __name__ == "__main__":
    main()

