import random
import sys

ROUGE = "\033[91m"
RESET = "\033[0m"


# Trouver le plus grand carré

# Un programme remplacant les caracteres vides par des caracteres plein pour representer le plus grand carré sur un plateau.
# Le plateau sera transmis dans un fichier. La premiere ligne contient les informations pour lire le plateau, c'est à dire, le nombre
# de lignes du plateau, caractères pour “vide”, “obstacle” et “plein”.
# Il faudra gérer les potentiels problèmes d’arguments, de fichiers, ou de carte invalide.
# Une carte est valide uniquement si: les lignes ont toute la même longueur, il y a au moins une ligne d’une case,
# les lignes sont séparées d’un retour à la ligne, les caractères présents dans la carte sont uniquement ceux de la première ligne.
# En cas de plusieurs solutions, le carré le plus en haut à gauche sera choisi.


def generer_carte(largeur: int, hauteur: int, densite: int) -> list[list[str]]:
    # Etape 1 : generer une carte avec les dimensions demandees.
    carte = []
    for _ in range(hauteur):
        ligne = []
        for _ in range(largeur):
            if random.randrange(hauteur) * 2 < densite:
                ligne.append("x")
            else:
                ligne.append(".")
        carte.append(ligne)

    return carte


def trouver_plus_grand_carre(
    carte: list[list[str]],
    caractere_vide: str,
    caractere_plein: str,
) -> tuple[list[list[str]], int]:
    # Etape 3 : definir les dimensions de la carte et les variables du resultat.
    hauteur = len(carte)
    largeur = len(carte[0])
    tailles = [[0] * largeur for _ in range(hauteur)]
    meilleure_taille = 0
    meilleure_ligne = 0
    meilleure_colonne = 0

    # Etape 4 : calculer, pour chaque case vide, la taille du carre qui s'y termine.
    for ligne in range(hauteur):
        for colonne in range(largeur):
            if carte[ligne][colonne] != caractere_vide:
                continue

            if ligne == 0 or colonne == 0:
                tailles[ligne][colonne] = 1
            else:
                tailles[ligne][colonne] = 1 + min(
                    tailles[ligne - 1][colonne],
                    tailles[ligne][colonne - 1],
                    tailles[ligne - 1][colonne - 1],
                )

            # Ne remplacer que par un carre plus grand : en cas d'egalite,
            # le premier trouve est celui le plus en haut, puis le plus a gauche.
            if tailles[ligne][colonne] > meilleure_taille:
                meilleure_taille = tailles[ligne][colonne]
                meilleure_ligne = ligne
                meilleure_colonne = colonne

    # Etape 5 : remplacer les cases du plus grand carre par le caractere plein.
    if meilleure_taille > 0:
        debut_ligne = meilleure_ligne - meilleure_taille + 1
        debut_colonne = meilleure_colonne - meilleure_taille + 1

        for ligne in range(debut_ligne, meilleure_ligne + 1):
            for colonne in range(debut_colonne, meilleure_colonne + 1):
                carte[ligne][colonne] = caractere_plein

    return carte, meilleure_taille


def main(arguments: list[str]) -> int:
    # Etape 6 : recuperer les dimensions et la densite depuis les arguments
    # ou les demander si le programme est lance sans argument.
    if len(arguments) == 1:
        try:
            largeur = int(input("Largeur de la carte : "))
            hauteur = int(input("Hauteur de la carte : "))
            densite = int(input("Densite des obstacles : "))
        except EOFError:
            print("Erreur : les dimensions et la densite doivent etre renseignees.")
            return 1
        except ValueError:
            print("Erreur : largeur, hauteur et densite doivent etre des entiers.")
            return 1
    elif len(arguments) == 4:
        try:
            largeur, hauteur, densite = (int(argument) for argument in arguments[1:])
        except ValueError:
            print("Erreur : largeur, hauteur et densite doivent etre des entiers.")
            return 1
    else:
        print(f"Utilisation : python {arguments[0]} <largeur> <hauteur> <densite>")
        return 1

    if largeur < 1 or hauteur < 1:
        print("Erreur : la largeur et la hauteur doivent etre superieures a zero.")
        return 1

    # Etape 7 : generer et afficher la carte avant de chercher le carre.
    carte = generer_carte(largeur, hauteur, densite)
    print(f"\nCarte generee ({largeur} colonnes x {hauteur} lignes) :")
    print(f"{hauteur}.xo")
    for ligne in carte:
        print("".join(ligne))

    # Etape 8 : chercher le plus grand carre vide et afficher la solution.
    carte, taille_carre = trouver_plus_grand_carre(carte, ".", "o")
    print(f"Taille du plus grand carre : {taille_carre}")
    for ligne in carte:
        for caractere in ligne:
            if caractere == "o":
                print(f"{ROUGE}{caractere}{RESET}", end="")
            else:
                print(caractere, end="")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
