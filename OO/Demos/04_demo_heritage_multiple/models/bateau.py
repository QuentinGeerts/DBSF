class Bateau:

    # Constructeur
    def __init__(self, couleur, type_energie) -> None:
        self.__couleur = couleur
        self.__type_energie = type_energie

    # Ascesseurs et mutateurs
    @property
    def couleur (self):
        return self.__couleur
    
    @couleur.setter
    def couleur(self, value):
        self.__couleur = value

    @property
    def type_energie (self):
        return self.__type_energie
    
    @type_energie.setter
    def type_energie(self, value):
        self.__type_energie = value

    # Méthodes
    def __str__(self):
        return f"Bateau {self.couleur} à {self.type_energie}"

    def avancer(self):
        print(self, "navigue")
    
    def tourner(self):
        print(self, "tourne")
    
    def accoster(self, port):
        print(self, "accoste au port", port)


if __name__ == "__main__":

    b = Bateau('Rouge', 'Vapeur')
    b2 = Bateau('Noir', 'Vapeur')
    b.avancer()

    b.tourner()

    b.accoster("Anvers")