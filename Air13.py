#  META EXERCICE

# Programme verifiant si les exercices l'epreuve 'Air' sont presents dans le repertoire
# et qu'ils fonctionnent (sauf pour celui ci).
# Creer au moins un test pour chaque exercice.

import os
import importlib

# Spécifiez le chemin complet vers le répertoire des exercices 'Air'
chemin_repertoire_air = "/home/val/Documents/Semaine II/3 - Air"

# Nom du fichier à exclure des tests
fichier_a_exclure = "Air13.py"

def afficher_contenu_repertoire():
    contenu_repertoire = os.listdir(chemin_repertoire_air)
    print("Contenu du répertoire :", contenu_repertoire)

def lister_exercices_air():
    try:
        exercices_air = [f for f in os.listdir(chemin_repertoire_air) if f.endswith(".py") and f != fichier_a_exclure]
        return exercices_air
    except Exception as e:
        print(f"Erreur lors de la récupération du contenu du répertoire : {e}")
        return []

def lister_et_tester_exercices_air():
    afficher_contenu_repertoire()

    exercices_air = lister_exercices_air()
    exercices_air.sort()  # Triez les fichiers dans l'ordre croissant

    print("Tests des exercices 'Air' :")
    total_success = 0
    total_tests = 0

    for fichier in exercices_air:
        chemin_fichier = os.path.join(chemin_repertoire_air, fichier)

        # Exclure le fichier spécifié des tests
        if fichier == fichier_a_exclure:
            print(f"{fichier} (1/{total_tests + 1}) : \033[93m{'excluded'}\033[0m")  # Jaune
            continue

        result = ouvrir_et_tester(chemin_fichier)
        total_tests += 1

        if result:
            total_success += 1
            print(f"{fichier} (1/{total_tests}) : \033[92m{'success'}\033[0m")  # Vert
        else:
            print(f"{fichier} (1/{total_tests}) : \033[91m{'failure'}\033[0m")  # Rouge

    print(f"\nTotal success: \033[92m({total_success}/{total_tests})\033[0m")  # Vert

def ouvrir_et_tester(chemin_fichier):
    try:
        module = importlib.import_module(os.path.splitext(os.path.basename(chemin_fichier))[0])

        # Vérifier si la fonction main() est définie dans le module et est callable
        if hasattr(module, 'main') and callable(getattr(module, 'main')):
            module.main()
            return True
        else:
            return False
    except Exception as e:
        return False

if __name__ == "__main__":
    lister_et_tester_exercices_air()
