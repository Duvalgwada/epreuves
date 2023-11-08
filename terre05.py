# Faire une division

while True:
    try:
        nombre1 = float(input("Entrez le premier nombre : "))
        nombre2 = float(input("Entrez le deuxième nombre : "))
        
        if nombre2 == 0:
            print("Erreur : Division par zéro n'est pas autorisée.")
        else:
            resultat = nombre1 / nombre2
            print(f"Le résultat de {nombre1} / {nombre2} est : {resultat}")
    except ValueError:
        print("Veuillez entrer des nombres valides.")
