#  Contrôle de pass sanitaire

# Programme supprimant d'un tableau tous les elements qui ne contiennent pas une autre chaine de caractere

def filtrer_elements_ne_contenant_pas(liste, sous_chaine):
    # Utiliser une liste en compréhension pour filtrer les éléments
    resultats_filtres = [element for element in liste if sous_chaine not in element]
    return resultats_filtres

def main():
# Exemple t
    ma_liste = ["Michel", "Albert", "Thérèse", "Benoit", "Paul", "t"]
    sous_chaine_a_chercher = "t"

    resultats_filtres = filtrer_elements_ne_contenant_pas(ma_liste, sous_chaine_a_chercher)
    print(f"Liste originale : {ma_liste}")
    print(f"Résultats filtrés : {resultats_filtres}")

    # Exemple a
    ma_liste = ["Michel", "Albert", "Thérèse", "Benoit", "Paul", "a"]
    sous_chaine_a_chercher = "a"

    resultats_filtres = filtrer_elements_ne_contenant_pas(ma_liste, sous_chaine_a_chercher)
    print(f"Liste originale : {ma_liste}")
    print(f"Résultats filtrés : {resultats_filtres}")

if __name__ == "__main__":
    main()