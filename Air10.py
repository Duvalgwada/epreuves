# AFFICHER LE CONTENU

# Programme affichant le contenu d'un fichier donné en argument. 

import sys

def afficher_contenu_fichier(nom_fichier):
    try:
        # Ouvrir le fichier en mode lecture
        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()
            print("Contenu du fichier:")
            print(contenu)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {nom_fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")

def main():
    # Vérifier si le nombre d'arguments est correct
    if len(sys.argv) != 2:
        # Message d'utilisation si le nombre d'arguments est incorrect
        print("Usage : python programme.py nom_du_fichier")
    else:
        # Récupérer le nom du fichier à partir des arguments en ligne de commande
        nom_du_fichier = sys.argv[1]

        # Appeler la fonction pour afficher le contenu du fichier
        afficher_contenu_fichier(nom_du_fichier)

if __name__ == "__main__":
    main()