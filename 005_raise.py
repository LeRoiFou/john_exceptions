class mon_exception(Exception):
    """ Pour créer sa propre exception, il faut créer une classe avec le nom de sa propre exception qui doît être
    héritée de la classe parente 'Exception' """

    def __init__(self, message):  # Constructeur
        self.message = message

    def __str__(self):  # Message à afficher
        return f'Erreur trouvé : {self.message}'


print('Age : ')
age = int(input())

if age < 18:
    try:
        raise mon_exception('âge non admis')
    except mon_exception as e:
        print(e)
    finally:
        print('Age saisi :', age)
else:
    print('Age saisi :', age)
