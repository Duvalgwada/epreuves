# combinaison de 2 nombres (non une suite logique de nombre allant de 00 à 99)

print("Les résultats possibles sont :")
for i in range(100):
    for j in range(i + 1, 100):
        print(f"{i:02d} {j:02d}")