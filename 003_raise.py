"""
Les exceptions : créer sa propre exception 

class NomClasse(Exception) 

Éditeur : Laurent REYNAUD 
Date : 10-09-2020 
"""


class exception_format_date(Exception):
    """ Pour créer sa propre exception, il faut créer une classe avec le nom de sa propre exception qui doît être
    héritée de la classe parente 'Exception' """
    pass


def demander_date():
    try:
        jour, mois, annee = date.split('-')
        return f'Jour saisi : {jour}, mois saisi : {mois} et année saisie : {annee}'
    except:
        raise exception_format_date('Format de la date invalide !')  # appel de sa propre exception créée


print('Entrer une date (format JJ-MM-AAAA) :')
date = input()
print(demander_date())
print('test')
