#  AFFICHER UNE PYRAMIDE

# Programme affichant un escalier constitué d'un caracterer et d'un nombre
# d'etages donné en parametre

def afficher_pyramide(caractere, nb_etages):
    largeur_base = 2 * nb_etages - 1

    for i in range(1, nb_etages + 1):
        nb_caracteres = 2 * i - 1
        ligne = caractere * nb_caracteres
        # Utiliser la méthode center pour centrer la ligne
        ligne_centree = ligne.center(largeur_base)
        print(ligne_centree)

def main():
    # Demander à l'utilisateur de saisir le caractère et le nombre d'étages
    caractere = input("Entrer le caractère de la pyramide : ")
    nb_etages = int(input("Entrer le nombre d'étages de la pyramide : "))

    # Appeler la fonction pour afficher la pyramide
    afficher_pyramide(caractere, nb_etages)

if __name__ == "__main__":
    main()
