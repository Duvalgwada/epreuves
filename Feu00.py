# ECHAUFFEMENT

# Programme affichant un rectangle plein d'etoiles, de longueur X et de hauteur Y.

def afficher_rectangle(longueur, hauteur):
    # Repeter une ligne de X etoiles pour chacune des Y rangees.
    for _ in range(hauteur):
        print("*" * longueur)


def main():
    # Etape 1 : demander les dimensions du rectangle.
    try:
        longueur = int(input("Entrez la longueur du rectangle : "))
        hauteur = int(input("Entrez la hauteur du rectangle : "))
    except ValueError:
        print("Erreur : veuillez saisir des nombres entiers.")
        return

    # Etape 2 : verifier que les dimensions sont strictement positives.
    if longueur <= 0 or hauteur <= 0:
        print("Erreur : la longueur et la hauteur doivent etre positives.")
        return

    # Etape 3 : afficher le rectangle.
    afficher_rectangle(longueur, hauteur)


if __name__ == "__main__":
    main()
