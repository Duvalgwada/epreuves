import re

#  Contrôle de pass sanitaire

# Programme affichant les elements qui ne contiennent pas le caractere saisi.

def filtrer_elements_ne_contenant_pas(liste, caractere):
    caractere = caractere.casefold()
    elements_filtres = []
    for element in liste:
        if caractere not in element.casefold():
            elements_filtres.append(element)
    return elements_filtres

def main():
    saisie_elements = input(
        "Entrez les elements, separes par des espaces ou des virgules : "
    )
    ma_liste = [
        element
        for element in re.split(r"[\s,]+", saisie_elements.strip())
        if element
    ]

    if not ma_liste:
        print("Erreur : veuillez saisir au moins un element.")
        return

    caractere_a_chercher = input("Entrez un caractere a rechercher : ").strip()

    if len(caractere_a_chercher) != 1:
        print("Erreur : veuillez saisir un seul caractere.")
        return

    print(f"Tableau saisi : {ma_liste}")
    elements_sans_caractere = filtrer_elements_ne_contenant_pas(
        ma_liste, caractere_a_chercher
    )
    print(f"Elements ne contenant pas '{caractere_a_chercher}' : {elements_sans_caractere}")

if __name__ == "__main__":
    main()