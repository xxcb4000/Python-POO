class animal:
    def __init__(self, nom, appétit, satisfaction, en_vie, soigneur):
        self._nom = nom
        self._appétit = appétit
        self._satisfaction = satisfaction
        self._en_vie = en_vie
        self._soigneur = soigneur

    def manger(self):
        self._appétit -= 10

    def afficher_infos(self):
        print(self.nom)
        print(self.rassasier)
        print(self.bonheur)
        print(self.en_vie)
        print(self.soigneur)

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, valeur):
        self._nom = valeur

    @property
    def soigneur(self):
        return self._soigneur

    @soigneur.setter
    def soigneur(self, valeur):
        self._soigneur = valeur

    @property
    def rassasier(self):
        return self._appétit

    @property
    def bonheur(self):
        return self._satisfaction

    @property
    def en_vie(self):
        return self._en_vie


class personnage:
    def __init__(self, nom, date_de_naissance, expérience, responsable_de):
        self._nom = nom
        self._date_naissance = date_de_naissance
        self._expérience = expérience
        self._responsable_de = responsable_de

    def nourrir(self, animal):
        animal.manger()
        self._responsable_de.add(animal)

    def entretenir(self, animal):
        animal._satisfaction += 10

    def les_animaux_sous_la_responsabilité_de(self):
        for a in self._responsable_de:
            print(a.nom)

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, valeur):
        self._nom = valeur

    @property
    def date_naissance(self):
        return self._date_naissance

    @property
    def expérience(self):
        return self._expérience
    
    @expérience.setter
    def expérience(self, valeur):
        if valeur < 0:
            return print('Ne peux pas être inéfieure à 0')
        self._expérience = valeur

    @property
    def nombre_animaux_responsable(self):
        return len(self._responsable_de)

class enclos:

    sol = "Herbe"



éléphant = animal('éléphant', 50, 50, True, 'Vincent')
girafe = animal('girafe', 60, 30, True, 'Vincent')
Vincent = personnage("Vincent", "06/02/1984", 3, set())



éléphant.afficher_infos()

Vincent.les_animaux_sous_la_responsabilité_de()

Vincent.nourrir(éléphant)

éléphant.afficher_infos()

print(Vincent.date_naissance)

Vincent.les_animaux_sous_la_responsabilité_de()

Vincent.nourrir(girafe)

Vincent.les_animaux_sous_la_responsabilité_de()


Vincent.expérience = int(input('Expérience de Vincent?'))
print(Vincent.expérience)



