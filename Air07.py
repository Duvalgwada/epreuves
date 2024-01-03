#  Insertion dans un tableau trié

# Programme ajoutant à une liste d'entiers triée un nouvel entier tout en gardant la liste triée dans l'ordre croissant.
# le dernier argument est l'élément à ajouter

def ajouter_element_trie(liste, nouvel_element):
    # Trouver l'index où ajouter le nouvel élément tout en maintenant la liste triée
    index = 0
    while index < len(liste) and liste[index] < nouvel_element:
        index += 1

    # Insérer le nouvel élément à l'index trouvé
    liste.insert(index, nouvel_element)

def main():
    # Exemple 1
    liste_triee = [1, 3, 4]
    nouvel_element_a_ajouter = 2

    ajouter_element_trie(liste_triee, nouvel_element_a_ajouter)
    print(f"Liste triée après ajout de {nouvel_element_a_ajouter} : {liste_triee}")

    # Exemple 2
    liste_triee = [10, 20, 30, 40, 50, 60, 70, 90]
    nouvel_element_a_ajouter = 33

    ajouter_element_trie(liste_triee, nouvel_element_a_ajouter)
    print(f"Liste triée après ajout de {nouvel_element_a_ajouter} : {liste_triee}")

if __name__ == "__main__":
    main()