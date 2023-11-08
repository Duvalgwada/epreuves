# Puissance d'un nombre

# Entrer les arguments et donner resultat
nombre = float(input("Entrez Nombre: ")) # Utiliser float afin de pouvoir mettre des nombres decimaux
puissance = int(input("Entrez la Puissance: ")) # Utiliser 'int' pour mettre que des nombres entiers
resultat = nombre ** puissance # ou resultat = pow(nombre, puissance)
print(resultat)