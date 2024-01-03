# Tri par ordre Ascii

# Programme triant les elements données en argument par ordre ASCII.

# definition
# Tr Lexicograhique ordre alphabétique basé sur l'ordre ASCII des caractères)

tableau1 = ["Alfred", "Momo", "Gilbert"]
tableau2 = ["a", "z", "e", "r", "t", "y"]

# Tri de la liste ensemble
# tableau_trie = sorted(tableau1 + tableau2, key=str.lower)

# Tri de la liste seul
tableau_trie1 = sorted(tableau1, key=str.lower)
tableau_trie2 = sorted(tableau2, key=str.lower)

print("Liste triée par ordre ASCII (lexicographique): ")
print(tableau_trie1)
print(tableau_trie2)
