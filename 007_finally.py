"""
Les exceptions : finally  
Avec l'instruction 'finally', quelque soit l'erreur ou non, le bloc 'finally' est toujours exécuté. 
L'intérêt de cette instruction est que lorsqu'on a recours à une fonction avec les instructions try / except, si on a un 
'return', quelque soit le résultat, le bloc 'finally' s'exécute toujours. 

Dans l'exemple ci-dessous, il n'y a pas d'erreur dans la formule, dans ce cas l'instruction 'return' s'exécute mais 
également le bloc 'finally' alors que l'instruction 'print('Test')' ne s'exécutera pas. 

Éditeur : Laurent REYNAUD  
Date : 10-09-2020  
"""


def test():
    try:
        a = 5
        b = 5
        return a / b
    except NameError as e:  # l'instruction 'as e' affiche le nom de l'erreur
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except (TypeError, ValueError) as e:
        print(e)
    finally:
        print("Je suis toujours exécuté !")

    print('Test')


test()
print('Suite...')
