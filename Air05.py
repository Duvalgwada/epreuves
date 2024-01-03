#  Sur chacun d'entre eux

# Programme etant capapble de reconneitre et de faire une operation (addition ou soustraction) sur chaque entier d'une liste

def operation_sur_liste(liste, valeur, operation):
    resultat = []

    # Vérifier le type d'opération
    if operation == 'addition':
        resultat = [nombre + valeur for nombre in liste]
    elif operation == 'soustraction':
        resultat = [nombre - valeur for nombre in liste]
    else:
        print("Opération non reconnue. Les opérations valides sont 'addition' et 'soustraction'")
        return None

    return resultat

def main():
    # Exemple d'utilisation
    ma_liste = [1, 2, 3, 4, 5]
    valeur_a_ajouter_ou_soustraire = 10

    # Ajouter la valeur à chaque élément de la liste
    resultat_addition = operation_sur_liste(ma_liste, valeur_a_ajouter_ou_soustraire, 'addition')
    print(f"Résultat de l'addition : {resultat_addition}")

    # Soustraire la valeur à chaque élément de la liste
    resultat_soustraction = operation_sur_liste(ma_liste, valeur_a_ajouter_ou_soustraire, 'soustraction')
    print(f"Résultat de la soustraction : {resultat_soustraction}")

if __name__ == "__main__":
    main()