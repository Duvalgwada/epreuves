#  LE ROI DES TRIS

# Programme triant une liste de nombres.
# Ce dernier devra implementer l'algorithme du tri rapide (Quicksort)
# Programme utilisant la Recursivite (Qui peut être répété un nombre indéfini de fois par l'application de la même règle.)
# pour implementer l'algorithme du tri rapide

def quicksort(liste):
    if len(liste) <= 1:
        return liste
    else:
        pivot = liste[0]
        elements_inf = [x for x in liste[1:] if x <= pivot]
        elements_sup = [x for x in liste[1:] if x > pivot]
        return quicksort(elements_inf) + [pivot] + quicksort(elements_sup)

def main():
    # Demander à l'utilisateur de saisir une liste de nombres
    input_liste = input("Entrer une liste de nombres séparés par des espaces : ")
    liste = [int(x) for x in input_liste.split()]

    # Appeler la fonction pour trier la liste
    liste_triee = quicksort(liste)

    # Afficher la liste triée
    print("Liste triée :", liste_triee)

if __name__ == "__main__":
    main()
