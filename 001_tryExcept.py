"""
Les exceptions : try / except - Gérer les erreurs lors du lancement de programme 

Les exceptions permettent de lever une anomalie dans le programme et de le continuer à s'exécuter car à défaut de lever 
une exception, une erreur s'affiche et le programme s'arrête. Instructions pour une exception : 

try: 
    'programme qui va générer une erreur' 
except 'type d'erreur': 
    affichage du message d'erreur 

Éditeur : Laurent REYNAUD 
Date : 10-09-2020 
"""

numerateur = 4
# denominateur = 0

try:
    print(numerateur / denominateur)
except (TypeError, ZeroDivisionError):  # 1ère possibilité : selection des erreurs concernées entre parenthèses
    print("Les types ne sont pas compatibles ainsi que les divisions par 0")
except:  # 2ème possibilité : ne pas saisir le type d'erreur et dans ce cas gérer tous les types d'erreurs
    print("Attention il y a une erreur")

print("test")
