class Voiture:

    # Constructeur
    def __init__(self, couleur, nb_roues) -> None:
        self.__couleur = couleur
        self.__nb_roues = nb_roues

    # Ascesseurs et mutateurs
    @property
    def couleur (self):
        return self.__couleur
    
    @couleur.setter
    def couleur(self, value):
        self.__couleur = value

    @property
    def nb_roues (self):
        return self.__nb_roues
    
    @nb_roues.setter
    def nb_roues(self, value):
        self.__nb_roues = value

    # Méthodes
    def __str__(self):
        return f"Voiture {self.couleur} à {self.nb_roues} roues"

    def avancer(self):
        print(self, "roule")
    
    def tourner(self):
        print(self, "tourne")


if __name__ == "__main__":

    b = Voiture('Rouge', 4)
    b.avancer()
    b.tourner()