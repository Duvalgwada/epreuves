# Parametres à l'envers

# Entrer les arguments
arg1 = input("Veuillez saisir un premier mot : ")
arg2 = input("Veuillez saisir un second mot : ")
arg3 = input("Veuillez saisir un troisième mot : ")

# Créer une liste avec les arguments
arguments = [arg1, arg2, arg3]

# Parcourir les arguments en ordre inversé
for arg in reversed(arguments):
    print(arg)
