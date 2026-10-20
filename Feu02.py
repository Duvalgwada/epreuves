# TROUVER UNE FORME

# Creer un plateau rempli de points, y placer deux O aleatoires,
# puis afficher les coordonnees du premier O trouve en le parcourant.

import random

def creer_plateau(longueur, hauteur):
    # Etape 1 : creer les lignes et les colonnes du plateau avec des points.
    plateau = [["." for _ in range(longueur)] for _ in range(hauteur)]

    # Etape 2 : choisir deux cases distinctes au hasard et y placer les O.
    cases = random.sample(
        [(x, y) for y in range(hauteur) for x in range(longueur)],
        2,
    )
    for x, y in cases:
        plateau[y][x] = "O"

    return plateau


def trouver_premier_point(plateau):
    # Etape 1 : parcourir les lignes de haut en bas et les colonnes de gauche a droite.
    for y, ligne in enumerate(plateau):
        for x, element in enumerate(ligne):
            if element == "O":
                # Etape 2 : retourner la position en commencant les coordonnees a 1.
                return x + 1, y + 1

    # Aucun O n'a ete trouve.
    return None


def main():
    # Etape 1 : demander la longueur X et la hauteur Y du plateau.
    try:
        longueur = int(input("Entrez la longueur X du plateau : "))
        hauteur = int(input("Entrez la hauteur Y du plateau : "))
    except ValueError:
        print("Erreur : veuillez saisir des nombres entiers.")
        return

    # Etape 2 : verifier que les dimensions permettent de placer deux O.
    if longueur <= 0 or hauteur <= 0 or longueur * hauteur < 2:
        print("Erreur : le plateau doit contenir au moins deux cases.")
        return

    # Etape 3 : creer le plateau et afficher son contenu.
    plateau = creer_plateau(longueur, hauteur)
    print("\nPlateau :")
    for ligne in plateau:
        print(" ".join(ligne))

    # Etape 4 : chercher le premier O et afficher ses coordonnees.
    coordonnees = trouver_premier_point(plateau)
    if coordonnees is not None:
        x, y = coordonnees
        print(f"Premier O trouve : coordonnees (X={x}, Y={y}).")


if __name__ == "__main__":
    main()
