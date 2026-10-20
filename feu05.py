import random
import sys
from collections import deque

ROUGE = "\033[91m"
RESET = "\033[0m"


# LABYRINTHE

# Un programme qui trouve le plus court chemin entre l’entrée et la sortie d’un labyrinthe en évitant les obstacles.
# Le labyrinthe est transmis en argument du programme.
# La première ligne du labyrinthe contient les informations pour lire la carte : LIGNES x COLONNES, caractère plein, vide, chemin, entrée et sortie du labyrinthe.
# Le but du programme est de remplacer les caractères “vide” par des caractères “chemin” pour représenter le plus court chemin pour traverser le labyrinthe.
# Un déplacement ne peut se faire que vers le haut, le bas, la droite ou la gauche.


def generer_labyrinthe(
    largeur: int,
    hauteur: int,
    densite: int,
) -> tuple[list[list[str]], tuple[int, int], tuple[int, int]]:
    # Etape 1 : creer l'interieur du plateau avec des cases vides et des obstacles.
    carte = [["." for _ in range(largeur + 2)] for _ in range(hauteur + 2)]

    for ligne in range(1, hauteur + 1):
        for colonne in range(1, largeur + 1):
            carte[ligne][colonne] = (
                "X" if random.random() < densite / 100 else "."
            )

    # Etape 2 : choisir l'entree et la sortie sur deux cotes differents.
    cotes = random.sample(("haut", "bas", "gauche", "droite"), 2)
    positions_cote = {
        "haut": [(0, colonne) for colonne in range(1, largeur + 1)],
        "bas": [(hauteur + 1, colonne) for colonne in range(1, largeur + 1)],
        "gauche": [(ligne, 0) for ligne in range(1, hauteur + 1)],
        "droite": [(ligne, largeur + 1) for ligne in range(1, hauteur + 1)],
    }
    entree = random.choice(positions_cote[cotes[0]])
    sortie = random.choice(positions_cote[cotes[1]])
    carte[entree[0]][entree[1]] = "E"
    carte[sortie[0]][sortie[1]] = "S"
    case_entree = case_interieure_depuis_contour(entree, largeur, hauteur)
    case_sortie = case_interieure_depuis_contour(sortie, largeur, hauteur)
    carte[case_entree[0]][case_entree[1]] = "."
    carte[case_sortie[0]][case_sortie[1]] = "."

    return carte, entree, sortie


def case_interieure_depuis_contour(
    position: tuple[int, int],
    largeur: int,
    hauteur: int,
) -> tuple[int, int]:
    ligne, colonne = position
    if ligne == 0:
        return 1, colonne
    if ligne == hauteur + 1:
        return hauteur, colonne
    if colonne == 0:
        return ligne, 1
    return ligne, largeur


def trouver_chemin(
    carte: list[list[str]],
    entree: tuple[int, int],
    sortie: tuple[int, int],
    largeur: int,
    hauteur: int,
) -> list[tuple[int, int]] | None:
    # Etape 3 : partir de la case interieure pres de l'entree et chercher la sortie.
    depart = case_interieure_depuis_contour(entree, largeur, hauteur)
    arrivee = case_interieure_depuis_contour(sortie, largeur, hauteur)
    if carte[depart[0]][depart[1]] != "." or carte[arrivee[0]][arrivee[1]] != ".":
        return None

    file = deque([depart])
    precedents: dict[tuple[int, int], tuple[int, int] | None] = {depart: None}
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    while file:
        ligne, colonne = file.popleft()
        if (ligne, colonne) == arrivee:
            break

        for decalage_ligne, decalage_colonne in directions:
            prochaine_case = (
                ligne + decalage_ligne,
                colonne + decalage_colonne,
            )
            prochaine_ligne, prochaine_colonne = prochaine_case

            if (
                1 <= prochaine_ligne <= hauteur
                and 1 <= prochaine_colonne <= largeur
                and carte[prochaine_ligne][prochaine_colonne] == "."
                and prochaine_case not in precedents
            ):
                precedents[prochaine_case] = (ligne, colonne)
                file.append(prochaine_case)

    if arrivee not in precedents:
        return None

    # Etape 4 : remonter les cases precedentes pour reconstruire le chemin.
    chemin = []
    case = arrivee
    while case is not None:
        chemin.append(case)
        case = precedents[case]

    chemin.reverse()
    return chemin


def afficher_carte(carte: list[list[str]]) -> None:
    hauteur = len(carte) - 2
    largeur = len(carte[0]) - 2
    for indice_ligne, ligne in enumerate(carte):
        caracteres = []
        for indice_colonne, caractere in enumerate(ligne):
            if caractere == "O":
                caracteres.append(f"{ROUGE}O{RESET}")
            elif caractere in ("E", "S"):
                caracteres.append(caractere)
            elif indice_ligne in (0, hauteur + 1) and indice_colonne in (0, largeur + 1):
                caracteres.append("+")
            elif indice_ligne in (0, hauteur + 1):
                caracteres.append("-")
            elif indice_colonne in (0, largeur + 1):
                caracteres.append("|")
            else:
                caracteres.append(caractere)
        print("".join(caracteres))


def main(arguments: list[str]) -> int:
    # Etape 5 : lire les dimensions et la densite, ou demander les valeurs.
    if len(arguments) == 1:
        try:
            largeur = int(input("Longueur du plateau : "))
            hauteur = int(input("Hauteur du plateau : "))
            densite = int(input("Densite des obstacles (0 a 100, defaut 25) : ") or "25")
        except (EOFError, ValueError):
            print("Erreur : entre des dimensions et une densite sous forme d'entiers.")
            return 1
    elif len(arguments) == 4:
        try:
            largeur, hauteur, densite = (
                int(argument) for argument in arguments[1:]
            )
        except ValueError:
            print("Erreur : longueur, hauteur et densite doivent etre des entiers.")
            return 1
    else:
        print(
            f"Utilisation : python {arguments[0]} "
            "<longueur> <hauteur> <densite 0-100>"
        )
        return 1

    if largeur < 1 or hauteur < 1:
        print("Erreur : longueur et hauteur doivent etre superieures a zero.")
        return 1
    if not 0 <= densite <= 100:
        print("Erreur : la densite doit etre comprise entre 0 et 100.")
        return 1

    # Etape 6 : generer un plateau et diminuer la densite si aucun chemin existe.
    densite_actuelle = densite
    while True:
        carte, entree, sortie = generer_labyrinthe(
            largeur, hauteur, densite_actuelle
        )
        print(
            f"\nPlateau genere (X = obstacle, . = case libre, "
            f"densite = {densite_actuelle} %) :"
        )
        afficher_carte(carte)

        # Etape 7 : chercher le plus court chemin sans toucher aux obstacles.
        chemin = trouver_chemin(carte, entree, sortie, largeur, hauteur)
        if chemin is not None:
            for ligne, colonne in chemin:
                carte[ligne][colonne] = "O"

            carte[entree[0]][entree[1]] = "E"
            carte[sortie[0]][sortie[1]] = "S"
            nombre_de_coups = len(chemin) + 1
            print(f"\nChemin trouve en {nombre_de_coups} coups :")
            afficher_carte(carte)
            return 0

        print("\nAucun chemin ne relie l'entree a la sortie.")
        if densite_actuelle == 0:
            print("La densite est deja a 0 %; impossible de la diminuer davantage.")
            return 0

        densite_actuelle = max(0, densite_actuelle - 2)
        print(f"Nouveau plateau genere avec une densite reduite a {densite_actuelle} %.")


if __name__ == "__main__":
    sys.exit(main(sys.argv))
