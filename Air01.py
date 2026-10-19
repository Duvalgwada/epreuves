# Split en Fonction

# Création d'un programme qui découpe une chaîne de caractères en tableau en fonction du séparateur donné en 2e argument.

import sys  # Permet de lire les arguments et de terminer le programme en cas d'erreur.


def ma_fonction(string_a_couper, string_separateur):
    """Découpe le texte selon le séparateur et renvoie la liste obtenue."""
    tableau_resultat = string_a_couper.split(string_separateur)  # Découpe le texte à chaque occurrence du séparateur.
    return tableau_resultat  # Renvoie les morceaux sous forme de liste.


def main():
    # Utilise les arguments de la commande ou demande les valeurs à l'utilisateur.
    if len(sys.argv) == 1:
        string_a_couper = input("Entrez le texte à découper : ")
        print("Le séparateur peut être un espace ou un signe de ponctuation (ex. ,).")
        string_separateur = input("Entrez le séparateur exact à rechercher : ")
    elif len(sys.argv) == 3:
        string_a_couper, string_separateur = sys.argv[1:]
    else:
        print("Error: deux arguments sont requis (texte et séparateur).", file=sys.stderr)
        sys.exit(1)  # Termine avec un code d'erreur.

    # Un séparateur vide ne permet pas de découper correctement la chaîne.
    if not string_separateur:
        print("Error: le séparateur ne peut pas être vide.", file=sys.stderr)
        sys.exit(1)  # Termine avec un code d'erreur.

    # Appelle la fonction de découpage avec le texte et le séparateur fournis.
    resultat = ma_fonction(string_a_couper, string_separateur)

    # Affiche chaque morceau sur une ligne différente.
    print("\n".join(resultat))


if __name__ == "__main__":
    main()  # Lance le programme uniquement si ce fichier est exécuté directement.
