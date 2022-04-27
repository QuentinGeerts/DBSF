class Personne:

    # -- Constructeur --
    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom
    
    # -- Ascesseurs & Mutateurs --
    # @property = getter
    # @<property_name>.setter = setter
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def prenom(self):
        return self.__prenom
    
    @prenom.setter
    def prenom(self, value):
        self.__prenom = value

    # -- Méthodes --
    def parler(self, message):
        print(f"{self.nom} {self.prenom} dit : {message}")

    def se_presenter(self):
        print("Je suis une personne.")

if __name__ == "__main__":
    p = Personne("Geerts", "Quentin")
    p.se_presenter()
    p.parler("Hello World !")