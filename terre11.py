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

    # Mettre à jour
    # time.sleep(1)