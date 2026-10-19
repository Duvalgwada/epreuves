# META EXERCICE

# Creer un programme qui vérifie si les exercices de l'épreuve de l’air sont présents dans le répertoire 
# et qu’ils fonctionnent (sauf celui là). Créer au moins un test pour chaque exercice.

# cette exercice est tres difficile, je me suis laissé guider par l'IA.

from pathlib import Path
import os
import subprocess
import sys


# Codes de couleur ANSI pour distinguer visuellement les resultats.
VERT = "\033[92m"
ROUGE = "\033[91m"
JAUNE = "\033[93m"
RESET = "\033[0m"

# Etape 1 : reperer le dossier de ce programme et construire la liste des fichiers attendus.
DOSSIER_AIR = Path(__file__).resolve().parent
FICHIERS_ATTENDUS = [f"Air{numero:02}.py" for numero in range(15)]

# Etape 2 : configurer les exceptions aux verifications.
# Les fichiers facultatifs peuvent manquer ; les fichiers sans test sont seulement verifies.
FICHIERS_OPTIONNELS = set()
FICHIERS_SANS_TEST = {"Air13.py"}

# Etape 3 : definir pour chaque exercice une saisie representative et un resultat attendu.
CAS_DE_TEST = {
    "Air00.py": ("alpha,beta\n", "alpha"),
    "Air01.py": ("alpha,beta\n,\n", "alpha"),
    "Air02.py": ("alpha beta\n", "alpha beta"),
    "Air03.py": ("chat chat\n", "Aucune erreur"),
    "Air04.py": ("aabbcc\n", "abc"),
    "Air05.py": ("1 2\n3\n", "[4, 5]"),
    "Air06.py": ("chat 42 pomme\na\n", "['42', 'pomme']"),
    "Air07.py": ("8 2 5 1\n4\n", "[1, 2, 4, 5, 8]"),
    "Air08.py": ("-10, -2 5\n-7 -3, 9\n", "[-10, -7, -3, -2, 5, 9]"),
    "Air09.py": ("bonjour, 12 -5 !\n", "[12, -5, '!', 'bonjour']"),
    "Air10.py": ("", "Contenu du fichier:"),
    "Air11.py": ("*\n3\n", "*****"),
    "Air12.py": ("3 -1 5 0\n", "[-1, 0, 3, 5]"),
    "Air14.py": ("genial\n", "genial"),
}


def tester_exercice(nom_fichier, saisie, texte_attendu):
    # Etape 1 : preparer la commande qui lance l'exercice avec l'interpreteur Python actuel.
    chemin = DOSSIER_AIR / nom_fichier
    arguments = [sys.executable, str(chemin)]

    # Air10 affiche le contenu du fichier donne en argument.
    if nom_fichier == "Air10.py":
        arguments.append("Air00.py")

    # Etape 2 : fixer le dossier de travail et l'encodage du processus lance.
    environnement = os.environ.copy()
    environnement["PYTHONIOENCODING"] = "utf-8"

    # Etape 3 : executer le programme avec une saisie preparee, sans depasser le delai.
    try:
        resultat = subprocess.run(
            arguments,
            input=saisie,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=DOSSIER_AIR,
            env=environnement,
            timeout=10,
            check=False,
        )
    except subprocess.TimeoutExpired:
        # Signaler un programme qui ne termine pas dans le delai imparti.
        return False, "delai depasse"
    except OSError as erreur:
        # Signaler si Python n'a pas pu lancer le fichier.
        return False, f"impossible de lancer le programme : {erreur}"

    # Etape 4 : verifier le code de sortie puis la presence du resultat attendu.
    if resultat.returncode != 0:
        detail = resultat.stderr.strip() or f"code de sortie {resultat.returncode}"
        return False, detail
    if texte_attendu not in resultat.stdout:
        return False, f"sortie attendue absente : {texte_attendu!r}"
    return True, ""


def main():
    # Etape 1 : afficher le dossier qui va etre controle.
    print(f"Verification du dossier : {DOSSIER_AIR}")

    # Etape 2 : verifier la presence de tous les fichiers attendus et noter les absents.
    fichiers_absents = []
    for nom_fichier in FICHIERS_ATTENDUS:
        if (DOSSIER_AIR / nom_fichier).is_file():
            print(f"{nom_fichier} : {VERT}present{RESET}")
        elif nom_fichier in FICHIERS_OPTIONNELS:
            print(f"{nom_fichier} : {JAUNE}absent (facultatif){RESET}")
        else:
            print(f"{nom_fichier} : {ROUGE}MANQUANT{RESET}")
            fichiers_absents.append(nom_fichier)

    # Etape 3 : tester chaque exercice present, en ignorant ceux exclus des tests.
    echecs = []
    print("\nVerification du fonctionnement :")
    for nom_fichier, (saisie, texte_attendu) in CAS_DE_TEST.items():
        if nom_fichier in FICHIERS_SANS_TEST:
            print(f"{nom_fichier} : {JAUNE}test ignore{RESET}")
            continue
        if not (DOSSIER_AIR / nom_fichier).is_file():
            continue

        reussi, detail = tester_exercice(nom_fichier, saisie, texte_attendu)
        if reussi:
            print(f"{nom_fichier} : {VERT}OK{RESET}")
        else:
            print(f"{nom_fichier} : {ROUGE}ECHEC - {detail}{RESET}")
            echecs.append(nom_fichier)

    # Etape 4 : afficher le bilan des fichiers manquants et des tests en echec.
    if fichiers_absents or echecs:
        print(
            f"\nBilan : {ROUGE}{len(fichiers_absents)} fichier(s) manquant(s), "
            f"{len(echecs)} test(s) en echec.{RESET}"
        )
    else:
        print(
            f"\nBilan : {VERT}tous les fichiers attendus sont presents "
            f"et les tests passent.{RESET}"
        )


if __name__ == "__main__":
    main()
