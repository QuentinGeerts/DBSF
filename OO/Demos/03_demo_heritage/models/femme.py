from models.personne import Personne
class Femme (Personne):

    # -- Constructeur --
    def __init__(self, nom, prenom, est_enceinte):
        super().__init__(nom, prenom)
        self.__est_enceinte = est_enceinte
    
    # -- Ascesseurs & Mutateurs --
    # @property = getter
    # @<property_name>.setter = setter
    @property
    def est_enceinte(self):
        return self.__est_enceinte
    
    @est_enceinte.setter
    def est_enceinte(self, value):
        self.__est_enceinte = value

    # -- Méthodes --
    def accoucher(self):
        if self.est_enceinte:
            print(f"{self.nom} {self.prenom} accouche.")
            self.est_enceinte = False
        else:
            print("N'est pas enceinte")

    def se_presenter(self):
        super().se_presenter()
        print("Je suis une femme.")

if __name__ == "__main__":
    f = Femme("Geerts", "Mélanie", False)
    f.se_presenter()
    f.parler("Hello World !")
    f.accoucher()
    f.est_enceinte = True
    f.accoucher()