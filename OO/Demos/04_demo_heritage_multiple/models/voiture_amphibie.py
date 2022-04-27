from models.voiture import Voiture
from models.bateau import Bateau

class VoitureAmphibie (Bateau, Voiture):
    
    def __init__(self, couleur, type_energie, nb_roues) -> None:
        # super().__init__(couleur, type_energie)
        # super().__init__(couleur, nb_roues)

        Bateau.__init__(self, couleur, type_energie)
        Voiture.__init__(self, couleur, nb_roues)
        self.__mode = 0 # O = sol ; 1 = eau

    @property
    def mode_sol(self):
        return self.__mode == 0

    @property
    def mode_eau(self):
        return self.__mode == 1


    def change_mode(self):
        self.__mode = (self.__mode + 1) % 2
        print('Changement de mode...')

    def __str__(self):
        return f"Voiture amphibie {self.couleur}"

    def avancer(self):
        if self.mode_sol:
            Voiture.avancer(self)
        else:
            Bateau.avancer(self)

    def accoster(self, port):
        if self.mode_eau:
            Bateau.accoster(self, port)
        else:
            print('Opération non valide en mode sol.')