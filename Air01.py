# Split en fonction

# Programme decoupant une chaine de caractere en tableau en fonction du separateur donné én 2eme argument


def ma_fonction(string_a_couper, string_separateur):
    # Utilisation de la méthode split pour découper la chaîne
    tableau_resultat = string_a_couper.split(string_separateur)
    return tableau_resultat

def main():
    string_a_couper = "Crevette magique dans la mer des étoiles la crevette magique dans mer des étoiles"
    separateur = " "

    # Appeler la fonction ma_fonction
    resultat = ma_fonction(string_a_couper, separateur)

    # Afficher le résultat
    print(resultat)

if __name__ == "__main__":
    main()
