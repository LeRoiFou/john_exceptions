"""
Les exceptions : assert - Gérer les exceptions même si le programme se lance sans afficher d'erreur 

Autre instruction identique que l'instruction 'raise' et qui est souvent utilisée dans Python : 
assert 'condition', 'message d'erreur' 

On peut s'apercevoir par ailleurs qu'avec cette instruction on gagne 2 lignes par rapport à l'instruction raise et il 
n'est pas nécessaire de mentionner le type d'erreur. 

Les instructions try / except n'étant pas présentes, si l'utilisateur saisi un chiffre différent entre 1 et 6, le 
programme s'arrêtera et l'instruction print('test') ne s'exécutera pas. 

Éditeur : Laurent REYNAUD 
Date : 10-09-2020 
"""

nombre = int(input("Entrer un nombre entre 1 et 6 : "))

assert 1 <= nombre <= 6, 'Erreur ! Le nombre doit être compris entre 1 et 6 !'
print(nombre)

print('test')
