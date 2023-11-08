# Trouver la Suisse
# Sur 3 arguments, trouve la valeur au milieu (Non la moyenne)

# Entrer les valeurs
num1 = int(input("Entrez le Premier nombre : "))
num2 = int(input("Entrez le Second nombre : "))
num3 = int(input("Entrez le Troisième nombre : "))

# Verifier par comparaison, quelle valeur est differente de l'autre
def middle_value(num1, num2, num3):
    if (num1 <= num2 <= num3) or (num3 <= num2 <= num1):
        return num2
    elif (num2 <= num1 <= num3) or (num3 <= num1 <= num2):
        return num1
    else:
        return num3

# Afficher le resultat
resultat = middle_value(num1, num2, num3)
print("La valeur du milieu est :", resultat)