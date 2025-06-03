class animal:
    def __init__(self, nom, sexe, date_de_naissance, santé, faim, bonheur, stress, enclos):
        self.nom = nom
        self.sexe = sexe
        self.date_de_naissance = date_de_naissance
        self.santé = santé
        self.faim = faim
        self.bonheur = bonheur
        self.stress = stress
        self.enclos = enclos

    def manger(self, quantité):
        if self.faim - quantité > 0 : 
            self.faim -= quantité
        else :
            self.faim = 0
        self.bonheur += 10
        self.santé += 10
    
    def dormir(self):
        self.faim += 20
        self.bonheur += 10
        self.santé += 10
    
    def cri(self):
        print('L animal fait un bruit')

class panda(animal):
    def __init__(self, nom, sexe, date_de_naissance, santé, faim, bonheur, stress, enclos, densité_population_max, faim_max, classe='mammifère', espèce='panda'):
        super().__init__(nom, sexe, date_de_naissance, santé, faim, bonheur, stress, enclos)
        self.classe = classe
        self.espèce = espèce
        self.densité_population_max = densité_population_max
        self.faim_max = faim_max

    
    def évaluation_stress(self):
        if self.enclos.densité_population > self.densité_population_max:
            self.stress += (self.enclos.densité_population - self.densité_population_max)
        elif self.stress - 10 > 0:
            self.stress -= 10
        else :
            self.stress = 0
    
    def cri(self):
        return '...'

class ours(animal):
        def __init__(self, nom, sexe, date_de_naissance, santé, faim, bonheur, stress, enclos, densité_population_max, faim_max, classe='mammifère', espèce='ours'):
            super().__init__(nom, sexe, date_de_naissance, santé, faim, bonheur, stress, enclos)
            self.classe = classe
            self.espèce = espèce
            self.densité_population_max = densité_population_max
            self.faim_max = faim_max
            self.enclos = enclos
    
        def évaluation_stress(self):
            if self.enclos.densité_population > self.densité_population_max:
                self.stress += (self.enclos.densité_population - self.densité_population_max)
            elif self.stress - 10 > 0:
                self.stress -= 10
            else :
                self.stress = 0
            
            if self.stress > 100:
                self.enclos.abimer_barrières()

        def cri(self):
            return 'boum'
                

class orque(animal):
        def __init__(self, nom, sexe, date_de_naissance, santé, faim, bonheur, stress, enclos, densité_population_max, faim_max, classe='mammifère', espèce='ours'):
            super().__init__(nom, sexe, date_de_naissance, santé, faim, bonheur, stress, enclos)
            self.classe = classe
            self.espèce = espèce
            self.densité_population_max = densité_population_max
            self.faim_max = faim_max
            self.enclos = enclos
    
        def évaluation_stress(self):
            if self.enclos.densité_population > self.densité_population_max:
                self.stress += (self.enclos.densité_population - self.densité_population_max)
            elif self.stress - 10 > 0:
                self.stress -= 10
            else :
                self.stress = 0
            if self.stress > 100:
                self.enclos.abimer_barrières()

        def cri(self):
            return 'oui enfin bon'

class canard(animal):
        def __init__(self, nom, sexe, date_de_naissance, santé, faim, bonheur, stress, enclos, densité_population_max, faim_max, classe='mammifère', espèce='ours'):
            super().__init__(nom, sexe, date_de_naissance, santé, faim, bonheur, stress, enclos)
            self.classe = classe
            self.espèce = espèce
            self.densité_population_max = densité_population_max
            self.faim_max = faim_max
            self.enclos = enclos
    
        def évaluation_stress(self):
            if self.enclos.densité_population > self.densité_population_max:
                self.stress += (self.enclos.densité_population - self.densité_population_max)
            elif self.stress - 10 > 0:
                self.stress -= 10
            else :
                self.stress = 0
            if self.stress > 100:
                self.enclos.abimer_barrières()

        def cri(self):
            return 'russians are loosers'


class pnj:
    def __init__(self, nom, sexe):
        self.nom = nom
        self.sexe = sexe


class enclos:
    def __init__(self, id_enclos, type_sol, taille, type_barrières, densité_population, dégâts_barrières, ensemble_animaux, brèche = False):
        self.id_enclos = id_enclos
        self.type_sol = type_sol 
        self.taille = taille
        self.type_barrières = type_barrières
        self.ensemble_animaux = ensemble_animaux
        self.densité_population = densité_population
        self.dégâts_barrières = dégâts_barrières
        self.brèche = brèche
    
    def abimer_barrières(self):
        if self.dégâts_barrières < 100 :
            self.dégâts_barrières += 10
        else :
            self.brèche = True
            print('Brèche dans l''enclos !!!', self.id_enclos)
    
    def montrer_animaux(self):
        print('Voici les animaux de l''enclos ', self.id_enclos)
        for animal in self.ensemble_animaux:
            print(animal.nom, ' (', animal.espèce, ')', sep='')
    

class soigneur(pnj):
    def __init__ (self, nom, sexe, efficacité, métier = 'soigneur'):
        super().__init__(nom, sexe)
        self. efficacité = efficacité
        self.métier = métier
    
    def nourrir(self, animal, quantité):
        animal.manger(quantité)
    
    def amener_dans_enclos(self, animal, enclos):
        if animal.enclos :
            animal.enclos.ensemble_animaux.remove(animal)
        animal.enclos = enclos
        enclos.ensemble_animaux.add(animal)
        enclos.densité_population = len(enclos.ensemble_animaux) / enclos.taille

def cri(animal):
    print(animal.cri())

XiJinping = panda('Xi Jinping', 'Male', '15/06/1953', 80, 80, 70, 50, None, 0.1, 90)
Tchernobyl = ours('Tchernobyl', 'Male', '26/04/1986', 70, 60, 55, 20, None, 0.2, 80)
Margaret = panda('Margaret', 'Female', '04/09/1981', 90, 50, 90, 70, None, 0.8, 100)
Willy = orque('Willy', 'Male', '17/03/1959', 50, 80, 90, 10, None, 0.8, 30)
Donald = canard('Donald', 'Male', '14/06/1946', 50, 80, 90, 10, None, 0.8, 30)
Georgette = canard('Georgette', 'Female', '14/06/1953', 50, 80, 90, 10, None, 0.8, 30)

enclos1 = enclos(1, 'Herbes', 10, 'Bois', 0, 0, set())
enclos2 = enclos(2, 'Terre', 20, 'Acier', 0, 0, set())
enclos3 = enclos(3, 'Eau', 10, 'Piscine', 0, 0, set())

Vincent = soigneur('Vincent', 'Male', 100)

print(XiJinping.faim)
Vincent.nourrir(XiJinping, 5)
print(XiJinping.faim)
XiJinping.manger(5)
print(XiJinping.faim)

Vincent.amener_dans_enclos(Tchernobyl, enclos2)
Vincent.amener_dans_enclos(XiJinping, enclos2)

enclos2.montrer_animaux()
enclos1.montrer_animaux()

Vincent.amener_dans_enclos(XiJinping, enclos1)

enclos2.montrer_animaux()
enclos1.montrer_animaux()

Donald.cri()
Tchernobyl.cri()
Willy.cri()


cri(Tchernobyl)
cri(Willy)
cri(XiJinping)








        

        

