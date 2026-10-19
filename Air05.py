#  Sur chacun d'entre eux

# Programme qui ajoute une valeur à chaque entier d'une liste.
# Une valeur négative produit une soustraction.

def operation_sur_liste(liste, valeur):
    # Ajouter la valeur (positive ou négative) à chaque nombre.
    return [nombre + valeur for nombre in liste]

def main():
    # Demander les nombres à traiter, séparés par des espaces.
    saisie_nombres = input("Entrez les nombres à traiter, séparés par des espaces : ")
    try:
        ma_liste = [int(nombre) for nombre in saisie_nombres.split()]
    except ValueError:
        print("Erreur : veuillez saisir uniquement des nombres entiers.")
        return

    if not ma_liste:
        print("Erreur : vous devez saisir au moins un nombre.")
        return

    # Demander la valeur à ajouter ; si elle est négative, cela revient à soustraire.
    saisie_valeur = input("Entrez la valeur à ajouter (négative pour soustraire) : ")
    try:
        valeur_a_ajouter = int(saisie_valeur)
    except ValueError:
        print("Erreur : veuillez saisir une valeur entière.")
        return

    # Ajouter la valeur saisie à chaque nombre.
    resultat = operation_sur_liste(ma_liste, valeur_a_ajouter)
    print(f"Résultat : {resultat}")

if __name__ == "__main__":
    main()