# Tri par ordre ASCII
# Le tri compare les caractères de gauche à droite selon leur code ASCII.
# Par exemple, les majuscules précèdent les minuscules.

# demande les éléments à trier, séparés par des espaces.
# split() transforme la saisie en une liste de chaînes.
elements = input("Entrez les éléments à trier, séparés par des espaces : ").split()

# vérifier que tous les caractères saisis appartiennent à ASCII.
if all(element.isascii() for element in elements):
    # sorted() trie les chaînes selon l'ordre de leurs caractères ASCII.
    elements_tries = sorted(elements)

    # afficher la liste triée.
    print("Éléments triés par ordre ASCII :")
    print(elements_tries)
else:
    # Signaler une entrée contenant des caractères non ASCII, comme « é ».
    print("Erreur : les éléments doivent contenir uniquement des caractères ASCII.")
