# Format horaire, de 24 à 12

import datetime
import time

# Mettre en boucle
while True:
    # Obtenir l'heure locale actuelle
    heure_locale = datetime.datetime.now().time()

    # Convertir l'heure en format 12 heures
    heure_format_12 = time.strftime("%I:%M %p", time.localtime())

    print("Heure locale (format 24 heures):", heure_locale)
    print("Heure locale (format 12 heures):", heure_format_12)

    # Petite option, une pause pour éviter de saturer la console avec des mises à jour trop rapides
    time.sleep(10)  # Attendre 10 secondes avant la prochaine mise à jour