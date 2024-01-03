# Combinaisons de 3 chiffres (Non une suite de nombre de 000 à 999)

for i in range(10):
    for j in range(i + 1, 10):
        for k in range(j + 1, 10):
            print(i, j, k)

