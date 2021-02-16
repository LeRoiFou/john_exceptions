"""
Les exceptions : raise - Gérer les exceptions même si le programme se lance sans afficher d'erreur 

Dans le programme ci-dessous, si le programmeur-utilisateur saisi un chiffre différent entre 1 et 6, un message d'erreur 
s'affiche de type 'ValueError'. 
Cependant, le fait qu'on ait pas recours à l'instruction try / except, l'instruction en dernière ligne : print('test') 
ne s'exécutera pas... 

Éditeur : Laurent REYNAUD 
Date : 10-09-2020 
"""

nombre = int(input("Entrer un nombre entre 1 et 6 : "))

if 1 <= nombre <= 6:
    print(nombre)
else:
    raise ValueError("Erreur ! Le nombre doit être compris entre 1 et 6 !")  # lever une exception de type ValueError()

print('test')
