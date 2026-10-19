# AFFICHER LE CONTENU

# Programme affichant le contenu d'un fichier donné en argument. 

from pathlib import Path
import sys

def afficher_contenu_fichier(nom_fichier):
    # Etape 1 : convertir le nom ou chemin saisi en objet chemin.
    chemin_fichier = Path(nom_fichier)

    # Etape 2 : si le nom seul n'existe pas depuis le dossier courant,
    # chercher le fichier dans le dossier où se trouve ce programme.
    if not chemin_fichier.is_file() and not chemin_fichier.is_absolute():
        chemin_fichier = Path(__file__).resolve().parent / chemin_fichier

    try:
        # Etape 3 : ouvrir le fichier en lecture et afficher tout son contenu.
        with chemin_fichier.open("r", encoding="utf-8") as fichier:
            contenu = fichier.read()
            print("Contenu du fichier:")
            print(contenu)
    except FileNotFoundError:
        # Signaler explicitement si le fichier demandé n'existe pas.
        print(f"Erreur : le fichier {nom_fichier} n'a pas été trouvé.")
    except (OSError, UnicodeDecodeError) as e:
        # Signaler les erreurs de lecture ou d'encodage.
        print(f"Erreur lors de la lecture du fichier : {e}")

def main():
    # Etape 1 : accepter au plus un argument, qui est le chemin du fichier.
    if len(sys.argv) > 2:
        print("Usage : python Air10.py [nom_du_fichier]")
        return

    # Etape 2 : prendre le chemin depuis l'argument ou le demander à l'utilisateur.
    if len(sys.argv) == 2:
        nom_du_fichier = sys.argv[1]
    else:
        nom_du_fichier = input("Entrez le nom ou le chemin du fichier : ").strip()

    # Etape 3 : verifier que la saisie n'est pas vide.
    if not nom_du_fichier:
        print("Erreur : veuillez saisir un nom de fichier.")
        return

    # Etape 4 : afficher le contenu du fichier choisi.
    afficher_contenu_fichier(nom_du_fichier)

if __name__ == "__main__":
    main()