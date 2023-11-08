# Nombre premier

# Donner le nombre
nombre = input('Écris un nombre entier positif : ')
nombre = int(nombre)

# Verifier si nombre est premmier
i = 2
while i < nombre and nombre % i != 0 :
    i = i + 1
if i == nombre :
    print('Le nombre', nombre, 'est premier!')
else :
    print('Ce n\'est pas un nombre premier.')