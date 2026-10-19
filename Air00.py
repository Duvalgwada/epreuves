#  Split

# Programme découpant une chaîne en tableau avec un séparateur choisi.

def ma_fonction(string_a_couper, string_separateur):
    return string_a_couper.split(string_separateur)

def main():
    chaine = input(
        "Entrez le texte à découper (écrivez \\t pour une tabulation "
        "et \\n pour un retour à la ligne) : "
    )
    chaine = chaine.replace("\\t", "\t").replace("\\n", "\n")

    for nom, separateur in (
        ("espace", " "),
        ("tabulation", "\t"),
        ("retour à la ligne", "\n"),
    ):
        resultat = ma_fonction(chaine, separateur)
        print(f"Séparation par {nom} : {resultat}")

if __name__ == "__main__":
    main()