"""
Les exceptions : else 
Avec l'instruction 'else', l'instruction qui suit 'else' est toujours exécutée seulement s'il n'y a pas eu d'erreurs 
Le bloc d'instruction 'else' doit toujours précédé le bloc d'instruction 'finally' 

Éditeur : Laurent REYNAUD 
Date : 10-09-2020 
"""

try:
    a = 5
    b = 5
    print(a / b)
except NameError as e:  # l'instruction 'as e' affiche le nom de l'erreur
    print(e)
except ZeroDivisionError as e:
    print(e)
except (TypeError, ValueError) as e:
    print(e)
else:
    print("Je suis toujours exécuté s'il n'y a pas eu d'exceptions !")
finally:
    print('Dans tous les cas, je suis toujours exécuté héhéhéhé !')

print('Test')
