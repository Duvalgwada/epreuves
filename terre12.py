# Format horaire, de 12 à 24

import datetime
import time

# Mettre en boucle
while True:
    # Obtenir l'heure locale actuelle
    heure_locale = datetime.datetime.now().time()

    print("Heure locale (format 24 heures):", heure_locale)
    
    # Mettre à jour, toutes les 5 secondes
    time.sleep(5)  # Attendre 5 secondes avant la prochaine mise à jour