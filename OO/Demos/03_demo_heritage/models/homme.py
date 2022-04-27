from models.personne import Personne
class Homme (Personne):

    # -- Constructeur --
    def __init__(self, nom, prenom, longueur_barbe):
        super().__init__(nom, prenom)
        self.__longueur_barbe = longueur_barbe
    
    # -- Ascesseurs & Mutateurs --
    # @property = getter
    # @<property_name>.setter = setter
    @property
    def longueur_barbe(self):
        return self.__longueur_barbe
    
    @longueur_barbe.setter
    def longueur_barbe(self, value):
        self.__longueur_barbe = value

    # -- Méthodes --
    def se_raser(self):
        print(f"{self.nom} {self.prenom} se rase.")
        self.longueur_barbe = 0

    def se_presenter(self):
        super().se_presenter()
        print("Je suis un homme.")

if __name__ == "__main__":
    h = Homme("Geerts", "Quentin", 1)
    h.se_presenter()
    h.parler("Hello World !")
    h.se_raser()
    print(h.longueur_barbe)