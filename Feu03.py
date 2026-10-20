# SUDOKU

# Programme qui lit une grille de Sudoku 9x9 et en cherche une solution.

TAILLE = 9
TAILLE_BLOC = 3
VERT = "\033[92m"
RESET = "\033[0m"


def afficher_grille(grille, grille_initiale):
    # Etape 1 : parcourir les lignes et separer visuellement les blocs de 3x3.
    for indice_ligne, ligne in enumerate(grille):
        if indice_ligne and indice_ligne % TAILLE_BLOC == 0:
            print("-" * 21)

        # Etape 2 : colorer en vert les chiffres trouves par le solveur.
        blocs = []
        for debut in range(0, TAILLE, TAILLE_BLOC):
            cases = []
            for colonne in range(debut, debut + TAILLE_BLOC):
                valeur = str(ligne[colonne])
                if grille_initiale[indice_ligne][colonne] == 0:
                    valeur = f"{VERT}{valeur}{RESET}"
                cases.append(valeur)
            blocs.append(" ".join(cases))

        # Etape 3 : afficher la ligne complete.
        print(" | ".join(blocs))


def lire_grille():
    # Etape 1 : preparer la grille et indiquer le format des lignes attendues.
    grille = []
    print("Entrez les 9 lignes du Sudoku (9 chiffres par ligne, 0 ou . pour une case vide).")

    for numero_ligne in range(1, TAILLE + 1):
        # Etape 2 : redemander la ligne courante tant qu'elle n'est pas correcte.
        while True:
            saisie = input(f"Ligne {numero_ligne} : ").strip().replace(" ", "")
            if len(saisie) != TAILLE or any(
                caractere not in "0123456789." for caractere in saisie
            ):
                print(
                    f"Erreur : la ligne doit contenir exactement 9 chiffres "
                    "(0 a 9) ou points. Ressaisissez cette ligne."
                )
                continue

            # Etape 3 : convertir les chiffres en entiers et les points en cases vides.
            ligne = [
                0 if caractere == "." else int(caractere)
                for caractere in saisie
            ]

            # Ajouter temporairement la ligne pour verifier qu'elle respecte les regles.
            grille.append(ligne)
            if grille_valide(grille):
                break

            # En cas de conflit, retirer uniquement cette ligne; les precedentes restent.
            grille.pop()
            print(
                "Erreur : cette ligne contient une valeur incompatible avec "
                "les lignes ou blocs precedents. Ressaisissez cette ligne."
            )

    # Etape 4 : retourner la grille complete apres la saisie des neuf lignes.
    return grille


def valeurs_possibles(grille, ligne, colonne):
    # Etape 1 : reperer les chiffres deja utilises dans la ligne et la colonne.
    utilisees = set(grille[ligne])
    utilisees.update(grille[indice][colonne] for indice in range(len(grille)))

    # Etape 2 : ajouter les chiffres utilises dans le bloc de 3x3.
    debut_ligne = (ligne // TAILLE_BLOC) * TAILLE_BLOC
    debut_colonne = (colonne // TAILLE_BLOC) * TAILLE_BLOC
    for indice_ligne in range(debut_ligne, min(debut_ligne + TAILLE_BLOC, len(grille))):
        for indice_colonne in range(debut_colonne, debut_colonne + TAILLE_BLOC):
            utilisees.add(grille[indice_ligne][indice_colonne])

    # Etape 3 : retourner les chiffres de 1 a 9 qui restent disponibles.
    return set(range(1, TAILLE + 1)) - utilisees


def grille_valide(grille):
    # Verifier chaque chiffre deja present dans la grille.
    for ligne in range(len(grille)):
        for colonne in range(TAILLE):
            valeur = grille[ligne][colonne]
            if valeur == 0:
                continue

            # Retirer temporairement le chiffre pour verifier ses autres occurrences.
            grille[ligne][colonne] = 0
            est_valide = valeur in valeurs_possibles(grille, ligne, colonne)
            grille[ligne][colonne] = valeur
            if not est_valide:
                return False
    return True


def resoudre_sudoku(grille):
    # Etape 1 : chercher une case vide avec le moins de valeurs possibles.
    meilleure_case = None
    meilleurs_candidats = None

    for ligne in range(TAILLE):
        for colonne in range(TAILLE):
            if grille[ligne][colonne] == 0:
                candidats = valeurs_possibles(grille, ligne, colonne)
                if not candidats:
                    return False
                if meilleurs_candidats is None or len(candidats) < len(meilleurs_candidats):
                    meilleure_case = (ligne, colonne)
                    meilleurs_candidats = candidats

    # Etape 2 : si aucune case n'est vide, le Sudoku est resolu.
    if meilleure_case is None:
        return True

    # Etape 3 : essayer chaque candidat; annuler un choix s'il empeche la resolution.
    ligne, colonne = meilleure_case
    for valeur in meilleurs_candidats:
        grille[ligne][colonne] = valeur
        if resoudre_sudoku(grille):
            return True
        grille[ligne][colonne] = 0

    return False


def main():
    # Etape 1 : presenter la taille et les regles du Sudoku.
    print("Un Sudoku est une grille de 9x9 composee de 9 blocs de 3x3.")
    print("Chaque ligne, colonne et bloc doit contenir les chiffres de 1 a 9 sans repetition.")

    # Etape 2 : saisir les lignes; une ligne invalide est redemandee sans perdre les autres.
    grille = lire_grille()

    # Etape 3 : verifier les valeurs donnees avant de chercher une solution.
    if not grille_valide(grille):
        print("Erreur : les valeurs saisies ne respectent pas les regles du Sudoku.")
        return

    # Etape 4 : garder une copie des indices pour distinguer saisie et solution en couleur.
    grille_initiale = [ligne.copy() for ligne in grille]

    # Etape 5 : resoudre et afficher la grille complete, ou signaler qu'elle est insoluble.
    if resoudre_sudoku(grille):
        print("\nSolution du Sudoku :")
        afficher_grille(grille, grille_initiale)
    else:
        print("Aucune solution n'existe pour cette grille.")


if __name__ == "__main__":
    main()
